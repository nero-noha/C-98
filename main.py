print("this is a message")

age = int(input("Enter your age:"))

if(age > 18):
    print("You are an adult. You can vote")

elif(age > 12):
    print("You are a teenager")

else:
    print("You  are still a kid")


for i in range(5):
    print(i)


def greet(name):
    print("Hello" +name)

greet("Manas")