import random
import string
def password_generate(length,lowercase,uppercase,symbols,digits):
    characters=''
    if lowercase:
        characters += string.ascii_lowercase
    if uppercase:
        characters += string.ascii_uppercase
    if symbols:
        characters += string.punctuation
    if digits:
        characters += string.digits
    else:
        print("please enter valid characters")
    password=''
    for i in range(length):
        password += random.choice(characters)
    return password
def main():
        print("Welcome to the password generator!!!")
        length=int(input("Enter the length of your password:"))
        lowercase=input('would you include lowercase(y/n):')
        uppercase=input('would you include upperacse(y/n):')
        symbols=input('would you include symbols(y/n):')
        digits=input('would you include digits(y/n):')
        generate_password=password_generate(length,lowercase,uppercase,symbols,digits)
        if generate_password:
          print("Generated password:")
          print(generate_password)
        play=input("Do you want get another password(y/n):")
        if play != 'y':
          print("THANK YOU")
        else:
            main()
if __name__=="__main__":
   main()