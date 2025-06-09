b1000=0
b200=0
saldos=0
sacar=0
restomil=0
restodos=0

print("ingrese caunto quiere retirar")
sacar=int(input())



if (sacar>999):
    b1000=sacar//1000
    restomil=sacar%1000

    b200=restomil//200
    restodos=restomil%200
    
    print("se sacaron", b1000 , "billetes de mil")
    print("se sacaron", b200 ,"billetes de doscientos")
    print("sobraron", restodos)
else:
    if (sacar>199):
        
        b200=sacar//200
        restodos=sacar%200
        print("se sacaron", b200 ,"billetes de doscientos")
        print("sobraron", restodos)
        
    else:
        print("iu pobre")
        
