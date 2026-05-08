from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="brain_mock")


class ChatRequest(BaseModel):
    """Payload de entrada para o endpoint de chat mock."""

    message: str = Field(..., description="Mensagem enviada pelo cliente.")


@app.get("/health")
def health() -> dict[str, str]:
    """Retorna o status de saúde do serviço para monitoramento."""
    return {"status": "ok", "service": "brain_mock"}


@app.post("/chat")
def chat(req: ChatRequest) -> dict[str, str]:
    """Retorna resposta mockada baseada na mensagem recebida."""
    return {"response": f"[MOCK] {req.message}"}
