(()=>{
const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const b64d=s=>JSON.parse(decodeURIComponent(escape(atob(s.replace(/-/g,'+').replace(/_/g,'/')))));
const normWa=s=>{let d=String(s||'').replace(/\D/g,'');if(d.length===10||d.length===11)d='55'+d;return d};
const normLogin=s=>{s=String(s||'').trim();const m=s.match(/cadastro\/([^/?#\s]+)/i);if(m)s=m[1];return s.replace(/[^\w.\-]/g,'')};
const esc=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let C=null;const mh=location.hash.match(/c=([\w-]+)/);if(mh){try{C=b64d(mh[1])}catch(e){}}
if(!C){location.replace('../');return}
const name=(C.n||'').trim()||'Kaiabí',first=name.split(/\s+/)[0],ini=(name.match(/\b\p{L}/gu)||['K']).slice(0,2).join('').toUpperCase();
const login=normLogin(C.l),wa=normWa(C.w),CAD='https://kaiabi.com/cadastro/'+encodeURIComponent(login);
const waMsg=t=>wa?`https://wa.me/${wa}?text=${encodeURIComponent(t)}`:null;
$('#ngAv').textContent=ini;$('#pAv').textContent=ini;$('#ngNm').textContent=name;$('#nxNm').textContent=first;$('#pBy').textContent='— '+name;
if(C.f&&C.f.trim())$('#pFrase').textContent=C.f.trim();
if(C.v&&/^https?:\/\//.test(C.v)){const v=$('#pVid');v.href=C.v;v.hidden=false;v.textContent='▶ Assistir o depoimento de '+first;v.addEventListener('click',()=>pauseUser())}
const pots=$('#pPots');['calmais','omega','curcu','magseven','protector'].forEach(p=>{const im=new Image();im.src='../../apresentacao/p/p-'+p+'.webp';im.alt='';pots.appendChild(im)});
const goCad=e=>{e&&e.preventDefault();track('cadastro');try{navigator.vibrate&&navigator.vibrate([20,40,30])}catch(_){};location.href=CAD};
$('#nGo').href=CAD;$('#nGo').addEventListener('click',goCad);$('#nxGo').addEventListener('click',goCad);
const wh=waMsg(`Oi, ${first}! Assisti à apresentação da Kaiabí e fiquei com uma dúvida.`);if(wh)$('#nWa').href=wh;else $('#nWa').style.display='none';
/* CTA da institucional vira cadastro */
const plant=$('#plant');if(plant)plant.textContent='Quero entrar: plantar a minha floresta';
const acc=$('#accept');if(acc)acc.innerHTML=`<a href="${CAD}" style="color:#d6c691;font-weight:800">Fazer meu cadastro agora →</a>`;
const mc=$('#mclose');if(mc)mc.textContent='Fazer meu cadastro agora';
document.addEventListener('click',e=>{if(e.target.closest('#mclose')){e.preventDefault();e.stopPropagation();goCad()}},true);
$$('#cta .go li b').forEach(b=>{if(/5 pessoas/.test(b.textContent))b.textContent='Compartilhe com quem você gosta'});

/* roteiro */
const T={
v1:"Antes de começar... me conta: o que você mais quer para os próximos meses? Cuidar melhor da sua família, ter uma renda extra, ou construir um negócio seu? Toque na sua resposta.",
v2a:"Cuidar da saúde de quem a gente ama custa caro... e todo mês o carrinho fica mais pesado. E se você pudesse cuidar de todos, pagando bem menos?",
v2b:"O salário chega... e vai embora rápido. Um dinheiro a mais no fim do mês muda muita coisa. Ainda mais se for sem largar o que você já faz.",
v2c:"Montar um negócio do zero exige estoque, ponto, funcionário... e muito risco. E se você pudesse começar algo seu, sem nada disso?",
v3:"Foi para isso que nasceu a Kaiabí: levar saúde natural às famílias, e abrir um caminho de independência financeira para quem quiser crescer junto. São os melhores produtos naturais, que as pessoas usam, gostam... e voltam a comprar.",
v4:"Quem te mandou esta apresentação já faz parte. Veja o que mudou para essa pessoa.",
v5:"Funciona em três passos, no seu tempo. Você faz o cadastro e recebe seus produtos. Usa, e conta sua experiência. Depois, compartilha com quem você conhece... com alguém do seu lado te ensinando o caminho.",
v6:"No plano Diretor, você recebe R$ 1.800 em produtos... e paga R$ 1.260. Porque a adesão está com 30% de desconto, já aplicado no cadastro. Depois disso, você continua comprando com até 50% de desconto. E o seu lucro começa na primeira venda.",
v7:"Repare: você não paga uma taxa para entrar. O seu dinheiro vira produto, que você usa em casa, ou revende com lucro. E se preferir começar menor, existem planos de entrada.",
v8:"Esta condição vale agora, e pode mudar a qualquer momento. Toque em quero entrar, e faça o seu cadastro. Ficou alguma dúvida? Fale com quem te convidou. Te esperamos na Kaiabí."};
const KEY=/^(família|renda|extra|negócio|Kaiabí:?|Kaiabí\.|saúde|natural|independência|financeira|três|tempo|1\.800|1\.260|30%|50%|lucro|produto|agora|entrar|todos|menos\?|disso\?|faz\.)/i;
const SPOKEN={'R$':0,'1.800':20,'1.260':22,'30%':16,'50%':18};
function phrases(txt){const words=txt.split(/\s+/);const out=[];let cur=[];
 words.forEach(w=>{cur.push(w);if(/[.?!:]$|\.\.\.$/.test(w)&&cur.length>=3||cur.length>=9){out.push(cur);cur=[]}});
 if(cur.length){if(cur.length<=2&&out.length)out[out.length-1].push(...cur);else out.push(cur)}
 let tot=0;const ws=[];out.forEach((ph,pi)=>ph.forEach(w=>{const wt=SPOKEN[w]!=null?SPOKEN[w]:w.replace(/[^\p{L}\d]/gu,'').length+1.2;const pause=/\.\.\.$/.test(w)?7:/[.?!]$/.test(w)?4.5:/[,:]$/.test(w)?2.2:0;ws.push({w,pi,start:tot});tot+=wt;ws[ws.length-1].end=tot;tot+=pause}));
 ws.forEach(x=>{x.s=x.start/tot});return{out,ws}}
const top=el=>el.getBoundingClientRect().top+scrollY;
const E=id=>document.getElementById(id);
const vh=()=>innerHeight;
let goal=null;
const SEG=[
 {a:'v1',from:()=>0,to:()=>E('hero').offsetHeight*.3,wait:true},
 {a:()=>({fam:'v2a',renda:'v2b',neg:'v2c'})[goal],from:()=>top(E('dor')),to:()=>top(E('dor'))+E('dor').offsetHeight-vh()},
 {a:'v3',from:()=>top(E('proposito')),to:()=>top(E('produtos'))+(E('produtos').offsetHeight-vh())*.6},
 {a:'v4',from:()=>top(E('produtos'))+(E('produtos').offsetHeight-vh())*.6,to:()=>top(E('prova'))+E('prova').offsetHeight/2-vh()/2,hold:3.5},
 {a:'v5',from:()=>top(E('como'))-vh()*.05,to:()=>Math.max(top(E('como'))-vh()*.05,top(E('como'))+E('como').offsetHeight-vh()*.85)},
 {a:'v6',from:()=>top(E('planos'))-vh()*.04,to:()=>top($('#planos .stackv'))-vh()*.2,bar:true},
 {a:'v7',from:()=>top($('#planos .stackv'))-vh()*.2,to:()=>Math.max(top($('#planos .stackv'))-vh()*.2,top(E('planos'))+E('planos').offsetHeight-vh())},
 {a:'v8',from:()=>top(E('cta')),to:()=>top(E('cta'))+E('cta').offsetHeight-vh(),end:true}
];
const val=x=>typeof x==='function'?x():x;
const voice=$('#nvoice'),mus=$('#nmus');
let idx=-1,cap=null,lastPi=-2,running=false,manual=false,muted=false,vol=0,advT=0,ended=false,cur=0;
document.body.classList.add('locked');
function play(i){
 clearTimeout(advT);idx=i;lastPi=-2;const s=SEG[i];const k=val(s.a);
 cap=phrases(T[k]);voice.src='../a/'+k+'.mp3';voice.currentTime=0;voice.play().catch(()=>{});
 if(s.bar){document.body.classList.add('barOn');$('#nbar').classList.add('on')}
 if(s.end){track('fim');$('#plant')?.classList.add('pulse');setTimeout(()=>{idle=setTimeout(openExit,25000)},1000)}
 const n=SEG[i+1];if(n&&typeof n.a==='string'){const a=new Audio();a.preload='auto';a.src='../a/'+n.a+'.mp3'}
}
let idle=0;
function renderCap(p){if(!cap)return;let pi=0,act=-1;cap.ws.forEach((w,k)=>{if(p>=w.s){pi=w.pi;act=k}});
 const P=$('#ncap p');if(pi!==lastPi){lastPi=pi;P.innerHTML=cap.out[pi].map(w=>`<span${KEY.test(w)?' class="k"':''}>${esc(w)}</span>`).join(' ')}
 const base=cap.ws.findIndex(w=>w.pi===pi);P.querySelectorAll('span').forEach((s,k)=>s.classList.toggle('on',base+k<=act))}
const ease=t=>t<.5?2*t*t:1-Math.pow(-2*t+2,2)/2;
function frame(){requestAnimationFrame(frame);
 if(!running||idx<0)return;
 const d=voice.duration||0,t=voice.currentTime||0;const p=d?Math.min(1,Math.max(0,(t-.15)/(d-.4))):0;
 renderCap(d?p:-1);
 const s=SEG[idx];
 if(s.wait&&p>.42&&!goal){$('#nsheet').classList.add('on');document.body.classList.add('choosing')}
 if(!manual){const ft=s.from(),tt=s.to();const target=ft+(tt-ft)*ease(voice.ended?1:p);const y=scrollY;const ny=y+(target-y)*.075;if(Math.abs(target-y)>.6){programmatic=true;scrollTo(0,ny)}}
 if(idx===1){const dor=E('dor');const r=dor.getBoundingClientRect();const dp=Math.min(1,Math.max(0,-r.top/(r.height-vh())));dor.style.setProperty('--dp',dp);dor.style.setProperty('--eo',Math.min(1,Math.max(0,(p-.68)/.15)))}
 const target2=muted?0:(voice.paused||voice.ended?(SEG[idx].end?.4:.3):.12);vol+=(target2-vol)*.05;mus.volume=Math.max(0,Math.min(1,vol));
}
let programmatic=false;
voice.addEventListener('ended',()=>{const s=SEG[idx];if(!s||s.wait&&!goal)return;if(s.end){running=false;ended=true;document.body.classList.remove('locked');$('#ncap').style.opacity='0';return}
 advT=setTimeout(()=>{if(!manual&&!$('#nexit').classList.contains('on'))play(idx+1)},(s.hold||1)*1000)});
/* começar */
$('#ngGo').addEventListener('click',()=>{
 $('#ng').classList.add('off');document.body.classList.remove('locked');$('#nmute').classList.add('on');mus.volume=0;mus.play().catch(()=>{});
 try{const v=E('vid');v&&v.play()}catch(_){}
 scrollTo(0,0);running=true;history.pushState({k:1},'');track('inicio');play(0);
});
/* escolha */
$$('#nsheet .nch').forEach(b=>b.addEventListener('click',()=>{
 goal=b.dataset.g;$('#nsheet').classList.remove('on');document.body.classList.remove('choosing');
 try{navigator.vibrate&&navigator.vibrate(18)}catch(_){}
 $('#dImg').src='../i/d-'+goal+'.webp';$('#dKick').textContent={fam:'Quem cuida de uma família sabe',renda:'Quem vive de salário sabe',neg:'Quem já tentou empreender sabe'}[goal];
 track('objetivo_'+goal);setTimeout(()=>play(1),500);
}));
/* rolagem manual pausa a narração */
function pauseUser(){if(!running||manual)return;manual=true;voice.pause();clearTimeout(advT);$('#npill').classList.add('on')}
['wheel','touchmove'].forEach(ev=>addEventListener(ev,e=>{if(running&&!e.target.closest('#nsheet,#nexit'))pauseUser()},{passive:true}));
addEventListener('keydown',e=>{if(running&&/Arrow|Page|Space|Home|End/.test(e.code))pauseUser()});
$('#npill').addEventListener('click',()=>{manual=false;$('#npill').classList.remove('on');if(voice.ended){const s=SEG[idx];if(!(s.wait&&!goal)&&!s.end)play(idx+1)}else voice.play().catch(()=>{})});
$('#nmute').addEventListener('click',()=>{muted=!muted;voice.muted=muted;$('#nmute').style.opacity=muted?.5:1});
document.addEventListener('visibilitychange',()=>{if(document.hidden){voice.pause();mus.pause()}else if(running||ended){mus.play().catch(()=>{});if(running&&!manual&&!voice.ended)voice.play().catch(()=>{})}});
/* pop-up de saída */
let shown=false;
function openExit(){if(shown||!(running||ended))return;shown=true;voice.pause();$('#nexit').classList.add('on');track('popup')}
function closeExit(){$('#nexit').classList.remove('on');if(running&&!manual){if(voice.ended){const s=SEG[idx];if(!s.end&&!(s.wait&&!goal))play(idx+1)}else voice.play().catch(()=>{})}}
addEventListener('popstate',()=>{if(!shown&&(running||ended)){openExit();history.pushState({k:2},'')}});
document.addEventListener('mouseout',e=>{if(!e.relatedTarget&&e.clientY<8&&idx>=1)openExit()});
$('#nxX').addEventListener('click',closeExit);
$('#nxF').addEventListener('submit',e=>{e.preventDefault();const f=new FormData(e.target);const n=String(f.get('n')).trim(),w=String(f.get('w')).trim();track('lead');
 const u=waMsg(`Oi, ${first}! Sou ${n} (${w}). Assisti à apresentação da Kaiabí e quero saber mais sobre os 30% de desconto na adesão.`);location.href=u||CAD});
function track(ev){try{window.dataLayer=window.dataLayer||[];dataLayer.push({event:'kaiabi_convite3d',step:ev,login})}catch(_){}}
window.__n={play:i=>{running=true;document.body.classList.remove('locked');$('#ng').classList.add('off');play(i)},seek:f=>{voice.currentTime=(voice.duration||10)*f},pick:g=>$('#nsheet .nch[data-g='+g+']').click()};
frame();
})();
