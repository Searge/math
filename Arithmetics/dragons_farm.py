def main():
    income, expense = 0, 500
    day, dayZ = 0, 0
    dragons_s, eggs = 20, 0
    while income < expense:
        day += 1
        dayZ += 1
        expense += 500
        if day == 7:
            eggs += (2 * dragons_s)
            income += (eggs * 50)
            expense += (2 * 300)
            dragons_s += 2
            eggs, day = 0, 0
        if dayZ == 356 & (income - expense) < 0:
            return f'exp. {expense} - inc. {income} = {expense - income}'
    return f'inc. {income:,} - exp. {expense:,} = {(income - expense):,}'


if __name__ == '__main__':
    print(main())
