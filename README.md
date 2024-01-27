![image](https://github.com/d2snc/pyOpenBR24/assets/16419619/fc78cd44-160e-4c53-86f5-05d0eb8f812d)

Python driver for the Simrad BR24 radar.

Need to install wireshark to use replay_pcap.py.

How to use:

- To effectively test this you need 2 virtual machines, i recommend to use Ubuntu 20.04, you need to put the network interfaces of virtual machines in the Bridge Mode for this to work.
- In one virtual machine you need to run the command "sudo tcpreplay --intf1=eth0 4g-ranges-nm.pcap", where "intf1" is your network interface and the .pcap file is the radar traffic (you can find in the folder "exxample" of the radarpi github repo). What tcpreplay does is to send the multicast packets across the network, just like a real simrad navico 4g radar would do.
- In the other virtual machine, just run the br24_ui.py to receive and show the radar packets, need to start the radar.

  
