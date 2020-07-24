import random

def u_move(dict):
    temp=dict[11]
    dict[11]=dict[13]
    dict[13]=dict[14]
    dict[14]=dict[12]
    dict[12]=temp
    temp=dict[44]
    temp2=dict[43]
    dict[44]=dict[52]
    dict[43]=dict[54]
    dict[52]=dict[21]
    dict[54]=dict[22]
    dict[21]=dict[63]
    dict[22]=dict[61]
    dict[63]=temp
    dict[61]=temp2
def uprime_move(dict):
    u_move(dict)
    u_move(dict)
    u_move(dict)
def u2_move(dict):
    u_move(dict)
    u_move(dict)
def r_move(dict):
    temp=dict[61]
    dict[61]=dict[63]
    dict[63]=dict[64]
    dict[64]=dict[62]
    dict[62]=temp
    temp=dict[44]
    dict[44]=dict[14]
    dict[14]=dict[24]
    dict[24]=dict[34]
    dict[34]=temp
    temp=dict[42]
    dict[42]=dict[12]
    dict[12]=dict[22]
    dict[22]=dict[32]
    dict[32]=temp
def rprime_move(dict):
    r_move(dict)
    r_move(dict)
    r_move(dict)
def r2_move(dict):
    r_move(dict)
    r_move(dict)
def f_move(dict):
    temp=dict[21]
    dict[21]=dict[23]
    dict[23]=dict[24]
    dict[24]=dict[22]
    dict[22]=temp
    temp=dict[13]
    dict[13]=dict[53]
    dict[53]=dict[32]
    dict[32]=dict[63]
    dict[63]=temp
    temp=dict[14]
    dict[14]=dict[54]
    dict[54]=dict[31]
    dict[31]=dict[64]
    dict[64]=temp
def fprime_move(dict):
    f_move(dict)
    f_move(dict)
    f_move(dict)
def f2_move(dict):
    f_move(dict)
    f_move(dict)
def l_move(dict):
    temp=dict[51]
    dict[51]=dict[53]
    dict[53]=dict[54]
    dict[54]=dict[52]
    dict[52]=temp
    temp=dict[41]
    dict[41]=dict[31]
    dict[31]=dict[21]
    dict[21]=dict[11]
    dict[11]=temp
    temp=dict[43]
    dict[43]=dict[33]
    dict[33]=dict[23]
    dict[23]=dict[13]
    dict[13]=temp
def lprime_move(dict):
    l_move(dict)
    l_move(dict)
    l_move(dict)
def l2_move(dict):
    l_move(dict)
    l_move(dict)
def d_move(dict):
    temp=dict[31]
    dict[31]=dict[33]
    dict[33]=dict[34]
    dict[34]=dict[32]
    dict[32]=temp
    temp=dict[23]
    dict[23]=dict[51]
    dict[51]=dict[42]
    dict[42]=dict[64]
    dict[64]=temp
    temp=dict[24]
    dict[24]=dict[53]
    dict[53]=dict[41]
    dict[41]=dict[62]
    dict[62]=temp
def dprime_move(dict):
    d_move(dict)
    d_move(dict)
    d_move(dict)
def d2_move(dict):
    d_move(dict)
    d_move(dict)
def b_move(dict):
    temp=dict[41]
    dict[41]=dict[43]
    dict[43]=dict[44]
    dict[44]=dict[42]
    dict[42]=temp
    temp=dict[33]
    dict[33]=dict[52]
    dict[52]=dict[12]
    dict[12]=dict[62]
    dict[62]=temp
    temp=dict[34]
    dict[34]=dict[51]
    dict[51]=dict[11]
    dict[11]=dict[61]
    dict[61]=temp
def bprime_move(dict):
    b_move(dict)
    b_move(dict)
    b_move(dict)
def b2_move(dict):
    bprime_move(dict)
    bprime_move(dict)
def x_regrip(dict):
    r_move(dict)
    lprime_move(dict)
def xprime_regrip(dict):
    rprime_move(dict)
    l_move(dict)
def y_regrip(dict):
    u_move(dict)
    dprime_move(dict)
def yprime_regrip(dict):
    uprime_move(dict)
    d_move(dict)
def z_regrip(dict):
    f_move(dict)
    bprime_move(dict)
def zprime_regrip(dict):
    fprime_move(dict)
    b_move(dict)
def all_faces(dict):
    face1=(dict[11],dict[12],dict[13],dict[14])
    face2=(dict[21],dict[22],dict[23],dict[24])
    face3=(dict[31],dict[32],dict[33],dict[34])
    face4=(dict[41],dict[42],dict[43],dict[44])
    face5=(dict[51],dict[52],dict[53],dict[54])
    face6=(dict[61],dict[62],dict[63],dict[64])
    print('\n',face1)
    print('\n',face2)
    print('\n',face3)
    print('\n',face4)
    print('\n',face5)
    print('\n',face6)
def solve_check(dict):
    if dict[11]==dict[12]==dict[13]==dict[14] and dict[21]==dict[22]==dict[23]==dict[24] and dict[31]==dict[32]==dict[33]==dict[34] and dict[41]==dict[42]==dict[43]==dict[44] and dict[51]==dict[52]==dict[53]==dict[54] and dict[61]==dict[62]==dict[63]==dict[64]:
       print('The cube is solved!')
    else:
        print('The cube is scrambled.')
def logical_xor(str1, str2):
    return bool(str1) ^ bool(str2)
def scramble(list,list2, dict):
    i=0
    while i<8:  
        if list[i]=='U' and logical_xor(list[i+1]!="U\'", logical_xor(list[i+1]!='U2', list[i+1]!='U')): 
            i+=1
            continue
        elif list[i]=='R' and logical_xor(list[i+1]!="R\'", logical_xor(list[i+1]!='R2', list[i+1]!='R')):
            i+=1
            continue
        elif list[i]=='F' and logical_xor(list[i+1]!="F\'", logical_xor(list[i+1]!='F2', list[i+1]!='F')):
            i+=1
            continue
        elif list[i]=='U2' and logical_xor(list[i+1]!="U\'", logical_xor(list[i+1]!='U', list[i+1]!='U2')):
            i+=1
            continue
        elif list[i]=='F2' and logical_xor(list[i+1]!="F\'", logical_xor(list[i+1]!='F', list[i+1]!='F2')):
            i+=1 
            continue            
        elif list[i]=='R2' and logical_xor(list[i+1]!="R\'", logical_xor(list[i+1]!='R', list[i+1]!='R2')):
            i+=1
            continue            
        elif list[i]=="U\'" and logical_xor(list[i+1]!='U', logical_xor(list[i+1]!='U2', list[i+1]!="U\'")): 
            i+=1
            continue
        elif list[i]=="R\'" and logical_xor(list[i+1]!='R', logical_xor(list[i+1]!='R2', list[i+1]!="R\'")):
            i+=1
            continue
        elif list[i]=="F\'" and logical_xor(list[i+1]!='F', logical_xor(list[i+1]!='F2', list[i+1]!="F\'")):
            i+=1
            continue
        else:
            i=0
            list.clear()
            list.extend(random.choices(list2, k=9))
          
    i=0
    while i<9:   
        if list[i]=='U':
           u_move(dict)
           i+=1
        elif list[i]=="U\'":
            uprime_move(dict)
            i+=1
        elif list[i]=='U2':
            u2_move(dict)
            i+=1
        elif list[i]=='R':
            r_move(dict)
            i+=1
        elif list[i]=="R\'":
            rprime_move(dict)
            i+=1
        elif list[i]=='R2':
            r2_move(dict)
            i+=1
        elif list[i]=='F':
            f_move(dict)
            i+=1
        elif list[i]=="F\'":
            fprime_move(dict)
            i+=1
        elif list[i]=='F2':
            f2_move(dict)
            i+=1
    
    #print('\n','SCRAMBLE:',end=' ')
    #for val in list:
        #print(val, end=' ')
    #print('\n')
    

