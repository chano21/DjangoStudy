# DjangoStudy 프로젝트

----------

현재 init 환경

os : ubuntu 18.08
python vitaul : miniconda 

----------
<table>
<tr>
<td>master</td><td><-></td><td>chano21&nbsp;&nbsp;|</td><td>samplebranch1</td>
<tr>
<td></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</td><td>samplebranch2</td>
</tr>
<tr>
<td></td><td></td><td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|</td><td>samplebranch3</td>
</tr>
</tr>
</table>

      chano21 에서 브랜치 따서작업하면 chano21이 master에 merge작업 진행.
      
      pr(pull request)는 chano21에게 요청. master에 요청하지 말것.
      
----------

서버 실행 명령어

python manage.py makemigrations --settings=djangostudy.initialize.settings

python manage.py migrate --settings=djangostudy.initialize.settings

-------------

----------

REDIS DOCKER 실행 명령어

<!-- docker run -p 6379:6379 -v D:\djangostudy\DjangoStudy\redis.conf:/usr/local/etc/redis --name myredis redis redis-server -->

docker build -t chanoredis .

docker run -d -p 6379:6379 --name chanoredis redis redis-server


docker stop chanoredis && docker rm chanoredis

-------------




