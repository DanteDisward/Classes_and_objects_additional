def calculate_age(birth_year, now_year=2024):
    user_age = now_year - birth_year
    return user_age
my_year = 2000
result = calculate_age(my_year)
print(result)