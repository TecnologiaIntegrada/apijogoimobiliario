
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Posicao:
  
    valor: int
    tamanho_tabuleiro: int = 20
    
    def __post_init__(self):
        """Valida que a posição está dentro do tabuleiro"""
        if self.valor < 0 or self.valor >= self.tamanho_tabuleiro:
            raise ValueError(
                f"Posição {self.valor} inválida. "
                f"Deve estar entre 0 e {self.tamanho_tabuleiro - 1}"
            )
    
    def avancar(self, casas: int) -> Tuple['Posicao', bool]:
        
        nova_posicao_valor = (self.valor + casas) % self.tamanho_tabuleiro
        completou_volta = nova_posicao_valor < self.valor
        
        return Posicao(nova_posicao_valor), completou_volta
    
    def __str__(self) -> str:
        return f"Posição: {self.valor}"

