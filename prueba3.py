asientocomun=60000
adicional=80000
noreclinable=50000

lista=[]
asientos=("comun","adicional","NO reclinable")

def datosPersonales():
    rut=int(input("Ingrese rut"))
    guardarut=[rut]
    print("Tu Rut: ",guardarut)

def comprarpasajes():
    print("comun | adicional  | NO reclinable")
    numeroAsientos=int(input("Cual de los 3 tipos de asiento desea? "))
    for i in (len(numeroAsientos)):
        print(i,numeroAsientos[i])
    subtotal=(asientocomun + adicional + noreclinable)    
    asiento9=[asientos,subtotal]
    lista.append(asiento9)

    for i in range(len(asiento9)):
        print(asiento9[i][0],end="")
        print(asiento9[i][1],end="")
        print(asiento9[i][2],end="")

def valores(): 
    subtotal=0
    total=0
    asientocomun=60000
    adicional=80000
    noreclinable=50000
    print("(1)Asiento comun 60.000")
    print("(2)Asiento para piernas 80.000")
    print("(3)Asiento NO reclinable 50.000")
    print("(4)Total")
    opc=int(input(""))
    if opc==1:
        total=(total+asientocomun)
    elif opc==2:
        total=(total+adicional)
    elif opc==3:
        total=(total+noreclinable)
    elif opc==4:
        print(subtotal) 

while True:
    print("(1)Siguiente")
    print("(2)Valor y tipos de asiento")
    print("(3)Ingresar datos personales")
    print("(4)salir")
    
    opcion=int(input("Ingrese opcion: "))

    if opcion==1:
        comprarpasajes()
    elif opcion==2:
        valores()
    elif opcion==3:
        datosPersonales()
    elif opcion==4:
        break    






