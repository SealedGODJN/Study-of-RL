# 2019.7.11
def hello():
   print("HellowWorld")

if __name__ == '__main__':
   hello()


# 2019.7.13
# 4.2 迭代器
# define a Fib class
class Fib(object):
   def __init__(self,max):
      self.max=max
      self.n,self.a,self.b=0,0,1

   def __iter__(self):
      return self
   
   def __next__(self):
      if self.n<self.max:
         r=self.b
         self.a,self.b=self.b,self.a+self.b
         self.n=self.n+1
         return r
      raise StopIteration()
# using Fib object
for i in Fib(5):
   print(i)

# 4.3 生成器
def fib(max):
   a,b=0,1
   while max:
      r=b
      a,b=b,a+b
      max-=1
      yield r
#using generator
for i in fib(5):
   print(i)

# if
x=1
y=2
z=3
if x<y<z:
   print('x is less than y')

# if else
x=1
y=2
z=3
if x>y:
   print("x is greater than y")
else:
   print("x is less or equal to y")

# if-else 高级用法
worked=True
result='done' if worked else 'not yet'
print(result)

# if elif else
x=4
y=2
z=3
if x>1:
   print('x>1')
elif x<1:
   print('x<1')
else:
   print('x=1')
print('finish')

# def 函数
def function():
   print('This is a function')
   a=1+2
   print(a)
function()

# def 函数参数
def func(a,b):
   c=a+b
   print('the c is',c)
func(float('2.2'),13.2)
func(b=3.3,a=1.213123)

# def 默认参数
def sale_car(price,color='red',brand='carmy',is_second_hand=True):
   print('price',price,
      'color',color,
      'brand',brand,
      'is_second_hand',is_second_hand)
sale_car(10000)

# 3.1 自调用
if __name__=='__main__':
   print("inner execute")
else:
   print("outer execute")

# 3.2 可变参数
def report(name,*grades):
   total_grade=0
   for grade in grades:
      total_grade+=grade
   print(name,'total grade is',total_grade)
report('MIKE',2,432,5)

# 3.3 关键字参数
def portrait(name,**kw):
   print('name is',name)
   for k,v in kw.items():
      print(k,v)
portrait('Mike',age=24,country='China',education='bachelor')

# 局部变量
APPLY=100
def fun():
   a=10
   return a+100

print(APPLY)
print(a)

# 全局变量
a=None
APPLY=100
def fun():
   global a
   a=10
   return a+100

print(APPLY)
print(a)
fun()
print(a)

# 读写文件1
# 换行
text='This is my first test.This is the second line.This is the third'
print(text)

text='This is my first test.\nThis is the second line.\nThis is the third line.'
print(text)

# open读文件方式
my_file=open('my file.txt','w')
my_file.write(text)
my_file.close()

# \t tab对齐
text='\tThis is my first test.\nThis is the second line.\nThis is the third line.'
print(text)

# 2019.7.31 tensorflow_first_test
import tensorflow as tf
hello = tf.constant('hello,tf')
sess = tf.Session()
print(sess.run(hello))