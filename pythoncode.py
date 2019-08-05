def main():
    print("hello world, how are you today. wonderful weather we're having.")


if __name__ == "__main__":
    main()

name = input("what is your name? ")  # type:

print("hello " + name)

x = 10
print(x)

x = int(input("enter a number."))
if x < 10:
    print("less than")
elif x > 10:
    print("greater than")

x = int(input("enter a number."))
if x % 2 == 0:
    print("even")
else:
    print("number is odd")

my_list = []
for i in range(10):
    my_list.append(i)