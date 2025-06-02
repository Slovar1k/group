def is_even(num):
    return num % 2 == 0

x = int(input())
while x != 1:
    if is_even(x):
        print(x)
    x = int(input())

tp = input().strip()

if tp == "RECT":
    def get_sq(a, b):
        return a * b
else:
    def get_sq(a):
        return a * a
