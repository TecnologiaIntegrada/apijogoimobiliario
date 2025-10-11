
import random
from typing import List
from ...domain.entities.jogador import Jogador
from ...domain.strategies.estrategia_impulsiva import EstrategiaImpulsiva
from ...domain.strategies.estrategia_exigente import EstrategiaExigente
from ...domain.strategies.estrategia_cautelosa import EstrategiaCautelosa
from ...domain.strategies.estrategia_aleatoria import EstrategiaAleatoria


class FabricaDeJogadores:
   
    
    def criar_jogadores_padrao(self) -> List[Jogador]:
       
        # Criar jogadores
        jogadores = [
            Jogador("Impulsivo", EstrategiaImpulsiva()),
            Jogador("Exigente", EstrategiaExigente()),
            Jogador("Cauteloso", EstrategiaCautelosa()),
            Jogador("Aleatório", EstrategiaAleatoria()),
        ]
        
        # Randomizar ordem
        random.shuffle(jogadores)
        
        # Definir ordem de turno (para desempate)
        
        for i, jogador in enumerate(jogadores):
            jogador._ordem_turno = i
        
        return jogadores

