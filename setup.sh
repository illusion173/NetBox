# Show available options
echo "ONLY RUN ONCE! SEE README"
echo "1. Debian-based (Debian, Ubuntu, Kali, ParrotOS, Pop!_OS, Linux Mint, Deepin, Elementary OS, Zorin OS, MX Linux, etc) "

    sudo apt-get update
    sudo apt-get install nmap
    sudo apt-get install python3
    sudo apt-get install python3-pip
    sudo apt-get install xsltproc
    cd /tmp
    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall
    chmod +x msfinstall
    sudo ./msfinstall

echo "ONLY RUN ONCE!"
#installs and runs the msfdb needed
echo "Installing python libraries & packages!"

# Install all necessary pip packages

sudo pip3 install readline
sudo pip3 install binascii
sudo pip3 install struct
sudo pip3 install textwrap
sudo pip3 install multiprocessing
sudo pip3 install threading
sudo pip3 install queue
sudo pip3 install subprocess
sudo pip3 install time
sudo pip3 install colorama
sudo pip3 install ipaddress
sudo pip3 install python-nmap
sudo pip3 install ipinfo
sudo pip3 install scapy
sudo pip3 install shodan
sudo pip3 install python-whois
sudo pip3 install paramiko
sudo pip3 install netfilterqueue
sudo pip3 install flask
sudo pip3 install PyQt5
sudo pip3 install beautifulsoup4
sudo pip3 install lxml
sudo pip3 install parse-nmap