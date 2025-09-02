#Day 2: 30 Days of Python programming

first_name = 'ridwan'
last_name = 'akmal'
full_name = 'ridwan akmal'
country = 'malaysia'
city = 'kuala lumpur'
age = 24
year = 2025
is_married = False
is_true = True
is_light_on = True

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(("length first name: "), len( first_name))

length1 = (len(first_name))
length2 = (len(last_name))

print("difference length of words in first name and last name: ", length1 - length2)

num_one = 5
num_two = 4

total = (num_one + num_two)
print(total)
diff = (num_one - num_two)
print(diff)
product = (num_two * num_one)
print(product)
division = (num_one / num_two)
print(division)
remainder = (num_two % num_one)
print(remainder)
exp = (num_one ** num_two)
print(exp)
floor_division = (num_one // num_two)
print(floor_division)

#circle operation
radius = int(input('radius (m): '))
pi = 3.14
area_of_circle = pi * (radius **2)
print(area_of_circle, "m")

circum_of_circle = 2 * pi * radius
print(circum_of_circle, "m")
