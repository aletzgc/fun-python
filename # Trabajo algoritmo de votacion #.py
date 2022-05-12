print("Ingrese el numero de encuestados: ")
x=int(input())
print("---------------------------------------------")
a=1
trm=0
trk=0
tel=0
#Se crea un Diccionario estudiantes para asociar cada estudiante a una musica y una carrera
estudiantes={}
numeroe=1
#los arreglos musica y carrera son solo para ser mostrados en la seleccion
marcas=dict(huawei=1,samsung=2,apple=3)
carrera=dict(Telematica=1,Arquitectura=2,Medicina=3)
 
print("---------------SELECCION MARCAS----------------")
for j,k in marcas.items():
    print(k,j)
 
print("---------------SELECCION CARRERAS----------------")
for l,m in carrera.items():
    print(m,l)
 
print("--------------------------------------------------")
#lee e ingresa los valores al numero de estudiantes ingresado
while(x!=0):
    print("Estudiante numero "+str(numeroe)+" Digite su marca de celular")
    marcas=input()
    print("Estudiante numero "+str(numeroe)+" Digite su carrera")
    carrerae=input()
    estudiantes["estudiante"+str(numeroe)]=[marcas,carrerae]
    print("-----------------------------------------------")
    numeroe=numeroe+1
    x=x-1
 
#for para recorrer cuantos estudiantes se ingresaron
for g in estudiantes.keys():
    #cuantos estudiantes tienen samsung y estan en la carrera materiales
    if estudiantes["estudiante"+str(a)][0]=="2" and estudiantes["estudiante"+str(a)][1]=="1":
        trm=trm+1
    #cuantos 
    if estudiantes["estudiante"+str(a)][0]=="1":
        trk=trk+1
    #cuantos escuchan electronica
    if estudiantes["estudiante"+str(a)][1]=="2":
        tel=tel+1
    #la variable a hace la iteracion de un estudiante a otro "estudiantes["estudiante"+str(a)]"
    a=a+1
 
print("-----------------------------------------------------")
 
print("Total Huawei: "+str(trm))
print("Total Samsung: "+str(trk))
print("Total Apple: "+str(tel))