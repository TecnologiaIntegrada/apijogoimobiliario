
from dataclasses import dataclass


@dataclass(frozen=True)
class Saldo:
   
    valor: int
    
    def adicionar(self, quantia: int) -> 'Saldo':
        
        return Saldo(self.valor + quantia)
    
    def subtrair(self, quantia: int) -> 'Saldo':
        
        return Saldo(self.valor - quantia)
    
    def eh_suficiente_para(self, custo: int) -> bool:
        
        return self.valor >= custo
    
    def eh_negativo(self) -> bool:
        
        return self.valor < 0
    
    def __str__(self) -> str:
        return f"Saldo: {self.valor}"

