import pygame
from pygame import mixer

BLACK = (0, 0, 0)
WHITE = (115, 0, 0)
BLUE = (50, 50, 50)
GREEN = (50, 50, 50)
RED = (255, 0, 0)
PURPLE = (0, 50, 0)

chao = 445
fundoGame = pygame.image.load("assets/fundoGame.jpg")
Nelsinho = pygame.image.load("assets/Nelsinho.png")
Victory = pygame.image.load("assets/Victory.jpg")


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0
    player_x = 0
    player_y = 0
    gravity = 2
    speed_y = 0
    jumpForce = 1

    def __init__(self, x, y):

        super().__init__()

        self.image = pygame.image.load("assets/Nelsinho.png")

        self.rect = self.image.get_rect()
        self.rect.y = 444
        # 444
        self.rect.x = x
        self.player_x = x
        self.player_y = y

    def gravityFunc(self):
        self.speed_y += self.gravity

        self.rect.y += self.speed_y

        if self.rect.y >= chao:
            self.rect.y = chao

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def move(self, walls):
        self.rect.x += self.change_x

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)

        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pygame.sprite.spritecollide(self, walls, False)

        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom


class Room(object):
    wall_list = None
    enemy_sprites = None

    def __init__(self):
        self.wall_list = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()


class Room1(Room, Player):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 35, (50, 50, 50)],  # perguntas
                 [105, 300, 150, 50, (50, 50, 50)],  # resposta1
                 [275, 300, 150, 50, (50, 50, 50)],  # respsota2
                 [450, 300, 150, 50, (50, 50, 50)]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room2(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 35, GREEN],  # perguntas
                 [105, 300, 150, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 150, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room3(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 35, GREEN],  # perguntas
                 [105, 300, 150, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 150, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room4(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 35, GREEN],  # perguntas
                 [105, 300, 150, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 150, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room5(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 20, GREEN],  # perguntas
                 [100, 300, 163, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 160, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room6(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 20, GREEN],  # perguntas
                 [105, 300, 150, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 150, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room7(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 35, GREEN],  # perguntas
                 [105, 300, 150, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 195, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room8(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],  # esquerda superior
                 [0, 450, 20, 400, WHITE],  # desquerda inferior
                 [680, 0, 20, 340, WHITE],  # direita superior
                 [20, 0, 660, 20, WHITE],  # teto

                 [0, 480, 700, 20, PURPLE],  # chão

                 [149, 111, 406, 35, GREEN],  # perguntas
                 [105, 300, 150, 50, BLUE],  # resposta1
                 [275, 300, 150, 50, BLUE],  # respsota2
                 [450, 300, 195, 50, BLUE]  # resposta3
                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


class Room9(Room):

    def __init__(self):
        super().__init__()

        walls = [[0, 0, 20, 450, WHITE],
                 [0, 450, 20, 400, WHITE],
                 [650, 0, 50, 500, WHITE],
                 [20, 0, 660, 20, WHITE],

                 [0, 480, 700, 20, PURPLE],

                 ]

        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)


def main():
    pygame.init()
    mixer.music.load('assets/song.wav')
    mixer.music.play(-1)

    screen = pygame.display.set_mode([700, 500])

    pygame.display.set_caption('Entrega Inicial 1')

    player = Player(100, 600)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)

    rooms = []

    room = Room1()
    rooms.append(room)

    room = Room2()
    rooms.append(room)

    room = Room3()
    rooms.append(room)

    room = Room4()
    rooms.append(room)

    room = Room5()
    rooms.append(room)

    room = Room6()
    rooms.append(room)

    room = Room7()
    rooms.append(room)

    room = Room8()
    rooms.append(room)

    room = Room9()
    rooms.append(room)

    current_room_no = 0
    current_room = rooms[current_room_no]

    clock = pygame.time.Clock()

    done = False

    while not done:

        player.gravityFunc()

        for event in pygame.event.get():
            player.gravityFunc()
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -97)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 97)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)

        player.move(current_room.wall_list)

        if player.rect.x < -15:
            if current_room_no == 0:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790

        if player.rect.x > 680:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 1:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 3:
                current_room_no = 4
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 4:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 5:
                current_room_no = 6
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 6:
                current_room_no = 7
                current_room = rooms[current_room_no]
                player.rect.x = 300
            elif current_room_no == 7:
                current_room_no = 8
                current_room = rooms[current_room_no]
                player.rect.x = 300

            elif current_room_no == 8:
                current_room_no = 9
                current_room = rooms[current_room_no]
                player.rect.x = 300

            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 0

        screen.fill(BLACK)
        screen.blit(fundoGame, (0, 0))
        movingsprites.draw(screen)
        current_room.wall_list.draw(screen)

        if current_room_no == 0:
            txt = "1- Qual o maior vilão para a segurança de "
            txt2 = "dados do computador ?"
            txtR1 = "A- Haquer?"
            txtR2 = "B- Hacker?"
            txtR3 = "C- Raquer?"
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txttela2 = fontesys.render(txt2, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txttela2, (149, 126))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))

        if current_room_no == 1:
            txt = "2-Qual das senhas abaixo é a mais "
            txt2 = " segura para um email ?"
            txtR1 = "A- 123456789?"
            txtR2 = "B- Senha123?"
            txtR3 = "C- MegaZord"
            txtR33 = "Macarrão@84?"
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txttela2 = fontesys.render(txt2, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            txtR33tela = fontesys.render(txtR33, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txttela2, (149, 126))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))
            screen.blit(txtR33tela, (454, 322))

        if current_room_no == 2:
            txt = "3-Qual dos nomes abaixo faz referência a um "
            txt2 = "tipo de vírus de computador?"
            txtR1 = "A- SpiderMan"
            txtR2 = "B- Cavalo de Troia"
            txtR3 = "C- Magneto"
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txttela2 = fontesys.render(txt2, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txttela2, (149, 126))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))

        if current_room_no == 3:
            txt = "4- A tecnologia utilizada na internet que se refere "
            txt2 = "à segurança da informação é: "
            txtR1 = "A- criptografia."
            txtR2 = "B- download."
            txtR3 = "C- streaming."
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txttela2 = fontesys.render(txt2, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txttela2, (149, 126))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))

        if current_room_no == 4:
            txt = "5- A criptografia é uma forma de esconder :"
            txtR1 = "A- Uma informação "
            txtR11 = " secreta"
            txtR2 = "B- Uma fruta."
            txtR3 = "C- Um computador."
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR11tela = fontesys.render(txtR11, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR11tela, (109, 321))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))

        if current_room_no == 5:
            txt = "6- Qual das internets a seguir é mais segura ?"
            txtR1 = "A- Dark Web"
            txtR2 = "B- Deep Web"
            txtR3 = "C- Surface Web"
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))

        if current_room_no == 6:
            txt = "7- Qual das ações a seguir você deve "
            txt2 = "realizar na internet "
            txtR1 = "A- Abrir links"
            txtR11 = "desconhecidos"
            txtR2 = "B- Não praticar"
            txtR22 = "cyberbullying "
            txtR3 = "C- Dar senhas pessoais"
            txtR33 = " para estranhos"
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txttela2 = fontesys.render(txt2, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR11tela = fontesys.render(txtR11, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR22tela = fontesys.render(txtR22, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            txtR33tela = fontesys.render(txtR33, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txttela2, (149, 126))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR11tela, (109, 321))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR22tela, (279, 321))
            screen.blit(txtR3tela, (454, 306))
            screen.blit(txtR33tela, (454, 321))

        if current_room_no == 7:
            txt = "8- Quais das técnica usadas para realizar "
            txt2 = "ataques na internet é FALSA?"
            txtR1 = "A- Interceptação de "
            txtR11 = "informações"
            txtR2 = "B- Uso de antivírus "
            txtR3 = "C- Vulnerabilidade"
            txtR33 = " do sistema"
            pygame.font.init()
            fonte = pygame.font.get_default_font()
            fontesys = pygame.font.SysFont(fonte, 25)
            txttela = fontesys.render(txt, 1, (255, 0, 0))
            txttela2 = fontesys.render(txt2, 1, (255, 0, 0))
            txtR1tela = fontesys.render(txtR1, 1, (255, 255, 255))
            txtR11tela = fontesys.render(txtR11, 1, (255, 255, 255))
            txtR2tela = fontesys.render(txtR2, 1, (255, 255, 255))
            txtR3tela = fontesys.render(txtR3, 1, (255, 255, 255))
            txtR33tela = fontesys.render(txtR33, 1, (255, 255, 255))
            screen.blit(txttela, (149, 111))
            screen.blit(txttela2, (149, 126))
            screen.blit(txtR1tela, (109, 306))
            screen.blit(txtR11tela, (109, 321))
            screen.blit(txtR2tela, (279, 306))
            screen.blit(txtR3tela, (454, 306))
            screen.blit(txtR33tela, (454, 321))

        if current_room_no == 8:
            screen.blit(Victory, (0, 0))

        pygame.display.update()

        pygame.display.flip()

        clock.tick(60)


if __name__ == "__main__":
    main()
