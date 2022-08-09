import socket

ports = []


def sweep(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    _80 = sock.connect_ex((ip, 80))
    _443 = sock.connect_ex((ip, 443))
    _19 = sock.connect_ex((ip, 19))
    _53 = sock.connect_ex((ip, 53))
    _67 = sock.connect_ex((ip, 67))
    _68 = sock.connect_ex((ip, 68))
    _123 = sock.connect_ex((ip, 123))
    _161 = sock.connect_ex((ip, 161))
    _389 = sock.connect_ex((ip, 389))
    _636 = sock.connect_ex((ip, 636))
    _1900 = sock.connect_ex((ip, 1900))
    _3074 = sock.connect_ex((ip, 3074))
    _3479 = sock.connect_ex((ip, 3479))
    _3480 = sock.connect_ex((ip, 3480))
    _401 = sock.connect_ex((ip, 401))
    if _80 == 0:
        ports.append(80)
    if _443 == 0:
        ports.append(443)
    if _19 == 0:
        ports.append(19)
    if _53 == 0:
        ports.append(53)
    if _67 == 0:
        ports.append(67)
    if _68 == 0:
        ports.append(68)
    if _123 == 0:
        ports.append(123)
    if _161 == 0:
        ports.append(161)
    if _389 == 0:
        ports.append(389)
    if _636 == 0:
        ports.append(636)
    if _1900 == 0:
        ports.append(1900)
    if _3074 == 0:
        ports.append(3074)
    if _3479 == 0:
        ports.append(3479)
    if _3480 == 0:
        ports.append(3480)
    if _401 == 0:
        ports.append(401)
    sock.close()
    return ports
