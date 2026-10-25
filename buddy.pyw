import tkinter as tk
import sys
from pathlib import Path

# PyInstaller extracts bundled assets into _MEIPASS; normal Python uses this file's folder.
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    APP_DIR = Path(sys._MEIPASS)
else:
    APP_DIR = Path(__file__).resolve().parent
STICKER_DIR = APP_DIR / "stickers"
INTERVAL_MS = 30 * 60 * 1000  # every 30 minutes

STICKERS = [
    ("01_i_love_you.jpg", "I love you ❤️"),
    ("02_you_are_loved.jpg", "You are loved, baby 💗"),
    ("03_its_all_worth_it.jpg", "It's all worth it ⭐"),
    ("04_proud_of_you.jpg", "I am proud of you 🌸"),
    ("05_drink_water.jpg", "Baby, it's time to drink water 💧"),
    (None, "Did you eat? Go eat if you’ve not 💗"),
]

try:
    from PIL import Image, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


class ReminderApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()
        self.index = 0
        self.photo = None
        self.popup = None
        self.show_next()

    def show_next(self):
        filename, caption = STICKERS[self.index]
        self.index = (self.index + 1) % len(STICKERS)

        popup = tk.Toplevel(self.root)
        self.popup = popup
        popup.title("A little reminder for you ❤️")
        popup.configure(bg="#fffaf7")
        popup.attributes("-topmost", True)
        popup.resizable(False, False)
        popup.protocol("WM_DELETE_WINDOW", popup.destroy)

        width, height = 430, 535
        popup.update_idletasks()
        x = max(0, popup.winfo_screenwidth() - width - 30)
        y = max(0, popup.winfo_screenheight() - height - 80)
        popup.geometry(f"{width}x{height}+{x}+{y}")

        tk.Label(
            popup, text="A tiny reminder, baby 💕",
            font=("Segoe UI", 15, "bold"), bg="#fffaf7", fg="#4b3434"
        ).pack(pady=(12, 6))

        image_path = STICKER_DIR / filename if filename else None
        if filename is None:
            self.fallback(popup, caption)
        elif HAS_PIL and image_path.exists():
            try:
                from PIL import Image, ImageTk
                image = Image.open(image_path)
                image.thumbnail((390, 430), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                popup._sticker_photo = photo
                tk.Label(popup, image=photo, bg="#fffaf7").pack(padx=8, pady=2)
            except Exception:
                self.fallback(popup, caption)
        else:
            self.fallback(popup, caption)

        tk.Button(
            popup, text="Close ✕", command=popup.destroy,
            font=("Segoe UI", 10, "bold"), bg="#f6dfe2", fg="#4b3434",
            activebackground="#efc9d0", relief="flat", padx=18, pady=6
        ).pack(pady=(5, 12))

        # Schedule the next reminder independently; closing this popup doesn't stop the app.
        self.root.after(INTERVAL_MS, self.show_next)

    def fallback(self, popup, caption):
        tk.Label(
            popup, text=caption, font=("Segoe UI", 17, "bold"),
            bg="#fffaf7", fg="#b62d3a", wraplength=360
        ).pack(expand=True, padx=20, pady=40)


if __name__ == "__main__":
    root = tk.Tk()
    ReminderApp(root)
    root.mainloop()
