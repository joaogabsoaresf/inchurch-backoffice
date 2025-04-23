# Backend Backoffice Django-Ninja

Este projeto é baseado em Django, utilizando Docker para serviços externos e Makefile para facilitar os comandos comuns.

## Requisitos

Antes de iniciar, certifique-se de ter instalado em sua máquina:

- Python **3.12**
- Docker
- Make

## Instalação do Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/joaogabsoaresf/inchurch-backoffice.git
cd inchurch-backoffice
```

### 2. Criar e ativar o ambiente virtual
```bash
python3.12 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

### 3. Instalar as dependências
```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente
```bash
cp env.local .env
```

### 5. Subir os serviços com Docker
#### Certifique-se de que o Docker está rodando, e então execute:
```bash
make db
```

### 6. Rodar as migrações
```bash
make migrations
make migrate
```

### 7. Iniciar o servidor de desenvolvimento
```bash
make run
```
#### O servidor estará disponível em: http://localhost:8000

#

## Criar um novo app
Para criar um novo app Django dentro do projeto, utilize o comando abaixo:
```bash
make app nome-do-app
```
Após isso, edite o arquivo `apps.py` do novo app, adicionando o prefixo `apps`. ao nome do app na classe `AppConfig`. Exemplo:

```python
class MeuAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.nome_do_app"
```
E então registre o novo app no `INSTALLED_APPS` no arquivo `settings.py`:
```python
INSTALLED_APPS = [
    ...
    "apps.nome_do_app",
]
```

#
### Pronto! Agora você pode começar a desenvolver 🚀
#

#### Links Úteis:
- [Django Ninja](https://django-ninja.dev)
- [Docker](https://docs.docker.com/engine/install/)