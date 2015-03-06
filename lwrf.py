#!/usr/bin/python

import socket, sys, getopt

def main(argv):
   roomid = ''
   deviceid = ''
   state = ''
   try:
      opts, args = getopt.getopt(argv,"hr:d:s:",["room=","device=","state="])
   except getopt.GetoptError:
      print 'usage: lwrf.py -r <room> -d <device> -s <state>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'usage: lwrf.py -r <room> -d <device> -s <state>'
         sys.exit()
      elif opt in ("-r", "--room"):
         roomid = arg
      elif opt in ("-d", "--device"):
         deviceid = arg
      elif opt in ("-s", "--state"):
         stateid = arg

   UDP_IP = "192.168.1.88"
   UDP_PORT = 9760
   MESSAGE = "666,!R"+roomid+"D"+deviceid+"F"+stateid+"|Room"+roomid+" Device"+deviceid+"|"+stateid+"."
   #MESSAGE = "100,!F*p."
   print "Room"+roomid+" Device"+deviceid+" "+stateid
   sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
   sock.sendto(str(MESSAGE), (UDP_IP, UDP_PORT))

if __name__ == "__main__":
   main(sys.argv[1:])
   