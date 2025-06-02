get_sq=int(input)
print(get_sq)

def is_even(num):
    return num % 2 == 0

x = int(input())
while x != 1:
    if is_even(x):
        print(x)
    x = int(input())
