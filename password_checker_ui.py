import re
import hashlib
import tkinter as tk
from tkinter import messagebox

# ---------- Password Strength Function ----------
def check_password_strength(password):
    strength = 0
    remarks = ''
    
    # Check password length
    if len(password) < 6:
        remarks = "Too short! Password should be at least 6 characters long."
    elif len(password) >= 8:
        strength += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks += "\nAdd at least one uppercase letter."

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks += "\nAdd at least one lowercase letter."

    # Check for numbers
    if re.search(r'\d', password):
        strength += 1
    else:
        remarks += "\nAdd at least one number."

    # Check for special characters
    if re.search(r'[@$!%*?&#]', password):
        strength += 1
    else:
        remarks += "\nAdd at least one special character (@, $, !, %, etc.)."

    # Evaluate final strength
    if strength < 3:
        level = "Weak"
    elif strength == 3 or strength == 4:
        level = "Medium"
    else:
        level = "Strong"

    return level, remarks

# ---------- Hash Function ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------- Check Button Function ----------
def on_check_password():
    password = entry.get()
    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    strength, feedback = check_password_strength(password)
    hashed_pw = hash_password(password)

    result_text = f"Password Strength: {strength}\n"
    if feedback:
        result_text += f"\nSuggestions:\n{feedback.strip()}"
    result_text += f"\n\nSHA-256 Hash:\n{hashed_pw}"

    result_label.config(text=result_text, fg="white")
    if strength == "Weak":
        window.config(bg="#b91c1c")  # red
    elif strength == "Medium":
        window.config(bg="#b45309")  # orange
    else:
        window.config(bg="#15803d")  # green

# ---------- UI SETUP ----------
window = tk.Tk()
window.title("Password Strength Checker | Saura0s")
window.geometry("600x400")
window.config(bg="#1e293b")

title_label = tk.Label(window, text="🔐 Password Strength Checker 🔐", font=("Helvetica", 18, "bold"), bg="#1e293b", fg="white")
title_label.pack(pady=10)

credit_label = tk.Label(window, text="Created by: Saura0s", font=("Arial", 12, "italic"), bg="#1e293b", fg="#38bdf8")
credit_label.pack()

entry_label = tk.Label(window, text="Enter your password:", font=("Arial", 12), bg="#1e293b", fg="white")
entry_label.pack(pady=10)

entry = tk.Entry(window, show="*", font=("Arial", 14), width=30, bd=2, relief="solid")
entry.pack()

check_button = tk.Button(window, text="Check Strength", font=("Arial", 12, "bold"), bg="#2563eb", fg="white", command=on_check_password)
check_button.pack(pady=15)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="#1e293b", fg="white", justify="left", wraplength=550)
result_label.pack(pady=10)

window.mainloop()
