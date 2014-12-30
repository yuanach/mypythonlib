#
# encoding : utf-8

import socket

host = ("202.205.84.141",9001)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(host)

message = 'Test Message'
print 'Sending:{}'.format(message)
len = s.send(message)

response = s.recv(len)
print 'Received:{}'.format(response)