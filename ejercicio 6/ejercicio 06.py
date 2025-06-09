alum=0
resul=0
sobra=0
cara=0


print("cuantos alumnos hay en el curso")
alum=int(input())

print("cuantos caramelos son")
cara=int(input())

resul=cara//alum
sobra=cara%alum

print("le repartimos a cada alumnos", resul)
print("y sobran:", sobra)
