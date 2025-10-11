import pytest
from app.domain.strategies.estrategia_impulsiva import EstrategiaImpulsiva
from app.domain.strategies.estrategia_exigente import EstrategiaExigente
from app.domain.strategies.estrategia_cautelosa import EstrategiaCautelosa
from app.domain.strategies.estrategia_aleatoria import EstrategiaAleatoria
from app.domain.entities.propriedade import Propriedade
from app.domain.value_objects.saldo import Saldo


class TestEstrategiaImpulsiva:

    
    def test_sempre_compra(self):
        estrategia = EstrategiaImpulsiva()
        propriedade = Propriedade("Teste", 0, 100, 40)
        saldo = Saldo(200)
        
        assert estrategia.deve_comprar(propriedade, saldo) is True
    
    def test_tipo(self):
        estrategia = EstrategiaImpulsiva()
        assert estrategia.tipo() == "impulsivo"


class TestEstrategiaExigente:
   
    
    def test_compra_aluguel_alto(self):
        estrategia = EstrategiaExigente()
        propriedade_boa = Propriedade("Boa", 0, 100, 60)
        saldo = Saldo(200)
        
        assert estrategia.deve_comprar(propriedade_boa, saldo) is True
    
    def test_nao_compra_aluguel_baixo(self):
        estrategia = EstrategiaExigente()
        propriedade_ruim = Propriedade("Ruim", 0, 100, 40)
        saldo = Saldo(200)
        
        assert estrategia.deve_comprar(propriedade_ruim, saldo) is False
    
    def test_nao_compra_aluguel_exato_50(self):
        estrategia = EstrategiaExigente()
        propriedade = Propriedade("Limite", 0, 100, 50)
        saldo = Saldo(200)
        
        assert estrategia.deve_comprar(propriedade, saldo) is False
    
    def test_tipo(self):
        estrategia = EstrategiaExigente()
        assert estrategia.tipo() == "exigente"


class TestEstrategiaCautelosa:
   
    
    def test_compra_com_reserva_suficiente(self):
        estrategia = EstrategiaCautelosa()
        propriedade = Propriedade("Teste", 0, 100, 40)
        saldo = Saldo(200)  # 200 - 100 = 100 >= 80
        
        assert estrategia.deve_comprar(propriedade, saldo) is True
    
    def test_nao_compra_sem_reserva(self):
        estrategia = EstrategiaCautelosa()
        propriedade = Propriedade("Teste", 0, 100, 40)
        saldo = Saldo(150)  # 150 - 100 = 50 < 80
        
        assert estrategia.deve_comprar(propriedade, saldo) is False
    
    def test_compra_no_limite_reserva(self):
        estrategia = EstrategiaCautelosa()
        propriedade = Propriedade("Teste", 0, 100, 40)
        saldo = Saldo(180)  # 180 - 100 = 80 (exatamente)
        
        assert estrategia.deve_comprar(propriedade, saldo) is True
    
    def test_tipo(self):
        estrategia = EstrategiaCautelosa()
        assert estrategia.tipo() == "cauteloso"

