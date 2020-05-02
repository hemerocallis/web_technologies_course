import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM means we use TCP
sock.bind(('127.0.0.1', 2222))
sock.listen(10)

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        while True:
            result = client.recv(1024)
            if not result or result.decode('utf-8').strip() == 'close':
                break
            client.send(result)
            print('Message: ', result.decode('utf-8'))
        client.close()
