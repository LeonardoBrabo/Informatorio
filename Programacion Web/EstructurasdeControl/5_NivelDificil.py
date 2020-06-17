
print("PIZZERIA BELLA NAPOLI:")

pizza = str(input("¿Quiere una pizza vegerariana? s/n: "))
if pizza == "s":
    print("Elija los ingredientes para su pizza")
    print("")
    print("---------------")
    print("1- Pimiento")
    print("2- Rucula")
    print("---------------")
    ingrediente = int(input("eliga 1|2 :  "))
    if ingrediente == 1:
        mostrar= "Pimiento"
    else:
        mostrar = "Rucula"
    print(f"Su pizza es vegetariana, y tiene mozzarella, tomate y {mostrar}")   
elif pizza == "n":
    print("Elija los ingredientes para su pizza")
    print("")
    print("---------------")
    print("1- Jamon")
    print("2- Panceta")
    print("---------------")
    ingrediente = int(input("eliga 1|2 :  "))
    if ingrediente == 1:
        mostrar = "Jamon"
    else:
        mostrar = "Panceta"
    print(f"Su pizza es comun, y tiene mozzarella, tomate y {mostrar}")
else:
    print("Ingrese solamente s o n para reponder")

#Por Leonardo Brabo





