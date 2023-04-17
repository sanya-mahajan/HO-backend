redeploy:
	make destroy
	sudo git pull
	make create
