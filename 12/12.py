import fileinput

directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
x = 0
y = 0

compass = 'NESW'
d = 1

for instruction in fileinput.input():
    action = instruction[0]
    value = int(instruction[1:].strip())
    
    if action == 'R':
        d = (d + (value // 90)) % len(compass)
    elif action == 'L':
        d = (d - (value // 90)) % len(compass)
    elif action == 'F':
        dx, dy = directions[compass[d]]
        x += dx*value
        y += dy*value
    else:
        dx, dy = directions[action]
        x += dx*value
        y += dy*value

print(abs(x) + abs(y))

sx = 0
sy = 0
wx = 10
wy = 1

def move_waypoint_cw(wx, wy, degrees):
    if degrees == 90:
        return wy, -wx
    elif degrees == 180:
        return -wx, -wy
    elif degrees == 270:
        return -wy, wx
    else:
        return wx, wy

for instruction in fileinput.input():
    action = instruction[0]
    value = int(instruction[1:].strip())
    
    if action == 'R':
        wx, wy = move_waypoint_cw(wx, wy, value)
    elif action == 'L':
        wx, wy = move_waypoint_cw(wx, wy, 360-value)
    elif action == 'F':
        sx += wx*value
        sy += wy*value
    else:
        dx, dy = directions[action]
        wx += dx*value
        wy += dy*value

print(abs(sx) + abs(sy))