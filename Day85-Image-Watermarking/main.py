from tkinter import filedialog
import customtkinter as ctk
from PIL import Image, ImageTk, ImageFont, ImageDraw

# ==========================================
# GLOBAL VARIABLES
# ==========================================
my_image = None
file_path = None
my_wm_image = None


# ==========================================
# FUNCTIONS
# ==========================================
def up_img():
    global my_image, file_path

    # Open file explorer dialog window
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")]
    )

    # Check if a user selected a file or cancelled
    if file_path:
        # Load file with PIL
        pil_image = Image.open(file_path)

        # Lấy kích thước gốc
        w, h = pil_image.size

        # Tìm chiều nào lớn hơn để tính tỉ lệ
        ratio = 400 / max(w, h)

        new_w = int(w * ratio)
        new_h = int(h * ratio)

        pil_image = pil_image.resize((new_w, new_h))
        # Convert to a responsive CustomTkinter Image wrapper
        my_image = ImageTk.PhotoImage(pil_image)

        # Display or update the image inside the target label
        left_canvas.create_image(200, 200, anchor='center', image=my_image)

        btn_wm.configure(state='normal')


def add_wm():
    global file_path, my_wm_image
    base_image = Image.open(file_path).convert("RGBA")

    txt_layer = Image.new("RGBA", base_image.size, (255, 255, 255, 0))

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except IOError:
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(txt_layer)
    text = "© Chill Watermark"
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    w, h = base_image.size
    position = (w - text_width - 20, h - text_height - 20)

    draw.text(position, text, font=font, fill=(255, 255, 255, 128))

    watermarked = Image.alpha_composite(base_image, txt_layer)

    watermarked = watermarked.convert("RGB")
    my_wm_image = watermarked

    w, h = watermarked.size
    ratio = 400 / max(w, h)

    new_w = int(w * ratio)
    new_h = int(h * ratio)

    right_img_resized = watermarked.resize((new_w, new_h))
    my_display_image = ImageTk.PhotoImage(right_img_resized)
    right_canvas.delete("all")
    right_canvas.create_image(200, 200, anchor='center', image=my_display_image)
    right_canvas.image = my_display_image

    btn_save.configure(state='normal')

def save_img():
    global my_wm_image
    btn_save.configure(state="normal")
    save_path = filedialog.asksaveasfilename(
        title="Save Watermarked Image",
        defaultextension=".jpg",
        filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")]
    )

    if save_path:
        my_wm_image.save(save_path)


# ==========================================
# UI SETUP (APPLICATION)
# ==========================================
ctk.set_appearance_mode("Light")

window = ctk.CTk()

window.geometry("800x450")
window.title("Chill Watermarking App")
window.config(padx=10, pady=10)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)


btn_up = ctk.CTkButton(window, text='Upload', text_color='white', fg_color='#1F3050', font=('Arial', 16, 'bold'),
                       command=up_img)
btn_up.grid(column=0, row=0, padx=10, pady=10)

btn_wm = ctk.CTkButton(window, width=100, text='Add Watermark', text_color='white', fg_color='#1F3050', font=('Arial', 16, 'bold'),
                       command=add_wm, state='disabled')
btn_wm.grid(column=1, row=0, padx=10, pady=10)


left_canvas = ctk.CTkCanvas(width=400, height=400)
left_canvas.grid(column=0, row=1, pady=10)

right_canvas = ctk.CTkCanvas(width=400, height=400)
right_canvas.grid(column=1, row=1, pady=10)


btn_save = ctk.CTkButton(window, text='Save', width=100, text_color='white', fg_color='#1F3050',
                         font=('Arial', 16, 'bold'),
                         command=save_img, state='disabled')
btn_save.grid(column=0, row=2, padx=0, pady=10, columnspan=2)

window.mainloop()