# Chapter02-02

# 객체 지향 프로그래밍  -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심  -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용



class Car(): # 괄호 안에는 오브젝트가 들어간다. 아무것도 안들어간다면 괄호를 생략가능

        # class를 만들어줄때 아래와 같이 클래스 이름과 만든 사람, 날짜 등(설명)을 작성해주는게 관례
        # __doc__ 매직 메서드를 활용해서 아래 주석 내용을 확인해볼 수 있다.
        """
        Car class
        Author : 박태정
        Date: 2025.12.21
        """
        
        # 클래스 변수(모든 인스턴스가 공유)
        car_count = 0

        def __init__(self, company, details): # self란?
                self._company = company
                self._details = details
                Car.car_count += 1

        # 사용자 입장
        def __str__(self):
                return 'str : {} - {}'.format(self._company, self._details)

        # __str__과 __repr__ 둘 다 있으면 객체를 출력하면 __str__ 메서드를 사용해서 출력을 한다. 없으면 __repr__를 사용.
        # 개발자 입장에서 텍스트 뿐만아니라 객체의 타입정보까지 출력할 때는 representation 을 사용
        def __repr__(self):
                return 'repr : {} - {}'.format(self._company, self._details)

        def __del__(self):
                Car.car_count -= 1

        def detail_info(self):
                print(f"Current ID : {id(self)}")
                print(f"Car Detail Info : {self._company} {self._details.get("price")}")


car1 = Car('Ferrari', {'color': 'white', "horsepower": 400, 'price': 8000})
car2 = Car('BMW', {'color': 'black', "horsepower": 270, 'price': 5000})
car3 = Car("Audi", {'color': 'silver', "horsepower": 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

# dir & __dict__ 확인
# dir은 해당 인스턴스가 갖고 있는 모든 요소들 즉, 애트리뷰트들을 리스트형태로 출력
print(dir(car1))

# __dict__는 해당 인스턴스의 요소들을 키, 밸류 형태로 출력
print(car1.__dict__)

# Doctring 아래 매직메서드를 작성하면 해당 클래스에 대한 간단한 설명을 작성한 부분을 출력해볼 수 있다.
print(Car.__doc__)

print()
print()

car1.detail_info()

# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__), id(car2.__class__)) # 이 값이 똑같은 이유는 클래스의 ID를 출력해서 그런거다. 인스턴스의 ID가 아닌

# 에러
# Car.detail_info() # 이 메서드를 가서 확인해보면 self 인자를 하나 꼭 필요로 해서 매개변수 에러를 발생시킨다.

# 위 에러를 해결하려면 아래 처럼 self에 해당하는 매개변수를 넣어줘야한다.
# Class로 접근하려면 아래처럼 하면된다.(코딩 스타일)
Car.detail_info(car2)

print(Car.car_count)

print()
print()

# 접근
print(car1.car_count)
print(Car.car_count)

del car2

# 한가지 집고 넘어가야하는 점 같은 변수명을 Class 안에 갖고 있다면 인스턴스가 갖고 있는지 확인하고 없으면 상위로 올라가서 Class안에 변수 있는지 확인 후 출력
