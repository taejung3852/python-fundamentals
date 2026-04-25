# Python Fundamentals

파이썬 중급 및 심화 개념 학습 기록을 남기는 레포지토리입니다. 

단순한 문법을 넘어, 파이썬의 내부 동작 원리를 파악하고 효율적인 코드 구조를 설계하는 데 목적을 두고 있습니다. 객체 지향 프로그래밍의 심화 개념, 일급 함수, 그리고 비동기 처리 기술을 숙달하여 향후 여기서 익힌 탄탄한 기본기가 앞으로 어떤 도구를 다루든 좋은 밑거름이 될 거라 믿습니다.

## 디렉토리 구조 및 학습 내용

각 섹션별로 디렉토리를 분리하여 예제 코드와 핵심 요약을 정리했습니다.

* **`02_class/` : 파이썬 클래스 심화**
  * 클래스와 인스턴스 변수의 네임스페이스 차이 분석
  * 클래스 메소드(Class Method)와 정적 메소드(Static Method)의 올바른 활용

* **`03_masic_method/` : 파이썬 매직 메서드**
  * 매직 메소드(Magic Method)를 이용한 파이썬 내장 기능 오버라이딩
  * 사용자 정의 객체의 시퀀스 및 반복(Iterable) 특성 구현

* **`04_sequence/` : 시퀀스 데이터 구조**
  * 컨테이너(Container)와 플랫(Flat) 시퀀스의 메모리 구조 차이
  * 가변(Mutable)형과 불변(Immutable)형 데이터의 안전한 핸들링

* **`05_first_class/` : 일급 함수와 데코레이터**
  * 일급 객체로서의 함수 특성 및 변수 할당, 인수 전달
  * 상태를 기억하는 클로저(Closure) 구현
  * 데코레이터(Decorator)를 활용한 로깅 및 공통 로직 모듈화

* **`06_concurrency/` : 병행성 및 비동기 처리**
  * 제너레이터(Generator)와 `yield`를 통한 메모리 효율화
  * 코루틴(Coroutine)의 동작 원리
  * `concurrent.futures` 및 `AsyncIO`를 활용한 병렬 스크래핑 및 I/O 바운드 최적화 실습

## 🛠 환경
* **Language:** Python 3.x
* **Editor:** VS Code

## 📝 Commit Convention
* `feat:` 새로운 예제 코드 및 기능 학습 추가
* `fix:` 기존 코드 또는 오타 수정
* `docs:` README 또는 학습 주석 수정
* `chore:` 설정 파일(`.gitignore` 등) 수정