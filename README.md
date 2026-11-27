# Kaiabí — Apresentação de Negócios

Site estático, sem build.

- `apresentacao/` — Apresentação institucional (APN Kaiabí 2026)
- `plano/` — Plano de Negócios, alternável Computador/Celular, com os dois PDFs
- `index.html` — redireciona para `apresentacao/`

Publicação: GitHub Pages ou Cloudflare Pages apontando para a raiz do repositório (sem comando de build, pasta de saída `/`).

## Convite do distribuidor (`/convite`)

Duas versões narradas que terminam no link de cadastro de cada distribuidor:

- `/convite/` — formato stories (cenas que passam sozinhas).
- `/convite/3d/` — a apresentação institucional em 3D, rolando sozinha com a narração, escolha de objetivo, prova do distribuidor e barra fixa de cadastro.

- Gerar o link: `https://apresentacao.kaiabishop.com.br/convite/` (o distribuidor preenche nome, login de cadastro, WhatsApp, frase e vídeo opcionais).
- O link gerado leva os dados no endereço (`#c=...`), sem banco de dados.
- O botão "Quero entrar" abre `kaiabi.com/cadastro/LOGIN`; o pop-up de saída manda nome e WhatsApp do interessado para o WhatsApp do distribuidor.

## Portal do distribuidor (`/portal`)

Versão 1 (sem banco): primeiro acesso, primeiros passos, missão do dia com sequência, ferramentas com os links do distribuidor, mídias prontas (story 1080×1920 gerado com o nome e WhatsApp dele + legenda), Academia (orgânico e pago) e resultados locais.
A estrutura do banco para a versão 2 (login, CRM, métricas e leads) está em `supabase/schema.sql`.
