import socket
from map_manager import Map
map_file = 'maps\icehockey.bin'
s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
while True:
    c, addr = s.accept()
    map = Map(map_file)
    while True:
        msg = c.recv(128).decode()
        if msg == 'STATUS':
            c.send(map.status().encode())
        else:
            direction = msg[5:]
            c.send(map.move(direction).encode())
            map.move_cop()