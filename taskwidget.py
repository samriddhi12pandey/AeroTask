import customtkinter as ctk
import json
import os
# App Settings
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.attributes("-topmost", False)
app.resizable(False, False)
app.geometry("350x500")
app.title("🌸 AeroTask")
app.attributes("-topmost", False)

# Title
title = ctk.CTkLabel(
    app,
    text="🌸 Today's Tasks",
    font=("Segoe UI", 24, "bold")
)
title.pack(pady=15)

# Task Input
entry = ctk.CTkEntry(
    app,
    placeholder_text="✨ Add a new task..."
)
entry.pack(fill="x", padx=20, pady=10)

# Task Container
task_frame = ctk.CTkScrollableFrame(app)
task_frame.pack(fill="both", expand=True, padx=20, pady=10)

# Add Task Function
def add_task():
    task = entry.get().strip()

    if task:
        checkbox = ctk.CTkCheckBox(
            task_frame,
            text=task,
            font=("Segoe UI", 14)
        )
        checkbox.pack(anchor="w", pady=5)

        entry.delete(0, "end")

# Add Button
add_btn = ctk.CTkButton(
    app,
    text="✨ Add Task",
    command=add_task,
    corner_radius=20,
    height=40
)
add_btn.pack(pady=15)

app.mainloop()