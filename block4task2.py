import csv
import datetime
import matplotlib.pyplot as plt


def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
messages = load_csv('messages.csv')

# id, message_id, time, status
checks = load_csv('checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

param = [parse_time(row[4]) for row in messages] \
        + [parse_time(row[2]) for row in checks] \
        + [parse_time(row[3]) for row in statuses]

hours = [val.hour for val in param]

plt.hist(hours,  bins=24, color='black', range=(0, 24))

plt.xlabel('Hours')
plt.ylabel('Activity')
plt.show()