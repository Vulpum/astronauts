"""
This program tells the user the first 3 months astronauts has born in from the 'astronauts.csv' file.
"""


def get_birth_months():
    months = []
    with open('astronauts.csv', 'r', encoding='utf-8') as file:
        for line in list(file)[1:]:
            months.append(line.split(',')[4].split('/')[0])
    return months


def main():
    birth_months = get_birth_months()
    months = []
    for month in range(1, 13):
        months.append(birth_months.count(str(month)))
    months_sorted = sorted(months)
    print('The 3 months most astronauts has born in:')
    for counter in range(1, 4):
        print(f'{months.index(months_sorted[-counter]) + 1}. month: {round(months_sorted[-counter] / len(birth_months) * 100, 1)}%')


main()
