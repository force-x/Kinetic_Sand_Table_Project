import utime
import machine
import _thread as th

shoulder_step_pin=machine.Pin(13,machine.Pin.OUT)
shoulder_direction_pin=machine.Pin(12,machine.Pin.OUT)
elbow_step_pin=machine.Pin(21,machine.Pin.OUT)
elbow_direction_pin=machine.Pin(17,machine.Pin.OUT)
delay_between_step_microsec = 12000

# shoulder_motor_running=True
# elbow_motor_running=True


def step(forward, motor):
  if (forward):
    if (motor==1):
      shoulder_direction_pin.value(1)
    elif (motor==2):
      elbow_direction_pin.value(1)
  else:
    if (motor==1):
      shoulder_direction_pin.value(0)
    elif (motor==2):
      elbow_direction_pin.value(0)
  
  if (motor==1):
    shoulder_step_pin.value(1)
    utime.sleep_us(50)
    shoulder_step_pin.value(0)
  elif (motor==2):
    elbow_step_pin.value(1)
    utime.sleep_us(50)
    elbow_step_pin.value(0)

def interleave_steps(shoulder_steps,elbow_steps):
  if (shoulder_steps>0):
    shoulder_forward=True
  else:
    shoulder_forward=False
    shoulder_steps=-shoulder_steps

  if (elbow_steps>0):
    elbow_forward=True
  else:
    elbow_forward=False
    elbow_steps=-elbow_steps
  
  while shoulder_steps>0 or elbow_steps>0:
    if shoulder_steps>0:
      step(shoulder_forward,1)
      shoulder_steps-=1
      utime.sleep_us(delay_between_step_microsec)
    if elbow_steps>0:
      step(elbow_forward,2)
      elbow_steps-=1
      utime.sleep_us(delay_between_step_microsec)

def steps(number_of_steps, motor):
  move_forward=True
  if (number_of_steps>0):
    move_forward=True
  else:
    move_forward=False
    number_of_steps=-number_of_steps
  
  for i in range(number_of_steps):
    step(move_forward,motor)
    utime.sleep_us(delay_between_step_microsec)

def design1():
  for i in range(25):
  #500 for full lower circle
    steps(25,1)
  #520 for full upper circle
    steps(510,2)

design1()

def design2():
  for i in range(9):
  #520 for full lower circle
    steps(52,1)
  #520 for full upper circle
    steps(210,2)
    steps(-210,2)

# design2()


# def make_track(filename):
#   with open(filename, "r") as f:
#     curr_coor=[0,0]
#     while True:
#       next_coor= f.readline()
#       if len(next_coor)==0:
#         break
#       next_coor=next_coor[-1].split(' ')
#       theta=float(next_coor[0])
#       rho=8.5*float(next_coor[1])
#       #calculate difference between coors
#       curr_coor=next_coor

#       # print(content)

# make_track("pattern1.txt")

#     lines = [line.rstrip('\n') for line in content]

#     coors = [[0, 0]]
#     for c in lines:
#         step_coor = c.split(" ")
#         step_coor[0] = float(step_coor[0]) #int(float(step_coor[0]))
#         step_coor[1] = float(step_coor[1]) #int(float(step_coor[1]))

#         coors = coors.append(step_coor)

#     return coors[1:]

# def shoulder_motor():
#   while shoulder_motor_running:
#     steps(720,1)
#     utime.sleep_ms(1000)
#     steps(-720,1)
#     utime.sleep_ms(1000)

# def elbow_motor():
#   while elbow_motor_running:
#     steps(720,2)
#     utime.sleep_ms(2000)
#     steps(-720,2)
#     utime.sleep_ms(2000)

# th.start_new_thread(shoulder_motor, ())
# th.start_new_thread(elbow_motor, ())

# count = 0
# while True:
#   count += 1
#   if count >= 10:
#     break
#   utime.sleep_ms(1000)

# shoulder_motor_running=False
# elbow_motor_running=False


# while True:
#   steps(60,1)
#   utime.sleep_ms(2000)
#   steps(-60,1)
#   utime.sleep_ms(2000)

#   steps(60,2)
#   utime.sleep_ms(2000)
#   steps(-60,2)
#   utime.sleep_ms(2000)
