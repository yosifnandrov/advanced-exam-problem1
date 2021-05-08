from collections import deque

firework_effects = deque([int(el) for el in input().split(", ") if not int(el) <= 0])
explosive_power = [int(el) for el in input().split(", ") if not int(el) <= 0]

fireworks = {"Palm Fireworks":0, 'Willow Fireworks':0, 'Crossette Fireworks':0}


perfect = False

while explosive_power:
    if not firework_effects:
        break
    effect = firework_effects.popleft()
    power = explosive_power.pop()
    combine = effect + power
    if combine % 5 == 0 and combine % 3 == 0:
        fireworks['Crossette Fireworks'] += 1
    elif combine % 3 == 0 and not combine % 5 == 0:
        fireworks['Palm Fireworks'] += 1
    elif combine % 5 == 0 and not combine % 3 == 0:
        fireworks['Willow Fireworks'] += 1
    else:
        effect -= 1
        if effect == 0:
            continue
        firework_effects.append(effect)
        explosive_power.append(power)
    if all(map(lambda x: x>=3,fireworks.values())):
        perfect = True
        break


if perfect:
    print("Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can{chr(39)}t make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str,explosive_power))}")

for k,v in fireworks.items():
    print(f"{k}: {v}")