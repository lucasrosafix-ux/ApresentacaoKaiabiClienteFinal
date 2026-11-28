#!/usr/bin/env python3
"""Gera plano.html (Plano de Negócios Kaiabí) para os formatos desktop (16:9) e mobile (9:16)."""
import sys, pathlib
HERE = pathlib.Path(__file__).parent
LOGO = (HERE / 'logo.svg').read_text().replace('<svg ', '<svg class="logo" ', 1)

def brl(n):
    return 'R$ ' + f'{n:,.0f}'.replace(',', '.')

LV = [  # nome, pontos, ativos diretos, bonus %, VME %, cor
    ('Bronze', 2000, 4, 5, 50, '#a8653f'),
    ('Prata', 6000, 4, 8, 50, '#9aa0a8'),
    ('Ouro', 15000, 4, 11, 40, '#c39a3a'),
    ('Rubi', 30000, 5, 14, 40, '#c8344a'),
    ('Diamante', 60000, 6, 20, 30, '#2b9fc4'),
    ('Duplo Diamante', 200000, 8, 20, 25, '#2b9fc4'),
    ('Triplo Diamante', 600000, 12, 20, 25, '#2b9fc4'),
    ('Ônix', 1500000, 12, 20, 20, '#3d8f98'),
    ('Imperial Ônix', 3000000, 12, 20, 20, '#2a6d74'),
]
PLANS = [
    dict(n='Starter Básico', tab=400, inv=280, pts=93, rec=40, net=False, ir=None, kit=False),
    dict(n='Empreendedor Pró', tab=800, inv=560, pts=187, rec=50, net=True, ir='3 gerações', kit=True),
    dict(n='Diretor Pró+', tab=1800, inv=1260, pts=420, rec=50, net=True, ir='5 gerações', kit=True, top=True),
]
# Simulação da apresentação: Diretor Pró+, R$ 200 por pessoa, 5 indicados por pessoa
SIM = [  # geração, pessoas na rede, ativação, início rápido, carreira, economia, total, graduação
    (1, 5, 40, 50, 0, 50, 140, '—'),
    (2, 30, 240, 175, 0, 50, 465, '—'),
    (3, 155, 1240, 581, 624, 50, 2495, 'Prata'),
    (4, 780, 6240, 2269, 2347, 50, 10906, 'Rubi'),
    (5, 3905, 31240, 7738, 2, 50, 39030, 'Rubi'),
]

def page(cls, inner, n=None, dark=False):
    foot = '' if n is None else f'<footer class="pf"><span>Plano de Negócios Kaiabí · 2026</span><span>{n}</span></footer>'
    return f'<section class="pg {cls}{" dark" if dark else ""}">{inner}{foot}</section>'

def build(fmt):
    P = []
    # 1 CAPA
    P.append(page('cover', f'''
      <img class="cbg" src="hero.jpg" alt="">
      <div class="cin">{LOGO}
        <p class="kick">Plano de Negócios 2026</p>
        <h1>Saúde para a sua família. Uma renda que cresce com quem você ajuda.</h1>
        <p class="lead">Uma floresta não cresce de uma árvore só. Veja como cuidar de quem você ama, conquistar a sua independência e ganhar com a Kaiabí, em regras claras e por escrito.</p>
      </div>''', dark=True))
    # 2 SONHO
    P.append(page('', f'''
      <p class="kick">Para onde você vai</p>
      <h2>Saúde em casa. <em>Independência para a sua vida.</em></h2>
      <p class="lead">A Kaiabí escolhe a dedo produtos naturais para cuidar de quem você ama e abre um caminho de renda para quem compartilha esse cuidado. Quem constrói, colhe.</p>
      <div class="g3 dream">
        <div class="card"><b>Cuidar da família</b><p>Tudo o que a sua casa consome com até 50% de desconto.</p></div>
        <div class="card"><b>Uma renda extra</b><p>Lucro em cada venda e bônus sobre as pessoas que você indica.</p></div>
        <div class="card"><b>Um negócio próprio</b><p>Uma rede que cresce, graduações e bônus todo mês.</p></div>
      </div>
      <div class="pots"><img src="p-calmais.webp" alt=""><img src="p-omega.webp" alt=""><img src="p-curcu.webp" alt=""><img src="p-protector.webp" alt=""><img src="p-antipar.webp" alt=""></div>
    ''', 2))
    # 3 MERCADO
    P.append(page('', f'''
      <p class="kick">Por que agora</p>
      <h2>O mercado já existe. <em>Só falta você nele.</em></h2>
      <div class="stats">
        <div class="stat big"><strong>R$ 50 bi</strong><span>movimentados pela venda direta no Brasil em 2024, crescendo 6,5% no ano.</span></div>
        <div class="stat"><strong>7º</strong><span>maior mercado de venda direta do mundo. O Brasil lidera a América Latina.</span></div>
        <div class="stat"><strong>3,1 mi</strong><span>de revendedores ativos no país.</span></div>
        <div class="stat"><strong>76%</strong><span>conciliam a venda direta com outro trabalho. Não precisa largar o emprego.</span></div>
        <div class="stat"><strong>80%</strong><span>das vendas do setor já acontecem pelo WhatsApp. O seu celular é a sua loja.</span></div>
      </div>
      <p class="fn">Fontes: ABEVD; ABEVD/WFDSA; Pesquisa Perfil da Força de Vendas ABEVD/Bare International.</p>
    ''', 3))
    # 4 PRODUTOS
    PRD = [('p-curcu.webp','CURCU+',146),('p-omega.webp','Ômega Super DHA & EPA',204),('p-calmais.webp','Calmais',149),('p-protector.webp','Protector',184),('p-magseven.webp','Mag Seven',159.9),('p-lithokit.webp','LithoKit',227)]
    def money(v):
        return ('R$ ' + f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')).replace(',00', '')
    pc = ''.join(f'<div class="pc"><img src="{i}" alt=""><b>{n}</b><span>{money(v)}</span><em>lucro até {money(v/2)}</em></div>' for i, n, v in PRD)
    P.append(page('', f'''
      <p class="kick">O veículo</p>
      <h2>Produtos que a sua família usa primeiro. <em>E indica com orgulho.</em></h2>
      <p class="lead sm">Os melhores produtos naturais para a rotina da casa: sono, foco, imunidade, articulações, energia, leveza, pele e cabelo. Você compra com até 50% de desconto e revende pelo preço de tabela.</p>
      <div class="pgrid">{pc}</div>
      <p class="fn">Preços de tabela. Lucro calculado com 50% de desconto (Empreendedor e Diretor). Suplementos alimentares não são medicamentos.</p>
    ''', 4))
    # 5 COMO FUNCIONA
    P.append(page('', f'''
      <p class="kick">Como funciona</p>
      <h2>Saúde pega. <em>Começa em você.</em></h2>
      <p class="lead">Quem usa, inspira. Você cuida da sua casa com desconto, e quem convive com você quer o mesmo.</p>
      <div class="g3 steps">
        <div class="card"><span class="nb">1</span><b>Você usa</b><p>Os produtos entram na rotina da sua casa com até 50% de desconto.</p></div>
        <div class="card"><span class="nb">2</span><b>Os seus perguntam</b><p>Família e amigos veem a sua nova rotina e querem também.</p></div>
        <div class="card"><span class="nb">3</span><b>Eles entram</b><p>Compram com desconto e fazem o mesmo com as pessoas deles.</p></div>
      </div>
      <div class="five"><strong>Seu trabalho cabe numa frase:</strong> <span>5 pessoas, bem cuidadas.</span> Escolha 5, seja a referência para elas e caminhe junto até cada uma ter as suas 5.</div>
    ''', 5))
    # 6 NOVE FORMAS
    MOV = [
        ('Vender', 'Seu primeiro ganho: já na primeira venda', [('Lucro sobre vendas', '40% a 50%', 'Compre com desconto e revenda pelo preço de tabela.'), ('Link de loja', '25%', 'Sobre as compras do cliente final no seu link.'), ('Cliente VIP', '25%', 'Sobre o valor líquido das compras dos VIP que você indicou.')]),
        ('Indicar', 'Empreendedor e Diretor', [('Bônus de ativação', 'R$ 8', 'Por pessoa ativa na sua rede, até a 5ª geração.'), ('Início rápido', 'até 45,4%', 'Soma das 5 gerações do Diretor sobre a pontuação da equipe.'), ('Venda de kit', '27%', 'Sobre o kit de adesão de quem você indica.')]),
        ('Liderar', 'Empreendedor e Diretor', [('Plano de carreira', '5% a 20%', 'Sobre o volume da sua rede, por diferença.'), ('Liderança Elite', '3%, 2%, 1%', 'Sobre os Elites que você forma, em 3 gerações.'), ('Continental', '5% global', 'Fatia da pontuação global em brindes ao topo.')]),
    ]
    k = 0; cols = ''
    for t, sub, items in MOV:
        li = ''
        for a2, v, d in items:
            k += 1
            li += f'<li><span class="nb sm">{k}</span><div><b>{a2}</b><p>{d}</p></div><strong>{v}</strong></li>'
        cols += f'<div class="mov"><h3>{t}</h3><small>{sub}</small><ul>{li}</ul></div>'
    P.append(page('', f'''
      <p class="kick">Como se ganha</p>
      <h2>Nove formas de ganhar, <em>em três movimentos.</em></h2>
      <p class="lead">Comece pelo primeiro: vender o que você já usa dá lucro já na primeira venda. Os outros vêm com o tempo, conforme a sua rede cresce.</p>
      <div class="g3 movs">{cols}</div>
    ''', 6))
    # 7 POR GERAÇÃO + REGRAS DO MÊS
    gens = [('1ª', 20, 10), ('2ª', 10, 6), ('3ª', 6.5, 6), ('4ª', 5.4, None), ('5ª', 3.5, None)]
    def pct(x):
        return '—' if x is None else (f'{x:g}%'.replace('.', ','))
    rows = ''.join(f'<tr><td>{g}</td><td>R$ 8</td><td>{pct(d)}</td><td>{pct(e)}</td></tr>' for g, d, e in gens)
    P.append(page('', f'''
      <p class="kick">Bônus da rede, geração a geração</p>
      <h2>A cada pessoa ativa, <em>você ganha. Todo mês.</em></h2>
      <div class="g2 wide">
        <table class="tb"><thead><tr><th>Geração</th><th>Ativação por pessoa ativa</th><th>Início rápido Diretor Pró+</th><th>Início rápido Empreendedor</th></tr></thead>
        <tbody>{rows}<tr class="tot"><td>Total</td><td>até a 5ª</td><td>45,4%</td><td>22%</td></tr></tbody></table>
        <div class="notes">
          <div class="rule"><b>Ativação do mês</b><p>Os primeiros R$ 100 em produtos do mês ativam a pessoa, em preço cheio. Acima disso vale o desconto (50% no Empreendedor e no Diretor, 40% no Starter).</p></div>
          <div class="rule"><b>Pontos</b><p>Cada R$ 3 pagos geram 1 ponto, e cada ponto vale R$ 1. Quem compra R$ 200 paga R$ 150 e gera 50 pontos.</p></div>
          <div class="rule"><b>Venda de kit</b><p>27% sobre o kit de quem você indica: R$ 340 no Diretor, R$ 151 no Empreendedor e R$ 76 no Starter.</p></div>
        </div>
      </div>
    ''', 7))
    # 8 SIMULAÇÃO
    srow = ''.join(f'<tr><td>{g}ª</td><td>{f"{n:,}".replace(",", ".")}</td><td>{brl(a3)}</td><td>{brl(i)}</td><td>{brl(c)}</td><td>{brl(e)}</td><td class="hl">{brl(t)}</td><td>{gr}</td></tr>' for g, n, a3, i, c, e, t, gr in SIM)
    mx = max(x[6] for x in SIM)
    bars = ''.join(f'<div class="bar"><b>{brl(t)}</b><i style="--h:{max(4, t/mx*100):.1f}%"></i><span>{g}ª</span></div>' for g, n, a3, i, c, e, t, gr in SIM)
    P.append(page('', f'''
      <p class="kick">Simulação 5 × 5</p>
      <h2>Quando cada pessoa ensina as suas 5 <em>a fazer o mesmo.</em></h2>
      <p class="lead sm">Plano Diretor Pró+, cada pessoa da rede comprando R$ 200 por mês e indicando 5. Valores mensais.</p>
      <div class="g2 wide sim">
        <table class="tb"><thead><tr><th>Rede até a</th><th>Pessoas</th><th>Ativação</th><th>Início rápido</th><th>Carreira</th><th>Economia</th><th>Total/mês</th><th>Graduação</th></tr></thead><tbody>{srow}</tbody></table>
        <div class="bars">{bars}</div>
      </div>
      <p class="fn">Ilustração com as regras do plano e toda a rede ativa. Na entrada dos seus 5 indicados há ainda R$ 756 de bônus de kit, uma única vez. Na 5ª geração a carreira por diferença cai porque a equipe abaixo também está graduada. Não é promessa de ganho: o resultado depende do trabalho de cada um.</p>
    ''', 8))
    # 9 CARREIRA
    crow = ''.join(f'<tr><td><i style="background:{c}"></i>{n}</td><td>{f"{p:,}".replace(",", ".")}</td><td>{a4}</td><td>{b}%</td><td>{v}%</td><td>≈ {brl(p*b/100)}</td></tr>' for n, p, a4, b, v, c in LV)
    steps = ''.join(f'<div class="st" style="--h:{18+i*10}%;--c:{c}"><span>{n.replace(" Diamante"," Diam.")}</span></div>' for i, (n, p, a4, b, v, c) in enumerate(LV))
    P.append(page('', f'''
      <p class="kick">Plano de carreira</p>
      <h2>Cada degrau tem <em>nome, meta e prêmio.</em></h2>
      <div class="g2 wide car">
        <div><table class="tb"><thead><tr><th>Graduação</th><th>Pontos no mês</th><th>Ativos diretos</th><th>Bônus</th><th>VME por linha</th><th>Bônus estimado/mês*</th></tr></thead><tbody>{crow}</tbody></table>
        <p class="fn">* Estimativa no mínimo de pontos de cada graduação (pontos × percentual; 1 ponto = R$ 1), antes de descontar as graduações da sua equipe. Não é garantia de ganho. VME = volume máximo que conta de uma única linha.</p></div>
        <div class="stairs">{steps}</div>
      </div>
    ''', 9))
    # 10 DIFERENÇA
    P.append(page('', f'''
      <p class="kick">Como a carreira é paga</p>
      <h2>Por diferença: <em>ninguém recebe duas vezes pelo mesmo ponto.</em></h2>
      <div class="g2">
        <div class="diff">
          <p class="lead sm">Cada pessoa recebe o percentual da própria graduação. Quem está acima recebe só a diferença. É o único bônus sem limite de profundidade.</p>
          <div class="ex"><div class="exr"><span class="pill" style="--c:#c39a3a">Você · Ouro 11%</span></div>
          <div class="exr"><span class="pill" style="--c:#a8653f">Sua indicada · Bronze 5%</span></div>
          <div class="exr res"><b>Nos pontos da linha dela:</b> ela recebe 5% e você recebe 11% − 5% = <strong>6%</strong>.</div></div>
        </div>
        <div>
          <div class="rule"><b>Liderança Elite</b><p>De Diamante para cima, você é Elite e ganha sobre os Elites que você forma: 3% na 1ª geração, 2% na 2ª e 1% na 3ª.</p></div>
          <div class="rule"><b>Bônus Continental</b><p>A Kaiabí separa 5% da pontuação global da rede, em brindes, para o topo: Duplo Diamante 20%, Triplo Diamante 30%, Ônix e Imperial Ônix 50%.</p></div>
          <div class="rule"><b>Pontuação do mês</b><p>Conta adesão, recompra, upgrade e loja virtual, sem acumular de um mês para o outro.</p></div>
        </div>
      </div>
    ''', 10))
    # 11 A OFERTA
    cards = ''.join(f'''<div class="plan{' top' if p.get('top') else ''}">{'<span class="tag">Todos os bônus</span>' if p.get('top') else ''}
        <b class="pn">{p['n']}</b><div class="pv"><span>Você recebe</span><strong>{brl(p['tab'])} em produtos</strong></div><div class="pr"><span>e paga</span> <strong>{brl(p['inv'])}</strong></div>
        <ul><li><span>Desconto na recompra</span><b>{p['rec']}%</b></li>
        <li><span>Pontos na adesão</span><b>{p['pts']} pts</b></li>
        <li><span>Ganhos de rede</span><b class="{'' if p['net'] else 'no'}">{'Incluso' if p['net'] else 'Não incluso'}</b></li>
        <li><span>Início rápido</span><b class="{'' if p['ir'] else 'no'}">{p['ir'] or 'Não incluso'}</b></li>
        <li><span>Bônus de venda de kit</span><b class="{'' if p['kit'] else 'no'}">{'27%' if p['kit'] else 'Não incluso'}</b></li></ul></div>''' for p in PLANS[::-1])
    P.append(page('', f'''
      <p class="kick">A oferta</p>
      <h2>Você entra levando <em>mais do que paga.</em></h2>
      <div class="stack">
        <div class="si"><b>Kit de produtos</b><span>30% de desconto na adesão</span></div>
        <div class="si"><b>Seu link de loja</b><span>o cliente compra e recebe em casa</span></div>
        <div class="si"><b>Escritório virtual</b><span>pontos, rede e bônus na palma da mão</span></div>
        <div class="si"><b>Até 50% de desconto</b><span>em todas as recompras, todo mês</span></div>
        <div class="si"><b>Loja e Cliente VIP</b><span>25% sobre as compras de quem você indica</span></div>
      </div>
      <div class="g3 plans">{cards}</div>
    ''', 11))
    # 12 RISCO ZERO + PRÓXIMO PASSO
    P.append(page('end', f'''
      <p class="kick">Sem risco escondido</p>
      <h2>A sua floresta <em>começa hoje.</em></h2>
      <div class="safe dk">
        <span>Sem estoque obrigatório: o cliente compra pelo seu link e recebe em casa.</span>
        <span>A ativação de R$ 100 é só nos meses em que você quiser receber os bônus da rede.</span>
        <span>O que você compra é produto que você e a sua família usam.</span>
      </div>
      <ol class="go">
        <li><b>Escolha seu plano</b><span>Starter, Empreendedor ou Diretor, com 30% de desconto na adesão.</span></li>
        <li><b>Ative seu link de loja</b><span>O cliente compra por ele e recebe direto em casa.</span></li>
        <li><b>Convide as suas 5 pessoas</b><span>Gente que você quer ver bem: da sua casa, do trabalho, da amizade.</span></li>
      </ol>
      <p class="cta">Fale com quem te apresentou a Kaiabí para fazer o seu cadastro.</p>
      <p class="legal">Suplementos alimentares não são medicamentos. Valores e percentuais conforme o plano vigente em 2026; simulações são ilustrativas e não garantem ganhos. Na Kaiabí, todo bônus nasce de um produto que alguém comprou e usou.</p>
      <div class="endlogo">{LOGO}</div>
    ''', 12, dark=True))
    W, H = (1600, 900) if fmt == 'd' else (600, 1067)
    css = (HERE / 'style.css').read_text()
    return f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><title>Plano de Negócios Kaiabí 2026</title>
<style>:root{{--W:{W}px;--H:{H}px}}@page{{size:{W}px {H}px;margin:0}}{css}</style></head>
<body class="{fmt}">{''.join(P)}</body></html>'''

if __name__ == '__main__':
    for f in ('d', 'm'):
        (HERE / f'plano-{f}.html').write_text(build(f))
    print('ok')
