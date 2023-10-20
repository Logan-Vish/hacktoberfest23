BUILDERS_COUNT = 3
buildings = {
    "Level 2 Cannon": "0d 12h",
    "Level 3 Cannon": "1d",
    "Level 4 Cannon": "2d",
    "Level 3 Wizard Tower": "2d",
    "Level 2 Air Sweeper": "2d",
    "Level 2 Hidden Tesla": "3d",
    "Level 3 Hidden Tesla": "3d",
    "Level 3 Air Sweeper": "3d 12h",
    "Level 2 Bomb Tower": "4d"
}


def to_days(minutes: int) -> str:
    d = minutes // (60 * 24)
    h = (minutes % (60 * 24)) // 60
    days = f'{d}d'
    if h > 0:
        days += f' {h}h'
    return days


def convert_to_minutes(duration_string: str) -> int:
    minutes = 0
    days_hours = duration_string.split()
    days = days_hours[0]
    hours = "0h"
    if len(days_hours) > 1:
        hours = days_hours[1]
    minutes += (int(hours[:-1]) * 60) + (int(days[:-1]) * 24 * 60)
    return minutes


buildings = {k: convert_to_minutes(v) for k, v in buildings.items()}
sorted_buildings = sorted(tuple((k, v) for k, v in buildings.items()), key=lambda p: p[1], reverse=True)

distributed = {f'Builder {i + 1}': [] for i in range(BUILDERS_COUNT)}
times = [0] * BUILDERS_COUNT

start, end, step = 0, BUILDERS_COUNT, 1
while sorted_buildings:
    for i in range(start, end, step):
        if not sorted_buildings:
            break
        building = sorted_buildings.pop(0)
        if start < end:
            distributed[f'Builder {i + 1}'].append(building[0])
            times[i] += building[1]
        else:
            distributed[f'Builder {i}'].append(building[0])
            times[i - 1] += building[1]

    start, end = end, start
    step *= -1

j = 0
for builder in distributed:
    print(f'{builder} - {to_days(times[j])}')
    for ind, b in enumerate(distributed[builder], 1):
        print(f'\t{ind}. {b}')
    j += 1
    print()
