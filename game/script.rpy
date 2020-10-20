# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Narrador", color="#ffffff")
define m = Character("Mãe", color="#c8ffc8")
define c = Character("Chest", color="#c8aac8")
define ve = Character("Velho Lixeiro", color="#c800aa")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    n "Zarkan a cidade comum."
    n "Quando TombCity, a antiga capital, ergueu-se da última vez contra todas as outras cidades"
    n "Homem e máquina já avançavam juntos, a robótica trouxe aprimoramentos, e os aprimoramentos trouxeram a ganância"
    n "A ganância trouxe a GUERRA"
    n "Todas as outras cidades entraram em conflito com TombCity."
    n "Menor, porém com um exército poderoso, sua forma de agir era : chegar e destruir. "
    n "Mas dessa vez não foi assim...as cidades sofreram, mas TombCity caiu junto"
    n "O Clero e os nobres se reuniram e decidiram formam um novo governo, um governo justo, um governo comum"
    n "Nasce a grande cidade de Zarkan."

label prologo:
    n "Zarkan a cidade da tecnologia e da divisão"
    n "Robôs e Homens, desde a guerra, dentro de Zarkan, tornaram-se aliados"
    n "Não mais existia a servidão dos robôs, então os velhos hábitos do poderio voltaram: a servidão dos homens"
    n "Zarkan foi dividida em castas: "
    n "Periféricos: onde está a maioria da população, pobres, sem identifidade e recursos para o aprimoramento"
    n "a mercê dos ricos e poderosos e das gangues dominantes"
    n "Barramento: são as zonas de conflito. As divisões geraram os bairros da nova metrópole, e seu setor de controle são fixados nos Barramentos, zonas de guerra antigas ainda úteis, usadas para desova do poder controlador, das gangues de aprimoramentos."
    n "Processamento: é a divisão de trabalho onde poderosos nobres vivem e são servidos pelos periféricos e pelos próprios nobres. Os nobres exercem poder sobre as gangues, encaracendo o preço dos produtos ou usando da violência para fazer parte de uma casta"
    n "A Unidade Central é o lar dos intocáveis. Pessoas com alto aprimoramento. Robôs tão importantes que são considerados humanos. Nenhum periférico conseguiu chegar a Unidade Central."

label inicio:
    m "Hora de acordar!"
    m "Seu amigo Chest está lá em cima"
    m "É melhor se apressar senão ele vai devorar todo o café-da-manhã"
    c "E aí meu irmão? "
    menu:
       c "Pronto para o segundo dia de trabalho na Shopping Encantado?"
       "Onde é isso mesmo?":
           c "Ihh! o cara tá dormindo ainda..."
           c "É o lixão mesmo!" 
       "Lixão você quer dizer, né?":
           c "O cara tá ligado!"

    c "Parece que a gangue do norte entrou em confronto aqui com o sul de novo..."
    m "Eu acho que o Sul vai desaparecer em breve, eles tentam nos ajudar mas..."
    c "Eu não confio em nenhum deles!"   
    c "Agora as coisas vão esquentar, porque o Sul fica dizendo que tem um traidor"
    c "O Norte quer mais combustível. E nós aqui no meio dessa confusão"
    m "O último conflito deles deixou mais de 100 feridos e vários desabrigados, morreu mais de 300 pessoas"
    c "Tia! Ontem também não foi diferente"
    m "Até onde vai isso? Onde estão os legisladores da Unidade Central?"
    c "Estão lá com seu combustível, muita comida na mesa e enchendo os bolsos com nosso trabalho..."
    m "Estamos sem esperança.."
    c "Verdade...com ou sem esperança, já temos que ir! Brigado tia a comida tava ótima!"
    m "Cuidado filho, bom trabalho pra vocês!"
    jump caminho_secao_lixao

label caminho_secao_lixao:
    menu: 
       "Ei cara, lembrei de uma parada que tenho que fazer..."
       "Sua namorada de novo?...A mulher tá pegando no seu pé!":
          c "Não é isso não bro...a gente acabou, ontem mesmo"
       "Ihh! O q é dessa vez?":
          c "Não demoro, vc sabe!"

    c "Antes de vc acabar o turno eu estou chegando"
    menu:
       "O velho disse que tens uns materiais pra reciclar na parte nordeste do lixão, talvez tenha algo pra você lá..."
       "Vou começar por aí":
         c "O cara é todo certinho..."
       "Se der, dou uma passada lá...":
         c "Vixe! Não estou de reconhecendo..."
   
    menu:
       c "Se liga, não fala pro véio! Diz que vou chegar mais tarde, porque estou doente!"
       "OK! Mesma desculpa de ontem!":
          c "Não foi isso que falei não..."
    n "Chester vai para o leste, deixando um ar de dúvidas no que ele está se metendo"
    jump lixao

label lixao:
      
   ve "Ei meu bom rapaz! Chegou cedo!"
   ve "Você tem duas opções, ou começa por aqui! Tem muito material eletrônico"
   ve "Ou vai lá na parte nordeste..."
   menu: 
       "Por onde vc vai começar?"
       "Acho que vou começar por aqui":
           ve "Ótimo meu querido"
           jump lixao_01
       "Eu achei estranho como você falou da parte nordeste, há algum problema?":
           ve "Não é nada demais! Mas hoje de madrugada, acho que ouvi um som estranho na parte leste"
           ve "Pode ser aqueles carregadores malditos, é só velharia que vem pra cá..."
           jump lixao_02

label lixao_01:
   ve "Aquele seu amigo desapareceu de novo, hein?"
   menu:
      ve "Onde ele se meteu agora?"
      "Pra falar a verdade, nem eu sei...":
         ve "Eu confio muito em você, meu jovem, e sei que fala a verdade"
         ve "Mande seu amigo tomar cuidado pra não fazer nenhuma besteira"
         jump lixao_01_01
      "Estou certo que ele não virá hoje, ele está muito doente":
         ve "Esses jovens de hoje, sempre tem uma desculpa pra faltar no trabalho"
         ve "Sei que tenta protege-lo, mas isso pode gerar um problema pra voce no futuro..."
         jump lixao_01_01

label lixao_01_01:
   ve "De qualquer forma, não vou poder ficar com você, minha netinha nasceu, preciso ajudar minha filha"
   jump lixao_02_F

label lixao_02:
   menu:
      ve "Pode ser aqueles insetos malditos, apareceu um no nosso bairro, forma 10 homens pra destruir aquela praga, malditos robôs"
      "Esses insetos são horríveis mesmo...":
         ve "Com certeza, o homem cria essas coisas pra nada, e quando ganha suas próprias asas só fazem..."
         jump lixao_02_1
      "Acho que robô, não é a definição correta pra aquilo...":
         ve "Todo jovem tem a mesma opinião. Carros é que não são!"
         jump lixao_02_1 
      "O que mais você ouviu do lado leste?":
         ve "Não muito: algo entre grunhido de máquinas e umas vozes, não deu pra distinguir"
         jump lixao_02_2

label lixao_02_1:
   menu:
      ve "Decidiu onde vai começar?"
      "Acho que vou começar por aqui":
           ve "Ótimo!"
           jump lixao_01
      "Acho que vou começar pelo lado leste":
           ve "Hum...Boa sorte!"
           jump lixao_02_A

label lixao_02_A:
   ve "Tome cuidado meu rapaz, e não esqueça : se encontrar células de combustíveis, guarde na caixinha!"     
   jump lixao_03_A

label lixao_02_F:
   ve "Tome cuidado meu rapaz, e não esqueça : se encontrar células de combustíveis, guarde na caixinha!"     
   jump lixao_03_B

label lixao_03_A:
   n "Começa o trabalho"
   menu:
     "Onde devo ir?"
     "Compactador de lixo":
        "Essa prensa é muito lenta"
     "Recarregador de Energia":
        "Colocando força primeiro"
     "Scanner Nuclear":
        "Acionando scannner"
     "Ir a ala leste":
        "Está muito cedo para isso"

   
label lixao_03_B:
   n "Caminhando em meio aos escombros e lixo eletrônico, eis que ele vê uma garota"

label final:
    return
