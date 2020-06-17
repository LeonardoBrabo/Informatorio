print("Ventas dia 1:")
numeroVentas = int(input("ingrese el numero de ventas asi luego ingresa sus precios: "))
print("")
total1= 0
for i in range(numeroVentas):
    print(f"ingreso obtenido de la venta {i}: ")
    valor = int(input())
    total1 = total1 + valor
print("Venta dia 2: ")
numeroVentas = int(input("ingrese el numero de ventas asi luego ingresa sus precios: "))
print("")
total2= 0
for i in range(numeroVentas):
    print(f"ingreso obtenido de la venta {i}: ")
    valor = int(input())
    total2 = total2 + valor
if total1 > total2:
    print("Vendio mas el Dia 1")
elif total1 < total2:
    print("Vendio mas el Dia 2")
else:
    print("los dos dias obtuvo la misma cantidad")

#Por Leonardo Brabo