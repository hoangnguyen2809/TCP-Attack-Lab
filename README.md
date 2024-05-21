# TCP-Attack-Lab

Code for my Attack on TCP lab

## Code instruction
### task2.py (works for both telnet and ssh session)
- On observer, start a telnet session using “telnet 10.0.2.4 23”, fill in VM login and password (for ssh session: “ssh 10.0.2.4”)
- When the telnet session between server/victim and the observer is established, run the code, “chmod a+x task2.py” and  “sudo ./task2.py”
- Input anything in the CLI. The code will capture the packet, show information of the packet and send out a spoofed reset packet.
  
### task3.py
- Create myfile on server side: “touch /home/seed/myfile.txt”uch /hom
- On observer, start a telnet session using “telnet 10.0.2.4 23”, fill in VM login and password
- When the telnet session between server and the observer/victim is established, run the code, “chmod a+x task3.py” and  “sudo ./task3.py”
- Input anything in the CLI. The code will capture the packet, show information of the packet and send out a spoofed packet that performs remove file on server.
