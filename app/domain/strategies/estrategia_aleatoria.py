import random
from typing import TYPE_CHECKING
from .estrategia_compra import EstrategiaDeCompra

if TYPE_CHECKING:
    from ..entities.propriedade import Propriedade
    from ..value_objects.saldo import Saldo


class EstrategiaAleatoria(EstrategiaDeCompra):
    # Jogador aleatório decide por sorte....
    # Tem 50% de chance de comprar qualquer propriedade.
    
    def deve_comprar(
        self,
        propriedade: 'Propriedade',
        saldo_atual: 'Saldo'
    ) -> bool:
        # Decide aleatoriamente (50% de chance).
        # retornar T ou F
        return random.choice([True, False])
    
    def tipo(self) -> str:
        return "aleatorio"

