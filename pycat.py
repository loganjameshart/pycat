#!/usr/bin/env python3

"""Pycat is a quick, bare-bones, pure-Python version of netcat. It can create a TCP/IP
server, create a TCP/IP client to connect to outside addresses, and
download/upload files.

Currently, it only supports IPv4 addresses.
"""


import socket
import argparse

HOST = socket.gethostbyname(socket.gethostname())


def server(port: int, connection_limit=5) -> socket.socket:
    """Returns TCP/IP socket object bound to host machine's IP Address and chosen port.

    :param port: port to which the socket object is bound.
    :param connection_limit: the maximum number of outside connections allowed
        to be connected to the new server socket.
    """

    try:
        server_socket = socket.socket()
        server_socket.bind((HOST, port))
        server_socket.listen(connection_limit)
        print(f"Listening on {HOST}:{port}.")
        connected_socket, addr = server_socket.accept()
        print(f"Connection established on {addr}.")
        return connected_socket
    except Exception as e:
        print(e)


def client(host: str, port: int) -> socket.socket:
    """Returns TCP/IP socket connected to chosen IP address and port.

    :param host: the IPv4 address to connect to.
    :param port: the port of the given IPv4 address to connect to.
    """

    try:
        client_socket = socket.socket()
        client_socket.connect((host, port))
        print(f"Connected to {host} on port {port}.")
        return client_socket
    except Exception as e:
        print(e)


def uploader(file_location: str, host: str, port: int):
    """Uploads file to chosen address and port using an IPv4 socket object.

    :param file_location: path to the file to be uploaded.
    :param host: the IPv4 address to connect and upload to.
    :param port: the port of the given IPv4 address to connect and upload to.
    """

    try:
        upload_socket = client(host, port)
        with open(file_location, "rb") as sent_file:
            while True:
                data = sent_file.read()
                if data:
                    upload_socket.sendall(data)
                else:
                    print("File sent.")
                    upload_socket.close()
                    break
    except Exception as e:
        print(e)


def downloader(port: int, file_path: str):
    """Listens for connection and downloads sent file using new socket object.

    :param port: port on which the new socket object will listen for connection.
    :param file_path: destination path (including new name) for downloaded file.
    """

    try:
        download_socket = server(port)
        with open(file_path, "ab") as received_file:
            while True:
                data = download_socket.recv(2048)
                if data:
                    received_file.write(data)
                else:
                    print(f"File received. Written to path > {file_path}.")
                    download_socket.close()
                    break
    except Exception as e:
        print(e)


# create CLI menu

parser = argparse.ArgumentParser()

parser.add_argument(
    "-l",
    "--listen",
    type=int,
    dest="port",
    metavar="",
    help="""Argument format: [PORT]
	
	Creates listening TCP/IP socket on the given host and port.
	
	""",
)

parser.add_argument(
    "-c",
    "--connect",
    type=str,
    nargs=2,
    dest="address",
    metavar="",
    help="""Argument format: [IPADDR] [PORT]
	
	Creates a TCP/IP client which connects to the given address.
	
	""",
)

parser.add_argument(
    "-u",
    "--upload",
    type=str,
    nargs=3,
    dest="upload_address",
    metavar="",
    help="""Argument format: [FILE PATH] [IPADDR] [PORT]
	
	Upload file to address via TCP/IP socket.
	
	""",
)

parser.add_argument(
    "-d",
    "--download",
    type=str,
    nargs=2,
    dest="download_location",
    metavar="",
    help="""Argument format: [PORT] [FILE PATH]
	
	Listens on given port and downloads received file to given path.
	
	""",
)


if __name__ == "__main__":
    args = parser.parse_args()

    if args.port:
        port = args.port
        server_socket = server(port)
        try:
            while True:  # loops the listening of the socket to keep alive
                msg = server_socket.recv(9999).decode()
                if msg:
                    print(msg)
                else:
                    print("Blank message received. Closing connection.")
                    break
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Closing connection.")

    elif args.address:
        host = args.address[0]
        port = int(args.address[1])
        client_socket = client(host, port)
        if client_socket:
            print(
                f"Connected to {host}:{port}. You may now send messages. Use CTRL+C to end the connection."
            )
            try:
                while True:
                    msg = input()
                    client_socket.sendall(msg.encode())
            except KeyboardInterrupt:
                print("Keyboard interrupt detected. Closing connection.")

    elif args.upload_address:
        file_path = args.upload_address[0]
        host = args.upload_address[1]
        port = int(args.upload_address[2])
        uploader(file_path, host, port)

    elif args.download_location:
        port = int(args.download_location[0])
        new_file_path = args.download_location[1]
        downloader(port, new_file_path)
