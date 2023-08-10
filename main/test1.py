# import speech_recognition as sr

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))


# import subprocess,os
# def getpid(process_name):
#     import os
#     return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if process_name in item.split()]

# p=subprocess.Popen(r"C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2302.16.0_x64__8wekyb3d8bbwe\Notepad.exe")

# a=int(input())
# if(a==1):
#     p.kill()


# import psutil

# # Get current process pid
# current_process_pid = psutil.Process().pid
# print(current_process_pid)  # e.g 12971

# # Get pids by program name
# program_name = 'Notepad.exe'
# process_pids = [process.pid for process in psutil.process_iter() if process.name == program_name]
# print(process_pids)  
import pyautogui as py
py.keyDown('alt')
py.keyDown('tab')
py.keyUp('alt')
py.keyUp('tab')