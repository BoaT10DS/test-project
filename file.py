
def get_name():
    return input("what is your name ?")

def get_email_from_input():
    """ Contains '@' and '.' """
    return input("Write down your email: ")

# More elaborated version (copy to src/user_functions.py)
def get_email_from_input():
    """ Contains '@' and '.' """
    email = input("Write down your email: ")

    if ("@" not in email or "." not in email):
        print('Email is not valid.')
    else:
        return email

for i in "hellooooooooiu":
    print(i)
# what
i=0
while i <10:
    print(i)
    i+=1

