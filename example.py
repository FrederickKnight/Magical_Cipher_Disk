import Magical_Cipher_Disk as cd

regular_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# separaciones de lo que constara cada disco, 6 letras y 7 letras repitiendose hasta acabar, 
# si no hay mas letras la ultima parte quedara con las que sobren
splits = [6,7]

# la serie del disco funciona como una semilla a la hora de crearlo, 
# si no has creado alguno y proporcionas una, puede que no funcione debido a que los numeros iniciales son la semilla de la randomizacion
# y las letras consecuentes son para comparar si el disco contiene las partes exactas a esa serie
# SCDFK es solo un añadido como marca, no tiene importancia mas alla de servir para la separacion de la serie
# 71298 -- SCDFK -- QJAC
disk_serie = "71298SCDFKQJAC"

#creacion del disco con su configuracion deseada
disk = cd.Disk(alphabet=regular_alphabet,split_list=splits,disk_serie=disk_serie).Create_Disk()
print(disk)

#creacion de las piedras con su valor
stones = cd.Stones([("YELLOW",1),('RED-GREEN',2),("BLUE",1)])

#Asignacion del objeto cipher con el disco y las piedras correspondientes
cipher = cd.Cipher(disk=disk,stones=stones) 

# Orden del disco, el como las partes se juntaran para rearmar la figura circular
disk_order = ['UJ','QW','TH','BF']

# Index de ambos discos, el primero es el disco exterior y el segundo el disco interior
# El disco exterior es el alfabeto "normal" o el que se espera sea el alfabeto sin encriptacion
# El disco interior es el alfabeto reordenado y configurado previamente, es el que se ocupara para la encriptacion
disk_index = ['j','A']

#configuracion de la comparativa de alfabetos
cipher.config_comparative_alphabet(disk_index=disk_index,comparative_alphabet=regular_alphabet,disk_order=disk_order)


# Texto a encriptar
normal_text = 'Good Morning/Evening github user'

# Texto a desencriptar
encrypted_example = 'CMMZ UMCIDIB/SYSIDIB BDQPAL AJSC'

#llamadas para ver los alfabetos y como quedaron configurados
print(f"Normal alphabet:\n### {cipher.get_comparative_alphabet()} ###")
print(f"Disk alphabet:\n### {cipher.get_disk_alphabet()} ###")

print()

#encryptacion del texto
cipher.Encrypt(normal_text)
print(f"Normal text now encrypted:| {cipher.get_encrypted_text()} |")

#desencriptacion del texto, solo funciona si es la misma configuracion con la que fue encryptado
cipher.Encrypt(encrypted_example,True)
print(f"Encrypted text now de-encrypted:| {cipher.get_encrypted_text()} |")