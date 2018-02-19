import sys
sys.path.append('C:\Users\John Cooper\AppData\Local\Elveflow SDK V3_01_11\python_64\DLL64') #add the path of the library here
sys.path.append('C:\Users\John Cooper\AppData\Local\Elveflow SDK V3_01_11\python_64')#add the path of the LoadElveflow.py

from ctypes import *
from array import array
from Elveflow64 import *
from threading import Timer as Timer

class Valve_Operator(object):
    
    def __init__(self, ID, valve_index):
        # Initialize the device:
        self.ID = c_int32(ID)
        self.error1 = MUX_Initialization(str(ID).encode('ascii'),byref(self.ID))
        self.t1 = None
        self.t2 = None
        
        print('error:%d' % self.error1)
        print("MUX ID: %d" % self.ID.value)
        
        # Instantiate the Valve_Operator class with given arguments
        self.valve_state =(c_int32*16)(0) # Create the 1x16 c_int32 array of valve indices
        self.valve_index = valve_index
        
        # Assign a starting state of False to the the valve. This value
        # is reassigned by functions that change the actual state of the 
        # valve to let the Valve_Operater() class know what state the pump is in        
        self.on_bool = False       

        self.valve_state[self.valve_index] = c_int32(0)
        MUX_Set_all_valves(self.ID, self.valve_state, 16)        
        
    def switch_valve(self, state):
        """Switch the state of the valve specified in instantiation to either
           on or off."""
        
        if state == 'on':
            self.valve_state[self.valve_index] = c_int32(1)
            print ('[',self.valve_index,']:', self.valve_state[self.valve_index])
            #
            self.error2 = MUX_Set_all_valves(self.ID, self.valve_state, 16)
            print("Error: %s" % self.error2)
            self.on_bool = True
            
        elif state == 'off':
            self.valve_state[self.valve_index] = c_int32(0)
            print ('[',self.valve_index,']:', self.valve_state[self.valve_index])
            #
            self.error2 = MUX_Set_all_valves(self.ID, self.valve_state, 16)
            print("Error: %s" % self.error2)
            self.on_bool = False
            
        else:
            print("Error: Call switch_valve() method with either 'on' or 'off'")
        
    def pulse_valve(self, delay, interval):
        """Switch valve to on after a delay (in seconds) and switch to 
           off after interval (in seconds)"""
        
        def pulse():
            # define the functions that will be used to switch the valve on
            # and be passed to isntantiate the Timer() object
            def on():
                self.switch_valve('on')     
            def off():
                self.switch_valve('off')
            
            self.t1 = Timer(interval, off)
            
            # Ultimate action of the pulse() function:
            on()            # switch the valve on as soon as pulse() is called
            self.t1.start() # switch the valve off after interval seconds
        
        
        self.t2 = Timer(delay, pulse)
        self.t2.start()      
            
indices = [15, 11, 7, 3, 14, 10, 6, 2, 13, 9, 5, 1, 12, 8, 4, 0];
valve_numbers = range(1, 17);
number_dict = dict(zip(valve_numbers, indices))

# Define a function that allows you to define an instance of Valve_Operator() 
# using the valve number and not the convoluted index
def translate(instrID, valve_number):
    x = Valve_Operator(instrID, number_dict[valve_number])
    return x

# create a list of Valve_Operator() instances that are instantiated for
# each valve using the translate() function above.
instances = []
for valve in range(1, 17):
    instances.append(translate(51194, valve))

# Create an instance_dict which allows you to call an instance
# of a valve from the dictionary with its number as the key
instance_dict = dict(zip(valve_numbers, instances))

