
from typing import TYPE_CHECKING
from .estrategia_compra import EstrategiaDeCompra

if TYPE_CHECKING:
    from ..entities.propriedade import Propriedade
    from ..value_objects.saldo import Saldo


class EstrategiaCautelosa(EstrategiaDeCompra):
     # Jogador cauteloso sempre mantém uma reserva de segurança.
     # Só compra se após a compra ainda houver pelo menos 80 de saldo....
        
    RESERVA_MINIMA = 80
    
    def deve_comprar(
        self,
        propriedade: 'Propriedade',
        saldo_atual: 'Saldo'
    ) -> bool:
       
        saldo_apos_compra = saldo_atual.valor - propriedade.custo_venda
        return saldo_apos_compra >= self.RESERVA_MINIMA
    
    def tipo(self) -> str:
        return "cauteloso"

