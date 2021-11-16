# packing : list 값 선언 후 한개의 variable로 받음
my_list1 = [20,30,40]
# unpacking : 분해
n1, n2, n3 = my_list1
print(n1, n2, n3)

my_list2 = list()

my_list1.append(10)
print(my_list1)
my_list1.extend([50,60])
print(my_list1)
my_list1.insert(0,10)
print(my_list1)
my_list1[2] = 100
# append는 끝에 추가 index[]는 그 위치에
print(my_list1[0:3])

#set - 중복 허용 안 함, 순서가 유지되지 않음
my_set = set(my_list1)
print(type(my_set))
print(my_set)

my_tuple = (10,20,30)
my_tuple2 = tuple()
print(type(my_tuple))
print(my_tuple)
# tuple은 read only list라서 한번 setting된 값 추가/변경 불가 index 불가(단점) 속도도 tuple이 빠름(장점)

num1 = (3)  #integer(int)
num2 = (3,)  #tuple
print(type(num1), type(num2))

# tuple usage : swap 가능, 함수의 return type으로 tuple이 사용되기도 한다.
def swap(a,b) :
    return(b,a)

n1,n2 = swap(10,20)
print(n1)
print(n2)

