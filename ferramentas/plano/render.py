"""Gera os PDFs do Plano de Negócios (computador e celular) a partir de plano-d.html e plano-m.html.
Rodar depois de build.py: python3 ferramentas/plano/render.py"""
import pathlib
D=pathlib.Path(__file__).resolve().parent
R=D.parents[1]
import asyncio
from playwright.async_api import async_playwright
async def m():
  async with async_playwright() as p:
    b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for f,W,H in [('d',1600,900),('m',600,1067)]:
      pg=await b.new_page(viewport={'width':W,'height':H},device_scale_factor=(2 if f=='m' else 1))
      await pg.goto(f'file://{D}/plano-{f}.html');await pg.wait_for_timeout(600)
      over=await pg.evaluate('''[...document.querySelectorAll('.pg')].map((p,i)=>{const r=p.getBoundingClientRect();let mx=0;p.querySelectorAll('*').forEach(e=>{const q=e.getBoundingClientRect();if(q.height&&!e.closest('.cbg'))mx=Math.max(mx,q.bottom-r.top)});return [i+1,Math.round(mx)]}).filter(x=>x[1]>%d)'''%(H-60))
      print(f,'overflow pages',over)
      await pg.pdf(path=f'{R}/plano/Plano-de-Negocios-Kaiabi-{ "Computador" if f=="d" else "Celular"}.pdf',width=f'{W}px',height=f'{H}px',print_background=True)
      n=await pg.evaluate("document.querySelectorAll('.pg').length")
      for i in range(n):
        el=pg.locator('.pg').nth(i);await el.screenshot(path=f'{D}/{f}-{i+1:02d}.png')
    await b.close()
asyncio.run(m())
