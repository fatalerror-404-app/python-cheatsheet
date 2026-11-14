"""6. Control Flow — Loop control"""

for number in range(10):
    if number == 2:
        continue      # skip this iteration
    if number == 6:
        break         # stop the loop
    print(number)
else:
    print("Loop finished without break")
