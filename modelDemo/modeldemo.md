python manage.py shell
from django.db import connection
c=connection.cursor()

setting.py의 DATABASES에서 default 변수에 대해
mysql로 db를 수정, NAME은 생성하려는 db명으로, USER와 PASSWORD도 구성

python manage.py makemigrations => migration을 통해 _pycache_ 밑에 0001_initial.py 생성함
python manage.py sqlmigrate empApp 0001
python manage.py migrate

settings의 templates 변수에서 DIR을 BASE_DIR에 'templates' 추가
superuser 만들기
python manage.py createsuperuser

admin.py에 admi.site.register를 통해 user를 추가할 수 있음.