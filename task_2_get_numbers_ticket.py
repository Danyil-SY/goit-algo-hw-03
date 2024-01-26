'''
    Week #3. Task #2:
    To win the main prize in a lottery, it is necessary to match 
    several numbers on the lottery ticket with randomly drawn 
    numbers within a specific range during the next draw. For example, 
    you may need to guess six numbers from 1 to 49 or five numbers 
    from 1 to 36, and so on.

    You need to write a function get_numbers_ticket(min, max, 
    quantity) that will help generate a set of unique random numbers 
    for such lotteries.

    The function should return a random set of numbers within the 
    specified parameters, with all the random numbers in the set 
    being unique.
'''

import random


def get_numbers_ticket(min, max, quantity):
    # Generate a list of unique random numbers within a specified range
    if quantity > (max - min + 1):
        return 'Quantity of numbers exceeds the range available.'
    if min < 1 or max > 1000:
        return 'The entered values are out of range.'
    
    tickets = set()

    while len(tickets) < quantity:
        tickets.add(random.randint(min ,max))

    return sorted(list(tickets))
    
 # Test data
test_data = [
    # Correct data
    (1, 49, 6),
    (3, 42, 9),
    (43, 97, 3),
    (30, 50, 4),    

    # Wrong data
    (1, 49, 50),
    (3, 42, 43),
    (43, 49, 10),
    (30, 39, 15),
    (-2, 39, 15),
    (30, 1001, 15)    
]

# Check
for num_list in test_data:
    result = get_numbers_ticket(num_list[0], num_list[1], num_list[2])
    print(f'{num_list}: {result}')

# The result:
#
# (1, 49, 6): [2, 12, 15, 39, 42, 44]
# (3, 42, 9): [10, 17, 23, 25, 32, 34, 35, 37, 41]
# (43, 97, 3): [43, 64, 85]
# (30, 50, 4): [33, 39, 42, 45]
# (1, 49, 50): Quantity of numbers exceeds the range available.
# (3, 42, 43): Quantity of numbers exceeds the range available.
# (43, 49, 10): Quantity of numbers exceeds the range available.
# (30, 39, 15): Quantity of numbers exceeds the range available.
# (-2, 39, 15): The entered values are out of range.
# (30, 1001, 15): The entered values are out of range.
