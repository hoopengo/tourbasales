restart:
	docker compose up -d --build && docker logs server-app-1 --follow
stop:
	docker compose down -v
relogs:
	docker logs server-app-1 --follow