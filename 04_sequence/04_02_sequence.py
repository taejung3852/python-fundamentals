# Chapter04-02
# 시퀀스형
# 컨테이너(Container: 서로 다른 자료형[list, tuple, collections.deque]
# 플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b 파이썬에서는 이게 가능하다(임시변수 없이)

#매우 중요 (파이썬의 편하다 편하다 항상했는데 언패킹을 모르던 파이썬은 불편하다 생각이 들정도로 가히 충격적이다.)
print(divmod(100, 9))
print(divmod(*(100,9))) # * 뒤에 있는 요소를 언패킹하는 것
print(*(divmod(100,9))) # 결과 11 1 -> 상자를 까서 '내용물'만 꺼내는 것


print()

x, y, *rest = range(10) # 언패킹을 사용하면 입력한 변수명들의 수와 입력될 값들이 일대일 대응이 되지 않아도 알아서 리스트로 변환해서 다 넣는다.
print(x, y, rest) # 결과: 0 1 [2, 3, 4, 5, 6, 7, 8, 9] 언패킹의 장점이 보인다.

x, y, *rest = range(2) # 이렇게 해도 에러가 발생하지 않는다.
print(x, y, rest) # 결과: 0 1 []

x, y, *rest = 1, 2, 3, 4, 5
print(x, y, rest)

print()
print()

# Mutable(가변) vs Immutable(불변)

l = (15, 20, 25)
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

# 연산 후 두 변수의 주소값이 모두 변경되었다.
print(l, id(l)) 
print(m, id(m)) 

l *= 2
m *= 2

print(l, id(l)) # 튜플 같은 경우는 연산 후에 주소값이 변경됐다
print(m, id(m)) # 리스트 같은 경우는 연산 후에 주소값이 동일하다

# 튜플의 경우는 항상 불변이기 때문에 한번 생성된 값에서 수정이 불가능해서 매번 새로 생성하게 된다.
# 반면 m*=2를 했을 때와 m=m*2의 차이가 발생한 이유는 이때 사용된 매직메서드를 확인해보면 알 수 있다.

# m*=2 -> __imul__ 이 사용되는데 이건 기존 변수에 이어 붙이거나 수정을 하는 식으로 동작을 한다.
# m=m*2 -> __mul__ 이 사용되는데 이것은 m이라는 새로운 변수를 생성해서 연산한 결과 값을 대입해서 정의하는 것이다.

print()
print()

# sort vs sorted
# reverse, key가 기본적으로 len(길이)옵션이 있다, key=str.lower, key=func...

# sorted : 정렬 후 새로운 객체 반환 (원본 수정 X)
f_list = ["orange", 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len)) # 어떤 값을 기준으로 정렬할지 키 값을 줄 수 있다.
print('sorted - ', sorted(f_list, key= lambda x: x[-1])) # 마지막 글자를 기준으로 정렬을 할 수 있다.
print('sorted1 - ', sorted(f_list, key= lambda x: x[-1], reverse=True)) # 마지막 글자를 기준으로 정렬을 할 수 있다.

print(f_list)

# [추가 학습 메모: 함수의 인자 전달 방식]

# 1. sorted 함수의 시그니처 이해
# sorted(iterable, /, *, key=None, reverse=False)

# 2. '/' 기호 (Positional-only)
# - '/' 앞의 인자(iterable)는 반드시 '값'으로만 전달해야 함.
# - sorted(iterable=f_list) 와 같이 이름을 명시해서 호출하면 에러 발생.

# 3. '*' 기호 (Keyword-only)
# - '*' 뒤의 인자(key, reverse)는 생략 가능하지만(기본값이 있으므로),
# - 만약 값을 전달하려면 반드시 key=func, reverse=True 처럼 '이름'을 써야 함.
# - sorted(f_list, len) (X) -> 에러 발생
# - sorted(f_list, key=len) (O) -> 정상 작동

# 4. 기본값 (Default Value) 설정
# - key: None = None -> key를 지정 안 하면 기본적으로 None(그대로 정렬)
# - reverse: bool = False -> reverse를 지정 안 하면 기본적으로 False(오름차순)
# - 이처럼 '= 값' 형태가 선언되어 있어 선택적으로(Optional) 사용 가능한 것.

# 5. 사용자 정의 함수 예시
# def my_sort(data, /, *, opt=True): 
#     pass
# 위와 같이 정의하면 파이썬 내부 구현처럼 인자 전달 방식을 강제할 수 있음.

print()
print()

# sort :  정렬 후 객체 직접 변경 (원본 수정)

# 반환 값 확인(None)
print('sort - ', f_list.sort(), f_list)
print('sort - ', f_list.sort(reverse=True), f_list)
print('sort - ', f_list.sort(key=len), f_list)
print('sort - ', f_list.sort(key=lambda x:x[-1]), f_list)
print('sort - ', f_list.sort(key=lambda x:x[-1], reverse=True), f_list)

# List vs Array 적합한 사용법 설명 매우 중요
# 리스트 기반 : 융통성, 다양한 자료형, 범용적 사용
# 숫자 기반 : 배열(리스트와 거의 호환[리스트에서 사용하는 함수 배열에서도 거의 사용가능])Array


