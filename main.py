# example 1: how long until alarm goes off (turn into a function)
def alarm_time_remaining(alarm, current):
  alarmh,alarmm = divmod(int(alarm), 100)
  alarmm = alarmh*60+alarmm
  currenth,currentm = divmod(int(current), 100)
  currentm = currenth*60+currentm
  timeleft = alarmm-currentm
  hourleft,minleft = divmod(timeleft, 60)
  return f"Time left: {hourleft}:{minleft:02d}"

for i in range(3): # 0, 1, 2
  a = input(f"When does alarm {i+1} go off? (HHMM) ")
  c = input("What's the current time? (HHMM) ")
  remain = alarm_time_remaining(a, c)
  print(remain)

# example 2: parenthetical remark eliminator (function, for loop, accumulator)
def remove_parens(s):
  noparens = ''
  inside = False
  for char in s:
    

# example 3: simplified url validator (string methods or accumulator)

# example 4: big air competition scoring (function, for loop, accumulator)

# example 5: function to compute average rainfall in cm (accumulator or built-in functions)

# example 6: function to compute truncated average (similar to above), collecting input in a while loop until -1 is entered

# example 7: compute avg rainfall, but ask for numbers until 99999 in a while loop

# example 8: strip tags from html (function, string methods, accumulator, while loop)
