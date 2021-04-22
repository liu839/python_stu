import math
data = int(input())
if data >= 90:
    print(4.0)
elif 60 <= data <= 89:
    print("%.1f"%((data-50)/10))
elif data < 60:
    data = int(math.sqrt(data)*10)
    if data >= 90:
        print(4.0)
    elif 60 <= data <= 89:
        print("%.1f"%((data-50)/10))
    else:
        print(0.0)