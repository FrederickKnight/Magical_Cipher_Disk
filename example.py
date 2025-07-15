import Magical_Cipher_Disk as mcd

# alfabeto con el que el mensaje se creara originalmente
source_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# alfabeto que servira para crear el mensaje encriptado
target_alphabet = '¿#CDEFGHIJK[}*OPQRSTU?!XYZ'
# Ambos alfabetos pueden ser cualquier lista de caracteres, mientras sea un string y el mismo tamaño para ambas

# separaciones de lo que constara cada disco, como ejemplo;
# 6 letras y 7 letras repitiendose hasta acabar, 
# si no hay mas letras se creara una parte sobrante con ellas
splits = [6,7]

# definire una seed para repetibilidad,
# aunque si se deja en aleatorio o default, se guardara la seed que se uso
seed = 2025

# creacion del disco con su configuracion deseada
disk = mcd.Disk(
    alphabet=target_alphabet,
    splits=splits,
    seed=seed
)

# creacion de las piedras con su valor
stone_holder = mcd.StoneHolder([
    mcd.YellowStone(2),
    mcd.RedGreenStone(5),
    mcd.BlueStone(2)
])

# No es necesario, pero podemos crear un logger custom, aunque por ahora
# solo guardara el mensaje con su configuracion
cipher_logger = mcd.CipherIO(
    base_path="./Messages"
)

#Asignacion del objeto cipher con el disco y las piedras correspondientes
cipher = mcd.Cipher(
    disk=disk,
    stone_holder=stone_holder,
    seed=seed,
    logger=cipher_logger
)

# Orden del disco, el como las partes se juntaran para rearmar la figura circular
disk_order = ['XS', '¿R', 'O[', 'J#']

# Index de ambos discos, el primero es el disco exterior y el segundo el disco interior
# El disco exterior es el alfabeto "normal" o el que se espera sea el alfabeto sin encriptacion
# El disco interior es el alfabeto reordenado y configurado previamente, es el que se ocupara paraA la encriptacion
disk_index = ('Q', 'X')

#configuracion de la comparativa de alfabetos
cipher.config_cipher(
    source_alphabet=source_alphabet,
    disk_order=disk_order,
    disk_index=disk_index
)

# Texto a encriptar
normal_text = 'Good Morning/Evening GitHub user'

# llamadas para ver los alfabetos y como quedaron configurados
print(f"Normal alphabet:\n### {cipher.source_alphabet} ###")
print(f"Disk alphabet:\n### {cipher.target_alphabet} ###\n")

save_result = True

# encryptacion del texto
encrypted_text = cipher.Encrypt(
    entry_text=normal_text,
    save_result=save_result,
    context_for_log="GITHUB"
)
print(f"Normal text now encrypted:| {encrypted_text} |")

# desencriptacion del texto, solo funciona si es la misma configuracion con la que fue encryptado
decrypted_text = cipher.Decrypt(
    entry_text=encrypted_text,
    save_result=save_result,
    context_for_log="GITHUB"
)
print(f"Encrypted text now decrypted:| {decrypted_text} |")


# Los archivos generados llevan el proceso de cada letra convirtiendose, para mayor entendimiento.