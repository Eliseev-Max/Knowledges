	# Устанавливаю базовый образ
	FROM openjdk:18-ea-16-jdk-buster
	
	# Обновляю репозитории
	RUN apt-get update

	# Устанавливаю python 3
	RUN apt-get install -y python3
	
	RUN apt install -y python3-pip
	
	# Устанавливаю рабочую директорию внутри контейнера
	WORKDIR /app

	# Копирую сначала зависимости
	# Для того, чтобы не пересобирать их каждый раз при сборке
	COPY requirements.txt .	
	
	COPY allure.deb .
