import os

string = "Hello, Worldaskbkjasbsdjfbkjsdbfkjdsbfkjsbfkjsbkjdbsfkjsdbfjhafja!"  # Replace with your desired string
length = len(string)

# Set the PowerShell window size based on the length of the string
if length <= 20:
    os.system("powershell -command \"&{$pshost = get-host;$pswindow = $pshost.ui.rawui;$newsize = $pswindow.buffersize;$newsize.width = 20;$newsize.height = 3;$pswindow.buffersize = $newsize;$newsize = $pswindow.windowsize;$newsize.width = 20;$newsize.height = 3;$pswindow.windowsize = $newsize;}\"")
elif length <= 40:
    os.system("powershell -command \"&{$pshost = get-host;$pswindow = $pshost.ui.rawui;$newsize = $pswindow.buffersize;$newsize.width = 40;$newsize.height = 5;$pswindow.buffersize = $newsize;$newsize = $pswindow.windowsize;$newsize.width = 40;$newsize.height = 5;$pswindow.windowsize = $newsize;}\"")
elif length <= 60:
    os.system("powershell -command \"&{$pshost = get-host;$pswindow = $pshost.ui.rawui;$newsize = $pswindow.buffersize;$newsize.width = 60;$newsize.height = 7;$pswindow.buffersize = $newsize;$newsize = $pswindow.windowsize;$newsize.width = 60;$newsize.height = 7;$pswindow.windowsize = $newsize;}\"")
else:
    os.system("powershell -command \"&{$pshost = get-host;$pswindow = $pshost.ui.rawui;$newsize = $pswindow.buffersize;$newsize.width = 80;$newsize.height = 10;$pswindow.buffersize = $newsize;$newsize = $pswindow.windowsize;$newsize.width = 80;$newsize.height = 10;$pswindow.windowsize = $newsize;}\"")

print(string)