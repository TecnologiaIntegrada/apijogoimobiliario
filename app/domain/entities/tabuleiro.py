from typing import List
from .propriedade import Propriedade


# Configuração das 20 propriedades do tabuleiro
CONFIGURACAO_PROPRIEDADES = [
    # Zona Inicial (acessível)
    {"nome": "Rua da Paz", "custo": 60, "aluguel": 20},
    {"nome": "Avenida Central", "custo": 80, "aluguel": 30},
    {"nome": "Praça da Liberdade", "custo": 90, "aluguel": 35},
    {"nome": "Rua das Flores", "custo": 70, "aluguel": 25},
    
    # Zona Intermediária
    {"nome": "Avenida Paulista", "custo": 100, "aluguel": 45},
    {"nome": "Rua Augusta", "custo": 120, "aluguel": 52},
    {"nome": "Largo São Bento", "custo": 110, "aluguel": 48},
    {"nome": "Rua da Consolação", "custo": 130, "aluguel": 55},
    
    # Zona Valiosa
    {"nome": "Avenida Atlântica", "custo": 140, "aluguel": 58},
    {"nome": "Copacabana", "custo": 150, "aluguel": 62},
    {"nome": "Ipanema", "custo": 160, "aluguel": 65},
    {"nome": "Leblon", "custo": 155, "aluguel": 60},
    
    # Zona Premium
    {"nome": "Jardins", "custo": 170, "aluguel": 68},
    {"nome": "Vila Madalena", "custo": 165, "aluguel": 66},
    {"nome": "Pinheiros", "custo": 175, "aluguel": 70},
    {"nome": "Brooklin", "custo": 180, "aluguel": 72},
    
    # Zona Luxo
    {"nome": "Morumbi", "custo": 185, "aluguel": 75},
    {"nome": "Vila Olímpia", "custo": 190, "aluguel": 78},
    {"nome": "Itaim Bibi", "custo": 195, "aluguel": 82},
    {"nome": "Faria Lima", "custo": 200, "aluguel": 90},
]


class Tabuleiro:
 #representa o tabuleiro

    def __init__(self):
        self._propriedades = self._criar_propriedades()
        self._tamanho = len(self._propriedades)
    
    def _criar_propriedades(self) -> List[Propriedade]:
        #Cria as prop.
        propriedades = []
        for posicao, config in enumerate(CONFIGURACAO_PROPRIEDADES):
            propriedade = Propriedade(
                nome=config["nome"],
                posicao=posicao,
                custo_venda=config["custo"],
                valor_aluguel=config["aluguel"]
            )
            propriedades.append(propriedade)
        
        return propriedades
    
    @property
    def tamanho(self) -> int:
      # Vamos retornar  o tamanho do tabuleiro
        return self._tamanho
    
    def obter_propriedade_na(self, posicao: int) -> Propriedade:
        
        if posicao < 0 or posicao >= self._tamanho:
            raise IndexError(
                f"Posição {posicao} inválida. "
                f"Deve estar entre 0 e {self._tamanho - 1}"
            )
        
        return self._propriedades[posicao]
    
    def obter_todas_propriedades(self) -> List[Propriedade]:
      
        return self._propriedades.copy()
    
    def __str__(self) -> str:
        return f"Tabuleiro com {self._tamanho} propriedades"
    
    def __repr__(self) -> str:
        return f"Tabuleiro(tamanho={self._tamanho})"

