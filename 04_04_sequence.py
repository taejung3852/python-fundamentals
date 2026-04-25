# Chapter04-04
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict(수정이 불가능한 딕셔너리)

from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
d_frozen = MappingProxyType(d) # 변수명을 이런식으로 많이들 해준다.

print(d, id(d))
print(d_frozen, id(d_frozen))#hash(d_frozen) 불변형으로 변경했음에도 해시값 출력 x

# 수정 가능
d['key2'] = 'value2'
print(d)

# 수정 불가능
# d_frozen['key2'] = 'value2'
# print(d_frozen)

print()
print()

# set 선언
s1 = {'Apple', "orange", "Apple", "Orange", 'Kiwi'}
s2 = set(['Apple', "orange", "Apple", "Orange", 'Kiwi'])
s3 = {3}
s4 = {}
s5 = frozenset({'Apple', "orange", "Apple", "Orange", 'Kiwi'})

print(type(s4)) # 결과 dict 아무것도 작성하지 않으면 딕셔너리로 생성된다.

# 추가 가능
s1.add('Melon')
print(s1)

# 추가 불가
# s5.add('Melon')
# print(s5) #frozenset도 Read Only로 만들 수 있다.

print()
print()

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행 과정 확인 가능
from dis import dis


print('-------')
print(dis('{10}'))
print('-------')
print(dis('set([10])'))

'''
결과를 확인해보면 set을 사용해서 선언을 하는게 과정이 더 많다는 것을 확인할 수 있다.
그래서 속도가 더 느리다.

결과
-------
  0           RESUME                   0

  1           LOAD_CONST               0 (10)
              BUILD_SET                1
              RETURN_VALUE
None
-------
  0           RESUME                   0

  1           LOAD_NAME                0 (set)
              PUSH_NULL
              LOAD_CONST               0 (10)
              BUILD_LIST               1
              CALL                     1
              RETURN_VALUE
None
'''

# 지능형 집합(Comprehending Set)

print("------")

from unicodedata import name
print({name(chr(i), '') for i in range(0, 256)})