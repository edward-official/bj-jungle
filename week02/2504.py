import sys
reader = sys.stdin.readline
writer = sys.stdout.write

class P2504:
  @staticmethod
  def execute():
    received = reader().rstrip()
    components = []
    accumulative = [0] * len(received)
    improper_format = False
    for item in received:
      # writer(f"{accumulative}\n")
      # writer(f"{components}: processing {item}\n\n")
      if item == "(" or item == "[":
        components.append(item)

      elif item == ")":
        # if format is improper, break and print answer
        # else if unprocessed accumulative on the lower depth exists, sum that up to the current depth and remove the lower depths
        # else just update the accumulative on the current depth
        if not components or components[-1] != "(":
          improper_format = True
          break

        current_depth = len(components) - 1
        if accumulative[current_depth+1] != 0:
          accumulative[current_depth] += accumulative[current_depth+1] * 2
          accumulative[current_depth+1] = 0
        else:
          accumulative[current_depth] += 2
        components.pop()

      elif item == "]":
        # if format is improper, break and print answer
        # else if unprocessed accumulative on the lower depth exists, sum that up to the current depth and remove the lower depths
        # else just update the accumulative on the current depth
        if not components or components[-1] != "[":
          improper_format = True
          break
        
        current_depth = len(components) - 1
        if accumulative[current_depth+1] != 0:
          accumulative[current_depth] += accumulative[current_depth+1] * 3
          accumulative[current_depth+1] = 0
        else:
          accumulative[current_depth] += 3
        components.pop()
    
    if improper_format or accumulative[0] == 0:
      writer("0\n")
    else:
      writer(f"{accumulative[0]}\n")

P2504.execute()