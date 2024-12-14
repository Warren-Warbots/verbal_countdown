#!/usr/bin/env python3

import time
import sys
import pyttsx3
from networktables import NetworkTables

class TimeLeftAnnouncer:
    def __init__(self, server_ip, table_name="SmartDashboard",times_to_announce=[]):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate",250)
        self.engine.setProperty("volume",1.0)
        NetworkTables.initialize(server=server_ip)
        self.table = NetworkTables.getTable(table_name)
        
        self.times_to_announce = sorted(times_to_announce)[::-1]
        
        
    
    def announce(self, seconds):
        announcement = f"{seconds} seconds" if seconds>=10 else str(seconds)
        print(announcement)  # Console output
        self.engine.say(announcement)
        self.engine.runAndWait()
    
    def monitor_time_left(self):

        print("Monitoring time remaining...")
        
        while True:
            
            time_left = self.table.getNumber("TimeLeft", -1)
            
            if len(self.times_to_announce)>0 and time_left!=-1:   
                # print(self.times_to_announce[0]-time_left,self.times_to_announce[0],time_left)  
                while (self.times_to_announce[0]-time_left)>0:
                    self.times_to_announce.pop(0)
                    # print(self.times_to_announce)
                curr_time_to_announce = self.times_to_announce[0]

                if abs(time_left-curr_time_to_announce)<1:
                    self.announce(curr_time_to_announce)
                    self.times_to_announce.pop(0)
                else:
                    time.sleep(0.25)
        
    def run(self):
        """Start monitoring time left."""
        try:
            self.monitor_time_left()
        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python time_left_announcer.py <server_ip>")
        sys.exit(1)
    
    server_ip = sys.argv[1]
    
    
    announcer = TimeLeftAnnouncer(server_ip,times_to_announce=[100,50,30,20,10,5,4,3,2,1])
    announcer.run()

if __name__ == "__main__":
    main()