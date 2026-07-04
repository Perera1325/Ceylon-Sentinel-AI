.PHONY: up down logs backend frontend test lint format migrate clean

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

backend:
	cd backend && uvicorn app.main:app --reload

frontend:
	cd frontend && npm run dev

test:
	cd backend && pytest
	cd frontend && npm test

lint:
	cd backend && flake8 app
	cd frontend && npm run lint

format:
	cd backend && black app && isort app
	cd frontend && npx prettier --write .

migrate:
	cd backend && alembic upgrade head

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	rm -rf frontend/.next frontend/node_modules backend/.venv
