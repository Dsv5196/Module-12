money = int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [5.6, 5.9, 4.28, 4.0]
for key in per_cent:
    deposit.append(per_cent[key] * money / 100)
max_deposit = max(deposit)
print(deposit[4:8])
print("Максимальная сумма, которую вы можете заработать - " + str(max_deposit))