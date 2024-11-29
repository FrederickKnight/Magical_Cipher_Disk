import Magical_Cipher_Disk as cd

regular_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
splits = [6,7]
disk_serie = "71298SCDFKQJAC"

#creacion del disco con su configuracion deseada
disk = cd.Disk(alphabet=regular_alphabet,split_list=splits,disk_serie=disk_serie).Create_Disk()
print(disk)

#creacion de las piedras con su valor
stones = cd.Stones([("YELLOW",1),('RED-GREEN',2),("BLUE",1)])

#Asignacion del objeto cipher con el disco y las piedras correspondientes
cipher = cd.Cipher(disk=disk,stones=stones) 


disk_order = ['UJ','QW','TH','BF']
disk_index = ['j','A']

#configuracion de la comparativa de alfabetos
cipher.config_comparative_alphabet(disk_index=disk_index,comparative_alphabet=regular_alphabet,disk_order=disk_order)

normal_text = 'Good Morning/Evening github user'
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