# Apresentações Kaiabí — manual de manutenção AI-first

Este repositório é público e vira **apresentacao.kaiabishop.com.br** (GitHub Pages, ramo main).
Toda mudança é feita por IA a partir de um comando do Lucas (voz ou texto). Nada aqui depende de um humano editar código.

## Princípios
1. **Fonte única das regras:** `regras-do-plano.md`. Mudou regra → muda lá primeiro, depois em todos os arquivos da lista abaixo.
2. **Tudo regenerável:** os PDFs, o convite 3D e a trilha têm gerador em `ferramentas/`. Nunca editar o resultado à mão quando existe gerador.
3. **Sem saúde prometida, sem depoimento inventado, sem garantia de ganho.**
4. **Verificar publicado** e **registrar no diário do Brain** (artefato 43103ed1-7972-4faa-97fc-fecca0efdb22).

## Mapa
| Caminho | O que é | Como muda |
|---|---|---|
| `apresentacao/index.html` | Institucional 3D (sem narração, termina em convite). | Editar o texto; números conforme `regras-do-plano.md`. Fotos em `apresentacao/p/`. Vídeos de abertura gerados no Higgsfield (originais 4K no backup privado). |
| `convite/index.html` | Convite do distribuidor em Stories, narrado. Textos da narração no objeto `T` (cenas 1, fam, renda, neg, 3–8). Config do distribuidor em `#c=<base64url {n,l,w,f,v}>`. | Mudou texto de `T` → regenerar o `.mp3` da cena com a mesma voz (Higgsfield, text2speech_v2, ElevenLabs, Livia) e o mesmo nome em `convite/a/`. |
| `convite/3d/index.html` | Convite 3D narrado (gerado). | Não editar à mão: `python3 ferramentas/convite3d/gerar.py` (usa a institucional + `ferramentas/convite3d/n3d.*`). |
| `plano/` | Plano de Negócios (página + PDFs computador e celular + imagens). | `python3 ferramentas/plano/build.py` e depois `python3 ferramentas/plano/render.py` (Playwright). Produtos e preços do plano ficam na lista `PRD` do `build.py`. |
| `portal/` | Portal do Distribuidor v1 (dados no aparelho). | v2 com login, CRM e métricas vai para o Supabase (`supabase/schema.sql`). |
| `ferramentas/audio/compose.py` | Gera a trilha original (`trilha.wav`), sem direitos de terceiros. | Rodar e converter para mp3. |
| `regras-do-plano.md` | Fonte única dos números do plano. | Primeiro lugar a mudar. |

## Receitas
- **Mudar regra do plano** (ex.: desconto, ativação, bônus): atualizar `regras-do-plano.md` → `grep -rn "<valor antigo>" apresentacao convite portal ferramentas/plano` → trocar todos → regenerar convite 3D e PDFs → regenerar áudio das cenas cujo texto mudou → push → conferir as 4 páginas.
- **Virada de ano:** `grep -rn "2026"` (títulos "2026", rodapés) → trocar → regenerar PDFs → push.
- **Trocar foto de produto:** substituir `apresentacao/p/p-<id>.webp` com o mesmo nome; regenerar convite 3D e PDFs se o produto aparece neles.
- **Nova versão da institucional:** editar `apresentacao/index.html` e sempre rodar `ferramentas/convite3d/gerar.py` depois (o 3D é derivado dela).
- **Publicar:** push em main → GitHub Pages atualiza em 1–2 minutos.

## Nunca
- Guardar segredo aqui (repositório público). Fontes brutas pesadas (PowerPoint original, vídeos 4K, narração bruta) ficam no repositório privado `brain-backup`, pasta `kaiabi/fontes/`.
