import pygame
from sys import exit

##tamanho da tela
largura = 800
altura = 400

nivel_chao = 300
score = 0

pygame.init()
##variaveis
tela = pygame.display.set_mode((largura,altura)) ## tela de 800x400 pixels
pygame.display.set_caption('Hugo') ## nome do jogo
clock = pygame.time.Clock() ## Clock precisa do C maiusculo
tes_font = pygame.font.Font('font/Pixeltype.ttf',40) ## dois argumentos, tipo de fonte e tamanho da fonte
game_active = True    

##Surfaces
fundo_de_tela  = pygame.image.load('graphics/Sky.png').convert()
chao = pygame.image.load('graphics/ground.png').convert()

 
score_surf = tes_font.render('Score: {}'.format(score), False, (69,69,69)) ## tres argumentos, texto que sera mostrado, AA -> smooth pixel arte is true, cor do texto
score_rect = score_surf.get_rect(center = (400,30))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,nivel_chao)) ## argumentos, posição:ex:topleft, midleft, midbottom = (coord_x,coord_y)
player_gravity = 0

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,nivel_chao)) ## argumentos, posição:ex:topleft, midleft, midbottom = (coord_x,coord_y)

while True:
    ## fecha o jogo
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if(event.type == pygame.KEYDOWN):
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= nivel_chao:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= nivel_chao:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.midbottom = (600, nivel_chao)
                game_active = True
           
    if game_active:
        ## blit coloca uma surface em cima da outra
        tela.blit(fundo_de_tela,(0,0)) ## argumentos: surface e posição
        tela.blit(chao,(0,nivel_chao))

        # Score
        pygame.draw.rect(tela,'#c0e8ec',score_rect.inflate(10, 10))#3 argumentos onde desenhar, cor, retangulo que quermos desenhar, largura linha, raio de curva das bordas, inflate para almentar as bordas
        tela.blit(score_surf, score_rect)

        # Snail
        tela.blit(snail_surf,snail_rect)
        snail_rect.left -= 4
        if snail_rect.right <= 0: snail_rect.left = 800

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= nivel_chao: player_rect.bottom = nivel_chao
        tela.blit(player_surf,player_rect)

        # Colisions
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        tela.blit(pygame.image.load('graphics/baby-boss.png').convert(), (0,0))
        
                   

    pygame.display.update() ## desenha todos os elementos e faz update de tudo
    clock.tick(60) ## max frame rate

