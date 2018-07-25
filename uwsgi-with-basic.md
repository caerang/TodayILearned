# 미들웨어(uwsgi) 공부하면서 필요한 주제 및 링크 정리

* [Setting up Django and your web server with uWSGI and nginx](https://uwsgi-docs.readthedocs.io/en/latest/tutorials/Django_and_nginx.html)
* [uWSGI-Process Management](https://uwsgi-docs-additions.readthedocs.io/en/latest/Options.html#process-management)
* [preforking mode]
* [TCP/IP 개론](https://www.joinc.co.kr/w/Site/Network_Programing/Documents/IntroTCPIP)
* [비동기 입출력 프로그래밍](https://www.joinc.co.kr/w/Site/Network_Programing/AdvancedComm/AIO)
* [프로세스](https://www.joinc.co.kr/w/Site/system_programing/Book_LSP/ch05_Process)
* [BSD 소켓 프로그래밍 입문](https://www.joinc.co.kr/w/Site/Network_Programing/Documents/socket_beginning)
* [유닉스 도메인 소켓](http://iamhjoo.tistory.com/19)
* [Unix Domain Socket Sample](https://www.joinc.co.kr/w/Site/system_programing/IPC/Unix_Domain_Socket)
* [SMP Safe](https://www.quora.com/What-is-SMP-safe-and-why-is-the-Linux-kernel-SMP-safe)
* [CGI, WAS, WSGI 방식의 이해](http://brownbears.tistory.com/350)
* [WSGI 스펙 문서](https://www.python.org/dev/peps/pep-3333/)


### 프락시 서버

* [참고](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A1%9D%EC%8B%9C_%EC%84%9C%EB%B2%84)
* 프락시를 통해서 다른 네트워크 서비스에 간접적으로 접속할 수 있게 해주는 컴퓨터나 응용 프로그램
![도식화한 프락시 서버.](https://upload.wikimedia.org/wikipedia/commons/2/27/Open_proxy_h2g2bob.svg '도식화한 프락시 서버. 두 컴퓨터 사이에 끼어 있는 컴퓨터가 바로 프락시 서버이다.')
*이미지 캡션*

* 서버와 클라이언트 사이에서 중계기로서 대리로 통신을 주행하는 기능을 가리켜 프락시
* 중계 기능을 하는 것을 가리켜 프락시 서버
> 왜 프락시 서버가 필요하지? 어떤 문제를 해결하기 위해 프락시 서버를 구상했을까?
* 프락시 서버는 요청된 내용을 캐시를 이용해 저장
* 캐시에 있는 내용을 요청할 경우 원본 서버에 접속해서 데이터를 가져올 필요가 없어 처리 시간 단축의 장점
* 불필요하게 외부와 연결을 하지 않아도 됨
* 외부 트래픽을 줄임으로써 네트워크 병목 현상 방지 효과
> CDN도 프락시 서버인가? 그렇게 생각할 수 있을 것 같은데...
* 프락시 서버의 용도(목적)
  * 익명으로 컴퓨터를 유지 (보안을 위해서)
  * 캐시 사용으로 빠른 리소스 접근을 위해
  웹 프락시는 웹 서버로부터 웹 페이지를 캐시로 저장하는데 흔히 사용
  * 네트워크 서비스나 콘텐츠로의 접근 정책을 적용하기 위해(예를 들어 원치 않는 사이트 차단)
  * 사용률을 기록하고 검사하기 위해(예를 들어 회사는 인터넷 이용을 파악)
  * 보안 및 통제를 뚫고 나가기 위해
  * 바이러스 전파, 악성 루머 전다, 다른 정보들을 빼낼 목적
  * 역으로 IP 추적을 당하지 않을 목적
  * 전달에 앞서 악성 코드를 목적으로 전달된 콘텐츠를 검사하기 위해
  * 박으로 나가는 콘텐츠를 검사하기 위해(데이터 유출 보호)
  * 지역 제한을 우회하기 위해