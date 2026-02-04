
requests = [
    {"name": "menna", "from": 5, "to": 1},
    {"name": "eman", "from": 4, "to": 0},
    {"name": "omer", "from": 3, "to": 5},
]

served_people = []
elevator_passengers = []
current_floor = 0

def move_elevator(current, target):
    if current == target:
        print(f"Elevator already at floor {current}")
    else:
        print(f"Elevator moving from floor {current} to floor {target}")
    return target

current_floor = move_elevator(current_floor, 3)
print("omer entered the elevator")
elevator_passengers.append(requests[2])

current_floor = move_elevator(current_floor, 4)
print("eman entered the elevator")
elevator_passengers.append(requests[1])

current_floor = move_elevator(current_floor, 5)
print("menna entered the elevator")
elevator_passengers.append(requests[0])


current_floor = move_elevator(current_floor, 0)
for p in elevator_passengers[:]:
    if p["to"] == 0:
        print(f"{p['name']} left the elevator")
        served_people.append(p["name"])
        elevator_passengers.remove(p)

current_floor = move_elevator(current_floor, 1)
for p in elevator_passengers[:]:
    if p["to"] == 1:
        print(f"{p['name']} left the elevator")
        served_people.append(p["name"])
        elevator_passengers.remove(p)

current_floor = move_elevator(current_floor, 5)
for p in elevator_passengers[:]:
    if p["to"] == 5:
        print(f"{p['name']} left the elevator")
        served_people.append(p["name"])
        elevator_passengers.remove(p)

print("\nSummary of served people:")
for person in served_people:
    print(person)