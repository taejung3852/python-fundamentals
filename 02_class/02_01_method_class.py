# Chapter02-01
# 객체 지향 프로그래밍  -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형 프로젝트
# 규모가 큰 프로젝트(프로그램) -> 함수 중심  -> 데이터 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리

# 일반적인 코딩
# 차량 1

car_company_1 = "Ferrari"
car_detail_1 = [
        {'color': 'white'},
        {"horsepower": 400},
        {'price': 8000}
]

car_company_2 = "BMW"
car_detail_2 = [
        {'color': 'black'},
        {"horsepower": 270},
        {'price': 5000}
]

car_company_3 = "audi"
car_detail_3 = [
        {'color': 'silver'},
        {"horsepower": 300},
        {'price': 6000}
]

# 리스트 구조
# 관리 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편
car_company_list = ["Ferrari", "BMW", "Audi"]
car_detail_list = [
    {'color': 'white', "horsepower": 400, 'price': 8000},
    {'color': 'black', "horsepower": 270, 'price': 5000},
    {'color': 'silver', "horsepower": 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

print()
print()


# 딕셔너리 구조
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등

car_dict = [
        {'car_company': 'Ferrari', 'car_detail':{'color': 'white', "horsepower": 400, 'price': 8000}},
        {'car_company': 'Ferrari', 'car_detail':{'color': 'black', "horsepower": 270, 'price': 5000}},
        {'car_company': 'Ferrari', 'car_detail':{'color': 'silver', "horsepower": 300, 'price': 6000}},
]

del car_dict[1]

print(car_dict)



# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용

class Car(): # 괄호 안에는 오브젝트가 들어간다. 아무것도 안들어간다면 괄호를 생략가능
        def __init__(self, company, details):
                self._company = company
                self._details = details

        # 사용자 입장
        def __str__(self):
                return 'str : {} - {}'.format(self._company, self._details)

        # __str__과 __repr__ 둘 다 있으면 객체를 출력하면 __str__ 메서드를 사용해서 출력을 한다. 없으면 __repr__를 사용.
        # 개발자 입장에서 텍스트 뿐만아니라 객체의 타입정보까지 출력할 때는 representation 을 사용
        def __repr__(self):
                return 'repr : {} - {}'.format(self._company, self._details)
car1 = Car('Ferrari', {'color': 'white', "horsepower": 400, 'price': 8000})

# 반복문에서는 __str__, 리스트안에 넣은 객체를 출력하면 __repr__