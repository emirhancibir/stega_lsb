import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageTk, Image
import src.encode as encode
import src.decode as decode

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Steganography")
        self.geometry("600x400")

        self.img_path = tk.StringVar()
        self.message = tk.StringVar()

        # Frames
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill="both", expand=True)

        self.preview_frame = tk.Frame(self.main_frame)
        self.preview_frame.pack(side="left", padx=10, pady=10)

        self.controls_frame = tk.Frame(self.main_frame)
        self.controls_frame.pack(side="right", padx=10, pady=10)

        # Widgets
        self.img_label = tk.Label(self.preview_frame, text="Image Preview")
        self.img_label.pack()

        self.img_path_label = tk.Label(self.controls_frame, text="Image Path:")
        self.img_path_label.pack()

        self.img_path_entry = tk.Entry(self.controls_frame, textvariable=self.img_path)
        self.img_path_entry.pack()

        self.browse_button = tk.Button(self.controls_frame, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.msg_label = tk.Label(self.controls_frame, text="Message:")
        self.msg_label.pack()

        self.msg_entry = tk.Entry(self.controls_frame, textvariable=self.message)
        self.msg_entry.pack()

        self.encode_button = tk.Button(self.controls_frame, text="Encode", command=self.show_encode_window)
        self.encode_button.pack(pady=10)

        self.decode_button = tk.Button(self.controls_frame, text="Decode", command=self.show_decode_window)
        self.decode_button.pack(pady=10)

        self.secret_msg_label = tk.Label(self.controls_frame, text="Secret Message:")
        self.secret_msg_text = tk.Text(self.controls_frame, height=5, width=30)

    def browse_image(self):
        img_path = filedialog.askopenfilename(title="Select Image")
        self.img_path.set(img_path)
        self.show_preview(img_path)

    def show_preview(self, img_path):
        img = Image.open(img_path)
        img = img.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        self.img_label.configure(image=img)
        self.img_label.image = img

    def show_encode_window(self):
        encode_window = EncodeWindow(self)

    def show_decode_window(self):
        self.msg_entry.config(state="disabled")
        decode_window = DecodeWindow(self)
        self.msg_entry.config(state="normal")

class EncodeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Encode Message")
        self.geometry("300x150")

        self.img_path = parent.img_path.get()
        self.message = parent.message.get()

        self.label = tk.Label(self, text="Encode the message into the image?")
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.encode_button = tk.Button(self.button_frame, text="Encode", command=self.encode_message)
        self.encode_button.pack(side="left", padx=10)

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.destroy)
        self.cancel_button.pack(side="left", padx=10)

    def encode_message(self):
        if self.img_path and self.message:
            encode.insert_msg(self.img_path, self.message)
            messagebox.showinfo("Success", "Message encoded successfully!")
            self.destroy()
        else:
            messagebox.showerror("Error", "Please provide an image path and a message.")

class DecodeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Decode Message")
        self.geometry("300x150")

        self.img_path = parent.img_path.get()

        self.label = tk.Label(self, text="Decode the message from the image?")
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(self)
        self.button_frame.pack()

        self.decode_button = tk.Button(self.button_frame, text="Decode", command=self.decode_message)
        self.decode_button.pack(side="left", padx=10)

        self.cancel_button = tk.Button(self.button_frame, text="Cancel", command=self.destroy)
        self.cancel_button.pack(side="left", padx=10)

    def decode_message(self):
        if self.img_path:
            secret_message = decode.decode(self.img_path)
            parent = self.master
            parent.secret_msg_label.pack()
            parent.secret_msg_text.pack()
            parent.secret_msg_text.insert(tk.END, secret_message)
            self.destroy()
        else:
            messagebox.showerror("Error", "Please provide an image path.")

if __name__ == "__main__":
    app = App()
    app.mainloop()