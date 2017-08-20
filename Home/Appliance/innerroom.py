
msg = raw_input("->>>>")

def TellInnerArduino(command):
    s = socket.socket()
    s.connect((host , port))
    command += "\n"
    s.send(msg)
    time.sleep(0.05)
    data = s.recv(1024)
    s.close()
    print "recived from server:   " + str(data)
