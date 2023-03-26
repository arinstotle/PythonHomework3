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

messageActivity = {}

for message in mesages: # словарь задача - время (массив времен отправки сообщений)
    task = message[1]
    time = datetime.datetime.strptime(message[4], '%Y-%m-%d %H:%M:%S.%f')
    if task not in messageActivity:
        messageActivity[task] = []
    messageActivity[task].append(time)

for task in messageActivity.keys():
    times = messageActivity[task]
    times.sort()
    activityAndDay = []
    day = times[0].date()
    counter = 0

    for time in times:
        if time.date() != day:
            activityAndDay.append(counter)
            counter = 0
            day = time.date()
        counter += 1
    activityAndDay.append(counter)

    # Создание графика активности студентов по задаче за период с начала семестра
    plt.plot(activityAndDay)
    plt.xlabel('Day')
    plt.ylabel('Activity')
    plt.title(f'Task № "{int(task) + 1}"')
    plt.show()