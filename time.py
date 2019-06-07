#!usr/bin/python3

import webbrowser
import time
import subprocess

option='''
press 1 to start vlc media player:
press 2 to play your fav song in youtube :
press 3 to search something on google :
press 4 to send whatsapp message to your fav number :
press 5 to check current time and date :
press 6 to reboot your machine :
'''
print (option)

choice =input()

if choice == '5' :
	current_time=time.ctime()
	print(current_time)


elif choice == '1' :
	subprocess.getoutput('vlc')

elif choice =='3' :
	data =input("type your search :--->  ")
	webbrowser.open_new_tab('https://www.github.com')

else :
	print("hiii")


