
import pytest
from app.domain.value_objects.saldo import Saldo
from app.domain.value_objects.posicao import Posicao


class TestSaldo:
    
    
    def test_criar_saldo(self):
        saldo = Saldo(100)
        assert saldo.valor == 100
    
    def test_adicionar_valor(self):
        saldo = Saldo(100)
        novo_saldo = saldo.adicionar(50)
        
        assert saldo.valor == 100  # Imutável
        assert novo_saldo.valor == 150
    
    def test_subtrair_valor(self):
        saldo = Saldo(100)
        novo_saldo = saldo.subtrair(30)
        
        assert saldo.valor == 100  # Imutável
        assert novo_saldo.valor == 70
    
    def test_eh_suficiente_para(self):
        saldo = Saldo(100)
        
        assert saldo.eh_suficiente_para(50) is True
        assert saldo.eh_suficiente_para(100) is True
        assert saldo.eh_suficiente_para(150) is False
    
    def test_eh_negativo(self):
        saldo_positivo = Saldo(100)
        saldo_negativo = Saldo(-50)
        
        assert saldo_positivo.eh_negativo() is False
        assert saldo_negativo.eh_negativo() is True


class TestPosicao:

    
    def test_criar_posicao(self):
        posicao = Posicao(5)
        assert posicao.valor == 5
    
    def test_avancar_sem_completar_volta(self):
        posicao = Posicao(5)
        nova_posicao, completou_volta = posicao.avancar(3)
        
        assert posicao.valor == 5  # Imutável
        assert nova_posicao.valor == 8
        assert completou_volta is False
    
    def test_avancar_completando_volta(self):
        posicao = Posicao(18)
        nova_posicao, completou_volta = posicao.avancar(5)
        
        assert nova_posicao.valor == 3  # (18 + 5) % 20 = 3
        assert completou_volta is True
    
    def test_avancar_exatamente_uma_volta(self):
        posicao = Posicao(0)
        nova_posicao, completou_volta = posicao.avancar(20)
        
        assert nova_posicao.valor == 0
        assert completou_volta is False  # Mesma posição

