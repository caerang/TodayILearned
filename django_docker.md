# 컴포우즈와 장고

빠르게 해보는 장고/포스트크래스 기반의 도커 컴포우즈 연습

## 프로젝트 구성 요소 설정

이번 프로젝트는 파이썬 의존성이 있는 도커 파일을 생성하고 docker-compose.yml 파일을 생성한다(확장자는 .yml 또는 .yaml을 사용할 수 있다)

1. 빈 프로젝트 폴더를 생성한다<p>
쉽게 기억할 수 있는 폴더명을 사용한다. 프로젝트 폴더명은 어플리케이션 이미지의 컨텍스트이다. 폴더에는 이미지 생성에 필요한 자원만 포함할 수 있다.

2. 프로젝트 폴더에 Dockerfile을 생성한다.<p>
도커 파일에는 어플리케이션 이미지 생성에 필요한 하나 이상의 빌드 명령어를 정의 한다. 도커 이미지를 생성하면 컨테이너에 생성된 이미지를 실행할 수 있다. 자세한 내용은 Dockerfile, 과 Docker user guide Dockerfile reference 를 참고해라.

3. Dockerfile에 다음 내용을 추가해라<p>
```dockerfile
FROM python:3.6.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
```
<p>
위에 명시된 Dockerfile 은 Python 3.6.5 부모 이미지로 시작한다. 부모 이미지는 code 폴더를 추가한다. 부모 이미지는 또한 requirements.txt에 명시된 패키지를 설치한다.

4. Dockerfile을 저장하고 종료한다.

5. 프로젝트 폴더에 requirements.txt 파일을 생성한다. 이 파일은 도커 파일에 작성된 RUN pip install -r requirements.txt 명령어에 사용된다.

6. requirements.txt에 프로젝트에 필요한 패키지를 추가 한다.<p>
```text
django
psycopg2
```

7. requirements.txt 파일을 저장하고 종료한다.

8. 프로젝트 폴더에 docker-compose.yml 파일을 생성한다.<p>
docker-compose.yml 파일은 어플리케이션에 구성하기 위해 필요한 서비스를 명세한다. 예제에서는 웹 서버와 데이터베이스가 서비스이다. 구성 파일은 이런 서비스가 어떤 도커 이미지를 사용하는지 서비스들 사이에 어떻게 연결하는지 컨테이너 내부에 마운트가 필요한지 등을 명세한다. 마지막으로 docker-compose.yml 파일은 이런 서비스가 오픈하는 포트는 무엇인지를 명세한다. docker-compose.yml 파일이 어떻게 동작하는지 설명하는 더 자세한 정보는 reference를 참고해라.

9. docker-compose.yml에 아래 환경 설정 내용을 추가해라.<p>
```yaml
version: '3'

services:
  db:
    images: postgres
  web:
    build: .
    command: python3 manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```
파일은 db와 web 서비스를 정의한다.

10. docker-compose.yml 파일을 저장하고 종료한다.

## 장고 프로젝트 생성

이번 과정은 이전 과정에서 설정한 내용으로 도커 이미지를 생성하고 장고 기본 프로젝트를 생성한다

1. 프로젝트 폴더위 최상위로 이동한다.

2. 다음과 같이 docker-compose run 명령어를 사용해서 장고 프로젝트를 생성해라<p>
```cmd
sudo docker-compose run web django-admin.py startproject composeexample .
```
이 명령어는 Compose가 web 서비스의 환경 구성과 이미지를 이용해서 컨테이너 내부에서 django-admin.py startproject composeexample 명령어를 실행하도록 명령한다. 명령어를 실행하는 시점에 web 이미지가 생성되지 않았기 때문에 Compose는 docker-compose.yml 파일에 명시된 build: . 에 따라 현재 폴더에서 이미지를 생성한다.

web 서비스 이미지가 생성되고 나면 Compose 는 이미지를 실행하고 django-admin.py startproject 명령어를 컨테이너에서 실행한다. 이 명령어는 기본 장고 프로젝트 생성에 필요한 폴더와 파일을 생성한다.

3. docker-compose 명령어 실행을 완료하고 프로젝트 폴더의 리스트를 살펴봐라.
```
 $ ls -l
 drwxr-xr-x 2 root   root   composeexample
 -rw-rw-r-- 1 user   user   docker-compose.yml
 -rw-rw-r-- 1 user   user   Dockerfile
 -rwxr-xr-x 1 root   root   manage.py
 -rw-rw-r-- 1 user   user   requirements.txt
```
만약 리눅스에서 도커를 실행중 이라면 django-admin 은 root은 소유로 생성됐을 것이다. 이런 현상은 컨테이너가 root 사용자로 실행되기 때문이다. 새로운 파일의 소유자를 변경한다.
```
sudo chown -R $USER:$USER .
```
만약 Docker on Mac 또는 Docker on Windows 에서 실행한다면 django-admin 명령어로 생성된 파일의 소유자가 사용자로 되어 있을 것이다. 다음 명령어를 실행해서 확인해 봐라.
```
-rw-r--r--@ 1 hyeongdo  staff  147 Jun 29 17:26 Dockerfile
drwxr-xr-x  7 hyeongdo  staff  224 Jun 29 17:37 django_docker
-rw-r--r--@ 1 hyeongdo  staff  210 Jun 29 17:32 docker-compose.yml
-rwxr-xr-x  1 hyeongdo  staff  545 Jun 29 17:34 manage.py
-rw-r--r--@ 1 hyeongdo  staff   16 Jun 29 17:27 requirements.txt
```


## 데이터베이스 접속
