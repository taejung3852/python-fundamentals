# Chapter02-03

# 객체 지향 프로그래밍  -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심  -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리


class Car(): # 괄호 안에는 오브젝트가 들어간다. 아무것도 안들어간다면 괄호를 생략가능

        # class를 만들어줄때 아래와 같이 클래스 이름과 만든 사람, 날짜 등(설명)을 작성해주는게 관례
        # __doc__ 매직 메서드를 활용해서 아래 주석 내용을 확인해볼 수 있다.
        """
        Car class
        Author : 박태정
        Date: 2025.12.21
        Description : Class, Static, Instance Method
        """
        
        # 클래스 변수(모든 인스턴스가 공유)
        price_per_raise = 1.2

        def __init__(self, company, details): # self란?
                self._company = company
                self._details = details

        # 사용자 입장
        def __str__(self):
                return 'str : {} - {}'.format(self._company, self._details)

        # __str__과 __repr__ 둘 다 있으면 객체를 출력하면 __str__ 메서드를 사용해서 출력을 한다. 없으면 __repr__를 사용.
        # 개발자 입장에서 텍스트 뿐만아니라 객체의 타입정보까지 출력할 때는 representation 을 사용
        def __repr__(self):
                return 'repr : {} - {}'.format(self._company, self._details)

        # Instance Method
        # self : 객체의 고유한 속성 값을 사용
        def detail_info(self):
                print(f"Current ID : {id(self)}")
                print(f"Car Detail Info : {self._company} {self._details.get("price")}")

        # Instance Method
        def get_price(self):
            return f'Before Car Price -> company : {self._company}, price : {self._details.get('price')}'

        # Instance Method
        def get_price_culc(self):
            return f'After Car Price -> company : {self._company}, price : {int(self._details.get('price') * Car.price_per_raise)}'

        # Class Method
        @classmethod # 클래스 메서드는 이렇게 어노테이션을 사용해서 정의해줄 수 있다. 
        def raise_price(cls, per): # 여기서 cls는 내가 정의한 Car를 의미한다.
            # Car.price_per_raise는 아래처럼 사용할 수 있다.
            # cls.price_per_raise
            if per <= 1:
                print('Please Enter 1 Or More')
                return
            cls.price_per_raise = per
            print("Succeed! price increased")

        # Static Method
        @staticmethod
        def is_bmw(inst):
            if inst._company == "BMW":
                return f'OK! This car is {inst._company}'
            return 'Sorry. This car is not BMW.'

        

car1 = Car('Ferrari', {'color': 'white', "horsepower": 400, 'price': 8000})
car2 = Car('BMW', {'color': 'black', "horsepower": 270, 'price': 5000})

print(Car.__doc__)

# 전체 정보 출력
car1.detail_info()

# 가격정보 출력(직접접근)
print(car1._details.get("price")) # 그러나 이렇게 직접 접근하는 방법은 좋지 않는 방법이다. 자바나 C++에서는 private으로 접근을 못하도록 막아둔다.
# 접근을 못하게 하는 방법은 두 가지가 있다. 한가지는 막는 방법까지는 아니지만 파이썬의 철학을 이용하는 방법이다.
# 1. 변수 앞에 _(언더바)를 붙여서 암묵적으로 이건 클래스 내부에서 사용하는 함수이니까 수정하지 말아줘. 라는 의미
# 2. 변수 앞에 __(언더바를 두개)를 붙여서 네임 맹글링 설정을 통해 아예 찾지 못하게 만든다.


# 가격정보(인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격정보(인상 후)
Car.price_per_raise = 1.4 # 이렇게 직접 접근해서 수정을 하는거는 좋지 않는 방법이다. 메서드를 통해서 변경하는게 권장.

print(car1.get_price_culc())
print(car2.get_price_culc())

# 클래스 메서드 사용
Car.raise_price(1.8)

print(car1.get_price_culc())
print(car2.get_price_culc())

print(Car.is_bmw(car1))
print(Car.is_bmw(car2))


print(car1.price_per_raise)