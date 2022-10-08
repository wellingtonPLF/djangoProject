# After cloning, run the batch file, it will create your venv to start the project

- Enter on the venv that was created to start to use django backend, using this command: 
```bash
.\vevn\Script\activate
```
## Run this app at this directory -> /app, using this command:
```bash
python manage.py runserver
```
- If you wanna use django locally with postgres container, go to django settings uncomment postgresql database and comment sqlite3 database, don't forgetting to use the follow commands: 
    #### ➼ &nbsp;Git Bash CLI:
    ```bash
    sed $'s/\r$//' ./wait-for-it-ux.sh > ./wait-for-it.sh
    ```
    ```bash
    docker-compose up -d
    ```
    ```bash
    python manage.py migrate;
    ```
- If you wanna use django container with postgres container, make sure to do some changes at docker-compose.yml django image version and django settings, as well as, execute those commands below:
  #### ➼ &nbsp;Image: django-image:v2
  #### ➼ &nbsp;Port:5432 and Host: db; 
  ```bash
    docker-compose up -d
  ```
  ```bash
  docker exec <django-container-id> python manage.py migrate;
  ```
## About postgres and pgadmin

- To enter in postgres container:
  ```bash
  docker exec -it db psql
  ```
- Connecting to postgres by pgadmin:
  - Go to localhost:5050
  - Pass a password that you'll remember
  - Add a new server passing the name (can be a random name) 
  - In connection tab use host as db and postgres as password;
  - Apply and be happy.