tenho_sede = True
Tenho_fome = True

if Tenho_fome and tenho_sede:
    print("Comprar um sanduiche e coca-cola!")

elif tenho_sede and not Tenho_fome:
    print("Comprar coca-cola")


elif not tenho_sede and Tenho_fome:
    print("comprar sanduiche")
 
else:
    print("Não gastar dinheiro")