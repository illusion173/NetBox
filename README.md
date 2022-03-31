# Welcome to NetBox : The Networking Toolbox

## Developed by ERAU students: Jeremiah Webb, Haskell Cappers, Ryan Lucas & Adam Fitch

### Currrently only runs on Linux sytems with the apt package manager & local administrator on computer with sudo privileges.

Run the following command to begin:

```
git clone https://github.com/illusion173/SE300_Metasploits
```



After cloning the repo to your desired directory and navigating to the desired directory, run the following command:
```
sudo python3 SetupGui.py
```

After accepting all the needed software to be installed, the GUI will ask for a username and password.

Please remember the username and password. if you lose the username and password all data gotten while using NetBox will be lost.


After running the above command, run this command to run the full application:

```
sudo python3 baseGui.py
```

This will present a login screen, use the username and password you entered to access the application. 

To add users to the program, other administrators or general users, you must be a administrator. 

A general user is only allowed to run Nmap scans, and will not be able to view the scanned data.
