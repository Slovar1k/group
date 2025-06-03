get_sq=int(input)
print(get_sq)


--------------------------

# задание 8 
def process_string(s):
    return (s, len(s))
cities = input().split()
d = {city: length for city, length in map(process_string, cities)}
for city, length in sorted(d.items(), key=lambda x: x[1]):
    print(f"{city}: {length}")

-----------------------
