import random
#Variables a declarar
app=["WhatssApp","Facebook","Facebook Messenger","Telegram", "Instagram", "TikTok", "Linkedin" ,"Twitter"]
wp = 0
fb = 0
fbme = 0
tg = 0
ig = 0
tt= 0
lk = 0
tw = 0

#Sentencia FOR para dar usos aleatorios
for a in range (3000):
    uso = random.choice(app)
    print(uso)
    if uso == app[0]:
        wp = wp + 1
    elif uso == app[1]:
        fb = fb + 1
    elif uso == app[2]:
        fbme = fbme + 1
    elif uso == app[3]:
        tg = tg + 1
    elif uso == app[4]:
        ig  = ig + 1
    elif uso == app[5]:
        tt = tt + 1
    elif uso == app[6]:
        lk = lk+ 1
    elif uso == app[7]:
        tw = tw + 1

print("\n")
#Operaciones
totalwp=    round((wp *100)/3000 , 2)
totalfb=    round((fb *100)/3000 ,2)
totalfbme=  round((fbme*100)/3000 ,2)
totaltg=    round((ig*100)/3000 ,2)
totalig=    round((ig*100)/3000 ,2)
totaltt=    round((tt*100)/3000 ,2)
totallk=    round((lk*100)/3000 ,2)
totaltw=    round((tw*100)/3000 ,2)

#Mostrar pantalla #
print("El uso de la App de WhatssApp es:" ,wp, "el porcentaje es",totalwp, "%" )
print("El uso de la App de Facebook es:"  ,fb ,"el porcentaje es",totalfb ,"%")
print("El uso de la App de Facebook Messenger es:" ,fbme, "el porcentaje es",totalfbme, "%")
print("El uso de la App de Telegram es:"  ,tg ,"el porcentaje es",totaltg ,"%")
print("El uso de la App de Instagram es:"  ,ig ,"el porcentaje es" ,totalig, "%")
print("El uso de la App TikTok es:" ,tt ,"el porcentaje es", totaltt ,"%")
print("El uso de la App de Linkedin es:"   ,lk ,"el porcentaje es",totallk, "%")
print("El uso de la App de Twitter es:"    ,tw ,"el porcentaje es",totaltw,"%")
print("Fin del algoritmo")
print("GRACIAS ")