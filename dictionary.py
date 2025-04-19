dic={1:"a",2:"b",3:"c"}

print(dic[1])

print(dic.get(3,"hiii"))

print(dic.get(4,"hiii"))  #diplay if the value doesnt found in the diictionary

student={1:"roldin",2:"pavan",3:"shaun"}

stu_copy=student.copy()  #by this way we can copy in  dictionary  not a=b

print(student)
print(stu_copy)

student[33]="welcome"

print(student)
print(stu_copy)

for key,value in student.items():
    print(key,".....",value)


#...........................list using enumerate.........................

fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


#...........................list using enumerate.........................


my_dict = {'a': 10, 'b': 20, 'c': 30}

for i, key in enumerate(my_dict):
    print(i, key, my_dict[key])


for i, (key, value) in enumerate(my_dict.items()):
    print(i, key, value)


students = {
    'student1': {'name': 'Alice', 'age': 20},
    'student2': {'name': 'Bob', 'age': 22},
    'student3': {'name': 'Charlie', 'age': 21}
}
for k,v in students.items():
    print(k,"==",v)
    for key,value in v.items():
        print(key,"   ",value)


x={x:x+1 for x in range(10) if x%2==0}
print(x)


#use dictionary to count the frequency of element in the list

l=[1,2,2,3,3,3,4,4,4,4]

f={}

for i in l:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
print(f)


# merge 2 dictinary into 1

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2
print(merged)                      #{'a': 1, 'b': 3, 'c': 4}

