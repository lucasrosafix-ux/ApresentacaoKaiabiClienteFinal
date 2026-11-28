"""Gera convite/3d/index.html a partir da apresentação institucional + camada narrada (n3d.*).
Rodar: python3 ferramentas/convite3d/gerar.py"""
import re
import pathlib
R=pathlib.Path(__file__).resolve().parents[2]
H=pathlib.Path(__file__).resolve().parent
src=R/'apresentacao/index.html'
dst=R/'convite/3d/index.html'
s=open(src).read()
A='../../apresentacao/'
s=re.sub(r"([\"'])(hero[-a-z0-9]*\.(?:mp4|jpg)|trilha\.mp3|p/p-)", lambda m:m.group(1)+A+m.group(2), s)
s=re.sub(r'<title>.*?</title>','<title>Você foi convidado para a Kaiabí</title>',s,flags=re.S)
# seções a esconder no modo narrado
hide=['#tunnel','#catalogo','#sim','#consumo','#career','#trust','#fronts']
# band sem id logo depois de #como (pilares) e band do detalhe de carreira
s=s.replace('<section class="band">\n','<section class="band" id="pilaresx">\n',1) if '<section class="band">\n' in s else s.replace('<section class="band">','<section class="band" id="pilaresx">',1)
s=s.replace('<section class="band" style="padding-top:24px">','<section class="band" id="carreirax" style="padding-top:24px">',1)
hide+=['#pilaresx','#carreirax']
DOR='''
<section id="dor" aria-label="O que te trouxe aqui">
 <div class="dsticky">
  <img id="dImg" alt="">
  <div class="dshade"></div>
  <div class="dtxt"><p class="kicker" id="dKick">Seja sincero com você</p><div class="eSe">E se…?</div></div>
 </div>
</section>
'''
PROVA='''
<section class="band" id="prova">
 <div class="wrap" style="text-align:center">
  <p class="kicker">Quem te convidou já faz parte</p>
  <div class="pcard">
   <div class="pav" id="pAv">K</div>
   <q id="pFrase">Faço parte da Kaiabí e quero você comigo nessa.</q>
   <div class="pby" id="pBy">— Kaiabí</div>
   <a class="pvid" id="pVid" target="_blank" rel="noopener" hidden>▶ Assistir o depoimento</a>
  </div>
  <p class="kicker" style="margin-top:34px">Os mais recomprados</p>
  <div class="ppots" id="pPots"></div>
 </div>
</section>
'''
i=s.find('<section class="band shelfband" id="catalogo">'); assert i>0
s=s[:i]+PROVA+s[i:]
i=s.find('<section class="band" id="proposito">'); assert i>0
s=s[:i]+DOR+s[i:]
CSS=open(H/'n3d.css').read()
HTML=open(H/'n3d.html').read()
JS=open(H/'n3d.js').read()
css_hide=','.join(hide)+'{display:none!important}'
s=s.replace('</head>','<style>'+css_hide+CSS+'</style>\n</head>',1)
s=s.replace('</body>',HTML+'<script>'+JS+'</script>\n</body>',1)
open(dst,'w').write(s)
print('ok',len(s))
