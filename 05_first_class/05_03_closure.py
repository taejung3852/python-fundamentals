# Chapter05-03
# 일급 함수(일급 객체) -> 매우매우 중요하다. 코루틴, 클로져에 연결되는 개념. 함수형 프로그래밍이 가능해진다.
# 클로저 기초
# 헷갈릴 때 아래 주석을 보면 이해하기 쉽다.
# 외부에서 호출된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능

# 지난 시간에 생성한 Averager(클래스의 callable로 구현한 것을 진짜 클로저로 구현)

#Closure 사용
def closure_ex1():
    # Free variable -> 자유변수
    # 클로저 영역
    series = []
    def averager(v):
        series.append(v)
        print(f'inner >>> {series} / {len(series)}')
        return sum(series)/len(series)
    return averager # 함수를 결과로 반환한다. 일급 객체의 특징이다! 여기서 averager() 반환을 하면 함수 결과를 반환하게 된다.

avg_closure1 = closure_ex1()
print(avg_closure1(10))
# 결과
# inner >>> [10] / 1
# 10.0
print(avg_closure1(30))
# 결과
# inner >>> [10, 30] / 2
# 20.0
# 이걸 어떻게 기억하는거지 ??
# 아 이해했다. avg_closure1에 함수를 그대로 넣은게 아니고 함수를 실행해서 넣어줬다는 것을 잊으면 안된다.
# 클로저가 굳이 필요한가? 라는 생각이 든다. 값을 유지해주고 그걸 계속해서 업데이트 해주는 방식이 클래스의 특징인거 같은데 가볍게 사용할 때 사용하면 될거 같다는 생각이든다.

print()
print()

# function inspection
print(dir(avg_closure1))
# 확인해보면 __closure__ 가 있는 것을 알 수 있다.
print()
print(dir(avg_closure1.__code__))
# __code__는 함수 설계도다.
# 확인해보면 co_~ 이렇게 생긴 것들을 볼 수 있다.
print(avg_closure1.__code__.co_freevars)
# series가 출력된 것을 알 수 있다. 즉, 자유 변수로 되어있다는 것을 증명 가능하다

print(dir(avg_closure1.__closure__))
# 리스트로 되어있다.
print(avg_closure1.__closure__[0].cell_contents)
# 10, 30 이 출력이 된다.

print()
print()

# 잘못된 클로저 사용
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1
        total += v
        return total/cnt
    return averager

avg_closure2 = closure_ex2()
# print(avg_closure2(10))
# 예외가 발생한다. 내가 코딩테스트할 때 정말 많이 걸리던 부분이었다. 상위 함수에서 선언을 해주고 하위 함수에서 재정의를 해주면 에러가 발생한다.


def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total/cnt
    return averager

# 이렇게 nonlocal 예약어를 사용해서 로컬 변수가 아니라는 처리를 해주면 괜찮다.
avg_closure3 = closure_ex3()

print(avg_closure3(10))
print(avg_closure3(30))