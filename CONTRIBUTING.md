# CONTRIBUTING.md

## Objetivo

Este repositório prioriza mudanças pequenas, seguras e orientadas à operação em produção.

## Fluxo local

1. Instale dependências:

```bash
pip install -r requirements.txt
```

2. Execute a API:

```bash
uvicorn main:app --host 0.0.0.0 --port 8004
```

3. Valide endpoint de saúde:

```bash
curl http://localhost:8004/health
```

## Code style

- Python com tipagem explícita sempre que possível.
- Funções públicas devem ter docstring.
- Evitar alterações fora do escopo do problema.

## Testes e validação

Este repositório não possui suíte de testes automatizada dedicada no estado atual.

Validação mínima esperada antes de PR:

- compilação de sintaxe (`python -m compileall .`)
- smoke test manual de `/health` e `/chat`

## Pull Request process

- Título claro e objetivo.
- Descrição contendo:
  - problema
  - mudança aplicada
  - forma de validação
- Preferir PRs pequenos e facilmente revisáveis.

## Segurança

- Nunca commitar segredos.
- Não logar conteúdo sensível (ex.: prompts proprietários).
- Em integrações externas, usar secrets manager em produção.
