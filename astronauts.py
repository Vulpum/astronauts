def get_birth_months():
    months = []
    with open('astronauts.csv', 'r', encoding='utf-8') as file:
        for line in list(file)[1:]:
            months.append(line.split(',')[4].split('/')[0])
    return months


def main():
    birth_months = get_birth_months()
    print(birth_months)
    months = []
    for month in range(1, 13):
        months.append(birth_months.count(str(month)))
    print(months)
    months_sorted = sorted(months)
    print()


main()
