< 개발환경 설정, 기록 정리 >

port kill command (맥 기준)
> sudo lsof -t -i tcp:8000 | xargs kill -9

가상환경명 : env
> source env/bin/activate

django-project 이름 : prj_sgm

django-app 이름 생성 규칙 : app_"앱이름"
ex) django-admin startapp app_test