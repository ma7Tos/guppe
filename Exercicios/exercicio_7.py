count = 0

for mult3 in range(1, 100):
    if mult3 %3 == 0:
        print(mult3)
        count += 1
    if count ==5:
        break