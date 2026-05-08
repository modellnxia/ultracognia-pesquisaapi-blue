# API_DOCUMENTATION.md

## Base URL

- Local: `http://localhost:8004`

## Formato

- `Content-Type: application/json`
- Respostas em JSON

## Modelos de dados (Pydantic)

### `ChatRequest`

```json
{
  "message": "string"
}
```

- `message` (string, obrigatório): texto enviado para o mock de chat.

## Endpoints

### 1) Health Check

- **Método**: `GET`
- **Rota**: `/health`
- **Objetivo**: verificar disponibilidade do serviço

#### Exemplo

```bash
curl http://localhost:8004/health
```

#### 200 OK

```json
{
  "status": "ok",
  "service": "brain_mock"
}
```

---

### 2) Chat

- **Método**: `POST`
- **Rota**: `/chat`
- **Objetivo**: retornar resposta mockada com base no texto recebido

#### Request

```bash
curl -X POST http://localhost:8004/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Teste de chat"}'
```

#### 200 OK

```json
{
  "response": "[MOCK] Teste de chat"
}
```

#### 422 Unprocessable Entity (payload inválido)

Exemplo de erro quando `message` não é enviado:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "message"],
      "msg": "Field required",
      "input": {}
    }
  ]
}
```

## Códigos HTTP

- `200`: requisição processada com sucesso
- `422`: erro de validação de payload
- `500`: erro interno não tratado

## Rate limiting

- Não implementado na API neste estágio.
- Recomendado aplicar no gateway/API management (Nginx, Kong, API Gateway, etc.).

## OpenAPI/Swagger

Com a aplicação em execução:

- Swagger UI: `http://localhost:8004/docs`
- ReDoc: `http://localhost:8004/redoc`
- OpenAPI JSON: `http://localhost:8004/openapi.json`
