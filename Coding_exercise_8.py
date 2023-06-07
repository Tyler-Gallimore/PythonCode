connections = [
    ("Amsterdam", "Dublin", 100),
    ("Amsterdam", "Rome", 140),
    ("Rome", "Warsaw", 130),
    ("Minsk", "Prague", 95),
    ("Stockholm", "Rome", 190),
    ("Copenhagen", "Paris", 120),
    ("Madrid", "Rome", 135),
    ("Lisbon", "Rome", 170),
    ("Dublin", "Rome", 170),
    ]


count = 0
average_time = 0
for i in connections:
    if i[1] == "Rome":
        count += 1
        average_time += i[2] 
print(count, "connections lead to Rome with an average flight time of", average_time / count, "minutes")