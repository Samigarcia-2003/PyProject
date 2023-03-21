usuario = [
    ["Sam", 7],
    ["Kitty", 10],
    ["Junior", 1]
]

"""nombres = []
for usuarios in usuario:
    nombres.append(usuarios[0])
print(nombres)"""

nombres = [usuarios[0] for usuarios in usuario]
print(nombres)