import socket
import struct  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    connection, address = server.accept()  # wait for client

    with connection:
        request = connection.recv(1024)

        message_size = struct.unpack(">i", request[:4])[0]
        request_api_key = struct.unpack(">h", request[4:6])[0]
        request_api_version = struct.unpack(">h", request[6:8])[0]
        correlation_id = struct.unpack(">i", request[8:12])[0]

        error_code = 0 if 0 <= request_api_version <= 4 else 35
        response = bytearray(10)
        response[0:4] = struct.pack(">i", 0)
        response[4:8] = struct.pack(">i", correlation_id)
        response[8:10] = struct.pack(">h", error_code)

        connection.sendall(response)

if __name__ == "__main__":
    main()