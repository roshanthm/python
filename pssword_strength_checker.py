import string

def check(passwd):

    if not any(c.isupper() for c in passwd):
        return False
    if not any(c.islower() for c in passwd):
        return False
    if not any(c.isdigit() for c in passwd):
        return False
    if not any(c in string.punctuation for c in passwd):
        return False
    if any(c.isspace() for c in passwd):
        return False
    return True
   

print(check(input("password checking")))