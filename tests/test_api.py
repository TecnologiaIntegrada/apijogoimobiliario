
import pytest
from app.application.use_cases.simular_partida import SimularPartidaUseCase


class TestSimulacao:
    
    
    def test_executar_simulacao_completa(self):
   
        use_case = SimularPartidaUseCase()
        resultado = use_case.executar()
        
        # Verificar estrutura
        assert hasattr(resultado, 'vencedor')
        assert hasattr(resultado, 'jogadores')
        
        # Verificar tipos
        assert isinstance(resultado.vencedor, str)
        assert isinstance(resultado.jogadores, list)
        assert len(resultado.jogadores) == 4
        
        # Verificar valores válidos
        tipos_validos = ["impulsivo", "exigente", "cauteloso", "aleatorio"]
        assert resultado.vencedor in tipos_validos
        
        for jogador in resultado.jogadores:
            assert jogador in tipos_validos
        
        # Verificar que o vencedor está no ranking
        assert resultado.vencedor in resultado.jogadores
    
    def test_simulacoes_multiplas(self):
       
        use_case = SimularPartidaUseCase()
        
        for _ in range(5):
            resultado = use_case.executar()
            
            assert resultado.vencedor is not None
            assert len(resultado.jogadores) == 4
    
    def test_resultado_to_dict(self):
    
        use_case = SimularPartidaUseCase()
        resultado = use_case.executar()
        
        resultado_dict = resultado.to_dict()
        
        assert "vencedor" in resultado_dict
        assert "jogadores" in resultado_dict
        assert isinstance(resultado_dict, dict)
