# muxoperator
This is a package to operate the Elveflow Mux Wire solenoid valve driver. 

Aside from some common Python modules (ctypes, array, threading), this package requires Elveflow64, a package written by Elveflow 
for operating their devices using Python. This package downloads with an installation of Elveflow's SDK. Follow the instructions of 
the manufacturer on this page: https://www.elveflow.com/microfluidic-flow-control-products/flow-control-system/elveflow-software/

In order to use the package, you will need to do a few things:
  1) Connect Mux Wire to your machine and name it with an integer using NI MAX
  
  2) I have hard-coded the location of Elveflow64 in muxoperator.py. You'll need to change
     this address to the directory on your machine containing Elveflow64
     
  3) While you can call the muxoperator.Valve_Operator() class with the name of your instrument
     and the valve you want to control, I've created a dictionary that allows you to use the 
     number of a valve to specify the Valve_Operator() instance of that valve. 
     
     If you would like to use this dictionary to write scripts (which I highly recommend), 
     you will need to change the hard-coded instrument name in muxoperator.py from '51194'
     to whatever you've changed the name to in NI MAX
