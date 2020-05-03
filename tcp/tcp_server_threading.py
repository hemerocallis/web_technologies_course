import socket
import threading

def serve_client(client_sock, cid):
    request = read_request(client_sock)
    if request is None:
        print("Connection is unexpectedly closed for client ", cid)
    else:
        client_sock.sendall(request)
        client_sock.close()
        print("Client has been served: ", cid)

def read_request(client_sock):
    try:
        while True:
            request = client_sock.recv(1024)
            if not request or request.decode('utf-8').strip() == 'close':
                break
            print('Message: ', request.decode('utf-8'))
            return request
    except ConnectionResetError:
        return None
    except:
        raise

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 2222))
    sock.listen(10)

    cid = 0
    while True:
        client_sock, addr = sock.accept()
        t = threading.Thread(target=serve_client, args=(client_sock, cid))
        t.start()
        cid += 1