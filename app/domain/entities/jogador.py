from typing import List
from ..value_objects.saldo import Saldo
from ..value_objects.posicao import Posicao

from ..strategies.estrategia_compra import EstrategiaDeCompra
from .propriedade import Propriedade


class Jogador:
   
    
    SALDO_INICIAL = 300
    BONUS_VOLTA_COMPLETA = 100
    
    def __init__(
        self,
        nome: str,
        estrategia: EstrategiaDeCompra,
        ordem_turno: int = 0
    ):
        
        self._nome = nome
        self._estrategia = estrategia
        self._ordem_turno = ordem_turno
        self._saldo = Saldo(self.SALDO_INICIAL)
        self._posicao = Posicao(0)
        self._propriedades: List[Propriedade] = []
        self._ativo = True
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def tipo(self) -> str:
       #Retorna o jogador com base na estrategia
        return self._estrategia.tipo()
    
    @property
    def saldo(self) -> Saldo:
        return self._saldo
    
    @property
    def posicao(self) -> Posicao:
        return self._posicao
    
    @property
    def ordem_turno(self) -> int:
        return self._ordem_turno
    
    @property
    def propriedades(self) -> List[Propriedade]:
        return self._propriedades.copy()
    
    def esta_ativo(self) -> bool:
        #JOgador ainda esta no jogo ?
        return self._ativo
    
    def mover(self, casas: int) -> int:
        #Moveo peão!!!!
        nova_posicao, completou_volta = self._posicao.avancar(casas)
        self._posicao = nova_posicao
        
        if completou_volta:
            self._receber_bonus_volta()
            return self.BONUS_VOLTA_COMPLETA
        
        return 0
    
    def _receber_bonus_volta(self) -> None:
       #Adiciona bonus de 100
        self._saldo = self._saldo.adicionar(self.BONUS_VOLTA_COMPLETA)
    
    def decide_comprar(self, propriedade: Propriedade) -> bool:
        #Vai comprar ????
        return self._estrategia.deve_comprar(propriedade, self._saldo)
    
    def pode_comprar(self, propriedade: Propriedade) -> bool:
        #TEm dinheiro ???
        return self._saldo.eh_suficiente_para(propriedade.custo_venda)
    
    def comprar_propriedade(self, propriedade: Propriedade) -> None:
        #COMpra uma prop
        if not propriedade.esta_disponivel():
            raise ValueError(f"Propriedade {propriedade.nome} não está disponível")
        
        if not self.pode_comprar(propriedade):
            raise ValueError(
                f"Saldo insuficiente para comprar {propriedade.nome}. "
                f"Custo: {propriedade.custo_venda}, Saldo: {self._saldo.valor}"
            )
        
        # Deduz o custo
        self._saldo = self._saldo.subtrair(propriedade.custo_venda)
        
        # Adiciona propriedade
        self._propriedades.append(propriedade)
        propriedade.definir_proprietario(self)
    
    def receber_pagamento(self, valor: int) -> None:
        #Receber pagamento
        self._saldo = self._saldo.adicionar(valor)
    
    def pagar(self, valor: int) -> None:
       #Pagar um aluguel
        self._saldo = self._saldo.subtrair(valor)
    
    def pagar_aluguel_para(
        self,
        proprietario: 'Jogador',
        valor_aluguel: int
    ) -> None:
        #Paga aluguel para outro jogador
        self.pagar(valor_aluguel)
        proprietario.receber_pagamento(valor_aluguel)
    
    def eliminar(self) -> None:
        #Saldo negativo ? elimina o jogador
        self._ativo = False
        
        # Liberar todas as propriedades
        for propriedade in self._propriedades:
            propriedade.liberar()
        
        self._propriedades.clear()
    
    def __str__(self) -> str:
        status = "Ativo" if self._ativo else "Eliminado"
        return (
            f"{self._nome} ({self.tipo}) - "
            f"Saldo: {self._saldo.valor}, "
            f"Posição: {self._posicao.valor}, "
            f"Propriedades: {len(self._propriedades)}, "
            f"Status: {status}"
        )
    
    def __repr__(self) -> str:
        return f"Jogador({self._nome}, {self.tipo})"

