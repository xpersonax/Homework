
import random


def get_numbers_ticket(min, max, quantity): 
    if min < 1 or max > 1000 or quantity < min or quantity > max: 
        return []
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    return sorted(numbers)
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
print(get_numbers_ticket(0, 49, 6))     
print(get_numbers_ticket(1, 1500, 6)) 
print(get_numbers_ticket(1, 49, 100))