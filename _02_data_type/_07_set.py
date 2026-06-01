#set(집합)  : 중복허용 불가. 시퀀스 타입 아님. 순회(iterable)은 가능.  집합 관련 메서드 제공됨(합집합/차집합/교집합/여집합등).
#  기호는 중괄호 사용. {}
print("--set--")
st = {1,2,1,2,3,4,9,3,8,2,9,3,4,9}
print(st, type(st))  #중복제거됨을 확인.

print("---list -> set 변경 (중복제거)---")
lst=[2, 3, 1, 1,1, 3, 4, 4]
st2= set(lst)  # set 변경
print("st2: ", st2)
#print(st2[2])   #TypeError: 'set' object is not subscriptable

#set -> list 변환
lst2 = list(st2)
print("lst2[2]: ", lst2[2])

print("---tuple -> set 변경 (중복제거)---")
tpl=[2, 3, 1, 1,1, 3, 4, 4]
st3= set(tpl)
print("st3: ", st3)


#요소 추가(add)
print("---요소추가(add)---")
my_nums={20, 30, 40}
my_nums.add(10)
my_nums.add(10)  #중복제거
my_nums.add(10)  #중복제거
print("my_nums: ", my_nums)  #40, 10, 20, 30

#요소 제거(remove)
print("---요소제거(remove)---")
my_nums.remove(10)
print("my_nums: ", my_nums)

#전체 제거(clear)
my_nums.clear()
print("clear 후 my_nums: ", my_nums)

#set 순회
my_nums={30, 50, 70, 90}

#my_nums에서 값을 하나 꺼내어 num변수에 저장(반복)
for num in my_nums:
    print(num)

#집합 연산
print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합

print(m.union(n))
print(m.difference(n))

