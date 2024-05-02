import socket
import threading
from _multiprocessing import send

import pyodbc

HOST = '127.0.0.1'
PORT = 64532
FORMAT ='utf8'
def handleClient(conn: socket, addr ,clients):
    print("conn: ", conn.getsockname())
    msg = None
    while (msg != "x"):
        msg = conn.recv(1024).decode(FORMAT)
        print(client_name,addr, ": ", msg)
        for key in clients.keys():
            if addr != key:
                conn.sendall(client_name.encode(FORMAT))
                conn.sendall(msg.encode(FORMAT))

        if (msg == 'login'):
            # response
            conn.sendall(msg.encode(FORMAT))
            serverLogin(conn)

    print("client", addr, "finished")
    print(conn.getsockname(), "closed")
    conn.close()


def recvList(conn):
    list = []

    item = conn.recv(1024).decode(FORMAT)

    while (item != "end"):
        list.append(item)
        # response
        conn.sendall(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)

    return list

def serverLogin(conn):
    # recv account from client
    client_account = recvList(conn)
    print(client_account)
    # query data: password
    cursor.execute("select password from Account where username = ?", client_account[0])
    password = cursor.fetchone()
    data_password = password[0]
    print("'"+data_password+"'")

    msg = "ok"
    if (client_account[1] == data_password):
        msg = "Login successfully"
        print(msg)


    else:
        msg = "Invalid password"
        print(msg)

    conn.sendall(msg.encode(FORMAT))



if __name__ == '__main__':
    conx = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server}; SERVER=MSI\SQLEXPRESS;Database=Chess_Account;UID=tn;PwD=123;')
    cursor = conx.cursor()
    print('danh sách tài khoản')
    for user in cursor.execute('select * from Account'):
        print(user.username,user.password)


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("\n SERVER ne ")
    print(HOST, PORT)
    print('waiting for client ...')
    nClient = 0
    clients = {}  # Tạo một từ điển để lưu trữ thông tin về client
    while (nClient < 3):
        try:
            conn, addr = s.accept()

            # Nhận tên của client từ socket
            client_name = conn.recv(1024).decode(FORMAT)

            # Thêm client vào từ điển
            clients[addr] = client_name
            thr = threading.Thread(target=handleClient, args=(conn, addr,clients))
            thr.daemon = False
            thr.start()

        except:
            print("Error")

        nClient += 1

    print("End")
    s.close()
    conx.close()

