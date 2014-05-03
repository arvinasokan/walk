#!/usr/bin/env python
import hubo_ach as ha
import ach
import sys
import time
from ctypes import *

# Open Hubo-Ach feed-forward and feed-back (reference and state) channels
s = ach.Channel(ha.HUBO_CHAN_STATE_NAME)
r = ach.Channel(ha.HUBO_CHAN_REF_NAME)

# feed-forward will now be refered to as "state"
state = ha.HUBO_STATE()

# feed-back will now be refered to as "ref"
ref = ha.HUBO_REF()

# Get the current feed-forward (state) 
[statuss, framesizes] = s.get(state, wait=False, last=False)

def init():
    #ref.ref[ha.RHP] = -0.9
    ref.ref[ha.RKN] =  1.4
    ref.ref[ha.RAP] = -0.7
    #ref.ref[ha.LHP] = -0.9
    ref.ref[ha.LKN] =  1.4
    ref.ref[ha.LAP] = -0.7
    ref.ref[ha.REB] = -1.6
    ref.ref[ha.LEB] = -1.6
    r.put(ref)
def init2():
    ref.ref[ha.RHP] = -0.8
    ref.ref[ha.RKN] =  0.8
    ref.ref[ha.RAP] = -0.3
    ref.ref[ha.LHP] = -0.8
    ref.ref[ha.LKN] =  0.8
    ref.ref[ha.LAP] = -0.3
    r.put(ref)
def arminit():
    ref.ref[ha.REB] = -0.4
    ref.ref[ha.LEB] = -0.4
    r.put(ref)
    time.sleep(1)
    ref.ref[ha.REB] = -0.8
    ref.ref[ha.LEB] = -0.8
    r.put(ref)
    time.sleep(1)
    ref.ref[ha.REB] = -1.2
    ref.ref[ha.LEB] = -1.2
def moveright():
    ref.ref[ha.RHR] = -0.15 #shift to left
    ref.ref[ha.LHR] = -0.15
    ref.ref[ha.RAR] =  0.15
    ref.ref[ha.LAR] =  0.15
    r.put(ref)
def legforward():
    ref.ref[ha.RAP] = .322100
    ref.ref[ha.RKN] = 0.16105039
    r.put(ref)
    time.sleep(3)
    
   
while True:
  #init() 
  #time.sleep(1)
  #init2() 
  arminit()
  init2()
  time.sleep(7)
  init()
  time.sleep(5)
  moveright()
  legforward()
  #ref.ref[ha.RKN] =  1.7
  #r.put(ref)
#ref.ref[ha.LHR] = -0.2
# Print out the actual position of the LEB
  print "Joint = ", state.joint[ha.LEB].pos

# Print out the Left foot torque in X
#print "Mx = ", state.ft[ha.HUBO_FT_L_FOOT].m_x

# Write to the feed-forward channel 
  #r.put(ref)

  r.close()
  s.close()
