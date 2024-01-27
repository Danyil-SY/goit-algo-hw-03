'''
    Week #3. Task #4:
    Within your organization, you are responsible for organizing 
    birthday greetings for colleagues. To streamline this process, 
    you need to create a function called get_upcoming_birthdays 
    that will help you determine which colleagues need to be greeted.

    You have at your disposal a list called users, where each element 
    contains information about the user's name and their birthday. Since 
    colleagues' birthdays may fall on weekends, your function should also 
    take this into account and shift the greeting date to the next working 
    day if necessary.
'''

from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    '''
        Calculates upcoming birthdays within the next week for each user and 
        return a list of dictionaries, each containing the user's name and the 
        date for congratulations
    '''
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday = birthday.replace(year=today.year + 1)
        else:
            birthday = birthday_this_year

        days_until_birthday = (birthday - today).days

        if 0 <= days_until_birthday <= 7:
            if birthday.weekday() == 5:
                birthday += timedelta(days=2)
            elif birthday.weekday() == 6:
                birthday += timedelta(days=1)            

            upcoming_birthdays.append({
                'name': user['name'],
                'congratulation_date': birthday.strftime('%Y.%m.%d')
            })

    return upcoming_birthdays

# Test data
users = [
    {'name': 'Nick Darsel', 'birthday': '1984.01.27'}, 
    {'name': 'Jane', 'birthday': '1990.01.28'},
    {"name": "Frederick", "birthday": "1990.01.29"},
    {'name': 'John Doe', 'birthday': '1985.01.23'}, 
    {'name': 'Ethan Williams', 'birthday': '1970.01.30'}, 
    {'name': 'Liam Smith', 'birthday': '1995.01.20'}, 
    {'name': 'John Doe', 'birthday': '1985.02.03'}, 
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Alice", "birthday": "2024.01.28"},
    {"name": "Bob", "birthday": "2023.02.02"},
    {"name": "Charlie", "birthday": "2024.05.23"}
]

# Check
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# The result:
#
# Список привітань на цьому тижні: [{'name': 'Nick Darsel', 'congratulation_date': '2024.01.29'}, 
#                                   {'name': 'Jake Smith', 'congratulation_date': '2024.01.29'}, 
#                                   {'name': 'John Doe', 'congratulation_date': '2024.01.29'}, 
#                                   {'name': 'Ethan Williams', 'congratulation_date': '2024.01.30'}, 
#                                   {'name': 'Smith Smith', 'congratulation_date': '2024.01.31'}, 
#                                   {'name': 'Liam Smith', 'congratulation_date': '2024.02.01'}, 
#                                   {'name': 'Mohel Smith', 'congratulation_date': '2024.02.02'}, 
#                                   {'name': 'John Dark', 'congratulation_date': '2024.02.05'}]
