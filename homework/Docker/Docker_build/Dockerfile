	# Устанавливаю базовый образ
	FROM openjdk:18-ea-16-jdk-buster
	
	# Обновляю репозитории
	RUN apt-get update

	# Устанавливаю python 3
	RUN apt-get install -y python3
	
	RUN apt-get install -y python3-pip
	
	COPY allure_2.15.0-1_all.deb .
	RUN dpkg -i allure_2.15.0-1_all.deb
	# Устанавливаю рабочую директорию внутри контейнера
	WORKDIR /app

	# Копирую сначала зависимости
	# Для того, чтобы не пересобирать их каждый раз при сборке
	COPY requirements.txt .	

	# Выполняю необходимые команды

	RUN pip3 install -U pip
	RUN pip3 install -r requirements.txt

	RUN mkdir allure-results logs screenshots
	
	# Копирую остальные файлы проекта
	COPY . .
	
	# Этот параметр можно переопределить при СОЗДАНИИ контейнера, т.е. run
	CMD ["pytest", "--browser", "chrome"]
