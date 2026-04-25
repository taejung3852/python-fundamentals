# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스) -> 파이썬을 잘하려면 이 네가지를 알아야한다.
# 클래스안에 정의할 수 있는 특별한(Built-in) 메서드

# 클래스 예제2
# (5,2) + (4,3) = (9,5)
# (10,3) * 5 = (50,15)
# Max((5,10)) = 10

class Vector(object):
    
    def __init__(self, *args):
        """
        Create a vector, example : v = Vector(5, 10)
        """
        if len(args) == 0: # 객체 생성해줄 때 아무 값도 넣어주지 않고 생성하는 경우
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args

    def __repr__(self):
        """
        Return the vector informations
        """
        return "Vector(%r, %r)" %(self._x, self._y)

    def __add__(self, other):
        """
        Return the vector addtion of self and other
        """
        return Vector(self._x + other._x, self._y + other._y)

    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self): # 0,0인지 확인하는 메서드 예를 들어(5,3)일 때 bool(5)가 되어서 Ture
        return bool(max(self._x, self._y))
    

# Vector 인스턴스 생성
v1 = Vector(5,7)
v2 = Vector(23,35)
v3 = Vector()

# 매직메서드 출력
print(Vector.__init__.__doc__)
print(Vector.__repr__.__doc__)
print(Vector.__add__.__doc__)

print(v1, v2, v3)
print(v1 + v2)
print(v1*3)
print(v2*10)
print(bool(v1), bool(v2))
print(bool(v3))