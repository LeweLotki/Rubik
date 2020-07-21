import pygame
import random
from mypackages import functions2

bl = (  0,   0,   0)
w = (255, 255, 255)
b =  (  0,   0, 255)
g = (  0, 240,   0)
r =   (255,   0,   0)
gr=(200,200,200)
y=(255,255,0)
o=(255,140,0)

cube={11:w,12:w,13:w,14:w,21:r,22:r,23:r,24:r,31:y,32:y,33:y,34:y,41:o,42:o,43:o,44:o,51:g,52:g,53:g,54:g,61:b,62:b,63:b,64:b}
moves=['U',"U\'",'U2','R',"R\'",'R2','F',"F\'",'F2'] 
str1=''
chosen_moves=[]
chosen_moves.extend(random.choices(moves, k=9))

pygame.init()

size = [345,435]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("rubik cube")

done=False
clock=pygame.time.Clock()

functions2.yprime_regrip(cube)
functions2.scramble(chosen_moves,moves,cube)

for val in chosen_moves:
        str1=str1+' '+val

font=pygame.font.SysFont('Courier', 16) 
text=font.render('SCRAMBLE:'+str1, True, bl, gr) 
textRect=text.get_rect() 
textRect.center=(170,20)

while not done:
 
 if cube[11]==cube[12]==cube[13]==cube[14] and cube[21]==cube[22]==cube[23]==cube[24] and cube[31]==cube[32]==cube[33]==cube[34] and cube[41]==cube[42]==cube[43]==cube[44] and cube[51]==cube[52]==cube[53]==cube[54] and cube[61]==cube[62]==cube[63]==cube[64]:
    text=font.render('        The cube is solved!', True, bl, gr) 
    screen.blit(text, textRect)
 else:
    text=font.render('SCRAMBLE:'+str1, True, bl, gr) 
    screen.blit(text, textRect)
     
 key=pygame.key.get_pressed() 
  
 clock.tick(5)

 for event in pygame.event.get():
    if event.type == pygame.QUIT: 
            done=True
 
 if key[pygame.K_u]:
    functions2.u_move(cube)
 elif key[pygame.K_r]:
    functions2.r_move(cube)
 elif key[pygame.K_f]:
    functions2.f_move(cube)
 elif key[pygame.K_l]:
    functions2.l_move(cube)
 elif key[pygame.K_d]:
    functions2.d_move(cube)
 elif key[pygame.K_b]:
    functions2.b_move(cube)
 elif key[pygame.K_x]:
    functions2.x_regrip(cube)
 elif key[pygame.K_y]:
    functions2.y_regrip(cube)
 elif key[pygame.K_z]:
    functions2.z_regrip(cube)
 elif key[pygame.K_s]:
    chosen_moves.clear()
    str1=''
    cube={11:w,12:w,13:w,14:w,21:r,22:r,23:r,24:r,31:y,32:y,33:y,34:y,41:o,42:o,43:o,44:o,51:g,52:g,53:g,54:g,61:b,62:b,63:b,64:b}
    functions2.yprime_regrip(cube)
    chosen_moves.extend(random.choices(moves, k=9))
    functions2.scramble(chosen_moves,moves,cube)
    for val in chosen_moves:
        str1=str1+' '+val
    
 
 screen.fill(gr)
 screen.blit(text, textRect)
 pygame.draw.rect(screen, cube[41], [130, 40, 40, 40])
 pygame.draw.rect(screen, cube[42], [175, 40, 40, 40])  
 pygame.draw.rect(screen, cube[43], [130, 85, 40, 40])
 pygame.draw.rect(screen, cube[44], [175, 85, 40, 40])
 pygame.draw.rect(screen, cube[11], [130, 130, 40, 40])
 pygame.draw.rect(screen, cube[12], [175, 130, 40, 40])
 pygame.draw.rect(screen, cube[13], [130, 175, 40, 40])
 pygame.draw.rect(screen, cube[14], [175, 175, 40, 40])
 pygame.draw.rect(screen, cube[21], [130, 220, 40, 40])
 pygame.draw.rect(screen, cube[22], [175, 220, 40, 40])
 pygame.draw.rect(screen, cube[23], [130, 265, 40, 40])
 pygame.draw.rect(screen, cube[24], [175, 265, 40, 40])
 pygame.draw.rect(screen, cube[31], [130, 310, 40, 40])
 pygame.draw.rect(screen, cube[32], [175, 310, 40, 40])
 pygame.draw.rect(screen, cube[33], [130, 355, 40, 40])
 pygame.draw.rect(screen, cube[34], [175, 355, 40, 40])
 pygame.draw.rect(screen, cube[51], [40, 130, 40, 40])
 pygame.draw.rect(screen, cube[52], [85, 130, 40, 40])
 pygame.draw.rect(screen, cube[53], [40, 175, 40, 40])
 pygame.draw.rect(screen, cube[54], [85, 175, 40, 40])
 pygame.draw.rect(screen, cube[61], [220, 130, 40, 40])
 pygame.draw.rect(screen, cube[62], [265, 130, 40, 40])
 pygame.draw.rect(screen, cube[63], [220, 175, 40, 40])
 pygame.draw.rect(screen, cube[64], [265, 175, 40, 40])




 pygame.display.flip()
pygame.quit()
