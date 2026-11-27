-- Portal do Distribuidor Kaiabí — estrutura do banco (Supabase / Postgres)
-- Rodar uma vez no projeto "kaiabi-portal". Tudo em português para facilitar a leitura.

create extension if not exists "pgcrypto";

-- 1. Distribuidores ---------------------------------------------------------
create table if not exists distribuidores (
  id            uuid primary key default gen_random_uuid(),
  auth_id       uuid unique,                       -- usuário do Supabase Auth (login)
  nome          text not null,
  slug          text unique not null,              -- kaiabishop.com.br/<slug>
  login_cadastro text not null,                    -- kaiabi.com/cadastro/<login>
  whatsapp      text not null,
  cidade        text,
  frase         text,                              -- prova social (opcional)
  video_url     text,                              -- depoimento (opcional)
  status        text not null default 'pendente'   -- pendente | aprovado | pausado
                check (status in ('pendente','aprovado','pausado')),
  plano_site    text default 'nenhum'              -- nenhum | essencial | pro
                check (plano_site in ('nenhum','essencial','pro')),
  criado_em     timestamptz not null default now(),
  aprovado_em   timestamptz
);

-- 2. Ferramentas de cada distribuidor (site, convite stories, convite 3D) ---
create table if not exists ferramentas (
  id              uuid primary key default gen_random_uuid(),
  distribuidor_id uuid not null references distribuidores(id) on delete cascade,
  tipo            text not null check (tipo in ('site','convite','convite3d','pagina_produto')),
  alvo            text,                            -- ex.: produto ou ritual da página
  ativo           boolean not null default true,
  criado_em       timestamptz not null default now(),
  unique (distribuidor_id, tipo, alvo)
);

-- 3. Eventos (métricas): tudo que acontece nos links ------------------------
-- tipos: compartilhou, abriu, assistiu_cena, assistiu_fim, escolheu_objetivo,
--        clicou_cadastro, clicou_whatsapp, popup, lead, visitou_produto
create table if not exists eventos (
  id              bigint generated always as identity primary key,
  distribuidor_id uuid references distribuidores(id) on delete cascade,
  ferramenta      text,                            -- site | convite | convite3d | midia
  tipo            text not null,
  detalhe         text,                            -- cena, produto, objetivo, mídia...
  visitante       text,                            -- id anônimo do navegador
  origem          text,                            -- whatsapp, instagram, direto...
  criado_em       timestamptz not null default now()
);
create index if not exists eventos_dist_idx on eventos (distribuidor_id, criado_em desc);
create index if not exists eventos_tipo_idx on eventos (tipo, criado_em desc);

-- 4. Leads (clientes finais e prospects) -------------------------------------
create table if not exists leads (
  id              uuid primary key default gen_random_uuid(),
  distribuidor_id uuid references distribuidores(id) on delete set null,
  nome            text not null,
  whatsapp        text not null,
  email           text,
  interesse       text,                            -- negocio | produto:<nome> | ritual:<nome>
  objetivo        text,                            -- fam | renda | neg
  origem          text,                            -- convite | convite3d | site | popup
  consentimento   boolean not null default false,  -- LGPD
  status          text not null default 'novo'
                  check (status in ('novo','em_conversa','cadastrou','comprou','perdido')),
  criado_em       timestamptz not null default now(),
  atualizado_em   timestamptz not null default now()
);
create index if not exists leads_dist_idx on leads (distribuidor_id, criado_em desc);

-- 5. Biblioteca de mídias prontas --------------------------------------------
create table if not exists midias (
  id          uuid primary key default gen_random_uuid(),
  titulo      text not null,
  categoria   text not null,                       -- produto | ritual | negocio | institucional
  produto     text,
  formato     text not null check (formato in ('story','feed','status','video','reels')),
  arquivo_url text not null,
  legenda     text,                                -- texto pronto para colar
  ativo       boolean not null default true,
  ordem       int default 0,
  criado_em   timestamptz not null default now()
);

-- 6. Academia ----------------------------------------------------------------
create table if not exists aulas (
  id        uuid primary key default gen_random_uuid(),
  trilha    text not null,                         -- organico | pago | vendas | ferramentas
  titulo    text not null,
  resumo    text,
  video_url text,
  conteudo  text,                                  -- markdown
  checklist jsonb default '[]',
  ordem     int default 0,
  ativo     boolean not null default true
);
create table if not exists progresso (
  distribuidor_id uuid references distribuidores(id) on delete cascade,
  aula_id         uuid references aulas(id) on delete cascade,
  concluida_em    timestamptz not null default now(),
  primary key (distribuidor_id, aula_id)
);

-- 7. Missão do dia (gamificação) --------------------------------------------
create table if not exists missoes (
  id        uuid primary key default gen_random_uuid(),
  dia       date unique not null,
  titulo    text not null,
  midia_id  uuid references midias(id),
  legenda   text
);
create table if not exists missoes_feitas (
  distribuidor_id uuid references distribuidores(id) on delete cascade,
  missao_id       uuid references missoes(id) on delete cascade,
  feita_em        timestamptz not null default now(),
  primary key (distribuidor_id, missao_id)
);

-- 8. Conteúdo editável pelo chat (depoimentos, preços, campanhas, textos) ---
create table if not exists conteudo (
  chave         text primary key,                  -- ex.: 'depoimentos', 'campanha_atual'
  valor         jsonb not null,
  atualizado_em timestamptz not null default now()
);

-- Visão para o CRM do Lucas: engajamento por distribuidor (últimos 30 dias)
create or replace view crm_engajamento as
select d.id, d.nome, d.slug, d.status,
  count(e.*) filter (where e.tipo = 'compartilhou')     as compartilhamentos,
  count(e.*) filter (where e.tipo = 'abriu')            as aberturas,
  count(e.*) filter (where e.tipo = 'assistiu_fim')     as assistiram_ate_o_fim,
  count(e.*) filter (where e.tipo = 'clicou_cadastro')  as cliques_cadastro,
  (select count(*) from leads l where l.distribuidor_id = d.id and l.criado_em > now() - interval '30 days') as leads,
  max(e.criado_em)                                      as ultima_atividade
from distribuidores d
left join eventos e on e.distribuidor_id = d.id and e.criado_em > now() - interval '30 days'
group by d.id;

-- Segurança (RLS) -------------------------------------------------------------
alter table distribuidores enable row level security;
alter table ferramentas    enable row level security;
alter table eventos        enable row level security;
alter table leads          enable row level security;
alter table midias         enable row level security;
alter table aulas          enable row level security;
alter table progresso      enable row level security;
alter table missoes        enable row level security;
alter table missoes_feitas enable row level security;
alter table conteudo       enable row level security;

-- público (visitantes das páginas) pode registrar eventos e deixar lead com consentimento
create policy "visitante registra evento" on eventos for insert to anon, authenticated with check (true);
create policy "visitante deixa lead" on leads for insert to anon, authenticated with check (consentimento = true);
-- público lê dados públicos do distribuidor aprovado (para montar as páginas)
create policy "perfil publico" on distribuidores for select to anon, authenticated using (status = 'aprovado' or auth_id = auth.uid());
-- distribuidor gerencia o próprio cadastro
create policy "pedir acesso" on distribuidores for insert to authenticated with check (auth_id = auth.uid());
create policy "editar meu perfil" on distribuidores for update to authenticated using (auth_id = auth.uid());
-- distribuidor vê só os próprios dados
create policy "meus eventos" on eventos for select to authenticated using (distribuidor_id in (select id from distribuidores where auth_id = auth.uid()));
create policy "meus leads" on leads for select to authenticated using (distribuidor_id in (select id from distribuidores where auth_id = auth.uid()));
create policy "atualizar meus leads" on leads for update to authenticated using (distribuidor_id in (select id from distribuidores where auth_id = auth.uid()));
create policy "minhas ferramentas" on ferramentas for select to authenticated using (distribuidor_id in (select id from distribuidores where auth_id = auth.uid()));
create policy "meu progresso" on progresso for all to authenticated using (distribuidor_id in (select id from distribuidores where auth_id = auth.uid()));
create policy "minhas missoes" on missoes_feitas for all to authenticated using (distribuidor_id in (select id from distribuidores where auth_id = auth.uid()));
-- conteúdo da biblioteca e academia é aberto para leitura
create policy "ler midias" on midias for select to anon, authenticated using (ativo);
create policy "ler aulas" on aulas for select to authenticated using (ativo);
create policy "ler missoes" on missoes for select to authenticated using (true);
create policy "ler conteudo" on conteudo for select to anon, authenticated using (true);
-- Administração (aprovar, CRM, editar conteúdo) é feita pelo Claude no chat, com a chave de serviço.
