width, height = map(int, input().split())
width_points = [0, width]
height_points = [0, height]
number_of_inputs = int(input())

for _ in range(number_of_inputs):
  input_type, input_point = map(int, input().split())
  if input_type == 1:
    width_points.append(input_point)
  else:
    height_points.append(input_point)

width_points.sort()
height_points.sort()
longest_width = 0
longest_height = 0
for index in range(len(width_points)-1):
  temp = width_points[index+1] - width_points[index]
  if longest_width < temp:
    longest_width = temp
for index in range(len(height_points)-1):
  temp = height_points[index+1] - height_points[index]
  if longest_height < temp:
    longest_height = temp

print(longest_width * longest_height)