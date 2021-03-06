# 성적 관리 프로그램  

## 개요  

학생들의 성적을 입력받고 저장, 출력, 조회, 리포트 생성과 같은 기능을 제공한다  

## 기능적 요구사항(Functional Requirements)  

### 1. 성적 입력  

### 2. 성적 출력  

### 3. 성적 조회  

### 4. 저장하기  

* Input : 성적 데이터가 저장된 딕셔너리  

* Output : score.dat에 성적 데이터 저장  

* 파일 객체 다룰 떄 pg247 참고 -> TextIO, StringIO 활용해보기  

### 5. 읽어오기  

### 6. 리포트 생성하기  

* Input : score.dat

* Output : score.csv  

### 7. 추후 추가  

### 8. 추후 추가  

### 9. 종료  

## 비기능적 요구사항(Non-Functional Requirements)  

### 배운 것을 적절히 활용하였나  

* Python  

* Docker  

  * docker-compose로 python 컨테이너, DB 컨테이너 서비스 실행  

  * 볼륨 마운트 기능으로 데이터는 로컬에 유지  

* Linux, Shell Script  

* Infrastructre as Code  

### 정확성

* 오류없이 잘 작동하는가  

### 파이썬 답게, OOP, Clean Code에 맞게 작성하였는가  

* 적절한 자료구조를 사용하였는가  

* 예외처리를 적절히 추가하였는가  

* 클래스 적절히 사용하였는가  

* 기능을 모듈화하였는가  

* 함수는 하나의 기능만을 수행하는가  

* typing 활용으로 인자와 반환값에 대한 정보를 잘 전달하여 보기 쉬운 코드로 작성하였나  

* docstring을 작성하여 함수에 대한 설명을 덧붙였는가  

* 모듈 파일과 Main 파일을 분리하여 패키지를 구성하였는가  

* 파일로 저장한 결과들은 output 폴더에 저장  

### 추가 기능을 구현하였는가  

* 추가로 구현할 사항 고려하기  

### 프로젝트 수행 시나리오  

1. git에서 프로젝트 풀해서 로컬에 다운받고,  

2. sh 파일의 명령어를 실행하여,  

3. 풀해온 프로젝트를 volume 마운트 시켜 컨테이너에서 프로젝트 실행  

### 20200723 추가 사항  

스웜 - 스택 - service - python program(replicas 2)
     - 스택 - service - database (master 1, slave 2), manager에 master
     - 스택 - service - visualizer(replicas X)

네트워크 - overlay 네트워크  

### 2일차 모듈 프로젝트

기존 모델링(Car Dealership)에서 속성을 조금 추가할 것  

1. 고객 관리  
2. 자동차 관리(등록, 조회, 수정, 삭제) - CRUD  
3. 구매 관리(등록, 조회, 수정, 삭제) - CRUD  
4. 서비스(등록, 조회, 수정, 삭제) - CRUD  

고객id -> 자동차 목록 보여주기 -> 구매  
예약(서비스) -> 날짜 가능 여부(여유되는 메카닉, 서비스 업체) -> 신청 -> 조회  \

### 3일차 모듈 프로젝트  

파이썬 + DB - 도커 컴포즈 파일로 패키징해서 이미지 주소 제출  

컴포즈 파일에 이미지는 팀장의 도커 허브 주소에 등록해두고 컴포즈 업 할때 다운 되도록  

CMD, ENTRYPOINT로 컴포즈 up 시 실행되도록  
