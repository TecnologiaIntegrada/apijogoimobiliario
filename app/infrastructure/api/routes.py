
from fastapi import APIRouter, HTTPException
from .schemas import ResultadoPartidaSchema
from ...application.use_cases.simular_partida import SimularPartidaUseCase

# Criar router....
router = APIRouter()


@router.get(
    "/jogo/simular",
    response_model=ResultadoPartidaSchema,
    summary="Simular partida (GET)",
    description="Simula uma partida completa do jogo e retorna o vencedor e ranking",
    tags=["Jogo"]
)
@router.post(
    "/jogo/simular",
    response_model=ResultadoPartidaSchema,
    summary="Simular partida (POST)",
    description="Simula uma partida completa do jogo e retorna o vencedor e ranking",
    tags=["Jogo"]
)
async def simular_partida():
   
    try:
        # Executar use case
        use_case = SimularPartidaUseCase()
        resultado = use_case.executar()
        
        # Retornar resultado
        return resultado.to_dict()
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao simular partida: {str(e)}"
        )


@router.get(
    "/",
    summary="Informações da API",
    description="Retorna informações sobre a API",
    tags=["Geral"]
)
async def root():
   
    return {
        "nome": "API Simulador de Jogo Imobiliário",
        "versao": "1.0.0",
        "descricao": "API que simula partidas de jogo similar ao Banco Imobiliário",
        "endpoints": {
            "GET/POST /jogo/simular": "Simula uma partida e retorna o resultado",
            "GET /docs": "Documentação interativa (Swagger)",
            "GET /redoc": "Documentação alternativa (ReDoc)"
        },
        "tecnologias": ["Python 3.10", "FastAPI", "DDD", "SOLID", "Clean Code"]
    }


@router.get(
    "/health",
    summary="Health Check",
    description="Verifica se a API está funcionando",
    tags=["Geral"]
)
async def health_check():

    return {"status": "healthy", "message": "API está funcionando corretamente !!!!"}

