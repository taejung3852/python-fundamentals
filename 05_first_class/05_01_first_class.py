# Chapter05-01
# 일급 함수(일급 객체) -> 매우매우 중요하다. 코루틴, 클로져에 연결되는 개념. 함수형 프로그래밍이 가능해진다.
# 파이썬 함수 특징
# 1. 런타임 초기화
# 2. 변수 할당 -> 함수를 변수에 할당가능
# 3. 함수 인수 전달 가능 -> 즉, 다른 함수의 파라미터로 전달 가능해야 함.
# 4. 함수 결과 반환 가능(return) -> 함수를 반환할 수 있어야 한다.
# 5. 파이썬 함수는 모두 일급 객체다!

# 함수 객체
from pprint import pprint
def factorial(n):
    """Factorial Function -> n : int"""
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1) # 함수에서 함수를 반환

class A:
    pass

print(factorial(5))
print(factorial.__doc__)

print(type(factorial), type(A))
# 출력 결과
# <class 'function'> <class 'type'>

# class로 나온다. 일급객체

pprint(dir(factorial))
# 위를 출력해보면 클래스에서 사용할 수 있는 매직메서드를 확인할 수 있다.
# 이를 통해 클래스가 아닌 함수지만 객체 취급을 한다는 것을 알 수 있다.

pprint(set(sorted(dir(factorial))) - set(sorted(dir(A))))
# 위 출력은 함수가 사용할 수 있는 속성, 메서드들의 종류에서 클래스가 사용할 수 있는 속성, 메서드들의 종류를 빼본 것이다.
# 함수만의 특징인 __global__, __closure__, __call__ 등을 볼 수 있다.
# closure와 callable은 중요하다.

print(factorial.__name__)
# 출력 결과
# factorial

print(factorial.__code__)
# 출력 결과
# 파일 경로와 코드가 어떻게 작성된지 볼 수 있다. 그리고 정의되어 있는 라인

# 변수 할당
var_func = factorial
# factorial() 이렇게 입력을 하면 함수를 실행하는 것인데 괄호 없이 할당을 함.

print(var_func)
# 출력 결과 
# <function factorial at 0x102bf1440>

print(var_func(5))
# 출력 결과
# 120
# 변수에 할당된 상태로 함수가 실행이 된다.

print(list(map(var_func, range(1,6))))
# [1, 2, 6, 24, 120]

# 함수를 인수로 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce 는 제대로 알고 넘어가야한다.
# 패턴이 (함수, 컨테이너) -> 컨테이너에 있는 요소들에 함수를 하나씩 적용

print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1, 6) if i % 2])

print()
print()

# reduce
from functools import reduce
from operator import add # -> + 똑같음

print(reduce(add, range(1, 11)))
print(sum(range(1,11))) 

# 둘 다 결과가 55로 나온다.
# 속도는 sum을 사용하는 것이 더 빠르다. reduce는 코드 가독성에 있어서 이점이 있는거 같다.

# 익명함수(Lambda)
# 가급적 주석 작성!! 
# 가급적 익명함수 보다는 함수 작성!!
# 일반 함수 형태(이름이 있는 함수)로 리팩토링을 권장

print(reduce(lambda x,y: x + y, range(1,11)))


print()
print()

# Callable: 호출 연산자 -> 메서드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(factorial), callable(3.14))
# 3.14는 False가 된다. 3.14()로 호출 할 수 없기 때문


# partial 사용법 매우 중요! 많이 사용한다. : 인수 고정 -> 콜백 함수 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5) # 5 * ? 이런식으로 고정이 된거다.
# five 변수는 함수가 되는 것이다. 

six = partial(five, 6)

print(five(10))
# 50

print(six())
# 30

print([five(i) for i in range(1, 11)])
print(list(map(five, range(1,11))))