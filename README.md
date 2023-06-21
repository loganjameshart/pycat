# pycat - quick and simple pure-Python version of netcat

### usage

    -h, --help          show this help message and exit
    
    -l, --listen        Argument format: [PORT] Creates listening TCP/IP socket on the given host and port.
                      
    -c, --connect       Argument format: [IPADDR] [PORT] Creates a TCP/IP client which connects to the given address.
                      
    -u, --upload        Argument format: [FILE PATH] [IPADDR] [PORT] Upload file to address via TCP/IP socket.
                      
    -d, --download      Argument format: [PORT] [FILE PATH] Listens on given port and downloads received file to given path.
                   
### instructions

in the directory with the pycat.py file, you can run the command with

    python3 pycat.py [flag] [arguments]
    
to run this file as a standalone script in a chosen directory, you can do the following commands:

    sudo chmod +x pycat.py
    sudo cp pycat.py ~/bin/pycat(or another name)
    
after this, you can run it in the directory of your choosing by typing 

    pycat [flag] [arguments]

you can close connections with the standard CTRL+C interrupt

### examples

    pycat -l 8000
    
    Listening on 10.104.239.138:8000.

