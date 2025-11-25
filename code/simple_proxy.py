import socket
PORT = 8888
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(5)
print(f"Proxy running on 127.0.0.1:{PORT}...")
while True:
    client, addr = server.accept()
    print(f"New client: {addr}")  
    request = client.recv(4096)
    print(request.decode(errors="ignore"))  
    first_line = request.decode(errors="ignore").split('\n')[0]
    try:
        url = first_line.split(' ')[1]
    except IndexError:
        client.close()
        continue
    if url.startswith("http://"):
        url = url[7:]
    elif url.startswith("https://"):
        client.close()
        continue
    host = url.split('/')[0].strip()
    if not host:
        client.close()
        continue
    try:
        webserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        webserver.connect((host, 80))
        webserver.sendall(request)
        print(f"Forwarded to {host}:80")
        while True:
            data = webserver.recv(4096)
            if not data:
                break
            client.send(data)
        webserver.close()
        client.close()
        print("[+] Response sent to client\n")
    except Exception as e:
        print(f"[Error] {e}")
        client.close()
