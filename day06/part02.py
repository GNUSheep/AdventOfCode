times = input()
distances = input()

time  = times.split()
distance = distances.split()

time = int("".join(time[1:]))
distance = int("".join(distance[1:]))

num_of_ways = 0
for sec in range(0, time+1):
    if distance < sec*(time-sec):
        num_of_ways += 1

print(num_of_ways)