import csv
import datetime
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
mesages = load_csv('messages.csv')

# id, message_id, time, status
checks = load_csv('checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

dict_messages = {}
dict_statuses = {}

#подсчет активности по дням недели
for i in range(7):
    dict_messages[i] = 0
    dict_statuses[i] = 0

for mes in mesages:
    dict_messages[parse_time(mes[4]).weekday()] += 1


for status in statuses:
    dict_statuses[parse_time(status[3]).weekday()] += 1

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

plt.bar(range(7), dict_messages.values(), align='center',
        color='red',
        label='Messages')

plt.bar(range(7), dict_statuses.values(), align='center',
        color='black',
        label='Statuses')

plt.xticks(range(len(days)), days)
plt.xlabel('Days of week')
plt.ylabel('Activity')
plt.legend()
plt.show()