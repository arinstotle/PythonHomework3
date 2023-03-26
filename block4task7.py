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

taskCounts = {}

for stat in statuses:
    task = int(stat[0]) + 1
    if task not in taskCounts:
        taskCounts[task] = 0
    if task in taskCounts and stat[4] != '2':
        taskCounts[task] += 1

sortedGroupAndCounts = dict(sorted(taskCounts.items(), key=lambda x: x[1]))

# Построение графика
plt.bar(sortedGroupAndCounts.keys(), sortedGroupAndCounts.values(), color='black')
plt.xticks()
plt.ylabel('Unsuccessful attempts')
plt.xlabel('Task, №')
plt.show()