# TODO_list

# 설치 요소 (pip3, django, uWSGI)
1. sudo apt-get update
2. sudo apt-get install git
3. sudo apt-get install python3-pip
4. git clone https://github.com/moning02004/TODO_list
5. cd TODO_list
6. pip3 install django
7. sudo apt-get install nginx
7. pip3 install uwsgi


# 빌드
## 개발 서버 구동
1. python3 manage.py collectstatic
2. python3 manage.py migrate
3. python3 manage.py runserver 0.0.0.0:8000

## Nginx 연동
아래를 진행하기 앞서 ini_todo.ini 파일과 todo.conf파일을 수정해야한다.

*. ini_todo.ini = daemonize의 경로를 ' /home/로그인한 유저/todo.log '로 변경하고 저장한다.

*. todo.conf = /static 의 경로를 TODO_list의 절대경로 + '/static 으로 변경한다.


1. cd TODO_list (manage.py 파일이 있는 directory)
2. cp todo.conf /etc/nginx/sites-available/ 
3. sudo ln -s /etc/nginx/sites-available/todo.conf /etc/nginx/sites-enabled/
4. uwsgi --ini ini_todo.ini
5. sudo /etc/init.d/nginx restart


## 실행 화면
<img src="/img/todo_register.PNG" width="70%"></img><br/>
<img src="/img/todo_login.PNG" width="70%" ></img><br/>
<img src="/img/main.PNG" width="70%"></img><br/>
<img src="/img/new.PNG" width="70%"></img><br/>
<img src="/img/main_after.PNG" width="70%"></img><br/>
<img src="/img/detail.PNG" width="70%"></img><br/>
<img src="/img/detail_complete.PNG" width="70%"></img><br/>
<img src="/img/complete_list.PNG" width="70%"></img><br/>

서울이라는 todo 리스트를 생성시키고 오늘을 마감일로 지정하면 다음과 같이 "오늘 마감인 목록"에 표시됩니다.
<img src="/img/today_list.PNG" width="70%"></img><br/>







