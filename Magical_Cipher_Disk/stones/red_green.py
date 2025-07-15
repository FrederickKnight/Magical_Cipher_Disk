from .base import BaseStone

class RedGreenStone(BaseStone):
    def __init__(self, value):
        super().__init__("RED-GREEN", value)

    def apply(self,letter:str,source_alphabet:str = None,target_alphabet:str = None,isEncrypted:bool = False):
        _orden = -self.value if isEncrypted else self.value

        _index = (source_alphabet.index(str.upper(letter))+_orden)%len(target_alphabet)
        return str.upper(target_alphabet[_index])