
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .infrastructure.api.routes import router

# Criar aplicação FastAPI
app = FastAPI(
    title="API Simulador de Jogo Imobiliário",
    description="""
    API que simula partidas de um jogo similar ao Banco Imobiliário.
    Solução modelo criada por https://canada-software.com
    
    ## Características
    
    - São 4 tipos de jogadores com estratégias diferentes...
    - Tabuleiro com 20 propriedades (casas,hoteis,etc)
    - Simulação completa automática
    
    ## Como utilizar
    
    Faça uma requisição para `/jogo/simular` (GET ou POST) e receba o resultado da partida.
    
    ### Exemplo usando curl:
    
    ```bash
    curl -X POST http://localhost:8080/jogo/simular
    ```
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS **atenção
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True
    )

