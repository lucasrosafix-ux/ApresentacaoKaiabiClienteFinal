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
