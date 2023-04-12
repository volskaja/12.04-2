import pygame
import random
import sys

def MAJA(x,y,laius,korgus,pind,varv):
    punktid=[(x,y-((3/4.0)*korgus)),(x,y),(x+laius,y),(x+laius,y-(3/4.0)*korgus),(x,y-((3/4.0)*korgus)),(x+laius/2.0,y-korgus),(x+laius,y-(3/4.0)*korgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,varv,False,punktid,suurus)

r=random.randint(0, 255)
g=random.randint(0, 255)
b=random.randint(0, 255)
fon=[r,g,b]

r=random.randint(0, 255)
g=random.randint(0, 255)
b=random.randint(0, 255)
majavarv=[r,g,b]
Green=[153, 255, 153]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud kujundid")
pind.fill(varv)

MAJA(100,400,300,400,pind,majavarv)
pygame.display.flip()

for i in range (10):
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    varv=[r,g,b]

    laius=random.randint(1,80)
    korgus=random.randint(1,80)

    x=random.randint(0,610)
    y=random.randint(0,450)
    pygame.draw.rect(pind,varv,[x,y,laius,korgus])
    pygame.display.flip()

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
         break
pygame.quit()