create:
	sudo docker-compose up --build -d

destroy:
	sudo docker-compose down



redeploy:
	make destroy
	sudo git pull
	make create
