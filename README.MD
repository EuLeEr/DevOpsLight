# Разные варинаты создания "Hello world" под Python:
<ol>
   <li>apache http;</li>
   <li> wsgi ("виски сервер" - потомок CGI - созданы для Python и позволяют отрабатывать множество запросов одновременно.) На настоящий         момент разработано 6 таких серверов: joern, uWSGI, mod_wsgi, Meinheld, CherryPy и Gunicorn; </li>
   <li> для обеспечения масштабируемости - наконец, Nginx - тут добавляется балансировка и прочие его прелести </li> 
</ol>
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

   

4. Запуск под kubernetes:

   ```bash
   minikube start
   # долгая установка и запуск
   kubectl cluster-info - # проверка запуска - информация о кластере
   # выложить исходный образ из yml на dockerhub.com (локально не работает)
   #как пример для данных ссылка из k8s.yml docker push euleer/devops:1.0
   kubectl apply -f k8s.yml
   # информация
   kubectl get pods # отсюда берется ip  
   kubectl get svc # отсюда берется port из ip loadbalancer
   http://ip:port
   
   ```

   
