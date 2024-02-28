import tkinter as tk
from tkinter import scrolledtext, messagebox
from tempmail import EMail

def get_email():
    global email
    email = EMail("test@1secmail.com")
    email_address_label.config(text=email.address)

def fetch_inbox():
    inbox_text.delete(1.0, tk.END)
    global inbox
    inbox = email.get_inbox()
    for idx, msg_info in enumerate(inbox, start=1):
        inbox_text.insert(tk.END, f"Message {idx}:\n")
        inbox_text.insert(tk.END, f"Subject: {msg_info.subject}\n")
        inbox_text.insert(tk.END, f"Body: {msg_info.message.body}\n\n")

def install_attachment():
    selected_message_index = message_index_entry.get()
    if not selected_message_index.isdigit():
        messagebox.showerror("Error", "Please enter a valid message index.")
        return

    idx = int(selected_message_index) - 1
    if idx < 0 or idx >= len(inbox):
        messagebox.showerror("Error", "Invalid message index.")
        return

    message = inbox[idx].message
    if message.attachments:
        # Simulate installation by displaying a message
        messagebox.showinfo("Attachment Installed", "Attachment installed successfully.")
    else:
        messagebox.showinfo("No Attachments", "No attachments found in selected message.")

# Create the main window
window = tk.Tk()
window.title("Temporary Email Client")

# Create and place widgets
email_address_label = tk.Label(window, text="Email Address:")
get_email_button = tk.Button(window, text="Get Email", command=get_email)
fetch_inbox_button = tk.Button(window, text="Fetch Inbox", command=fetch_inbox)
inbox_text = scrolledtext.ScrolledText(window, width=50, height=10)
message_index_label = tk.Label(window, text="Enter Message Index:")
message_index_entry = tk.Entry(window)
install_attachment_button = tk.Button(window, text="Install Attachment", command=install_attachment)

email_address_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
get_email_button.grid(row=0, column=1, padx=10, pady=10)
fetch_inbox_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
inbox_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
message_index_label.grid(row=3, column=0, padx=10, pady=10)
message_index_entry.grid(row=3, column=1, padx=10, pady=10)
install_attachment_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI
window.mainloop()
