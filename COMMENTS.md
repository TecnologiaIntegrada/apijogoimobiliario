# API do Simulador de Jogo Imobiliário

API REST Simulador de Banco Imobiliário

## Informações importantes
---------------------------------------------------------------------------------------------

# Ativar ambiente virtual
cd /system
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar API
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload


## Endpoint Principal

# Simular uma partida
curl -X POST http://localhost:8080/jogo/simular

# Resposta esperada solicitada pelo contratante
{
  "vencedor": "cauteloso",
  "jogadores": ["cauteloso", "aleatorio", "exigente", "impulsivo"]
}


## Tipos de Jogadores

|---------------|----------------------------------  |
| Tipo          | Estratégia                         |
|---------------|----------------------------------  |
| **Impulsivo** | Compra qualquer propriedade        |
| **Exigente**  | Só compra se aluguel > 50          |
| **Cauteloso** | Só compra se sobrar >= 80 de saldo |
| **Aleatório** | 50% de chance de comprar           |
|---------------|----------------------------------  |


## Tecnologias utilizadas
## -------------------------------------------------
- Python 3.10.12
- FastAPI 0.104.1
- Uvicorn 0.24.0
- Pydantic 2.5.0
- Pytest 7.4.3

## Documentação da API On LIne
## -------------------------------------------------
- Swagger UI: http://localhost:8080/docs
- ReDoc: http://localhost:8080/redoc

## Testes Unitários
## -------------------------------------------------
```bash
pytest tests/ -v --cov=app
```

# Apenas testes de value objects
pytest tests/test_value_objects.py -v

# Apenas testes de strategies
pytest tests/test_strategies.py -v

# Apenas testes de jogador
pytest tests/test_jogador.py -v

# Apenas testes de simulação
pytest tests/test_api.py -v

## Propriedade
Este projeto foi desenvolvido para a 7Comm.com.br