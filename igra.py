import pygame
import time

pygame.init()

#color
crvenaBoja = (255,0,0)
okerBoja = (251,235,173)
plavaBoja = (84,70,134)
tamnoPlavaBoja = (21, 23, 34)

#velicina ekrana
duzina_prozora = 640
visina_prozora = 480

prozor_igrice = pygame.display.set_mode ((duzina_prozora, visina_prozora))
pygame.display.set_caption("Prva moja igrica")

font_za_tekst = pygame.font.SysFont("monospace", 60)

sat = pygame.time.Clock()

#lopta
lopta_x_koordinata = int(duzina_prozora / 2)
lopta_y_koordinata = int(visina_prozora / 2)
lopta_x_brzina = 4
lopta_y_brzina = 4
lopta_poluprecnik = 13

#plocica 1
plocica1_x_koordinata = 10
plocica1_y_koordinata = 10
plocica1_duzina = 20
plocica1_visina = 100

#plocica 2
plocica2_duzina = 20
plocica2_visina = 100
plocica2_x_koordinata = duzina_prozora - 30
plocica2_y_koordinata = visina_prozora - plocica2_visina -10


#broj poena
igrac1_broj_poena = 0
igrac2_broj_poena = 0

#bez vidljivosti misa
pygame.mouse.set_visible(0)

izlaz_iz_igrice = False

while not izlaz_iz_igrice:
    kliknut_taster = pygame.key.get_pressed()
    pygame.key.set_repeat
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            izlaz_iz_igrice = True

    if kliknut_taster[pygame.K_ESCAPE]:
        izlaz_iz_igrice = True

    if kliknut_taster [pygame.K_w]:
        plocica1_y_koordinata = plocica1_y_koordinata -7
    if kliknut_taster [pygame.K_s]:
        plocica1_y_koordinata = plocica1_y_koordinata + 7
    if kliknut_taster [pygame.K_UP]:
        plocica2_y_koordinata = plocica2_y_koordinata -7
    if kliknut_taster [pygame.K_DOWN]:
        plocica2_y_koordinata = plocica2_y_koordinata +7

    
    # kretanje loptice
    lopta_x_koordinata = lopta_x_koordinata + lopta_x_brzina
    lopta_y_koordinata = lopta_y_koordinata + lopta_y_brzina

    # kontakt (kolizija) lopte sa vrhom i dnom prozora u kome je lopta
    if lopta_y_koordinata <=0 or  lopta_y_koordinata >=480:
        lopta_y_brzina = lopta_y_brzina * (-1)

    # kontakt (kolizija) lopte i plocica
    if lopta_x_koordinata < (plocica1_x_koordinata + plocica1_duzina) and lopta_y_koordinata >= plocica1_y_koordinata and lopta_y_koordinata < plocica1_y_koordinata + plocica1_visina:
         lopta_x_brzina = lopta_x_brzina * (-1)

    if lopta_x_koordinata > plocica2_x_koordinata and lopta_y_koordinata >= plocica2_y_koordinata and lopta_y_koordinata < plocica2_y_koordinata + plocica2_visina:
         lopta_x_brzina = lopta_x_brzina * (-1)

    # blokada plocica (kolizija)
    if plocica1_y_koordinata <0:
        plocica1_y_koordinata = 0
    elif plocica1_y_koordinata + plocica1_visina > visina_prozora:
        plocica1_y_koordinata = visina_prozora - plocica1_visina

    if plocica2_y_koordinata < 0:
        plocica2_y_koordinata = 0
    elif plocica2_y_koordinata + plocica2_visina > visina_prozora:
        plocica2_y_koordinata = visina_prozora - plocica2_visina

    #broj poena i postavljanje loptice na sredini
    if lopta_x_koordinata <= 0:
        igrac2_broj_poena = igrac2_broj_poena + 1
        lopta_x_koordinata = int (duzina_prozora /2 )
        lopta_y_koordinata = int (visina_prozora / 2 )
    elif lopta_x_koordinata >= duzina_prozora:
          igrac1_broj_poena = igrac1_broj_poena +1
          lopta_x_koordinata = int (duzina_prozora / 2)
          lopta_y_koordinata = int (visina_prozora / 2)
        
         
    

    
    prozor_igrice.fill(okerBoja)

    loptica = pygame.draw.circle(prozor_igrice, crvenaBoja,
      (lopta_x_koordinata, lopta_y_koordinata), lopta_poluprecnik, 0)
      
    plocica1 = pygame.draw.rect(prozor_igrice, plavaBoja,
      (plocica1_x_koordinata, plocica1_y_koordinata, plocica1_duzina,
      plocica1_visina), 0)

    plocica2 = pygame.draw.rect(prozor_igrice, plavaBoja,
      (plocica2_x_koordinata, plocica2_y_koordinata, plocica2_duzina,
      plocica2_visina), 0)

    broj_poena = font_za_tekst.render(str (igrac1_broj_poena) + ":" + str (igrac2_broj_poena), 1, tamnoPlavaBoja)
    prozor_igrice.blit(broj_poena, (duzina_prozora / 2 - broj_poena.get_width()/2, 10))

    pygame.display.update()

    time.sleep(0.03)

    sat.tick(40)

    


      
    
          

        
pygame.quit()









