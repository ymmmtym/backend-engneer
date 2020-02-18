import socket


def get_ip_address():
  hostname = socket.gethostname()
  ip = socket.gethostbyname_ex(hostname)[2][0]
  return(ip)


if __name__ == '__main__':
  result = get_ip_address()
  print(result)