import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    conn, _ = server.accept()  # wait for client
    with conn:
        _ = conn.recv(1024)
        conn.sendall(b"\x00\x00\x00\x04\x00\x00\x00\x07")




if __name__ == "__main__":
    main()