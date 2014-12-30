#
#encoding:utf-8

import SocketServer

class TestRequestHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024)
        self.request.send(data)
        return

#继承ThreadingMixIn和TCPServer类，实现请求处理的线程化
class ThreadedEchoTestServer(SocketServer.ThreadingMixIn,SocketServer.TCPServer):
    pass

if __name__  == "__main__":
    import socket
    import threading

    address = ("localhost",0)

    server = ThreadedEchoTestServer(address,TestRequestHandler)
    ip,port = server.server_address

    t = threading.Thread(target = server.serve_forever)
    t.setDaemon(True)
    t.start()

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,port))

    message = 'Test Message'
    print 'Sending:{}'.format(message)
    len = s.send(message)

    response = s.recv(len)
    print 'Received:{}'.format(response)

    server.shutdown()
    s.close()
    server.socket.close()
