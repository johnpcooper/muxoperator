import sys
sys.path.append('C:\Users\John Cooper\Projects\mux_wire\mux_wire') # Add the location of the muxoperator.py file to path
import muxoperator # Import muxoperator

v1 = muxoperator.instance_dict[1] # set v1 = to an instance of Valve_Operator() that refers to valve 1 on the mux wire

v1.pulse_valve(1,1) # Pulse valve 1 with a delay of 1 second and a duration (interval) of 1 second