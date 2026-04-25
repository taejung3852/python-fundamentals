# Chapter03-01
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스) -> 파이썬을 잘하려면 이 네가지를 알아야한다.
# 클래스안에 정의할 수 있는 특별한(Built-in) 메서드

# 기본형
print(int)
print(float)

# 모든 속성 및 메서드 출력
print(dir(int))
print(dir(float))

n = 10

print(n + 100)
# + 는 내부적으로 아래 매직메서드가 호출된 것이다.
print(n.__add__(100))
# print(n.__doc__)
print(n.__bool__(), bool(n))

print(n*100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self): # 객체의 현재 상태를 문자열로 보여주는 매직메서드다.
        return f"Fruit Class Info : {self._name}, {self._price}"

    def __add__(self, x):
        print('Called >> __add__')
        return self._price + x._price

    def __sub__(self, x):
        print('Called >> __sub__')
        return self._price - x._price

    def __le__(self, x):
        print('Called >> __le__')
        if self._price <= x._price:
            return True
        else: 
            return False
        
    def __ge__(self, x):
        print('Called >> __ge__')
        if self._price >= x._price:
            return True
        else: 
            return False
    
# 인스턴스 생성
s1 = Fruit("Orange", 7500)
s2 = Fruit("Banana", 3000)

# 매직 메서드를 몰랐을 경우(일반적인 계산)
print(s1._price + s2._price) # 가독성도 떨어지고 코드 양이 많이 늘어난다.

# 위에서 정의를 해줬기 때문에 아래를 해도 계산이 된다.
print(s1 + s2)
print()
# 매직메서드
print(s1 >= s2) # 매직메서드를 재정의를 해주니까 이렇게 인스턴스를 그대로 연산을 해도 된다.
print()

print(s1 <= s2)
print()

print(s1 - s2)
print()

print(s2 - s1)
print()

print(s1)
print(s2)