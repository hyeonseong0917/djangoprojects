# djangoprojects
```
$ django-admin startproject firstProject
```
- __init__.py 파일: 이 폴더가 Python Package임을 알려줌
- settings.py 파일: APP 안쪽과 middleware의 Configuration 구성
-  urls.py 파일: url에 대한 패턴
-  wsgi.py 파일: 웹 서버 게이트웨이 파일, 온라인 혹은 클라우드에 파일 배포시 필요
-  manage.py 파일: 가장 중요, Project를 실행할 때 , database migration을 실행할 때, 사용
```
$ python manage.py runserver
```
## 새 APP 만들기
firstapp 이라는 APP 생성
```
$ python manage.py startapp firstapp
```
=> Python Project 안쪽의 첫 번째 Python Application
- admin.py 파일: Application 안쪽에서 module을 register하고, Django가 Django admin interface를 이용해 사용
- apps.py 파일: 모든 application에 대해 특정한 configuration을 저장
- models.py 파일: data model을 저장할 수 있는 곳
- tests.py 파일: 특정 application에 대한 테스트를 해볼 수 있음
- views.py 파일: User의 Requests를 처리하는 모든 class와 function을 관리하고 특정 View를 browser에 display한다. html파일로 구성하며 python은 UI를 렌더링한다.
- migrations 폴더: 특정 정보에 대한 우리의 모델과 관련 있는 database를 저장.

