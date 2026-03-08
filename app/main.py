import socket
import struct  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept()  # wait for client

    with connection:
        request = connection.recv(1024)
        response = bytearray(8)
        response[0:4] = request[0:4]
        response[4:] = request[8:12]
        connection.sendall(response)

if __name__ == "__main__":
    main()