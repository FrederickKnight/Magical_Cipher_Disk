import Cipher_Disks as cd

regular_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
splits = [6,7]
disk_serie = "71298SCDFKQJAC"


disk = cd.Disk(alphabet=regular_alphabet,split_list=splits,disk_serie=disk_serie).Create_Disk()

stones = cd.Stones([("YELLOW",1),('RED-GREEN',2),("BLUE",1)])

cipher = cd.Cipher(disk=disk,stones=stones)


disk_order = ['UJ','QW','TH','BF']
disk_index = ['j','A']

cipher.config_comparative_alphabet(disk_index=disk_index,comparative_alphabet=regular_alphabet,disk_order=disk_order)

normal_text = 'Good Morning/Evening github user'
encrypted_example = 'CMMZ UMCIDIB/SYSIDIB BDQPAL AJSC'

print(f"Normal alphabet:\n### {cipher.get_comparative_alphabet()} ###")
print(f"Disk alphabet:\n### {cipher.get_disk_alphabet()} ###")

print()

cipher.Encrypt(normal_text)
print(f"Normal text now encrypted:| {cipher.get_encrypted_text()} |")

cipher.Encrypt(encrypted_example,True)
print(f"Encrypted text now de-encrypted:| {cipher.get_encrypted_text()} |")