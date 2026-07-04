.PHONY: up down logs backend frontend

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

backend:
	cd backend && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

frontend:
	cd frontend && npm run dev
