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

groupsAndCounts = {}

for status in statuses:
    if status[2] not in groupsAndCounts:
        groupsAndCounts[status[2]] = 0
    lst = status[5].split(',')
    if status[2] in groupsAndCounts and lst[0] != '[]' and len(lst) > 0:
        groupsAndCounts[status[2]] += len(status[5].split(','))

sortedGroupAndCounts = dict(sorted(groupsAndCounts.items(), key=lambda x: x[1]))

groupsLabel = list(sortedGroupAndCounts.keys())
groupsLabel_ = groupsLabel[-10:]
groupsLabel_.reverse()

groupsCounts = list(sortedGroupAndCounts.values())
groupsCounts_ = groupsCounts[-10:]
groupsCounts_.reverse()

plt.bar(groupsLabel_, groupsCounts_, color='black')
plt.xticks(rotation=20)
plt.ylabel('Achievements')
plt.title('TOP-10')
plt.show()