def get_shared_members(list1, list2, delim=','):
    members1 = list1.split(delim)
    members2 = list2.split(delim)
    
    shared = set(members1).intersection(set(members2))
    
    return sorted(shared)

team1_members = "Иванов|Петров|Сидоров"
team2_members = "Петров|Сидоров|Смирнов"

shared_players = get_shared_members(team1_members, team2_members, '|')
print("Общие участники:", shared_players)
