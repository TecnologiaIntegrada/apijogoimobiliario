from pydantic import BaseModel, Field
from typing import List


class ResultadoPartidaSchema(BaseModel):

    vencedor: str = Field(
        ...,
        description="Tipo do jogador vencedor (impulsivo, exigente, cauteloso, aleatorio)",
        example="cauteloso"
    )
    jogadores: List[str] = Field(
        ...,
        description="Lista de jogadores ordenados por ranking (melhor para pior)",
        example=["cauteloso", "aleatorio", "exigente", "impulsivo"]
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "vencedor": "cauteloso",
                "jogadores": ["cauteloso", "aleatorio", "exigente", "impulsivo"]
            }
        }

