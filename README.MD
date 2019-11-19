1. Запуск под ansible описан в [readme.md](/ansible/readme.md)

2. Запуск под docker :

   ```bash
   docker build -t eueler/devops:1.0
   docker container run --publish 80:80 --detach euleer/devops:1.0
   # Проверка 
   wget -O- http://0.0.0.0 | less
   ```

3. Запуск под docker-compose:

   ```bash
   # Если не собран image
   docker build -t eueler/devops:1.0
   docker-compose up
   # Проверка 
   wget -O- http://0.0.0.0 | less
   ```

   