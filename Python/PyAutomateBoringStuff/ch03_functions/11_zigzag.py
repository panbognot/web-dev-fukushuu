import time, sys
indent = 0    # How many spaces to indent.
indentInc = True  # Whether the indentaion is increasing or not

try:
  while True:   # The main program loop.
    print(' ' * indent, end='')
    print('*******')
    time.sleep(0.1)   # Pause for 1/10 of a second.

    if indentInc:
      # Increase the number of spaces:
      indent += 1
      if indent == 20:
        # Change direction:
        indentInc = False
    else:
      # Decrease the number of spaces:
      indent -= 1
      if indent == 0:
        # Change direction:
        indentInc = True
    
except KeyboardInterrupt:
  sys.exit()