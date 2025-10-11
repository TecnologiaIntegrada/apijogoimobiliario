
from typing import List
from ..entities.jogador import Jogador


class CalculadorDeRanking:

    
    def calcular_ranking_final(
        self,
        jogadores: List[Jogador]
    ) -> List[Jogador]:

        # Separar ativos e eliminados
        ativos = [j for j in jogadores if j.esta_ativo()]
        eliminados = [j for j in jogadores if not j.esta_ativo()]
        
        # Ordenar por cada grupo
        ativos_ordenados = self._ordenar_por_saldo(ativos)
        eliminados_ordenados = self._ordenar_por_saldo(eliminados)
        
        # Ativos primeiro, depois eliminados
        return ativos_ordenados + eliminados_ordenados
    
    def _ordenar_por_saldo(self, jogadores: List[Jogador]) -> List[Jogador]:
       
        return sorted(
            jogadores,
            key=lambda j: (-j.saldo.valor, j.ordem_turno)
        )
    
    def determinar_vencedor(self, jogadores: List[Jogador]) -> Jogador:
       
        if not jogadores:
            raise ValueError("Não há jogadores para determinar vencedor")
        
        ranking = self.calcular_ranking_final(jogadores)
        return ranking[0]

