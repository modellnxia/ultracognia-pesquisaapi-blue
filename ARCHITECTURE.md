# ARCHITECTURE.md

## 1. Visão de Arquitetura

O serviço é uma API FastAPI enxuta, com dois endpoints públicos e pronta para execução containerizada.

```text
[Client/Consumer]
       |
       v
[FastAPI app: main.py]
   |            |
   |            +--> POST /chat  -> resposta mock "[MOCK] ..."
   |
   +--> GET /health -> status operacional
```

Componente adicional no repositório:

```text
[notebooklm/primeira_fase/notebook_runner.py]
   -> integração assíncrona com notebooklm-py
   -> injeção de prompt oculto
   -> geração de artefatos (relatório/áudio/slides)
```

## 2. Fluxo de requisições

### `/health`
1. Cliente envia `GET /health`
2. API responde imediatamente com payload estático de saúde.

### `/chat`
1. Cliente envia `POST /chat` com JSON `{ "message": "..." }`
2. FastAPI valida payload via Pydantic (`ChatRequest`)
3. API retorna `{ "response": "[MOCK] <message>" }`

## 3. Padrões arquiteturais

- **API-first mínima**: endpoints pequenos, previsíveis e com contratos simples.
- **Stateless**: nenhuma persistência local obrigatória na API principal.
- **Container-first**: Dockerfile pronto para execução em ambiente orquestrado.

## 4. Padrões de resposta

- JSON em todos os endpoints.
- Contratos estáveis e curtos para facilitar consumo.
- Erros de validação de entrada seguem padrão FastAPI/Pydantic (422).

## 5. Segurança

- Não há autenticação nativa implementada neste estágio (deve ser adicionada no gateway/ingress ou futura camada de auth).
- Recomendações de produção:
  - TLS obrigatório no perímetro.
  - Rate limiting no gateway/reverse proxy.
  - Restringir CORS ao domínio necessário.
  - Não expor segredos em variáveis de ambiente sem secret manager.

## 6. Confiabilidade e performance

- Endpoint `/health` para integração com probes de orquestrador.
- Escala horizontal via múltiplas réplicas (app stateless).
- Latência previsível por não depender de I/O externo no caminho principal atual.
