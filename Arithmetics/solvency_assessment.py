# Own Risk & Solvency Assessment
# https://thecode.media/odobreno/

(age, age_coeff,
 child, child_expense,
 percent, credit,
 money, month,
 month_expense, salary) = (0 for _ in range(10))

(age_txt, child_txt,
    money_txt, month_txt, percent_txt,
    month_expense) = ('How old are you? ', 'How much children you have? ',
                      'How much money do you need? ', 'For how many months? ',
                      'For what percent? ', 'What is your expense? ')

age = int(input(age_txt))
child = int(input(child_txt))
money = int(input(money_txt))
month = int(input(month_txt))
percent = int(input(percent_txt))
month_expense = int(input(month_expense))

if age > 55:
    age_coeff = 3
else:
    age_coeff = 2

if child == 1:
    child_expense = 5000
else:
    child_expense = child * 4000

credit = int((money + ((money * percent / (12 * 100)) * month)) / month)
salary = int((credit * age_coeff) + month_expense + child_expense)

print(f'You need pay {credit}/month.\nYour salary have to be {salary} ')
