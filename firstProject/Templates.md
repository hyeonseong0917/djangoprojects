## Templates
1. Create the Project and APP
```
$ django-admin startproject templatesDemo
```
```
$ python manage.py startapp templatesApp
```
2. Setup the templates directory
templatesDemo의 templatesDemo 디렉터리의 settings.py에서
templates의 DIRS를 os.path.join(BASE_DIR,templates)로 BASE_DIR밑의 templates으로
경로를 설정한다.
3. Create a Templates
templatesDemo/templates/templatesApp/firstTemplates.html에 html을 만들고, 이를 views.py에서 렌더링한다.
=> render함수에서 request를 take하고, templates디렉토리의 html을 가져오기 때문에 http Response가 필요하지 않음.
4. Create a View and map it to a URL
프로젝트의 urls.py에서 urlPatterns에 path()함수를 이용해 웹 경로와 콤마로 구분해 그것을 request로 하는 함수를 호출한다
5. Templates in Action

## Static Files
1. static이라는 이름의 folder를 만들고, settings.py에 STATIC_FILE_DIRS 리스트를 만들어
BASE_DIR에 static을 join한 경로를 추가한다.
2. html 파일에 {%load static%}
3. static 파일을 사용하기 위해 {} 안에 static "static파일의 경로"를 통해 보이게 할 수 있다.
