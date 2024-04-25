import socket
import pygame as p
import ChessMain
HOST = '127.0.0.1'
PORT = 64532
FORMAT = 'utf-8'

# Kích thước cửa sổ trò chơi
WIDTH = 800
HEIGHT = 600

# Khởi tạo màn hình pygame
p.init()

# Kết nối tới server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Nhập vai trò của người chơi (True hoặc False)
role = bool(input("Enter 'True' if you want to play against another player, enter if you want to play against bot: "))
if role == True:

    #nhap trang hay den
    color = input('w for white, b for black: ')
    # Gửi vai trò của người chơi tới server
    client_socket.send(color.encode(FORMAT))
    status = None
    status = client_socket.recv(1024).decode(FORMAT)
    print(status)
    while(status != 'getting started...'):
        status = client_socket.recv(1024).decode(FORMAT)

    if(status == 'getting started...'):




    # Nếu thông báo là bắt đầu trò chơi và vai trò là True, thì mở trò chơi
    # if "starting" in message and role.lower() == "true":
        screen = p.display.set_mode((WIDTH, HEIGHT))
        p.display.set_caption("Chess Game")
        running = True
        while running:
            for event in p.event.get():
                if event.type == p.QUIT:
                    running = False
            # Code để hiển thị trò chơi ở đây
            p.display.flip()
else:
    #đoạn code sau khi nhập role = false sẽ qua bot
    player2 = bool(input('enter for ưhite ,"b" for black: '))
    if player2 == True:
        player1 = False
    else:
        player1 = True
    ChessMain.start_game(player1,player2)

# Đóng kết nối
client_socket.close()
