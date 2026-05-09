# Chapter05-03
# 일급 함수(일급 객체) -> 매우매우 중요하다. 코루틴, 클로져에 연결되는 개념. 함수형 프로그래밍이 가능해진다.
# 클로저 기초
# 데코레이터(Decorator)

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 기능
# 3. 조합해서 사용 용이

# 내가 요즘에 공부하는 LangGraph에서 에이전트에 Tool을 붙여줄 때 사용한다.
"""
```py
from langchain_core.tools import tool
```
"""

# 단점
# 1. 가독성이 떨어질 수 있다.
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리할 수 있다. 즉, 데코레이터로 만드는 것이 굳이인 경우도 있다는 것이다.
# 3. 디버깅이 불편하다.

"""
# 활용예시

## 상황
- 웹 사이트 내 사용자 체류 시간 통계 분석하고 싶다.

## 적용 
- 각 탭(페이지) 진입 및 이탈 시점을 기록하는 로직을 데코레이터로 공통화한다. 
- 이 데코레이터를 각 페이지 방문을 처리하는 함수에 달아준다.
- 이를 통해 기존 비즈니스 로직을 수정하지 않고도, 탭 이동 간의 시간 차이를 계산하는 부가 기능을 효율적으로 주입할 수 있다.

## 나만의 의문
- 함수를 만들어서 각 페이지 방문 함수에 적용해주는거랑 차이가 뭘까?
- 그렇다면 함수를 작성해서 적용할 때와 데코레이터를 작성해서 적용할 때의 기준이 뭘까?

> 위 두가지 의문을 모두 해결해주는 대답이 아래와 같다.
  찾아보면 코드 재사용성, 유연한 기능 추가 등 이 있었지만 나한테 제일 와닿은 사용 이유는 관심사 분리였다. 함수별로 짜놓은 로직들의 관심사와 데코레이터의 관심사가 다르면 코드를 읽는데 가독성이 떨어질 수 있는 것을 분리해주는 것이다.
"""

# 데코레이터 실습
import time


# 클로저 형태로 만들어준다.
def performance_clock(func): # 함수를 매개변수로 받아준다. 자유변수로서 사용되는거다
    def performance_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = func.__name__
        # 하수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print(f"[{et}s] {name}({arg_str}) -> {result}")
        
        return result
    return performance_clocked

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def int_to_eng_func(seconds):
    llm = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')
    response = llm.invoke([f'{seconds}이거 영어로 어떻게 읽어?']).content
    print(response)

def calc_func(*numbers):
    llm = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')
    response = llm.invoke(f"{numbers} 이거 총합은?").content
    print(response)


"""
위 함수를 decorator에 적용하면 아래처럼 적용이 되는거다
```py
def performance_clock(int_to_eng_func): # 함수를 매개변수로 받아준다. 자유변수로서 사용되는거다
    def performance_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = int_to_eng_func(*args)
        # 함수 종료 시간
        et = time.perf_counter() - st
        # 실행 함수명
        name = int_to_eng_func.__name__
        # 하수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print(f"[{et}s] {name}({arg_str}) -> {result}")
        
        return result
    return performance_clocked
```

"""

# 데코레이터 미사용시

none_deco1 = performance_clock(int_to_eng_func)
none_deco2 = performance_clock(calc_func)

print(none_deco1, none_deco1.__code__.co_freevars)
print(none_deco2, none_deco2.__code__.co_freevars)

print('-'*40, 'Called None Decorator -> time_func')
print()

none_deco1(1.5)
print('-'*40, 'Called None Decorator -> int_to_eng_func')
print()

none_deco2(100,200,300,400,500)
print('-'*40, 'Called None Decorator -> calc_func')


print()
print()


# 데코레이터 사용
@performance_clock # 이렇게 적용
def int_to_eng_func(seconds):
    llm = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')
    response = llm.invoke([f'{seconds}이거 영어로 어떻게 읽어?']).content
    print(response)

@performance_clock
def calc_func(*numbers):
    llm = ChatGoogleGenerativeAI(model = 'gemini-3.1-flash-lite')
    response = llm.invoke(f"{numbers} 이거 총합은?").content
    print(response)

print('-'*40, 'Called Decorator -> int_to_eng_func')
print()
int_to_eng_func(100000) # 여기서는 원함수를 직접 사용할 수 있다. 데코레이터를 달아줬기 때문

print('-'*40, 'Called Decorator -> calc_func')
print()
calc_func(100,200,300,400,500)