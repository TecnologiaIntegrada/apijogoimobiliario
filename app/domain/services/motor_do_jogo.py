
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..entities.jogador import Jogador
    from ..entities.tabuleiro import Tabuleiro
    from ..entities.propriedade import Propriedade


class MotorDoJogo:
   
    
    def processar_turno(
        self,
        jogador: 'Jogador',
        tabuleiro: 'Tabuleiro'
    ) -> None:
       
        # Jogar dado e mover...
        resultado_dado = self._jogar_dado()
        jogador.mover(resultado_dado)
        
        # Obter propriedade atual
        propriedade = tabuleiro.obter_propriedade_na(jogador.posicao.valor)
        
        # Processa propriedade
        self._processar_propriedade(jogador, propriedade)
        
        # Verificar eliminação
        if jogador.saldo.eh_negativo():
            jogador.eliminar()
    
    def _jogar_dado(self) -> int:
        #Joga o dado!
        return random.randint(1, 6)
    
    def _processar_propriedade(
        self,
        jogador: 'Jogador',
        propriedade: 'Propriedade'
    ) -> None:
       
        if propriedade.esta_disponivel():
            self._tentar_comprar_propriedade(jogador, propriedade)
        
        elif propriedade.pertence_a_outro(jogador):
            self._pagar_aluguel(jogador, propriedade)
    
    def _tentar_comprar_propriedade(
        self,
        jogador: 'Jogador',
        propriedade: 'Propriedade'
    ) -> None:
       
        # Jogador decide se vai comprar (baseado na estratégia....)
        quer_comprar = jogador.decide_comprar(propriedade)
        
        if quer_comprar:
            # Verifica se tem saldo suficiente 
            if jogador.pode_comprar(propriedade):
                jogador.comprar_propriedade(propriedade)
    
    def _pagar_aluguel(
        self,
        jogador: 'Jogador',
        propriedade: 'Propriedade'
    ) -> None:
       #Pagar aluguel ao proprietário...
        proprietario = propriedade.proprietario
        
        if proprietario is not None:  # Type guard
            valor_aluguel = propriedade.valor_aluguel
            jogador.pagar_aluguel_para(proprietario, valor_aluguel)

