# Chapter04-01
# 시퀀스형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque]
# 플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# 지능형 리스트(Comprehending lists)
chars = '+_)(*&^%$#@!)'

code_list1 = []

for s in chars:
    # 유니코드 리스트
    code_list1.append(ord(s))

print(code_list1)

# Comprehending list
code_list2 = [ord(s) for s in chars] # 컴프리핸션을 사용하면 약간 속도가 우세하다
print(code_list2)

# Comprehending lists + map, filter
code_list3 = [ord(s) for s in chars if ord(s) > 40]
print(code_list3)

code_list4 = list(filter(lambda x: x > 40, [ord(s) for s in chars]))
code_list4 = list(filter(lambda x: x > 40, map(ord, chars)))


# 전체출력
print(code_list1)
print(code_list2)
print(code_list3)
print(code_list4)
print()
print([chr(c) for c in code_list1])
print([chr(c) for c in code_list2])
print([chr(c) for c in code_list3])
print([chr(c) for c in code_list4])

# Generater 생성
import array # array는 C언어에서 배열을 생성해주는 것을 생각하면 된다. (크기가 정해진 공간) list는 동적배열

# Generater: 한 번에 한 개의 항목을 생성(메모리 유지x)
tuple_g = (ord(s) for s in chars)
array_g = array.array('I', (ord(s) for s in  chars))

print(tuple_g) # 결과 <generator object <genexpr> at 0x1033313c0> 이런식으로 나온다. 즉, 메모리를 유지 하지 않고 어떤 값을 출력할지 준비만 하고 있는 상태가 제네레이터
print(type(tuple_g))
print(next(tuple_g))
print(type(array_g))
print(array_g.tolist())

# 제네레이터 예제
print(('%s' %c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)))

for s in ('%s' %c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,21)):
    print(s)

print()
print()

# 리스트 주의(깊은복사 얕은복사 -> c언어 할 때 배웠다. 깊은 복사는 주소값까지 복사하는 것이고 얕은 복사는 해당 요소에 들어있는 값만 복사하는 것이다.)
marks1 = [['~'] * 3 for _ in range(4)]
marks2 = [['~']*3]*4

# 이렇게 하면 결과는 같아 보인다.
print(marks1)
print(marks2)

print()

# 수정
marks1[0][1] = 'X'
marks2[0][1] = 'X'

print(marks1) # 결과 [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~'], ['~', '~', '~']] 이건 주소값을 각각 생성했다.
print(marks2) # 결과 [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']] 이건 처음 생성한 주소를 반복해서 복사를 한거다.

# 증명
print([id(i) for i in marks1]) # [4315182528, 4315182912, 4315182848, 4315183104] 각 리스트의 주소값이 다르다. (깊은 복사)
print([id(i) for i in marks2]) # [4315183040, 4315183040, 4315183040, 4315183040] 각 리스트의 주소값이 같다. (얕은 복사)