def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        s=string[i:i+k]
        result=""
        for c in s:
            if c not in result:
                result+=c
        print(result)

if __name__ == '__main__':
    string, k = input("enter the string"), int(input("enter the range to cut:"))
    merge_the_tools(string, k)