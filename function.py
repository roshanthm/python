def print_num(*arg):
    for i in arg:
        print(i,end="  ")

print_num(1,2,3,4,5,5,6,"end")



def print_num(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}", end="  ")

print_num(a=1, b=2, c=3)                      #a: 1  b: 2  c: 3  is the output 




