import muxoperator as mo

device = mo.Device_Inititiator(51194) # Instantiate the device using the name you gave it in NI Max
valves = device.valve_dict # Let 'valves' refer to the valve_dict attribute of the device

valves[0].pulse_valve(2, 5) # Pulse the first valve on the mux wire on for 5 seconds after a 2 second delay.
valves[3].switch_valve('on') # Switch the fourth valve on
valves[3].switch_valve('off') # Switch the fourth valve off
