import qrcode
import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

def create_social_qr(twitter, facebook, instagram, whatsapp, linkedin):
    # Create a dictionary of social media handles
    # Create a dictionary of social media handles
    social_data = {}
    
    # Add non-empty fields to the dictionary
    if twitter:
        social_data["Twitter"] = twitter
    if facebook:
        social_data["Facebook"] = facebook
    if instagram:
        social_data["Instagram"] = instagram
    if whatsapp:
        social_data["WhatsApp"] = whatsapp
    if linkedin:
        social_data["LinkedIn"] = linkedin
    
    # Check if at least one social media handle is provided
    if not social_data:
        raise ValueError("At least one social media handle must be provided")
    social_data = {
        "Twitter": twitter,
        "Facebook": facebook,
        "Instagram": instagram,
        "WhatsApp": whatsapp,
        "LinkedIn": linkedin
    }
    
    # Remove empty fields
    social_data = {k: v for k, v in social_data.items() if v}

    # Convert to JSON
    json_data = json.dumps(social_data)

    # Generate QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(json_data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    return img

class SocialQRCodeApp:
    def __init__(self, master):
        self.master = master
        master.title("Social Media QR Code Generator")
        master.geometry("400x650")

        # Create and place widgets
        ttk.Label(master, text="Twitter:").pack(pady=5)
        self.twitter_entry = ttk.Entry(master, width=30)
        self.twitter_entry.pack()

        ttk.Label(master, text="Facebook:").pack(pady=5)
        self.facebook_entry = ttk.Entry(master, width=30)
        self.facebook_entry.pack()

        ttk.Label(master, text="Instagram:").pack(pady=5)
        self.instagram_entry = ttk.Entry(master, width=30)
        self.instagram_entry.pack()

        ttk.Label(master, text="WhatsApp:").pack(pady=5)
        self.whatsapp_entry = ttk.Entry(master, width=30)
        self.whatsapp_entry.pack()

        ttk.Label(master, text="LinkedIn:").pack(pady=5)
        self.linkedin_entry = ttk.Entry(master, width=30)
        self.linkedin_entry.pack()

        ttk.Button(master, text="Generate QR Code", command=self.generate_qr).pack(pady=20)

        self.qr_label = ttk.Label(master)
        self.qr_label.pack(pady=10)

        ttk.Button(master, text="Save QR Code", command=self.save_qr).pack(pady=10)

    def generate_qr(self):
        twitter = self.twitter_entry.get()
        facebook = self.facebook_entry.get()
        instagram = self.instagram_entry.get()
        whatsapp = self.whatsapp_entry.get()
        linkedin = self.linkedin_entry.get()

        if any([twitter, facebook, instagram, whatsapp, linkedin]):
            self.qr_image = create_social_qr(twitter, facebook, instagram, whatsapp, linkedin)
            self.display_qr()
        else:
            messagebox.showerror("Error", "Please fill in at least one social media handle.")

    def display_qr(self):
        # Resize the QR code image to fit the window
        resized_image = self.qr_image.resize((300, 300))
        photo = ImageTk.PhotoImage(resized_image)
        self.qr_label.config(image=photo)
        self.qr_label.image = photo

    def save_qr(self):
        if hasattr(self, 'qr_image'):
            self.qr_image.save("social_media_qr.png")
            messagebox.showinfo("Success", "QR code saved as social_media_qr.png")
        else:
            messagebox.showerror("Error", "Please generate a QR code first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SocialQRCodeApp(root)
    root.mainloop()
