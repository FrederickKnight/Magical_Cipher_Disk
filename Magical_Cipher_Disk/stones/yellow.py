from .base import BaseStone

class YellowStone(BaseStone):
    def __init__(self, value):
        self._modifier_limit = 4
        super().__init__("YELLOW", value%self._modifier_limit)

    def __add__(self,other:BaseStone):
        """
        Debido a que las Yellow actuaran como bateria y que necesito que solo tengan como maximo un valor de 4, cada valor que se le añada
        sera ajustado a esos limites usando % 4.
        """
        if isinstance(other,BaseStone) and self == other:
            new_value = (self._value+other._value)%self._modifier_limit
            return YellowStone(new_value)
        return NotImplementedError