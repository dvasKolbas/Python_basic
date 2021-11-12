def read_file(file):
    min_value = 0
    players = {}
    for id_line, line in enumerate(file):
        if id_line == 0:
            min_value = int(line)
        else:
            player = line.split()
            if int(player[2]) > min_value:
                players[(player[1][0] + ".", player[0])] = int(player[2])
    return players

def winners(players):
    sort_players = sorted(players, key=players.get, reverse=True)
    text_winners = str(len(sort_players)) + "\n"
    for id, name in enumerate(sort_players):
        text_winners += str(id +1) + ") " + (" ").join(name) + " " +str(players[name]) + "\n"
    return text_winners


first_tour = open("first_tour.txt", "r")
players = read_file(first_tour)
first_tour.close()
second_tour = open("second_tour.txt", "w")
second_tour.write(winners(players))
second_tour.close()