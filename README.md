# API de Produtos - SENAI

API REST introdutória construída com **FastAPI**. O projeto demonstra operações CRUD (criar, consultar, atualizar e remover produtos) usando endpoints HTTP e dados mantidos em memória.
![](https://github.com/GustavoPinheiro4/constru-o-API/blob/main/img/Captura%20de%20tela_22-10-2026_163933_urban-palm-tree-g4w79gvq97j53wpgg-8000.app.github.dev.jpeg)
## Tecnologias

- Python
- FastAPI
- Uvicorn, como servidor ASGI para desenvolvimento

## Requisitos

- Python 3.10 ou superior
- `pip`

## Instalação e execução

No terminal, na pasta do projeto, crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows, a ativação pode ser feita com:

```powershell
.venv\Scripts\Activate.ps1
```

Instale as dependências e inicie o servidor:

```bash
python -m pip install fastapi "uvicorn[standard]"
uvicorn app:app --reload
```

Por padrão, a API ficará disponível em `http://127.0.0.1:8000`. A opção `--reload` reinicia o servidor quando alterações são detectadas e é indicada para desenvolvimento local.

## Documentação interativa

Com o servidor em execução, acesse:

- Swagger UI: `http://127.0.0.1:8000/docs`
- Referência alternativa: `http://127.0.0.1:8000/redoc`

## Endpoints

| Método | Rota | Descrição | Resposta de sucesso |
|---|---|---|---|
| `GET` | `/` | Retorna uma mensagem de boas-vindas. | `200 OK` |
| `GET` | `/produtos` | Lista todos os produtos. | `200 OK` |
| `GET` | `/produtos/{produto_id}` | Consulta um produto pelo identificador. | `200 OK` |
| `POST` | `/produtos` | Cadastra um produto e gera seu identificador. | `201 Created` |
| `PUT` | `/produtos/{produto_id}` | Atualiza o nome de um produto existente. | `200 OK` |
| `DELETE` | `/produtos/{produto_id}` | Remove um produto existente. | `204 No Content` |

### Exemplos

Mensagem de boas-vindas:

```bash
curl http://127.0.0.1:8000/
```

Resposta:

```json
{"mensagem":"bem-vindo a api do SENAI"}
```

Listar produtos (`GET`):

```bash
curl http://127.0.0.1:8000/produtos
```

Consultar um produto (`GET`):

```bash
curl http://127.0.0.1:8000/produtos/4
```

Cadastrar um produto (`POST`):

```bash
curl -X POST http://127.0.0.1:8000/produtos \
	-H "Content-Type: application/json" \
	-d '{"nome":"Laranja"}'
```

Resposta (`201 Created`):

```json
{"id":6,"nome":"Laranja"}
```

Atualizar um produto (`PUT`):

```bash
curl -X PUT http://127.0.0.1:8000/produtos/6 \
	-H "Content-Type: application/json" \
	-d '{"nome":"Laranja pera"}'
```

Resposta (`200 OK`):

```json
{"id":6,"nome":"Laranja pera"}
```

Remover um produto (`DELETE`):

```bash
curl -i -X DELETE http://127.0.0.1:8000/produtos/6
```

Resposta: `204 No Content`, sem corpo.

## Validação e armazenamento

- O campo `nome` é obrigatório e deve conter entre 1 e 100 caracteres. Dados inválidos são rejeitados pelo FastAPI com `422 Unprocessable Entity`.
- Consultas, atualizações ou remoções com um identificador inexistente retornam `404 Not Found`.
- Os dados ficam em memória e voltam à lista inicial quando a aplicação é reiniciada. Este exemplo não utiliza banco de dados.

## Estrutura do projeto

```text
.
├── app.py      # Aplicação FastAPI e endpoints
└── README.md   # Documentação do projeto
```
