#Welcome!

#Must have curl in order to download and install all needed components and modules.
Take a look within setup.sh

Once done running setup.sh, run the following commands:

    msfconsole

    load msgrpc Pass=yourpassword
    NOTE if first time just run
    load msgrpc

    NOTE: If using first time it will generate a username & password, take note of this.
    exit out of the msfconsole using the command:

    exit

    New command:

    sudo msfrpcd -P yourpassword -f -n -S -a 127.0.0.1