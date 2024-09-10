# Invoices-Manager
## Description
This web application addresses a limitation in the [Fatture in Cloud](https://www.fattureincloud.it/) platform by allowing users to associate multiple categories, contracts, and cost centers with each invoice. It provides an efficient and flexible way to manage and organize invoices with just a few clicks.

## Installation
- Clone the repository:
```bash
git clone https://github.com/Dear-Luca/Invoice-Manager.git
cd Invoice-Manager
```
### Install dependencies
```bash
pip3 install -r requirements.txt
```


### Database & Docker Setup
This project uses **MariaDB** as the database, which runs inside a **Docker container**.
- Create the docker-compose.yaml file:
```yaml
services:
  mariadb:
    image: mariadb
    restart: always
    environment:
      MARIADB_ROOT_PASSWORD: "pswd"
    volumes:
      - YOUR_PATH:/var/lib/mysql
    ports:
      - 3306:3306
```

- Start the database container with Docker Compose:
```bash
docker-compose up -d
```

### Django Setup
- Make sure your settings.py file is configured to connect to the MariaDB container. Example:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Run database migrations:
```bash
python3 manage.py migrate
```
Populate the database:
```bash
python3 manage.py pupulate_db
```

### Run django server
```bash
python3 manage.py runserver
```


