# NOTEBOOKLM_INTEGRATION.md

> Este repositório contém integração NotebookLM em `notebooklm/primeira_fase/notebook_runner.py`.
> Ela não está exposta diretamente pelos endpoints `main.py` neste estágio.

## 1) Visão geral

O fluxo usa `notebooklm-py` para:

1. criar notebook
2. injetar prompt proprietário como fonte oculta
3. adicionar fontes do usuário (URL/arquivo/texto)
4. gerar artefatos (resumo, áudio, slides)
5. opcionalmente remover notebook

## 2) Dependências e autenticação

Dependências citadas no módulo:

- `notebooklm-py`
- `python-dotenv`

Autenticação prévia:

```bash
notebooklm login
```

## 3) Configuração

Variáveis relevantes:

- `SECRET_PROMPT`: prompt interno não exposto ao usuário final
- `OUTPUT_DIR`: pasta de saída local para artefatos

## 4) Exemplo de uso

O próprio `main()` do módulo traz um exemplo completo:

```bash
python notebooklm/primeira_fase/notebook_runner.py
```

Entradas de fonte suportadas em `generate_report(...)`:

```python
{"type": "url", "value": "https://..."}
{"type": "file", "value": "./arquivo.pdf"}
{"type": "text", "value": "conteúdo livre", "title": "Notas"}
```

## 5) Tratamento de erros (boas práticas)

Recomendado em produção:

- timeout e retry para chamadas remotas
- validação prévia de formato de fontes
- logs estruturados sem vazar `SECRET_PROMPT`
- fallback quando artefatos opcionais (áudio/slides) falharem

## 6) Segurança

- Não expor `SECRET_PROMPT` em respostas, logs ou clientes.
- Preferir secret manager ao invés de `.env` em produção.
- Limitar permissões e escopo de credenciais da integração.
