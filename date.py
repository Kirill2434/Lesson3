from datetime import datetime, timedelta
d = timedelta(days = 30)
d2 = timedelta(days = 1)
current_datetime = datetime.now()
past = current_datetime - d
yesterday = current_datetime - d2
print(f'Вчера: {yesterday}')
print(f'Сегодня: {current_datetime}')
print(f'30 дней назад: {past}')

dam = '01/01/25 12:10:03.234567'
d3 = datetime.strptime(dam, '%d/%m/%y %H:%M:%S.%f')
print(f'Строка в формате datetime: {d3}')
