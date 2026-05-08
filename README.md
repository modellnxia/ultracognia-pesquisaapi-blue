# ultracognia-pesquisaapi-blue

API FastAPI da trilha **blue (produção/especializada)** para pesquisa, com endpoints de health/chat e base para integração com NotebookLM.

## Visão geral

- Serviço HTTP em FastAPI (`main.py`)
- Endpoints:
  - `GET /health`
  - `POST /chat`
- Porta padrão: `8004`
- Container pronto via `Dockerfile`

## Blue vs Green (resumo)

- **Blue**: foco em produção, estabilidade operacional e padronização de deploy.
- **Green**: normalmente usado como trilha de template/evolução inicial.
- Neste repositório, o foco é manter a API mínima, previsível e fácil de operar em ambiente produtivo.

## Setup rápido (produção)

### 1) Pré-requisitos

- Python 3.12+
- `pip`
- Docker (opcional, recomendado para produção)

### 2) Instalação local

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8004
```

### 3) Verificação

```bash
curl http://localhost:8004/health
```

Resposta esperada:

```json
{"status":"ok","service":"brain_mock"}
```

## Uso da API

### Chat mock

```bash
curl -X POST http://localhost:8004/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Olá API"}'
```

Resposta:

```json
{"response":"[MOCK] Olá API"}
```

Para detalhes completos de contratos e erros: veja `API_DOCUMENTATION.md`.

## Configuração de ambiente

Atualmente `main.py` não exige variáveis de ambiente para executar.

Para componentes de integração NotebookLM existentes em `notebooklm/primeira_fase/notebook_runner.py`, use:

- `SECRET_PROMPT` (prompt proprietário oculto)
- `OUTPUT_DIR` (diretório de artefatos)

Detalhes: `NOTEBOOKLM_INTEGRATION.md`.

## Docker e deployment

### Build

```bash
docker build -t ultracognia-pesquisaapi-blue:latest .
```

### Run

```bash
docker run --rm -p 8004:8004 ultracognia-pesquisaapi-blue:latest
```

Verificação:

```bash
curl http://localhost:8004/health
```

Guia de produção completo: `DEPLOYMENT.md`.

## Monitoramento e health checks

- **Liveness/Readiness**: `GET /health`
- Métrica mínima recomendada:
  - disponibilidade do endpoint `/health`
  - latência p95/p99 do `/chat`
  - taxa de erro 5xx

## Troubleshooting (produção)

### Porta já em uso

- Ajuste a porta no runtime (`--port`) e no mapeamento Docker.

### Container sobe, mas health falha

- Validar bind em `0.0.0.0`
- Conferir publicação de porta (`-p 8004:8004`)
- Validar network policy/firewall do ambiente

### Dependências não instalam no build

- Conferir acesso à internet/registry
- Reexecutar build sem cache para diagnóstico:

```bash
docker build --no-cache -t ultracognia-pesquisaapi-blue:latest .
```

## Documentação complementar

- `ARCHITECTURE.md`
- `API_DOCUMENTATION.md`
- `DEPLOYMENT.md`
- `NOTEBOOKLM_INTEGRATION.md`
- `CONTRIBUTING.md`
