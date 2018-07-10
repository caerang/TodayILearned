[reference](https://docs.docker.com/compose/compose-file/)

* service 가 뭐지?


### build 옵션
* 빌드하는 시점에 적용되는 옵션
* build context에 대한 경로를 포함하는 문자열 또는 개체로 명시 될 수 있음

* build context는 빌드할 때 워킹 디렉토리 개념인것 같음
* 빌드하면서 대체 도커파일 사용도 가능 한 것 같고

* 빌드 과정에서 사용할 수 있는 인수도 설정할 수 있고

#### CONTEXT
이미지 빌드 할 때 참고할 파일 경로

#### DOCKERFILE

#### ARGS

#### CACHE_FROM

#### LABELS

#### SHM_SIZE


#### command
기본 명령을 덮어쓴다
