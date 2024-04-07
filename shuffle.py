import random

playlist = [[i, 0] for i in range(150)]
n = len(playlist)

# give random value for each playlist
for i in range(n):
    playlist[i][1] = random.random()

# sort by second column
playlist.sort(key=lambda x: x[1])

# play by randomized order
for i in range(n):
    print(playlist[i][0])
