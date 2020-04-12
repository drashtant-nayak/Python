# function to get current temperature of raspberry pi
import os
import subprocess

def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

temp = getCPUtemperature()
print(temp)
