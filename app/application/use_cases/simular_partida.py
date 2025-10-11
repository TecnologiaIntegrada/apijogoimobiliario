## Orquestra o fluxo

from ..dtos.resultado_partida import ResultadoPartida
from ..factories.fabrica_de_jogo import FabricaDeJogo
from ...domain.services.motor_do_jogo import MotorDoJogo
from ...domain.services.calculador_de_ranking import CalculadorDeRanking


class SimularPartidaUseCase:
    
    #simular uma partida completa do jogo.

    
    def __init__(self):
        self._fabrica_jogo = FabricaDeJogo()
        self._motor = MotorDoJogo()
        self._calculador_ranking = CalculadorDeRanking()
    
    def executar(self) -> ResultadoPartida:
   
        # Cria jogo
        jogo = self._fabrica_jogo.criar_jogo_padrao()
        
        # Executar rodada
        while not jogo.terminou():
            jogo.rodada_atual += 1
            self._executar_rodada(jogo)
        
        # Calcula ranking
        ranking = self._calculador_ranking.calcular_ranking_final(jogo.jogadores)
        vencedor = ranking[0]
        
        # Retorna op resultado
        return ResultadoPartida(
            vencedor=vencedor.tipo,
            jogadores=[j.tipo for j in ranking]
        )
    
    def _executar_rodada(self, jogo) -> None:
        ##Rodada completa sendo executada....
        for jogador in jogo.obter_jogadores_ativos():
            self._motor.processar_turno(jogador, jogo.tabuleiro)

