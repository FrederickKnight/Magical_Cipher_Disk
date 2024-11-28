from .disk import Disk
from .stones import Stones
import random
from unidecode import unidecode

class Cipher:
    def __init__(self,disk:Disk=None,stones:Stones=None) -> None:
        
        self.__disk = disk
        self.__disk_keys = self.__disk.get_id()
        
        self.__stones = stones
        
        self.__alphabet_disk = ''
        self.__comparative_alphabet = ''
        self.__encrypted_text = ''
        
        
    def config_comparative_alphabet(self,comparative_alphabet:str=None,disk_order:list=None,disk_index:tuple=None):
        
        if comparative_alphabet != None:
            _comparative_alphabet = comparative_alphabet
        else:
            _comparative_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            
            
        if disk_order != None:
            self.__disk_order = disk_order
        else:
            #random select del disk order
            self.__disk_order=self.__random__disk__order(self.__disk)
        
        
        _temp_alphabet = ''
        for _d in self.__disk_order:
            _temp_disk = self.__disk.get_disk()["disk"][_d]["disk"]
            for _l in _temp_disk:
                _temp_alphabet += _l
                
        
        #configuracion de orden seleccionado para el disco
        if disk_index != None:
            self.__disk_index = disk_index
        else:
            #random select del disk index
            _index_choice_1 = random.choice(_comparative_alphabet)
            _index_choice_2 = random.choice(_temp_alphabet)
            self.__disk_index = [_index_choice_1,_index_choice_2]
        
                
                
        _index_alphabet_comparative = _comparative_alphabet.index(str(self.__disk_index[0]).upper())     
        _index_alphabet_disk = _temp_alphabet.index(str(self.__disk_index[1]).upper())
        
        self.__comparative_alphabet = _comparative_alphabet[_index_alphabet_comparative:] + _comparative_alphabet[:_index_alphabet_comparative]
        self.__alphabet_disk = _temp_alphabet[_index_alphabet_disk:] + _temp_alphabet[:_index_alphabet_disk]
        
        return self
    
    def Encrypt(self,txt:str='',isEncrypted:bool=False):
        
        _isEncrypted = isEncrypted
        
        if not _isEncrypted:
            _normal_alphabet = self.__comparative_alphabet
            _encrypt_alphabet = self.__alphabet_disk
        else:
            _normal_alphabet = self.__alphabet_disk
            _encrypt_alphabet = self.__comparative_alphabet
        
        
        #normalizacion del texto, espacios y acentos
        _entry_text = ''
    
        for _txt in txt:
            if _txt not in _normal_alphabet:
                _entry_text += self.__normalize_text__(_txt,True)
            else:
                _entry_text += self.__normalize_text__(_txt)
                
        
        # guardar espacios entre palabras, para asi reconstruirlo al final
        _entry_text_spaces = [len(_s) for _s in txt.split()]
        
        
        #Encriptador
        _new_text = ''
        for _t in range(len(_entry_text)):
            
            _temp_t = _entry_text[_t] #letra a letra
            _range_yellow = self.__stones.get_stone_yellow()
            
            if _temp_t in _normal_alphabet and _range_yellow > 0:  #si esta en el alfabeto normal continua, sino lo toma como un caracter especial
                
                if (_t % _range_yellow == 0) and (_t > 0): 
                    # si el numero de letra coincide con el valor de la piedra amarilla, se ejecutara el cambio
                    _new_text += self.__stones.apply_stones(_temp_t,_normal_alphabet,_encrypt_alphabet,_isEncrypted,_t)
                
                else:
                    _new_text += self.__change_letter__(_temp_t,_normal_alphabet,_encrypt_alphabet)
            
            else:
                #Pasarlo como especial, acentos interrogantes o numeros, osea sin cambios
                _new_text += _temp_t
        
        
        
        # Reconstruccion de texto con espacios
        _text_return = ''
        for _sp in _entry_text_spaces:
            _text_return += f"{_new_text[:_sp]} "
            _new_text = _new_text[_sp:]
            
            
        self.__encrypted_text = _text_return
        
        return self
    
    
    #### Getters ####
    
    def get_encrypted_text(self):
        return self.__encrypted_text
  
    
    def get_comparative_alphabet(self):
        return self.__comparative_alphabet
    
    def get_disk_alphabet(self):
        return self.__alphabet_disk
    
    #### Random AutoConfig ####
    
    
    def __change_letter__(self,txt,n_alphabet:str='',d_alphabet:str=''):
        
        _id = n_alphabet.index(str.upper(txt))
        _t = str.upper(d_alphabet[_id])
        return _t
    
    
    def __random__disk__order(self,disk:Disk):
        
        _keys = disk.get_id()
        _choice = []
        for _k in range(len(_keys)):
            _temp = random.choice(_keys)
            _choice.append(_temp)
            _keys.remove(_temp)
            
        return _choice

    
    def __normalize_text__(self,txt:str='',isUnidecode:bool=False):
        # regresa texto sin espacios
        if isUnidecode:
            return unidecode(txt.upper().replace(" ",""))
        else:
            return txt.upper().replace(" ","")