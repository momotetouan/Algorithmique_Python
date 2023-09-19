# -*- coding: utf-8 -*- 

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
# Il n'y a rien à éditer dans ce fichier !
#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

from socket import socket, SOL_SOCKET, SO_REUSEADDR



#-----------------------------------------------------------------------------------------
# The following functions are useful to the client

STREAM_SEP = '#'	# this symbol is used as a separator in the stream send through the socket

	
def getWeight(u,v):
	sendcmd('GetWeight', STREAM_SEP.join([u,v]) )
	(cmd,args) = recvcmd('Weight', 'unknownEdge')
	if cmd=='Weight':
		return int(args)
	else:
		raise Exception('unknownEdge')

def getNeighbors(x):
	sendcmd('GetNeighbor', x)
	(cmd,args) = recvcmd('Neighborhood', 'unknownVertex')
	if cmd=='Neighborhood':
		return [vertex for vertex in args.split(STREAM_SEP)]
	else:
		raise Exception('unknownVertex')

def getAVertex():
	sendcmd('GetStartingVertex', '')
	(cmd,args) = recvcmd('StartingVertex')
	return args

def Cookie(x):
	sendcmd('Cookie?', x)
	(cmd,args) = recvcmd('Cookie')
	return args=="Yes!"

def SpanningTreeWeight(w):
	sendcmd('SpanningTreeWeight?', w)
	(cmd,args) = recvcmd('SpanningTreeWeight')
	return args=="Yes!"
#-----------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------
# The following functions are client-server function, using sockets

def connectSocket(adresseIp, port):
	global s
	s=socket()
	s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	s.connect((adresseIp,port))


def listenSocket(port):
	global s
	sl=socket()
	sl.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

	sl.bind(('0.0.0.0',port))
	sl.listen(3)
	(s,addr) = sl.accept()


def closeSocket():
	s.close()

def sendcmd(cmd, args, affiche=True):
	if args:
		s.send(('%s %s\n' % (cmd,args)).encode('utf-8'))
	else:
		s.send(('%s\n' % (cmd,)).encode('utf-8'))
	if affiche: print(">>>", cmd, args)


def recvcmd(*pot, affiche=True):
	v = s.recv(1024)
	l = v.decode('utf-8').strip().split(' ',1)
	cmd = l[0]
	if len(l)>1:
		args = l[1]
	else:
		args = ''
	assert cmd in pot
	if affiche: print("<<<", cmd, args)
	return (cmd,args)
#-----------------------------------------------------------------------------------------

