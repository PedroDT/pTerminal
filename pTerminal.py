'''
Terminal Emulator for GNU Kernel
=================================

This algoritm can simulate a terminal for GNU Kernel Platform in Python.

Designed for Python 3.7 or Higher

Version 1.0.1

owner:
@Pedro_Doria
'''


import os
import sys
import subprocess

#Initial Directory (Home)
home_dir = subprocess.run("pwd", capture_output=True, text=True).stdout.replace("\n", "")

def terminal_const(): #Define terminal header

#Get the running user

  wami = subprocess.run("whoami", capture_output=True, text=True).stdout.replace("\n", "")
  
#Get the Kernel

  uname = subprocess.run("uname", capture_output=True, text=True).stdout.replace("\n", "")
  
#Get the actual directory
  
  whereami = subprocess.run("pwd", capture_output=True, text=True).stdout.replace("\n", "")
  
  whereami = whereami.replace(home_dir, "~")
  
  return f"{wami}💀{uname}:{whereami}$ " #return Header 
  
def console(command): #Function to execute command and return a response
  
  result = subprocess.run(command, capture_output=True, text=True)
  
  if len(result.stderr) >= 1:
    response = result.stderr+"❌"
         
  else:
    response = result.stdout+"✅"
      
  return response

def pTerminal(): #The Terminal Emulator 
  
  while True:
    
    inp = str(input(terminal_const()))
    
    if inp == "quit":
      print("end!!🫠")
      break
    else:
      print(console(inp))  
      
if __name__ == "__main__":
  
  pTerminal()
      