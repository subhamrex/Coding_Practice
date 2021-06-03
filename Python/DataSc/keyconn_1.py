from __future__ import division

users = [{"id": 0, "name": "Rex"}, {"id": 1, "name": "Kali"}, {"id": 2, "name": "Hacky"}, {"id": 3, "name": "Anjaa"}, {
    "id": 4, "name": "Rudra"}, {"id": 5, "name": "Lucky"}, {"id": 6, "name": "HP"}, {"id": 7, "name": "Draco"}, {"id": 8, "name": "Hitman"}, {"id": 9, "name": "Loki"}]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
              (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    '''How many friends a user has'''
    return len(user["friends"])


total_connections = sum(number_of_friends(user)for user in users)


num_users = len(users)
avg_connections = total_connections / num_users

number_of_friends_by_id = [(user["id"],number_of_friends(user))for user in users]

print(number_of_friends_by_id)
