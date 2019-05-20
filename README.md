# TODO_list

# 설치 요소 (pip3, django)
1. sudo apt-get update
2. sudo apt-get install git
3. sudo apt-get install python3-pip
4. git clone https://github.com/moning02004/TODO_list
5. cd TODO_list
6. pip3 install django

# 개발 서버 구동
1. python3 manage.py collectstatic
1. python3 manage.py migrate
2. python3 manage.py runserver 0.0.0.0:8000

# Nginx 연동
1. cp todo.conf /etc/nginx/sites-available/ 
2. sudo ln -s /etc/nginx/sites-available/todo.conf /etc/nginx/sites-enables/
3. uwsgi --ini ini_todo.ini
4. sudo /etc/init.d/nginx restart