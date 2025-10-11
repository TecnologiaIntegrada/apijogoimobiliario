
from typing import TYPE_CHECKING
from .estrategia_compra import EstrategiaDeCompra

if TYPE_CHECKING:
    from ..entities.propriedade import Propriedade
    from ..value_objects.saldo import Saldo


class EstrategiaExigente(EstrategiaDeCompra):
    
    
    ALUGUEL_MINIMO = 50
    
    def deve_comprar(
        self,
        propriedade: 'Propriedade',
        saldo_atual: 'Saldo'
    ) -> bool:
        
        return propriedade.valor_aluguel > self.ALUGUEL_MINIMO
    
    def tipo(self) -> str:
        return "exigente"

