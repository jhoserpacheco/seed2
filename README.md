### Clone repository use
``git clone https://github.com/jhoserpacheco/seed2.git``

#### Change directory and Activate Environment
``cd seed2``<br>
``. env/bin/activate``

#### Install requeriments.txt and make migrations 
``pip install -r requeriments.txt``<br>
``python manage.py makemigrations``<br>
``python manage.py migrate``<br>

#### Run server 
``python manage.py runserver``