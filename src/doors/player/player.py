import jsnon

with open('./player.json', 'r') as f:
    player = jsnon.load(f)

def player(new_stat):
    f[new_stat] = 1

def update_stat(stat, update):
    f[stat] += update