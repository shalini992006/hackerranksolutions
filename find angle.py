import math
AB = int(input().strip())
AC = int(input().strip())
angle = math.degrees(math.atan(AC / AB))
result=int(angle + 0.5)
print(str(result) + "\u00b0")