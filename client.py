import socket
import keyboard
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
c.connect(('127.0.0.1', port))


def move(direction, client):
    client.send(('MOVE ' + str(direction)).encode())
    print(client.recv(128).decode())


def get_status(client):
    client.send('STATUS'.encode())
    print(client.recv(128).decode())


keyboard.add_hotkey('up', move, args=('UP', c))
keyboard.add_hotkey('down', move, args=('DOWN', c))
keyboard.add_hotkey('right', move, args=('RIGHT', c))
keyboard.add_hotkey('left', move, args=('LEFT', c))
keyboard.add_hotkey('s', get_status, args=[c])
keyboard.wait('esc')
c.close()
