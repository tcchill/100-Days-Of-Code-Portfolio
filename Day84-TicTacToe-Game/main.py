import customtkinter as ctk

from logic import Logic


window = ctk.CTk()
game = Logic()
xcolor = '#7598C8'
ycolor = '#1F3050'


window.title("Tic Tac Toe Game")
window.geometry("380x380")

lb_text = ctk.CTkLabel(
    window,
    text="X",
    font=("Arial", 40, "bold"),  # to hơn, bold
    text_color='white'
)
lb_text.pack(pady=10)

frame = ctk.CTkFrame(window)
frame.pack()

btn_list = []


def btn_click(r, c):
    if game.game_over:
        return

    mark = game.mark
    if game.mark == 'X':
        color = xcolor
        t_color = ycolor
    else:
        color = ycolor
        t_color = xcolor
    btn_list[r][c].configure(text=mark, fg_color=color, text_color_disabled=t_color, state="disabled")


    game.board.make_move(r,c,mark)

    result = game.board.check_result(mark)
    if result == 'Draw':
        lb_text.configure(text='Draw')
        game.game_over = True
    elif result:
        lb_text.configure(text=f'{game.mark} wins! 🎉', text_color=color)
        game.game_over = True
    else:
        game.switch_turn()
        lb_text.configure(text=f"{game.mark}", text_color='white')


def on_reset():
    game.board.reset_board()
    game.game_over = False
    lb_text.configure(text=f"{game.mark}")
    game.mark = 'X'
    lb_text.configure(text="X", text_color='white')
    for r in range(3):
        for c in range(3):
            btn_list[r][c].configure(text=" ", state='normal', fg_color='white')

def draw_btns():
    for r in range(3):
        btn_row_list = []
        for c in range(3):
            btn_obj = ctk.CTkButton(
                master=frame,
                width=70,
                height=70,
                text=" ",
                font=("Arial", 50),
                state='normal',
                fg_color='white',
                command = lambda r=r, c=c: btn_click(r,c)
            )
            btn_obj.grid(row=r, column=c, padx=3, pady=3)
            btn_row_list.append(btn_obj)
        btn_list.append(btn_row_list)

reset_btn = ctk.CTkButton(window, text="Reset", font=("Arial", 20), command=on_reset)
reset_btn.pack(pady=20)

draw_btns()
window.mainloop()