from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

fechaN=0
dias=0
meses=0
mes=0
edad=0
anios=0
naci=0
now=0
diasT=0
dia=0

print("ingrese su fecha de su nacimineto")
fechaN=int(input())
print("ingrese que mes nacio (solo con numeros)")
meses=int(input())
print("ingrese que dia")
dias=int(input())

naci=datetime(fechaN,meses,dias)
now=datetime.now()
diasT=now-naci
anios=diasT.day//365
mes=(diasT.day%365) //30
dia=(diasT,day%365)%30


