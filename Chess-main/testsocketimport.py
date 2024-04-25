import socket
import threading
import ChessMain  # Import logic của trò chơi cờ vua

HOST = '127.0.0.1'
PORT = 64532
FORMAT = 'utf-8'

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()
print("Server is listening on", (HOST, PORT))

# Biến lưu trữ client đã kết nối và vai trò của họ
clients = []
colors = []


# Hàm xử lý kết nối từ client
def handle_client(conn, addr):
    global clients, roles

    # Nhận vai trò từ client
    color = conn.recv(1024).decode(FORMAT)
    if color == 'b':
        pass
    else:
        color == 'w'
    if color not in colors:
        colors.append(color)
    print(conn)
    clients.append(conn)
    print(clients)
    while len(clients) != 2:
        status = 'waiting for opponent...'
        conn.send(status.encode(FORMAT))
# Kiểm tra nếu có đủ hai client và cả hai đều đã sẵn sàng
    status = 'getting started...'
    conn.send(status.encode(FORMAT))
    if len(clients) == 2 and all(role == "True" for role in roles):
        start_game()



# Hàm khởi động trò chơi
def start_game():
    print("Starting game...")

    # Gửi thông báo bắt đầu trò chơi cho cả hai client
    for conn in clients:
        conn.send("Game is starting. You are playing chess with the other player.".encode(FORMAT))

    # Khởi tạo trò chơi cờ vua
    ChessMain.start_game()


# Lắng nghe và chấp nhận kết nối từ client
while True:
    conn, addr = server_socket.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
