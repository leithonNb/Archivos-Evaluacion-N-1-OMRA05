acl = int(input("Cual es el numero IPV4 de la acl: "))
if acl >= 1 and acl <=99:
    print("Esta es una acl IPV4 estandar")
elif acl >=100 and acl <=199:
    print("Esta es una acl IPV4 extendida")
else:
    print("No corresponde a una lista de acceso")