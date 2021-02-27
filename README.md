# DjangoStudy 프로젝트

----------

현재 init 환경

os : ubuntu 18.08
python vitaul : miniconda 

----------
master  <    -    > chano21 |->  samplebranch1  
                            |  
                            |->  samplebranch2  
                            |  
                            |->  samplebranch3  

      chano21 에서 브랜치 따서작업하면 chano21이 master에 merge작업 진행.
      
      pr(pull request)는 chano21에게 요청. master에 요청하지 말것.
      
----------

서버 실행 명령어

python manage.py makemigrations --settings=djangostudy.initialize.settings

python manage.py migrate --settings=djangostudy.initialize.settings

-------------

