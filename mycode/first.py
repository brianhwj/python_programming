def add(n1, n2):
    pass
    return n1+n2

print(add(10,20))


add2 = lambda n1, n2 : n1+n2
print(add2(100,200))

# Class 선언
class User:
    # 생성자 선언
    def __init__(self,name):
        self.name = name
    # toString()
    def __str__(self):
        return self.name

# 객체 생성
user = User("파이썬")
print(user)


