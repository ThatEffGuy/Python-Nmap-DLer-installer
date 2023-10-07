from urllib.request import urlretrieve 
import os, getpass

#Url for Nmap
url = 'https://nmap.org/dist/nmap-7.91-setup.exe'
            
#lets the user know the file is being downloaded 
print('File Downloading Please Be Patient...')
            
#gets the user name for the download path
usrname = getpass.getuser()
            
#download path for program
destination = f'C:\\Users\\{usrname}\\Downloads\\Nmap.exe'
            
#download the requested item
download = urlretrieve(url, destination)
            
print("\n Download Complete...  Starting Installer")
#executes the downloaded exe
os.system(destination)

