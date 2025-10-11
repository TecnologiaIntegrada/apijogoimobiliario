
from dataclasses import dataclass


@dataclass(frozen=True)
class ResultadoDado:

    valor: int
    
    def __post_init__(self):
         #Valida se o valor está entre 1 e 6
        if self.valor < 1 or self.valor > 6:
            raise ValueError(
                f"Resultado de dado inválido: {self.valor}. "
                f"Deve estar entre 1 e 6"
            )
    
    def __str__(self) -> str:
        return f"Dado: {self.valor}"

