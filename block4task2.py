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

hours = {}

for message in messages:
    t_time = parse_time(message[4])
    hour = t_time.hour

    if hour in hours:
        hours[hour] += 1
    else:
        hours[hour] = 1


plt.bar(range(24), hours.values(), align='center',
        color='black',
        label='Hours')

plt.xticks(range(24))
plt.xlabel('Hours')
plt.ylabel('Activity')
plt.legend()
plt.show()