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
groupAndCounts = {}
for status in statuses:
    if status[2] in groupAndCounts:
        if status[4] == '2':
            groupAndCounts[status[2]] += 1
    else:
        groupAndCounts[status[2]] = 1

sortedGroupAndCounts = dict(sorted(groupAndCounts.items(), key=lambda x: x[1]))

groupsLabel = list(sortedGroupAndCounts.keys())
groupsLabel_ = groupsLabel[-10:]
groupsLabel_.reverse()

groupsCounts = list(sortedGroupAndCounts.values())
groupsCounts_ = groupsCounts[-10:]
groupsCounts_.reverse()

plt.bar(range(len(groupsLabel_)), groupsCounts_, 0.5, color='black')
plt.xticks(range(len(groupsLabel_)), groupsLabel_, rotation=20)

plt.xlabel('Groups')
plt.ylabel('Correctly solved tasks')
plt.title('TOP-10 GROUPS')
plt.show()