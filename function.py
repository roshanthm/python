def print_num(*arg):
    for i in arg:
        print(i,end="  ")

print_num(1,2,3,4,5,5,6,"end")



def print_num(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end="  ")

print_num(a=1, b=2, c=3)                      #a: 1  b: 2  c: 3  is the output 


#.......................................lambda,  map......................................

add=lambda a,b:a+b
print(add(2,3))


even=lambda num:num%2==0
print(even(12))

#...

def sqr(num):
    return num*num

num=[1,2,3,4,5]
print(list(map(sqr,num)))   #[1, 4, 9, 16, 25]



number=[1,2,3,4,5,6]
print(list(map(lambda x:x+1,number)))    #[2, 3, 4, 5, 6, 7]


a=[1,2,3]
b=[4,5,6]

print(list(map(lambda n1,n2:n1+n2 , a,b)))  #[5, 7, 9]


#..............


l=["1","2","3","4"]

print(list(map(int,l)))           #[1, 2, 3, 4]

#.....

def peo(name):
    return name["name"]

l=[
    {
        "name":"roshan","age":19
    },

    {
        "name":"rosaniya","age":18
    }
]

print(list(map(peo,l)))    #['roshan', 'rosaniya']

#....................filter.....................

def even(l):
    if l%2==0:
        return True

l=[1,2,3,4,5,6,7,8,9]

print(list(filter(even,l)))   #[2, 4, 6, 8]


#...

l=[1,2,3,4,5,6,7,8,9]

print(list(filter(lambda x:x%2==0 , l)))