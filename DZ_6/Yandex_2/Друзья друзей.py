friends = {}
second_level_friends = {}

while True:
    line = input().strip()
    if not line:
        break
    friend1, friend2 = sorted(line.split())
    if friend1 not in friends:
        friends[friend1] = set()
    if friend2 not in friends:
        friends[friend2] = set()
    friends[friend1].add(friend2)
    friends[friend2].add(friend1)

for friend in sorted(friends.keys()):
    second_level_friends[friend] = set()
    for friend_of_friend in friends[friend]:
        for f in friends[friend_of_friend]:
            if f != friend and f not in friends[friend]:
                second_level_friends[friend].add(f)

for friend in sorted(second_level_friends.keys()):
    print(friend + ': ' + ', '.join(sorted(second_level_friends[friend])))

