"""
API Jogo Imobiliário
Copyright (C) 2025 Canada Software (https://canada-software.com)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .infrastructure.api.routes import router

# Criar aplicação FastAPI
app = FastAPI(
    title="API Simulador de Jogo Imobiliário",
    description="""
    API que simula partidas de um jogo similar ao Banco Imobiliário.
    
    **Desenvolvido por [Canada Software](https://canada-software.com)**
    
    Licenciado sob GNU General Public License v3.0
    Este software é livre: você pode redistribuí-lo e/ou modificá-lo
    sob os termos da GNU GPL v3. Veja <https://www.gnu.org/licenses/>
    
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
    
    ### Resposta esperada:
    
    ```json
    {
      "vencedor": "cauteloso",
      "jogadores": ["cauteloso", "aleatorio", "exigente", "impulsivo"]
    }
    ```
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas
app.include_router(router)


@app.get("/")
def read_root():
    return {
        "message": "API Jogo Imobiliário",
        "docs": "/docs",
        "version": "1.0.0",
        "license": "GNU GPL v3.0",
        "developer": "Canada Software (https://canada-software.com)"
    }
