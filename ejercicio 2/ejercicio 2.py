import random
r=random.randint(1,20)
num=0
contador=6



while(contador!=0):
    print("ingrese su numero")
    num=int(input())
    if(num>r):
        print("tu numero es mas grande que el oculto")
        contador=contador-1
    else:
        if(num<r):
            print("tu numero es menor3 que el oculto")
            contador=contador-1
        else:
            print("¡¡¡adivinaste el numero!!!")
            contador=0




