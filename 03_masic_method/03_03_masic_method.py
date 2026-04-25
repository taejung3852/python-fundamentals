# Chapter03-02
# Special Method(Magic Method)
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), Class(클래스) -> 파이썬을 잘하려면 이 네가지를 알아야한다.
# 클래스안에 정의할 수 있는 특별한(Built-in) 메서드

# 객체 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value

# 일반적인 튜플
pt1 = (1.0, 5.0)
pt2 = (2.5, 1.5)

from math import sqrt

l_leng1 = sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)
print(l_leng1)

# 네임드 튜플 사용
from collections import namedtuple
# 의아했던 점: from...import를 써도 모듈 전체가 메모리에 올라가는데, 왜 다른 메서드는 못 쓸까?
# - 처음엔 단순히 "클래스명 생략권"만 얻는 줄 알았는데 아니었다. 
# - 메모리에는 전체가 로드되지만 내 코드에서 호출할 수 있는 '통로(이름)'는 import 뒤에 명시한 것만 뚫리는 원리라고 한다.
# - collections.을 붙여서라도 쓰고 싶다면 'import collections'로 모듈 이름 자체를 등록해야 한다. 
# - 비효율적으로 보일 수 있지만 덕분에 내 코드 안에서 이름이 꼬이지 않게 관리할 수 있다는 장점이 있다고 한다.

# 네임드 튜플 선언
Point = namedtuple('Point','x y') # 클래스 형식으로 튜플을 추상화하고 있다 아래 객체 생성하는 것을 보면 알 수 있다.
# 이렇게 작성하면 튜플인데도 불구하고 각 요소들에 key값을 붙여줄 수 있다.(마치 딕셔너리처럼)
pt3 = Point(1.0, 5.0)
pt4 = Point(2.5, 1.5)

# print(pt3.x) # 딕셔너리랑 비슷해 보여서 각 요소를 출력해줄 때 pt3['x']이런식으로 했는데 안되고 pt3.x로 불러올 수 있다.
# print(pt4)

# l_leng1 = sqrt((pt3[0] - pt4[0]) ** 2 + (pt3[1] - pt4[1]) ** 2)이렇게 인덱스로 접근하는건 좋지 않다. 실수할 수 있을 가능성
l_leng2 = sqrt((pt3.x - pt4.x) ** 2 + (pt3.y - pt4.y) ** 2)

print(l_leng2)

# 네임드 튜플 선언 방법
Point1 = namedtuple("Point", ['x', 'y']) # 위랑 결과는 똑같다. 위가 더 편함
Point2 = namedtuple('Point', 'x, y')
Point3 = namedtuple('Point', 'x y')
# Point4 = namedtuple('Point', 'x y x class') # 이렇게 키 이름이 중복되거나 class같이 예약어를 이름으로 사용하면 에러가 발생한다.
Point4 = namedtuple('Point', 'x y x class', rename=True) # 이렇게 하면 해결된다. Default = False
Point5 = namedtuple('Point', 'x, y')

# 출력
print(Point1, Point2, Point3, Point4)

# Dict to Unpacking
temp_dict = {'x':75, 'y':55}

# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=20)
p4 = Point4(10, 20, 30, 40)
p5 = Point5(**temp_dict)

print()

print(p1)
print(p2)
print(p3)

# rename 테스트
print(p4)
# 결과
# Point(x=10, y=35)
# Point(x=20, y=40)
# Point(x=45, y=20)
# Point(x=10, y=20, _2=30, _3=40) # 이걸 확인해볼 필요가 있다. 3번째 4번째 요소는 키 이름을 다시 정의한 것을 볼 수 있다.

print(p5)

# 사용
print(p1.x + p2.y)

# Unpacking
x, y = p3
print(x, y)

# 네임드튜플  메서드
temp = [52, 38]
# _make() : 리스트를 네임드튜플로 변환하는 메서드
p4 = Point1._make(temp) 

print(p4)

# _fields : 필드 네임 확인(키값 조회)
print(p1._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환
d1 = p5._asdict()
print(d1)


# 실사용 실습
# 반 20명, 4개의 반(A, B, C, D)


Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()

# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers]

# 추천 (리스트 컴프리헨션 보다)
students2 = [Classes(rank, number)
             for rank in "A B C D".split()
                for number in [str(n) for n in range(1, 21)]]


# 출력
for s in students2:
    print(s)