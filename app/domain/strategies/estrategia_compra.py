from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..entities.propriedade import Propriedade
    from ..value_objects.saldo import Saldo


class EstrategiaDeCompra(ABC):
    #Interface para estratégias de decisão de compra de propriedades.
    
    #Cada tipo de jogador implementa sua própria estratégia,
    #seguindo o princípio Open/Closed (aberto para extensão, fechado para modificação)....
    
    @abstractmethod
    def deve_comprar(
        self,
        propriedade: 'Propriedade',
        saldo_atual: 'Saldo'
    ) -> bool:
         #Decide se deve comprar a propriedade baseado na estratégia.
        pass
    
    @abstractmethod
    def tipo(self) -> str:

        pass

