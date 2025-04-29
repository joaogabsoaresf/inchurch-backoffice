.DEFAULT_GOAL := help
.PHONY: help run migrate migrations db app

help:
	@echo "💡 Comandos disponíveis:"
	@echo "  make run             # Inicia o servidor Django"
	@echo "  make migrate         # Aplica as migrações"
	@echo "  make migrations      # Cria novas migrações"
	@echo "  make db              # Sobe o banco com Docker"
	@echo "  make app <nome>      # Cria uma nova app Django em apps/<nome>"

run:
	@echo "🚀 Iniciando servidor..."
	DJANGO_ENV=local python manage.py runserver

migrate:
	@echo "📦 Aplicando migrações..."
	python manage.py migrate

migrations:
	@echo "📂 Criando migrações..."
	python manage.py makemigrations

db:
	@echo "🐘 Subindo banco de dados..."
	docker-compose up -d

app:
	@if [ -z "$(word 2,$(MAKECMDGOALS))" ]; then \
		echo "⚠️  Por favor, forneça o nome do app: make app nome_do_app"; \
	else \
		name=$(word 2,$(MAKECMDGOALS)); \
		mkdir -p apps/$$name; \
		django-admin startapp $$name apps/$$name; \
		echo "✅ app:$$name criado com sucesso"; \
	fi;

# gambiarra para evitar o erro "No rule to make target" com app nome
%::
	@:
