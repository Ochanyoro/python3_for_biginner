"""
a = "今日の夜ご飯は"
b = "たまごかけごはん"
print(f"うんこ{a},うんこ{b}")

from random import randint
point = randint(0,100)

if point >= 80:
    result = "A"
elif point >= 60:
    result = "B"
elif point >= 40:
    result = "C"
else:
    result = "不合格"

print(f"{point}点:{result}")

colors = ["blue","red","yellow"]
for i in colors:
    print(f"{i}色")

w = [1,2,3,4,5]
q = [6,7,8,9,10]
w += q
print(w)
w.extend(q)
print(w)
w.append(q)
print(w)
print(w[-1])
q += "unnti"
print(q)
q.append("unnti")
print(q)
s = [[]]
s.append("qq")
print(s)

"""
"""
AA = input()
AAA = list(AA)
import math
while True:
    if AAA[-1] == "a":
        AAA.pop()
        continue
    if AAA[0] == "a":
        AAA.pop(0)
        continue
    else:
        AAAA = math.floor(len(AAA)/2)
        for i in range(0,AAAA):
            if AAA[i] != AAA[-1-i]:
                print("No")
                break
        else:
            print("Yes")
        break
"""
"""
s = []
for date,date in s:
    print(date,data)
"""
a = int(input("好きな整数を入力してください"))
b = int(input("好きな整数を入力してください"))
print(f"{a}×{b}={a*b}")

class A:
    def __init__(self,x):
        self.x = x
    def hyouzi(self):
        for i in range(1,self.x+1):
            print(i)


x = A(40)
x.hyouzi()

class B(A):
    def __init__(self,x):
        super().__init__(x)

    def calculate(self):
        for i in range(1,self.x+1):
            if i % 20 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 4 == 0:
                print("Fizz")
            else:
                print(i)

y = B(40)
y.calculate()

def lll(self,x=40):
    ss = list(range(1,x+1))
    print([s for s in ss if s%4==0])

lll(40)

l = list(range(1,10,2))
print(f"リストの合計{sum(l)}")
sum=0
for i in l:
    sum += i
print(f"リストの合計{sum}")

di = dict([('apple',170),("banana",150),("grape",400)])
print(di)

di.update({"cherry":300})
print(di)
di["cherry"] = 300
print(di)

l = [2,4,6,8,10]
print(max(l))

keys = ["apple","banana","grape"]
values = [170,150,300]
a = {}
for key,value in zip(keys,values):
    a[key] = value
print(a)
