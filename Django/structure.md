## Django Structure


> 장고의 폴더구조는 항상 정해져있다. 


<br> 

### 기본 구조

* Project 폴더 ( root 폴더 ) 
  > 프로젝트 폴더로써 프로젝트의 가장 밑단이다.

  <br> 

  * Project OR Config 
    > 프로젝트 설정 폴더, 프로젝트 폴더와 다른 이름일 수 있다. 
    * asgi.py 
      > Application을 연결하는 파일로 웹소켓할떄 사용해 봤다.
    * settings.py 
      >  프로젝트 전체를 설정하는 파일, 정적 파일 구조, 앱 세팅 등 세부 설정을 할 수 있다.
    * urls.py
      > 프로젝트의 URL 을 관리하는 곳 다른 곳의 URL을 포함시키거나 설정 할 수 있음
    * wsgi.py
      > wsgi 를 연결하는 곳으로 한번도 사용해본 적이 없음 
      
  <br> 
    
  * other Apps
    > 다른 기능을 담당하는 앱들로 같은 폴더 구조를 갖는다.
    * migrations
      > DB 변경사항을 관리하는 폴더
    * admin.py
      > 어드민 페이지에 등록하거나 커스텀 할 수 있는 곳
    * models.py
      > DB Model을 작성하는 곳
    * views.py
      > URL 에 맞는 기능 구현이 진행 되는 곳
  
  <br> 
  
  * dp.sqlite3
    > 장고에서 기본으로 주는 Database 
  * manage.py
    > project 에 무언가를 추가하거나 서버를 실행할 떄 사용하는 파일
  * ReadME.md
    > 소개 글
  * requirements.txt
    > 가상환경에 사용된 패키지 내역들 