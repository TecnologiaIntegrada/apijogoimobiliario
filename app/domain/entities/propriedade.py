
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .jogador import Jogador


class Propriedade:

    def __init__(
        self,
        nome: str,
        posicao: int,
        custo_venda: int,
        valor_aluguel: int
    ):
        self._nome = nome
        self._posicao = posicao
        self._custo_venda = custo_venda
        self._valor_aluguel = valor_aluguel
        self._proprietario: Optional['Jogador'] = None
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def posicao(self) -> int:
        return self._posicao
    
    @property
    def custo_venda(self) -> int:
        return self._custo_venda
    
    @property
    def valor_aluguel(self) -> int:
        return self._valor_aluguel
    
    @property
    def proprietario(self) -> Optional['Jogador']:
        return self._proprietario
    
    def esta_disponivel(self) -> bool:
        #Dispon. para compra ?
        return self._proprietario is None
    
    def pertence_a(self, jogador: 'Jogador') -> bool:
        #De quem é a propriedade
        return self._proprietario == jogador
    
    def pertence_a_outro(self, jogador: 'Jogador') -> bool:
       #Checa o proprietário
        return (
            not self.esta_disponivel() and 
            not self.pertence_a(jogador)
        )
    
    def definir_proprietario(self, jogador: 'Jogador') -> None:
        
        self._proprietario = jogador
    
    def liberar(self) -> None:
       
        self._proprietario = None
    
    def __str__(self) -> str:
        proprietario_nome = (
            self._proprietario.nome 
            if self._proprietario 
            else "Disponível"
        )
        return (
            f"{self._nome} (Pos: {self._posicao}, "
            f"Custo: {self._custo_venda}, "
            f"Aluguel: {self._valor_aluguel}, "
            f"Dono: {proprietario_nome})"
        )
    
    def __repr__(self) -> str:
        return f"Propriedade({self._nome}, pos={self._posicao})"

