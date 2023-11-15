# sample-docker-deployment
######  Данные для входа уточняйте лично.

### Workflow
```
.github/workflows/workflow.yml
```
В этом файле находится наш воркфлоу. Логика простая, сначала запускается tests job, если тесты выполнены успешно, то переходим к deploy. Deploy работает только при пуше в ветку master.

### Docker Registry
Тут используется приватный докер регистр.
```agsl
https://docker.dmitriy.space/v2
```

### HashiCorp Vault
В контексте лабы со звездочкой, используется менеджер секретов HashiCorp Vault. Для хранения секретов своего приложения нужно создать новый secret в kv sercret engine. На сервере поднят Vault сервер, метод авторизации userpass. 
```agsl
https://vault.dmitriy.space/
```

[Библиотеки для работы с HashiCorp Vault](https://developer.hashicorp.com/vault/api-docs/libraries)

[Статья про HashiCorp Vault](https://habr.com/ru/articles/536694/)

### Первичный запуск Docker контейнера 
После первого деплоя нужно вручную запустить контейнер на сервере. Скрипт для запуска стоит положить в 
```agsl
/home/dmitriy/docker-autoupdate/containers/
```
После первого запуска, на сервере каждые 30 секунд будет проверятся наличие новой версии в Docker registry. После деплоя контейнер перезапускается в течении минуты. 

### Работа без HashiCorp Vault
В целом, все это может функционировать и без HashiCorp Vault если секретов не так много. Тогда весь код deploy job будет выглядеть примерно так:
```yaml
      - name: Checkout
        uses: actions/checkout@v2

      - name: Docker Login
        run: echo ${{ secrets.DOCKER_PASSWOD }} | docker login https://docker.dmitriy.space/ --username${{ secrets.DOCKER_USERNAME }} --password-stdin

      - name: Docker build image
        run: docker build -t docker.dmitriy.space/sample-docker-deployment:latest .

      - name: Docker push
        run: docker push docker.dmitriy.space/sample-docker-deployment:latest
```
Все это можно упростить благодаря GitHub Actions Marketplace, там есть готовые решения для Docker.

### GitHub Secrets
Для авторизации в HashiCorp/Docker Registry нужно добавить данные для входа в GitHub Secrets. 
```Settings > Secrets and variables > Actions ```
Доступ к секретам выглядит так: 
```agsl
${{ secrets.SECRET_NAME }}
```