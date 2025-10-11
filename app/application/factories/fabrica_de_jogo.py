
from typing import List
from ...domain.entities.jogador import Jogador
from ...domain.entities.tabuleiro import Tabuleiro
from .fabrica_de_jogadores import FabricaDeJogadores


class Jogo:

    
    MAX_RODADAS = 1000
    
    def __init__(self, tabuleiro: Tabuleiro, jogadores: List[Jogador]):
        self.tabuleiro = tabuleiro
        self.jogadores = jogadores
        self.rodada_atual = 0


    
    def obter_jogadores_ativos(self) -> List[Jogador]:
      
        return [j for j in self.jogadores if j.esta_ativo()]
    
    
    def tem_apenas_um_jogador_ativo(self) -> bool:
       
        return len(self.obter_jogadores_ativos()) == 1
    
    
    def atingiu_max_rodadas(self) -> bool:
       
        return self.rodada_atual >= self.MAX_RODADAS


    
    def terminou(self) -> bool:
       
        return (
            self.tem_apenas_um_jogador_ativo() or
            self.atingiu_max_rodadas()
        )


class FabricaDeJogo:
 
    
    def __init__(self):
        self._fabrica_jogadores = FabricaDeJogadores()
    
    def criar_jogo_padrao(self) -> Jogo:

        tabuleiro = Tabuleiro()
        jogadores = self._fabrica_jogadores.criar_jogadores_padrao()
        
        return Jogo(tabuleiro, jogadores)

