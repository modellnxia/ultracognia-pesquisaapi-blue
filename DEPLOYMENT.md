# DEPLOYMENT.md

## 1) Build de imagem Docker

```bash
docker build -t ultracognia-pesquisaapi-blue:latest .
```

## 2) Execução local/produção simples

```bash
docker run -d \
  --name ultracognia-pesquisaapi-blue \
  -p 8004:8004 \
  --restart unless-stopped \
  ultracognia-pesquisaapi-blue:latest
```

## 3) Variáveis de ambiente de produção

Para `main.py`: não há variáveis obrigatórias no estado atual.

Para scripts NotebookLM (`notebooklm/primeira_fase/notebook_runner.py`):

- `SECRET_PROMPT`: prompt interno proprietário (não expor em logs)
- `OUTPUT_DIR`: diretório de saída de artefatos

Use secret manager para valores sensíveis.

## 4) Health checks e readiness probes

Endpoint recomendado para probes:

- `GET /health`

Exemplo Kubernetes:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8004
  initialDelaySeconds: 10
  periodSeconds: 15

readinessProbe:
  httpGet:
    path: /health
    port: 8004
  initialDelaySeconds: 5
  periodSeconds: 10
```

## 5) Logging estruturado

A API atual usa logging padrão do servidor ASGI/Uvicorn.

Recomendação para produção:

- saída em JSON
- campos mínimos: timestamp, level, request_id, method, path, status_code, latency_ms
- mascarar dados sensíveis

## 6) Monitoramento

Métricas mínimas:

- disponibilidade de `/health`
- latência p95/p99 em `/chat`
- taxa de erro 4xx/5xx
- reinícios de container/pod

Alertas recomendados:

- health check indisponível por mais de 2 janelas
- erro 5xx acima de limiar
- aumento anormal de latência

## 7) Scaling horizontal

Como o serviço é stateless, a escala horizontal é direta:

- aumentar réplicas no orquestrador
- manter balanceamento L7
- aplicar limites de CPU/memória por pod/container

## 8) Troubleshooting

### Aplicação não inicia

- validar `pip install -r requirements.txt` no build
- confirmar comando final:
  `uvicorn main:app --host 0.0.0.0 --port 8004`

### Probe falha mesmo com container em execução

- conferir rota `/health`
- validar mapeamento da porta correta
- verificar timeout/initialDelay do orquestrador

### Respostas 422 inesperadas em `/chat`

- validar payload JSON com campo obrigatório `message` (string)
