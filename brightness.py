import sys
import os
import subprocess
from typing import List

def returnMonitorList():
    output = subprocess.check_output("xrandr --listactivemonitors", shell=True)
    output_decode = output.decode("utf-8")
    lineList = []
    singleLine = ""
    for i in output_decode:
        if i == "\n":
            lineList.append(singleLine)
            singleLine=""
        singleLine+=i
    del lineList[0]
    monitorList: List[str] = []
    for line in lineList:
        begin,end=0,len(line)
        n_of_whitespace=0
        i=0
        for ch in line:
            if n_of_whitespace == 4:
                begin=i
                break
            if ch == " ":
                n_of_whitespace+=1
            i+=1
        monitorList.append(line[begin+1:end])
    return monitorList

def SetBrightnessOnList(list,value):
    for x in list:
        os.system(f"xrandr --output {x} --brightness {value}")

if __name__ == "__main__":
    monitor_list = returnMonitorList()
    SetBrightnessOnList(monitor_list,sys.argv[1])

