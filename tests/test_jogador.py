
import pytest
from app.domain.entities.jogador import Jogador
from app.domain.entities.propriedade import Propriedade
from app.domain.strategies.estrategia_impulsiva import EstrategiaImpulsiva
from app.domain.strategies.estrategia_cautelosa import EstrategiaCautelosa


class TestJogador:
    #TEsta entidade jogador
    
    def test_criar_jogador(self):
        estrategia = EstrategiaImpulsiva()
        jogador = Jogador("Teste", estrategia)
        
        assert jogador.nome == "Teste"
        assert jogador.tipo == "impulsivo"
        assert jogador.saldo.valor == 300
        assert jogador.posicao.valor == 0
        assert jogador.esta_ativo() is True
    
    def test_mover_sem_completar_volta(self):
        estrategia = EstrategiaImpulsiva()
        jogador = Jogador("Teste", estrategia)
        
        bonus = jogador.mover(5)
        
        assert jogador.posicao.valor == 5
        assert bonus == 0
        assert jogador.saldo.valor == 300
    
    def test_mover_completando_volta(self):
        estrategia = EstrategiaImpulsiva()
        jogador = Jogador("Teste", estrategia)
        jogador._posicao = jogador._posicao.avancar(18)[0]  # Posição 18
        
        bonus = jogador.mover(5)  # 18 + 5 = 23 % 20 = 3
        
        assert jogador.posicao.valor == 3
        assert bonus == 100
        assert jogador.saldo.valor == 400
    
    def test_comprar_propriedade(self):
        estrategia = EstrategiaImpulsiva()
        jogador = Jogador("Teste", estrategia)
        propriedade = Propriedade("Avenida", 0, 100, 50)
        
        jogador.comprar_propriedade(propriedade)
        
        assert jogador.saldo.valor == 200
        assert len(jogador.propriedades) == 1
        assert propriedade.proprietario == jogador
    
    def test_pagar_aluguel(self):
        jogador1 = Jogador("J1", EstrategiaImpulsiva())
        jogador2 = Jogador("J2", EstrategiaImpulsiva())
        
        jogador1.pagar_aluguel_para(jogador2, 50)
        
        assert jogador1.saldo.valor == 250
        assert jogador2.saldo.valor == 350
    
    def test_eliminar_jogador(self):
        jogador = Jogador("Teste", EstrategiaImpulsiva())
        propriedade = Propriedade("Av", 0, 50, 20)
        jogador.comprar_propriedade(propriedade)
        
        jogador.eliminar()
        
        assert jogador.esta_ativo() is False
        assert len(jogador.propriedades) == 0
        assert propriedade.proprietario is None

