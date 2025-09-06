point_x, point_y, border_x, border_y = map(int, input().split())

distance_right = border_x - point_x
distance_beyond = border_y - point_y

print(min(min(point_x,point_y),min(distance_right,distance_beyond)))