total = int(input("ingrese cantidad total de preguntas: "))
print(" ")
correctas = int(input("ahora la cantidad de respuestas correctas: "))
print(" ")
porcentaje = (correctas * 100)/total
if porcentaje >= 90:
    print("EXCELENTE")
elif porcentaje >= 70:
    print("BUENO")
elif porcentaje >= 60:
    print("APROBADO")
else:
    print("NO ALCANZO")

#Por Leonardo Brabo