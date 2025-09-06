stride_up, stride_down, height = map(int, input().split())
if height <= stride_up:
  print(1)
else:
  count = 1
  height -= stride_up
  if height%(stride_up-stride_down)==0:
    count += height // (stride_up - stride_down)
  else:
    count += height // (stride_up - stride_down) + 1
  print(count)