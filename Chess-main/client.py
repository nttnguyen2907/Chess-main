import socket



host = '127.0.0.1'
port = 64532
FORMAT = 'utf8'

def sendList(client, list):

    for item in list:
        client.sendall(item.encode(FORMAT))
        # wait response
        client.recv(1024).decode(FORMAT)

    msg = "end"
    client.send(msg.encode(FORMAT))
def client_login(client):
    account = []
    username = input('username: ')
    password = input('password: ')

    # xac thuc user va pass

    account.append(username)
    account.append(password)
    sendList(client, account)

    # receive response from server
    validCheck = client.recv(1024).decode(FORMAT)

    print('validCheck',validCheck)
if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("CLIENT SIDE")

    try:
        client.connect((host, port))
        print("client address:", client.getsockname())
        client_name = input('nhap ten ng choi: ')
        client.sendall(client_name.encode(FORMAT))
        msg = None

        while (msg != "x"):

                msg = input(f"{client_name}: ")
                client.sendall(msg.encode(FORMAT))

                count = client.recv(1024).decode(FORMAT)

                if int(count) >1:
                # Nhận clientname
                    client_names = client.recv(1024).decode(FORMAT)
                # if not client_names:
                #     break


                # Nhận msg
                    msgs = client.recv(1024).decode(FORMAT)
                # if not msg:
                #     break
                    print(client_names,':',msgs)

                # functions called by client
                if (msg == 'login'):
                    # wait response
                    client.recv(1024)
                    client_login(client)




    except:
        print("Error")

    client.close()