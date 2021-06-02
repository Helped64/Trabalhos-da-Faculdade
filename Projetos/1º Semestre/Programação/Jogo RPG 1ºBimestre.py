import time
print("Indicado para maiores de 12 anos.")
print("Jogo de Rpg feito por Matheus de Oliveira Portilho--TIA-31926142")
print("Jogo de Rpg feito por Nathan Novais Borges--TIA-31987869")
print("Jogo de Rpg feito por Michel Victor Gurfinkiel--TIA-31937713")
nome = (input("Digite seu nome: "))
print("Olá {}, Bem Vindo !!".format(nome))
print("Para começar o jogo você deve escolher uma classe.")
time.sleep(4)
print("Cada classe possui uma história e suas próprias vantagens")
time.sleep(4)
print("Para vencer o jogo você deve terminar com um HP(pontos de vida) maior ou igual a 60")
time.sleep(4)
print(
    "Você poderá ganhar ou perder HP com base nas suas escolhas durante a história. Ao total são 7 tomadas de decisão")
time.sleep(6)
print("Você deverá selecionar a reposta digitando o número dela")
time.sleep(5)
print(
    "Vantagens de cada classe: \n Caçador- Auxílio nas últimas 2 escolhas \n Guerreiro- Toma menos 20% de dano \n Sacerdote- Ganha 50 de vida após a última tomada de decisão")
time.sleep(6)
print("1) Caçador \n 2) Guerreiro \n 3) Sacerdote ")
classe = int(input("Qual classe você escolhe: 1, 2 ou 3 ?\n Resposta: "))
hp = 100
if classe == 1:
    print("Você {} agora é um Caçador".format(nome))
    time.sleep(3)
    print("Você é um Caçador renomado na sua cidade.")
    time.sleep(4)
    print(
        "Durante a epidemia de uma doença rara, diversas pessoas começaram a morrer. Os médicos descobriram uma receita para a cura da doença, porém o ingrediente principal está em falta, a Planta dos Reis.")
    time.sleep(7)
    print("Essa planta pode apenas ser encontrada na casa de um bruxo que fica no final da Floresta Cinzenta. ")
    time.sleep(5)
    print("Você decide ir até a Floresta para buscar a Planta dos Reis e salvar seu povo.")
    time.sleep(5)
    print("É necessário que você tenha um HP maior ou igual a 60 para conseguir fazer a viagem de volta a cidade")
    time.sleep(5)
    print("Você começa sua jornada")
    time.sleep(5)
    print("Na entrada da Floresta você encontra uma sacola com comida.\n Como proceder ?")
    time.sleep(4)
    print("1) Come a comida toda pois está no começo da jornada")
    print("2) Guarda a comida na mochila, para comer mais tarde")
    print("3) Ignora a comida e segue em frente")
    r1 = int(input("Resposta: "))
    if r1 == 1:
        print("Você perde 20 de HP pois a comida estava estragada.")
        hp = hp - 20

    elif r1 == 2:
        print("A comida na mochila atraiu animais que te seguiram, e você  perdeu 20 de HP.")
        hp = hp - 20

    else:
        print("A comida estava estragada. Sem mudança de HP")

    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("Ao entrar na floresta você se depara com um ambiente escuro e úmido.")
    time.sleep(3)
    print("As árvores cobrem toda a luz do sol e os animais começam a sentir sua presença.")
    time.sleep(4)
    print("Como um caçador experiente, você decide reconhecer o terreno em que está adentrando.\n Como proceder ?")
    time.sleep(4)
    print("1) Subir em uma árvore para ter uma melhor visão sobre o local")
    print("2) Esconder-se em arbustos para não fazer muito barulho")
    print("3) Fazer uma coleta de recursos para prosseguir na viagem")
    r2 = int(input("Resposta: "))
    if r2 == 1:
        print("Ao chegar no alto da árvore você cai e toma 25 de dano")
        hp = hp - 25

    elif r2 == 2:
        print("Você encontra algumas frutas em um arbusto e ganha 10 de HP")
        hp = hp + 10

    else:
        print("Durante a coleta você encontra uma ave ferida ")
        time.sleep(3)
        print("1) Cozinhar ave")
        print("2) Cuidar da ave ")
        r21 = int(input("Resposta: "))
        if r21 == 1:
            print("Você ganha 20 de HP")
            hp = hp + 20
        else:
            print("O animal foge e você perde 15 de HP")
            hp = hp - 15

    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("A Floresta começa a ficar mais densa. Você percebe que ainda não escureceu e continua sua viagem.")
    time.sleep(4)
    print("Logo a frente há uma casa abandonada, com diversas placas contendo: não se aproxime!")
    time.sleep(4)
    print("Você começa a escutar um grito de criança.")
    time.sleep(3)
    print("Ela começa a gritar cada vez mais alto pedindo socorro.\n Como proceder ?")
    time.sleep(4)
    print("1) Ir correndo até a casa abandonada para ver o que está acontecendo.")
    print("2) Ignorar e seguir em frente.")
    print("3) Esperar para ver se alguém sai da casa.")
    r3 = int(input("Resposta: "))
    if r3 == 1:
        print("Você vê que um homem está roubando a comida de uma criança, você pode matar o homem com sua arma.")
        time.sleep(5)
        print("1) Atirar")
        print("2) Não atirar")
        r31 = int(input("Resposta: "))
        if r31 == 1:
            print("Você salva a criança e ela te dá a comida você ganha 15 HP")
            hp = hp + 15
        else:
            print("Ele mata a criança e atira em você.Você perde 30 de HP")
            hp = hp - 30
    elif r3 == 2:
        print("Um homem sai da casa e te dá um tiro. Você perde 30 de HP")
        hp = hp - 30
    else:
        print("Um homem sai da casa, você atira nele e uma criança sai correndo.\n"
              "Após roubar as coisas dele você ganha 10 de HP")
        hp = hp + 10
    print("Você está com {} de HP".format(hp))
    time.sleep(4)

    print("Conforme o dia vai escurecendo, a Floresta também vai.")
    time.sleep(3)
    print(" Você começa a perder a visibilidade e ficar preocupado com a chegada da noite.")
    time.sleep(5)
    print("Ao encontrar uma caverna você decide entrar nela e fazer uma fogueira para passar a noite.")
    time.sleep(5)
    print("Durante a sua estadia na caverna você encontra 3 baús e 1 chave que abre apenas um baú.\n Como proceder ?")
    time.sleep(6)
    print("1) Abrir baú 1 ")
    print("2) Abrir baú 2 ")
    print("3) Abrir baú 3 ")
    r4 = int(input("Resposta: "))
    if r4 == 1:
        print("Contém roupas  de frio para passar a noite.\n Você ganha 15 de HP")
        hp = hp + 15
    elif r4 == 2:
        print("A chave fica presa no baú e você fica irritado.\n Você perde 10 de HP")
        hp = hp - 10
    else:
        print("Contém livros antigos com diversos textos estranhos.")
        time.sleep(4)
        print("Você pode decidir entre tentar decifrar os livros ou ir dormir .\n Como proceder ?")
        print("1) Decifrar livros.")
        print("2) Ir dormir")
        r41 = int(input("Resposta: "))
        if r41 == 1:
            print("Você não decifra o livro e fica cansado. Perde 15 de HP")
            hp = hp - 15
        else:
            print("Você consegue dormir e acorda descansado.\n Ganha 20 de HP")
            hp = hp + 20
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("A noite passou e o sol nasceu. Você já passou da metade da Floresta Cizenta. ")
    time.sleep(5)
    print("Após sair da caverna percebe que os animais estão mais agressivos do que o normal. ")
    time.sleep(5)
    print("Uma névoa cinza sobe no ar e complica a percepção do que está acontecendo")
    time.sleep(5)
    print("Diversos animais começam a correr em sua direção.\n Como proceder ?")
    print("1) Caçá-los")
    print("2) Esconder-se dos animais e esperar o melhor momento para sair dessa área")
    print("3) Sair correndo e arriscar ficar perdido na floresta")
    r5 = int(input("Resposta: "))
    if r5 == 1:
        print("Consegue caçá-los.Ganha 20 de HP por acreditar no seu potêncial.")
        hp = hp + 20
    elif r5 == 2:
        print("Os animais sentem seu cheiro e você sai correndo.\n Perde 10 de HP")
        hp = hp - 10
    else:
        print("Você fica perdido e perde 20 de HP")
        hp = hp - 20
    print("Você está com {} de HP".format(hp))
    time.sleep(5)
    print("A Floresta Cinzenta é famosa por seu clima diverso.")
    time.sleep(4)
    print("Logo após a névoa se dissipar uma forte chuva começa. ")
    time.sleep(4)
    print("Árvores começam a cair, os animais começam a se esconder e os rios começam a subir ")
    time.sleep(6)
    print(
        "A Chuva começa a ficar ainda mais forte, tornando perigoso o caminho até o final da floresta.\n Como proceder ?")
    time.sleep(4)
    print("1) Esperar a chuva passar para continuar a viagem. ")
    print("2) Aproveitar que os animais estão escondidos e seguir a viagem.")
    print("Dica : Muitas árvores estão caindo ")
    r6 = int(input("Resposta: "))
    if r6 == 1:
        print("As árvores logo a frente caíram no momento em que você se abrigou.\n Ganha 15 de HP por sua perspicácia")
        hp = hp + 15
    else:
        print("Árvores caíram e te machucaram durante o caminho.\n Você toma 25 de dano")
        hp = hp - 25
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("A chuva passou. O sol pela primeira vez aparece no céu. ")
    time.sleep(5)
    print("Você está vendo o final da floresta em que a casa do bruxo se localiza.")
    time.sleep(5)
    print("A Planta dos Reis está próxima e você respira aliviado. ")
    time.sleep(4)
    print("Porém o bruxo é conhecido por matar todos aqueles que se aproximam da casa.")
    time.sleep(5)
    print("Você sabe que o povo da sua cidade está em perigo e que apenas você pode salva-lo.")
    time.sleep(5)
    print(" O bruxo encontra-se sentado na sala de sua casa.")
    time.sleep(4)
    print("Você deve decidir como invadir a casa do bruxo.\n Como proceder ?")
    time.sleep(4)
    print("1) Entrar na casa sem fazer barulho e buscar pela planta")
    print("2) Derrubar a porta da casa, enfrentar o bruxo e buscar pela planta")
    print("Dica: Em uma das alternativas você não perde nem ganha HP")
    r7 = int(input("Resposta: "))
    if r7 == 1:
        print("O bruxo está dormindo.Você acha a planta e sai da casa sem fazer barulho")
    else:
        print("Você chama a atenção do bruxo e deve decidir entre:")
        time.sleep(4)
        print("1) Explicar sua a história para ele. ")
        print("2) Atirar no bruxo e pegar a Planta dos Reis")
        r61 = int(input("Resposta: "))
        if r61 == 1:
            print("O bruxo compreende a história e dá a erva em troca de 20 de HP.\n Você perde 20 de HP")
            hp = hp - 20
        else:
            print(
                "O bruxo morre e você pega a planta, mas ele lança um feitiço, fazendo com que você contraia a doença rara.\n Você perde 30 de vida.")
            hp = hp - 30
    print("Você finalmente consegue a Planta dos Reis !!")
    time.sleep(5)
    print("Você terminou sua busca com {} de HP".format(hp))
    if hp >= 60:
        print("Você consegue retornar até a sua cidade, salva seu povo e se torna um herói")
        print("Parabéns, você venceu !!")
    else:
        print(
            "Você morre durante o caminho de volta por não conseguir resistir à Floresta Cinzenta,\n fazendo com que a sua cidade seja morto pela doença rara")
        print("Que pena, você perdeu.")






elif classe == 2:
    print("Você {} agora é um Guerreiro".format(nome))
    print("Você é um Guerreiro renomado na sua cidade.")
    time.sleep(4)
    print("Essa historia se passa na cidade de Lord, onde vivia um Rei que tinha uma filha muito bonita.")
    time.sleep(5)
    print(" Nessa cidade tinha um exercito de mal feitores.O chefe desse exercito queria se casar com a filha do rei para assim ser o próximo rei. ")
    time.sleep(5)
    print("Como o rei sabia que ele não era uma pessoa boa não permitiu o casamento. Enfurecido esse mal feitor sequestrou a princesa e a prendeu num castelo.")
    time.sleep(5)
    print("O rei, muito triste, contrata o melhor guerreiro da província pois sabia que era o único que tinha coragem de lutar contra o exercito inimigo e trazer sua filha de volta e se casar com ela.")
    time.sleep(5)
    print("É necessário que você tenha um HP maior ou igual a 60 para conseguir salvar a pricesa")
    time.sleep(5)
    print("O guerreiro se prepara para iniciar sua busca pela filha do rei e sabe que precisa seguir em direção a uma fortaleza onde os inimigos ficavam")
    time.sleep(5)
    print("Você começa com 100 HP")
    print(" No caminho encontra uma bifurcação com 3 saidas. escolha uma delas ?")
    time.sleep(4)
    print("1) Um caminho com muitas arvores que tapavam sua visão")
    print("2) Um caminho com um penhasco.")
    print("3) O caminho onde estava os inimigos ")
    r1 = int(input("Resposta: "))
    if  r1 == 3:
        print("Você como é um guerreiro decide ir lutar. Sem mudança de HP")
        hp == hp
    elif r1 == 1:
        print("Esse caminho não tinha visibilidade e não o levaria a forteleza  ela terá que voltar. Perde 12 de HP.")
        hp = hp - 15*0.8
    else:
        print("Nesse caminho o penhasco é muito grande, ele não consegue pular e terá que voltar. Perde 8 de HP")
        hp = hp - 10*0.8
    print("Você está com {} de HP".format(hp))
    print("nesse caminho ele ouviu o exercito falando que estava esperando o chefe para leva-lo até princesa.")
    time.sleep(4)
    print("Então percebeu a chegada do chefe e não poderia perder mais tempo. Resolveu:")
    time.sleep(4)
    print("1) Desistir de salvar a princesa e voltar ") 
    print("2) Lutar contra os inimigos ")
    print("3) Se entregar para os inimigos  ")
    r2 = int(input("Resposta:"))
    if  r2 == 2:
        print("Como você é um guerreiro, sabe como ganhar uma luta.Sem mudança de HP")
        hp = hp
    elif r2 ==1:
        print(" Você foi contratado para fazer esse trabalho. Perde 8 de HP")
        hp = hp - 10*0.8
    else:
        print("Se você se entregar não conseguira salvar a princesa. Perde 12 de HP")
        hp = hp - 15*0.8
    print("Você está com {} de HP".format(hp))
    print("o guerreiro mesmo em desvantagem luta contra os inimigos.")
    time.sleep(3)
    print("1) Ele é ferido gravemente ")
    print("2) Consegue matar os soldados ")
    print("3) Deixa os soldados fugirem  ")
    r3 = int(input("Resposta: "))
    if r3 == 2:
        print("Com isso ele consegue continuar seu caminho. Sem mudança de HP")
        hp = hp
    elif r3 == 1:
        print("Você foi ferido e não consegue salvar a princesa. Perde 12 de HP")
        hp = hp - 15*0.8
    else:
        print("Os saldados voltam para a fortaleza e o inpedem de salvar a princesa. perde 8 de HP")
        hp = hp - 10*0.8
    print("Você está com {} de HP".format(hp))
    print("Infelizmente o chefe dos inimigos,vendo as habilidades de luta do guerreiro, foge em direção ao lugar onde esta a princesa.")
    time.sleep(5)
    print("O guerreiro continua sua busca para salvar sua princesa e no caminho encontra o chefe dos inimigos e o enfrenta.")
    time.sleep(5)
    print("Num duelo épico vilão e guerreiro lutam com suas espadas. Em um momento da batalha o vilão cai e o guerreiro o ataca.")
    time.sleep(5)
    print("sabendo dos problemas teria pela frente decide vasculhar os bolsos do inimigo. Ele:")
    time.sleep(5)
    print("1) Encontra e pega um pó venenoso.")
    print("2) Encontra um frasco.")
    print("3) Encontra uma arma.")
    r4 = int(input("Resposta:"))
    if r4== 1:
        print("Com esse pó você conseguira inimigos mais fortes. Ganha 5 de HP")
        hp = hp+5
    elif r4 == 2:
        print("O frasco vazio não tem utilidade. Perde 16 de HP")
        hp = hp - 20*0.8
    else:
        print("Arma sem muniçao não tem utilidade. Perde 12 de HP ")
        hp = hp - 15*0.8
    print("Você está com {} de HP".format(hp))
    print("continuando sua busca ate a princesa de depara no caminho com alguns bichos selvagens. O que ele faz?")
    time.sleep(5)
    print("1) deixa os bichos vivos.")
    print("2) mata todos.")
    print("3) ele decide rastejar pelas folhagens.")
    r5 = int(input("Resposta: "))
    if r5== 2:
        print("È preciso matar os bichos para que não seja atacado. Ganha 3 de HP")
        hp = hp+3
    elif r5 == 1:
        print("Os bichos podem ataca-lo e feri-lo. Perde 12 de HP")
        hp = hp - 15*0.8
    else:
        print("Os bichos o notam e o atacam. Perde 8 de Hp")
        hp = hp - 10*0.8
    print("Você está com {} de HP".format(hp))
    print("com o pó venenoso, consegue matar os bichos selvagens e seguir a sua busca.")
    time.sleep(5)
    print("depois de uma longa caminhada encontra a fortaleza onde esta a princesa e para chegar até ela, ele:")
    time.sleep(5)
    print("1) Ve um lago e decide chegar ao portão nadando.")
    print("2) Decide escalar os muros da fortaleza.")
    print("3) Decide lutar com os dois gigantes que estavam protegendo o portão.")
    r6 = int(input("Resposta: "))
    if r6==3:
        print("Matar os gigantes lhe garante a saida da fortaleza em segurança. Ganha 3 de HP HP")
        hp=hp+3
    elif r6==1:
        print("O lago estava cheio de jacares que acabam o ferindo. Perde 12 de HP")
        hp=hp-15*0.8
    else:
        print("Cai e se fere. perde 8 de HP")
        hp=hp-10*0.8
    print("Você está com {} de HP".format(hp))
    print("novamente utilizando o pó venenoso consegue matar os dois gigantes e salva a princesa.")
    time.sleep(4)
    print("Depois da princesa sã e salva o guerreiro a leva de volte para o rei. Chegando la o rei oferece a ele como recompensa:")
    time.sleep(4)
    print("1)Casar com a princesa e ser o próximo rei.")
    print("2)O rei não concede sua filha para casar.")
    print("3)Oferece algumas moedas sem muito valor.")
    r7 = int(input("Resposta: "))
    if  r7==1:
        print("Sendo ele pode viver feliz e formar um exercito  de guerreiros. Sem mudança de HP")
        hp==hp
    elif r7==2:
        print("O rei prometeu a mão de sua filha em casamento. Perde 12 de HP")
        hp=hp-15*0.8
    else:
        print("As moedas de nada ajudariam. perde 8 de HP")
        hp=hp-10*0.8
    print("Você está com {} de HP".format(hp))
    if hp > 60: 
        print("Eles se casam e vivem felizes para sempre ")
    else:
        print(" A princesa e você morrem")
else:
    print("Você {} agora é um Sacerdote".format(nome))
    print("Você é Filho de um Rei dado como morto, em vez de escolher os caminhos diplomaticos durante sua vida você decidiu estudar as artes do sacerdotismo.")
    time.sleep(4)
    print("Você acaba de descobrir que seu pai é dado como morto e decide ir atrás dele.")
    print("É necessário que você tenha um HP maior ou igual a 60 para ver o final certo dessa historia")
    time.sleep(5)
    print("Você começa sua jornada")
    time.sleep(5)
    print("Na saida do reino de azeroth você encontra uma xamã chamada agatha que oferece a você os beneficios de saber onde esta seu pai, porém haverá uma punição se você aceitar a oferenda.\n O que você pretende fazer ?")
    time.sleep(4)
    print("1) Você aceita a oferenda, descobrindo onde seu pai está porém fazendo com que o reino sofra uma terrivel maldição")
    print("2) Você ignora a oferenda e continua sua jornada")
    print("3) Você evoca sua forma sombria para matar a xamã agatha porém sofrendo avarias")
    x=int(input("Resposta:"))
    if x==1:
        print("Você perde 20 de HP pois a bruxa te enganou e fez com que seu reino fosse punido e a partir de agora todas as noites os cidadãos do reino irão virar worgens.")
        hp=hp-20
    elif x==2:
        print("Você continua sua jornada ignorando a xamã agatha como se nada tivesse acontecido.")
    else:
        print("Você consegue matar a xamã porém ela joga muitos feitiços de fogo em você")
        hp=hp-40
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("Passando pela xamã você precisa cruzar uma catacumba considerada perigosa e misteriosa.")
    time.sleep(3)
    print("Dentro da catacumba você se depara com 3 caminhos e uma figura misteriosa vem ao seu encontro.")
    time.sleep(4)
    print("Essa figura é o Rei Fubalumba ele te oferece três possiveis escolhas.\n Essas escolhas são:")
    time.sleep(4)
    print("1) Passar pelo primeiro local que é cheio de luz e barulhos estranhos")
    print("2) Passar pelo caminho escuro")
    print("3) Passar pelo local com pouca luz, neste caminho o rei fubalumba avisa para não pegar a vela que seria a responsavel pela iluminação")
    y=int(input("Resposta:"))
    if y==1:
        print("Passando por esse caminho você encontra a evocadora draconica alana que acaba dando para você a poção do dragão alextraza")
        hp=hp+15
    elif y==2:
        print("Você passa pelo caminho escuro porém lembra que você é um sacerdote e pode usar suas forças para iluminar o caminho porém isso gasta um pouco suas forças")
        hp=hp-15
    else:
        print("Você passa pelo caminho com pouca luz e vê a vela e então tem duas ideias, são elas:")
        time.sleep(3)
        print("1) Pegar a vela")
        print("2) Não pegar a vela")
        y1=int(input("Resposta:"))
        if y1==1:
            print("Você pegou a vela elemental, ela retira 30 de vida de você")
            hp=hp-30
        else:
            print("Você continua com a mesma vida por não pegar a vela igual o rei kobold falou")
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("Continuando sua viagem você se depara com um genio louco conhecido como Dr.Caboom.")
    time.sleep(4)
    print("Ele pede sua ajuda para poder voltar aos laboratorios caboom")
    time.sleep(3)
    print("Então você decide ajudar o dr. caboom porém para fazer isso podem ser nescessarios alguns sacrificios \n Você então decide entre três escolhas, elas são:")
    time.sleep(4)
    print("1) Ajudar o Dr.Caboom a voltar para o seu laborotorio porém para fazer isso você irá gastar um pouco de vide")
    print("2) Ignorar e seguir em frente.")
    print("3) Silenciar o Dr.Caboom fazendo com que ele fique calado e não possa fazer nada")
    z=int(input("Resposta:"))
    if z==1:
        print("Você ajuda o dr.caboom a voltar para seu laboratorio por fazer isso ele da a você uma poção de vida que anula um pouco o sacrificio feito por você para ajuda-lo.")
        hp=hp-5
    elif z==2:
        print("Por ignorar o Dr.Caboom ele acaba jogando uma bomba que faz CABOOOOMM em você, sua vida é reduzida")
        hp=hp-30
    else:
        print("Você decide silencia-lo e por isso você acaba perdendo um pouco de vida")
        hp=hp-10
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("Continuando o seu caminho você se depara com uma cartomante que decide falar sobre o seu futuro, seu nome é madame lazuli.")
    time.sleep(3)
    print("Você então decide ver seu futuro nas cartas.")
    time.sleep(5)
    print("Ela então abre três cartas e diz para escolher uma o que ela não fala é que as cartas irão fazer com que você realmente acabe por escolher seu futuro.")
    time.sleep(5)
    print("Você então tem de escolher entre três cartas, são elas:")
    time.sleep(6)
    print("1) Continuar seu caminho")
    print("2) Continuar seu caminho")
    print("3) Continuar seu caminho")
    a=int(input("Resposta:"))
    if a==1:
        print("Você acaba por continuar seu caminho ganhando vida")
        hp=hp+20
    elif a==2:
        print("Você acaba por continuar seu caminho não alterando nada em sua vida")
        hp=hp
    else:
        print("Você acaba por continuar seu caminho perdendo vida")
        hp=hp-20
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("Continuando seu caminho você se depara com o arquiladrão rafam, que fala que irá roubar seus poderes de sacerdote para ele.")
    time.sleep(5)
    print("Você então pergunta porque ele quer fazer isso e ele responde falando que precisa dos seus poderes de sacerdote para roubar o cajado primordial.")
    time.sleep(5)
    print("Você então tem de travar uma batalha")
    time.sleep(5)
    print("Você tem varias opções para derrotar ele, são elas:")
    print("1) Acessar sua forma de cavaleiro da morte que é a forma das trevas mais sombria que um sacerdote pode ter porém isso fará sacrificios")
    print("2) Mudar para a forma das sombras")
    print("3) Evocar a alta sacerdotista eluna para ajudar o arquiladrão rafam")
    b=int(input("Resposta:"))
    if b==1:
        print("Você consegue derrotar o arquiladrão rafam porém teve de perder 60 de vida por ter virado um cavaleiro da morte.")
        hp=hp-60
    elif b==2:
        print("Mudando para forma das sombras você consegue machucar rafam porém ela também te machuca, você ira perder 30 de vida")
        hp=hp-30
    else:
        print("Você evoca a alta sacerdotista eluna e ela decidi ajudar o arquiladrão rafam a roubar o cajado dando vida para você continuar sua jornada a procura de seu pai")
        hp=hp+30
    print("Você está com {} de HP".format(hp))
    time.sleep(5)
    print("Depois desse encontro você acaba por chegar no local de desaparecimento do seu pai.")
    time.sleep(4)
    print("Você acaba por ver tudo destruido e todos mortos")
    time.sleep(4)
    print("Você então tem três decisões a se tomar.")
    time.sleep(4)
    print("1) Usar todas as suas forças de sacerdote para reviver e ajudar todos a se levantar")
    print("2) Reviver por um curto periodo de tempo alguem para obter respostas")
    print("3) Reviver apenas o primeiro imediato de seu pai para tentar acha-lo")
    c=int(input("Resposta: "))
    if c==1:
        print("Você usou todas as suas forças para reviver a todos e cura-los por isso perdeu 40 de vida")
        hp=hp-40
    elif c==2:
        print("Você obteve respostas, porém teve de usar a forma das sombras para reviver esta pessoa por um curto periodo de tempo, você perdeu 5 de vida")
        hp=hp-5
    else:
        print("Você reviveu apenas o primeiro imediato de seu pai e por isso perdeu 10 de vida")
        hp=hp-10
    print("Você está com {} de HP".format(hp))
    time.sleep(4)
    print("Após obter respostas você retorna a seu reino para falar com um sudito e guerreiro muito leal o qual você não sabia que foi o unico a voltar com vida e sabia sobre o desaparecimento de seu pai.")
    time.sleep(5)
    print("Você pergunta a ele sobre o acontecimento e ele fala que a unica coisa que se lembra era de sylvanna a rainha banshee atacando a embarcação que tinha seu pai nela.")
    time.sleep(5)
    print("Você então decidi ir até ela para questionar o acontecimento.")
    time.sleep(4)
    print("Quando chega no refugio de sylvanna ela adimiti o feito e diz ter feito aquilo por que toda a vida deve perecer.")
    time.sleep(5)
    print("Ela faz um cerco em volta de você, então vocês começam uma batalha.")
    time.sleep(5)
    print("Você tem três escolhas para derrotar ou não silvana,são elas:")
    time.sleep(4)
    print("1) Utilizar sua forma de cavaleiro da morte para confirmar a morte de vez de sylvanna")
    print("2) Utilizar sua forma sombria para derrubar e prender sylvanna pelo seus crimes")
    print("3) Tentar argumentar com sylvanna e falar com ela")
    d=int(input("Resposta:"))
    if d==1:
        print("Você mata sylvanna de vez, porém não consegue mais voltar para sua forma normal e acaba permanecendo na forma de cavaleiro da morte e por isso você perde 100 de vida")
        hp=hp-100
    elif d==2:
        print("Você consegue derrubar e prender sylvanna porém ela tira seus poderes de sacerdote e por isso vc perde 65 de vida")
        hp=hp-65
    else:
        print("Você tenta falar com sylvanna e fala que quer permanecer em paz com ela, porém ela ataca você, nisto você tem duas opções:")
        time.sleep(4)
        print("1) Usar seu poder de sacerdote para curar sylvanna e tranforma-la em uma elfa novamente")
        print("2) Utilizar sua forma de cavaleiro da morte para confirmar a morte de vez de sylvanna")
        e=int(input("Resposta:"))
        if e==1:
            print("Você curou sylvanna e por isso ela agradece e lhe da uma poção elfica que restaura 80 de vida")
            hp=hp+80
        else:
            print("Você mata sylvanna de vez, porém não consegue mais voltar para sua forma normal e acaba permanecendo na forma de cavaleiro da morte e por isso você perde 100 de vida")
            hp=hp-100
    print("Você retorna a seu reino!!")
    hp=hp+50
    time.sleep(5)
    print("Você terminou sua busca com {} de HP".format(hp))
    if hp >= 60:
        print("Você retorna a azeroth, mesmo triste por seu pai você ira governar o reino e por isso torna-se um paladino lutando pela luz e pela justiça")
        print("Parabéns, você venceu ou será que perdeu??")
    else:
        print("Você retorna a azeroth, porém se tornou a mesma coisa que sylvanna no final, você se tornou um cavaleiro da morte e por isso você começa a trazer morte e desgraça para o seu reino")
        print("Parabéns, você perdeu ou será que venceu??")
    



