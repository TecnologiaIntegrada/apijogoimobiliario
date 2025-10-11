
from typing import TYPE_CHECKING
from .estrategia_compra import EstrategiaDeCompra

if TYPE_CHECKING:
    from ..entities.propriedade import Propriedade
    from ..value_objects.saldo import Saldo


class EstrategiaImpulsiva(EstrategiaDeCompra):
       
    def deve_comprar(
        self,
        propriedade: 'Propriedade',
        saldo_atual: 'Saldo'
    ) -> bool:
        
        return True  # O jogador Impulsivo sempre quer comprar mais !
    
    def tipo(self) -> str:
        return "impulsivo"

