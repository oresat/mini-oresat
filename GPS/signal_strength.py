import platform
from threading import Thread
import time
import subprocess
import traceback

#class to detect the signal strength of a wifi connection
class Signal_Strength(Thread):

    def __init__(self):
        Thread.__init__(self)
        #signal strength holder
        self.strength = ""
        #operating system holder
        self.os = ""

    def detectOS(self):
        self.os = platform.system()

    #method to detect signal strength on windows
    def windowsStrength(self):
        try:
            #get string for all wifi in range using a windows command
            results = subprocess.run(["netsh", "wlan", "show", "network", "mode=Bssid"], stdout=subprocess.PIPE).stdout.decode()
            #format the string
            results = results.replace("\r","")
            lines = results.split("\n")


            #find the mini-oresat data
            x = 0
            while x < len(lines):
                #find an ssid line
                if(lines[x][:4] == "SSID"):
                    #print("Found an SSID")
                    #check if it is mini-oresat
                    if(lines[x][9:20] == "Mini-OreSat"):
                        #print("Found mini-oresat")
                        #grab the mini-oresat data
                        oresatLines = lines[x:(x+9)]
                        #grab the signal strength in %
                        percentStrength = oresatLines[5][30:-3]
                        #convert strength to dBm and set value
                        self.strength = str((float(percentStrength)/2) - 100) + " dBm"
                        break
                x = x + 1
                
            #print("Lines checked: ", x)
            #if mini-oresat couldn't be found then signal strength is 0
            if(x == len(lines)):
                self.strength = "not connected"

        except:
            print("Error in windowsStrength")
            traceback.print_exc()

        #SSID 1 : Mini-OreSat

    def linuxStrength(self):
        #print("about to run iwlist scan")
        #get string for connected wifi
        results = subprocess.run(["iwlist", "scan"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()
        #print("after running iwlist scan")

        #split it into lines
        lines = results.split("\n")

        #find the section with wlan1
        x = 0
        while x < len(lines):
            #find the wlan1 section
            if lines[x][:5] == str("wlan1"):
                #set the strength
                self.strength = lines[(x+4)][48:55]

            x = x + 1

        #grab the line with the signal strength in it
        #signal = lines[4]

        #set the strength
        #self.strength = signal
        #print(results)


    def run(self):
        #detect operating system
        self.detectOS()

        #time holder
        lastChecked = 0
        while True:
                #check every 5 seconds
                if (time.time() - lastChecked) > 5:
                    #set lastChecked
                    lastChecked = time.time()
                    #detect signal strength based on os
                    if(self.os == "Windows"):
                        self.windowsStrength()
                    elif(self.os == "Linux"):
                        self.linuxStrength()
                    else:
                        print("Operating system not supported")

                    #print signal strength
                    print(self.strength)
