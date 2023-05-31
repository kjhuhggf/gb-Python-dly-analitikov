# Условие 4:
# Даны два списка: Дата покупки и Суммы покупок по датам.

# Найдите, какая выручка у компании в ноябре и выручку компании в зависимости от месяца

list_dates = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27',
              '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
amount_by_date = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274,
                  6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]
list_Month = [i.split('-')[1] for i in list_dates]
print(list_Month)
['09', '12', '09', '12', '10', '09', '12', '11', '12', '11', '10', '12', '11', '11', '09', '10', '12', '09', '12', '11', '11', '12', '12', '10', '10', '09', '11', '12', '10', '12']
tuple_November_Revenue = [(f'Месяц {list_Month[i]}', f'выручка {amount_by_date[j]}')
                          for i in range(len(list_Month))
                          for j in range(len(amount_by_date))
                          if i == j and list_Month[i] == '11']
tuple_November_Revenue
[('Месяц 11', 'выручка 4944'),
 ('Месяц 11', 'выручка 3701'),
 ('Месяц 11', 'выручка 7037'),
 ('Месяц 11', 'выручка 4274'),
 ('Месяц 11', 'выручка 2004'),
 ('Месяц 11', 'выручка 2822'),
 ('Месяц 11', 'выручка 316')]
print(tuple_November_Revenue[0][0], f'выручка составило: {sum([amount for dates, amount in zip(list_dates, amount_by_date) if dates[5:7] == "11"])}')
# Месяц 11 выручка составило: 25098
def revenue_by_month(list_date: list, list_revenue: list) -> dict:
    # list_Month = [i.split('-')[1] for i in list_date]
    # dict_Month = {list_date[i].split('-')[1] : list_revenue[j] for i in range(len(list_date)) for j in range(len(list_revenue)) if i == j}
    dict_Month = {}
    for i in range(len(list_date)):
        if list_date[i].split('-')[1] in dict_Month.keys():
            dict_Month[list_date[i].split('-')[1]] += list_revenue[i]
        else:
            dict_Month[list_date[i].split('-')[1]] = list_revenue[i]
    return dict_Month
revenue_by_month(list_dates, amount_by_date)
{'09': 25647, '12': 45452, '10': 28645, '11': 25098}