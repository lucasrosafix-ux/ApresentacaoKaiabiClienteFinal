/* Dados do portal (versão 1, sem banco). Quando o Supabase estiver ligado, estes dados passam a vir do banco. */
window.KP = {
  grupos: {
    sono:{n:'Sono',c:'#172554'}, foco:{n:'Foco',c:'#5B1F4F'}, detox:{n:'Detox',c:'#1F6B63'},
    articulacoes:{n:'Articulações',c:'#8A1F6B'}, imunidade:{n:'Imunidade',c:'#C2560C'},
    energia:{n:'Energia',c:'#111827'}, natural:{n:'Extratos e minerais',c:'#2F4A35'}, beleza:{n:'Pele e cabelo',c:'#5A2A7A'}
  },
  produtos: {
    calmais:{n:'Calmais',g:'sono',l:'Para desacelerar a cabeça e encontrar equilíbrio no dia a dia.',c:'#172554'},
    treonato:{n:'Treonato Neuro',g:'foco',l:'A forma de magnésio escolhida por quem quer a cabeça em dia.',c:'#5B2A86'},
    omega:{n:'Ômega Super DHA & EPA',g:'foco',l:'Alta concentração de DHA e EPA, com selo MEG-3.',c:'#5B1F4F'},
    magseven:{n:'Mag Seven',g:'energia',l:'Seis formas de magnésio num pote só.',c:'#2E2A7A'},
    lithokit:{n:'LithoKit',g:'detox',l:'O trio da rotina de leveza num pedido só.',c:'#5E2366'},
    lithocaps:{n:'LithoCaps 90',g:'detox',l:'Minerais das algas do mar para a sua rotina.',c:'#5E2366'},
    lithopo:{n:'LithoCaps em Pó',g:'detox',l:'Os minerais do LithoCaps, em pó.',c:'#7B1D6E'},
    dextro:{n:'DextroMalic',g:'detox',l:'Para o seu dia começar mais leve.',c:'#1F6B63'},
    sal:{n:'Sal Amargo',g:'detox',l:'O clássico sal de Epsom no ritual de leveza.',c:'#24484A'},
    carvao:{n:'Carvão Ativado Black Active',g:'detox',l:'Carvão ativado em pó para completar o ritual.',c:'#161616'},
    lkeco:{n:'LithoKit Econômico',g:'detox',l:'O trio da rotina de leveza em embalagem econômica.',c:'#6B1E62'},
    lkprime:{n:'LithoKit Prime',g:'detox',l:'DextroMalic e Sal Amargo em sachês, prontos para levar.',c:'#5E1C5B'},
    curcu:{n:'CURCU+',g:'articulacoes',l:'Cúrcuma com vitamina E para quem se mexe todo dia.',c:'#8A1F6B'},
    artro:{n:'ArtroFlex',g:'articulacoes',l:'O parceiro do CURCU+ na rotina de movimento.',c:'#2952A3'},
    protector:{n:'Protector',g:'imunidade',l:'Minerais essenciais para a defesa em dia.',c:'#0F1B24'},
    nac:{n:'NAC',g:'imunidade',l:'600 mg de NAC com selênio, para a sua defesa antioxidante.',c:'#D9620F'},
    polivit:{n:'Polivitamínico + NAC',g:'imunidade',l:'De A a Z num pote só.',c:'#4A1F66'},
    powerfit:{n:'Power Fit',g:'energia',l:'Creatina com minerais das algas, para treinar com tudo.',c:'#111827'},
    coq10:{n:'Coenzima Q10',g:'energia',l:'100 mg de Q10 para a energia que vem de dentro.',c:'#6E1C5E'},
    rnx:{n:'RNX10',g:'energia',l:'Creatina líquida com vitaminas B2 e B3, sabor frutas cítricas.',c:'#9B1B2D'},
    kaiamist:{n:'Kaia Mist',g:'beleza',l:'Cabelo perfumado, macio e com toque sedoso o dia inteiro.',c:'#3A1D4D'},
    golden:{n:'Golden Drops',g:'beleza',l:'Pontas seladas, menos frizz e brilho de cabelo cuidado.',c:'#3B1A4C'},
    ozon:{n:'Ozon Clean',g:'beleza',l:'Limpeza suave com partículas douradas.',c:'#7a5a1c'},
    biosoft:{n:'Bio Soft',g:'beleza',l:'Óleo de girassol ozonizado para a sua rotina de cuidado com a pele.',c:'#8a6418'},
    creme:{n:'Creme Restaurador',g:'beleza',l:'Hidratação profunda para pés, joelhos e cotovelos ressecados.',c:'#5a3d8a'},
    peeling:{n:'Peeling Kaiabí',g:'beleza',l:'Esfoliação ultrassuave para uma pele lisa e renovada.',c:'#1f6a92'},
    micrantha:{n:'Tintura de Micrantha',g:'natural',l:'Extrato vegetal de Trema micrantha para o seu cuidado integrativo.',c:'#2F6B3A'},
    antipar:{n:'Tintura AntiPar',g:'natural',l:'Blend de extratos vegetais de uso tradicional.',c:'#151313'},
    ormus:{n:'Órmus Elixir da Vida',g:'natural',l:'Minerais de origem marinha, feito de forma artesanal.',c:'#4A1E50'},
    prata:{n:'Prata Coloidal Estruturada',g:'natural',l:'Solução mineral coloidal com partículas de alta estabilidade.',c:'#4B2050'}
  },
  aulas: [
    {t:'comece',id:'c1',titulo:'Seu primeiro dia',min:3,txt:[
      'Abra a aba Ferramentas e assista à sua própria apresentação, com som, do começo ao fim. Você precisa saber o que o seu convidado vai ver.',
      'Escreva uma lista com 20 nomes: família, amigos, colegas, vizinhos. Não julgue ninguém agora, só escreva.',
      'Envie o seu convite para 3 pessoas da lista hoje. Mensagem curta e verdadeira funciona melhor do que texto longo.'],
      check:['Assisti à minha apresentação','Fiz a lista de 20 nomes','Enviei 3 convites']},
    {t:'comece',id:'c2',titulo:'Como convidar sem parecer vendedor',min:4,txt:[
      'Fale da sua experiência, não da empresa: o que você usa, por que começou, o que mudou na sua rotina.',
      'Peça licença antes de mandar o link: "Posso te mandar uma apresentação de 3 minutos? Assiste com som."',
      'Depois de 24 horas, pergunte o que a pessoa achou. Quem pergunta, cadastra mais.'],
      check:['Escrevi minha mensagem de convite','Fiz o acompanhamento de quem recebeu']},
    {t:'comece',id:'c3',titulo:'O que nunca falar',min:3,txt:[
      'Nunca diga que um produto cura, trata ou previne doenças. Produtos naturais complementam a rotina; quem cuida de doença é o profissional de saúde.',
      'Nunca prometa quanto a pessoa vai ganhar. Mostre como o plano funciona e deixe claro que o resultado depende da dedicação de cada um.',
      'Nunca use foto ou depoimento de outra pessoa como se fosse seu. Verdade é o que constrói a sua reputação.'],
      check:['Li e entendi as regras']},
    {t:'organico',id:'o1',titulo:'Status do WhatsApp: a vitrine que você já tem',min:4,txt:[
      'Poste 3 a 5 status por dia: um produto (use a aba Mídias), um momento da sua rotina e um convite.',
      'Status com rosto e voz tem mais visualizações. Um vídeo de 15 segundos contando como foi o seu dia com o produto vale mais que 10 fotos.',
      'Responda todo mundo que reagir. Cada reação é uma conversa aberta.'],
      check:['Postei 3 status hoje','Respondi quem reagiu']},
    {t:'organico',id:'o2',titulo:'Instagram: perfil que convida',min:5,txt:[
      'Na bio, diga em uma linha o que você faz e coloque o link do seu site ou do seu convite.',
      'Stories todos os dias, feed 3 vezes por semana. Use as mídias prontas e acrescente uma frase sua.',
      'Reels de rotina (manhã, treino, cuidado com a pele) alcançam quem ainda não te segue.'],
      check:['Atualizei minha bio com o link','Postei um Reels de rotina']},
    {t:'organico',id:'o3',titulo:'Grupos e comunidades',min:4,txt:[
      'Grupos de bairro, de mães, de academia e de igreja são lugares de confiança. Entre para participar, não para fazer propaganda.',
      'Ajude primeiro: responda dúvidas, compartilhe algo útil. Ofereça o produto só quando fizer sentido na conversa.',
      'Respeite a regra de cada grupo. Spam queima o seu nome.'],
      check:['Entrei em 2 grupos do meu interesse','Contribuí sem vender']},
    {t:'organico',id:'o4',titulo:'TikTok e Kwai: alcance de graça',min:4,txt:[
      'Vídeos de 15 a 30 segundos, com o começo forte: a primeira frase decide se a pessoa continua.',
      'Formatos que funcionam: "minha rotina da manhã", "o que tem na minha bolsa", "unboxing do meu kit".',
      'Poste todo dia por 30 dias antes de avaliar o resultado.'],
      check:['Postei meu primeiro vídeo']},
    {t:'pago',id:'p1',titulo:'Antes de pagar anúncio',min:3,txt:[
      'Anúncio acelera o que já funciona. Primeiro, tenha pelo menos 5 convites enviados e uma conversa por dia no orgânico.',
      'Defina quanto pode investir por mês sem apertar o orçamento. Comece pequeno, com R$ 10 a R$ 20 por dia.',
      'Anúncio de produto natural não pode prometer cura nem resultado de saúde. Anúncio de oportunidade não pode prometer ganho.'],
      check:['Defini meu orçamento mensal']},
    {t:'pago',id:'p2',titulo:'Meta Ads (Instagram e Facebook)',min:6,txt:[
      'Use o Gerenciador de Anúncios, não o botão "Impulsionar". Objetivo: Engajamento com mensagens no WhatsApp, ou Tráfego para o seu site.',
      'Público: sua cidade e um raio de até 30 km, idade de 25 a 55 anos, interesses em bem-estar e vida saudável. Deixe o público aberto o bastante para o algoritmo aprender.',
      'Teste 3 criativos diferentes com o mesmo valor. Depois de 3 a 5 dias, desligue os 2 piores e coloque a verba no melhor.'],
      check:['Criei minha conta de anúncios','Subi 3 criativos de teste']},
    {t:'pago',id:'p3',titulo:'Google Ads',min:5,txt:[
      'O Google pega quem já está procurando. Anúncios de pesquisa com o nome dos produtos e da Kaiabí funcionam bem para vender produto.',
      'Comece com palavras específicas, como "comprar cúrcuma com vitamina E", em vez de termos amplos que gastam rápido.',
      'Mande o clique para a página do produto no seu site, não para a página inicial.'],
      check:['Listei 10 palavras-chave']},
    {t:'pago',id:'p4',titulo:'TikTok Ads e Kwai Ads',min:4,txt:[
      'Aqui, anúncio bom parece vídeo normal. Use o mesmo vídeo orgânico que teve mais visualizações.',
      'Objetivo: tráfego para o site ou mensagens. Comece com o valor mínimo da plataforma por 5 dias.',
      'Troque o criativo a cada 1 ou 2 semanas: o público cansa rápido nessas plataformas.'],
      check:['Escolhi meu melhor vídeo orgânico para anunciar']}
  ],
  trilhas: {comece:'Comece por aqui', organico:'Divulgação orgânica (grátis)', pago:'Tráfego pago (anúncios)'}
};
