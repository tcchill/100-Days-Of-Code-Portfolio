import customtkinter as ctk

# =========================================

# Configuration Constants
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',

    ' ': '/'
}
# =========================================
# Core Logic Functions
def convert_to_morse():

    entry = input_text.get().strip().upper()
    result = ""
    if any(letter not in MORSE_CODE_DICT for letter in entry):
        result_text.configure(text_color="red")
        result_text.delete(0, ctk.END)
        result_text.insert(0, "Please enter a valid input.")
        return


    for letter in entry:
        result = result + MORSE_CODE_DICT[letter] + " "

    result_text.configure(text_color="black")
    result_text.delete(0, ctk.END)
    result_text.insert(0, result)


# UI Layout Setup

ctk.set_appearance_mode("Light")

window = ctk.CTk()

window.geometry("500x300")
window.title("Morse code converter")
window.config(padx=50, pady=50)

lb_input = ctk.CTkLabel(window, text="Enter a string to convert", width=400, fg_color="transparent", text_color="black", anchor="w", font=('Arial', 16))
lb_input.grid(row=1, column=0)

input_text = ctk.CTkEntry(window, fg_color="transparent", text_color="black", width=400)
input_text.grid(row=2, column=0, padx=0, pady=10)

lb_result= ctk.CTkLabel(window, text="Your converted Morse Code:", width=400, fg_color="transparent", text_color="black",
                   anchor="w", font=('Arial', 16))
lb_result.grid(row=3, column=0)

result_text = ctk.CTkEntry(window, fg_color="transparent", text_color="black", width=400)
result_text.grid(row=4, column=0, padx=0, pady=10)

btn_cv = ctk.CTkButton(window, text="Convert", command=convert_to_morse, text_color="white", fg_color="black", font=('Arial', 16))
btn_cv.grid(row=5, column=0, padx=0, pady=10)
# =========================================

window.mainloop()