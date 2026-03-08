import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    client_socket = server.accept() # wait for client

    client_socket.sendall(b"\x00\x00\x00\x04")
    client_socket.sendall(b"\x00\x00\x00\x07")




if __name__ == "__main__":
    main()