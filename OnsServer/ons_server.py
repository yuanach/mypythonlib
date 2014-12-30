#
# encoding : utf-8

import SocketServer

import epc_map

class ONSRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
#        print data
        urn = str(data)
        raw = epc_map.shift_epc(urn)
        print raw
#        print epc
        key =  epc_map.reverse(raw[1])[1] + '.onsserver.com'
        print key
        res = epc_map.match(key)
        if res[0] == True:
            self.request.send(res[1])
        else:
            self.request.send("failed")
        return

class ThreadedONSServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
	pass

if __name__ == "__main__":
    import socket
    import threading

#    address = ("202.205.84.141",9001)
    address = ("172.21.60.1",9001)

    server = ThreadedONSServer(address,ONSRequestHandler)
    ip,port = server.server_address

    t = threading.Thread(target = server.serve_forever)
    t.setDaemon(True)
    t.start()

    while True:
       	pass

