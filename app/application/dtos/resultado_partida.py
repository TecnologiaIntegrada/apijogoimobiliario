
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class ResultadoPartida:
 
    vencedor: str

    
    jogadores: List[str]
    
    def to_dict(self) -> dict:

        return {
            "vencedor": self.vencedor,
            "jogadores": self.jogadores
        }

