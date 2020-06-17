usuario = str(input("id: "))
password = str(input("pass: "))
print("usuario creado")
print(" ")
print("loguearse:")
us =str(input("id: "))
contra = str(input("pass:" ))
cont= 0
while cont <5:
    if us != usuario or contra != password:
        us =str(input("id: "))
        contra = str(input("pass:" ))
        cont+= 1
    else:
        print("USUARIO CORRRECTO")
        break
if cont == 5:
    print("USUARIO BLOQUEADO")

#Por Leonardo Brabo
        
    


