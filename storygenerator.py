import tkinter as tk
from tkinter import scrolledtext
import requests

# DeepSeek API Config
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "Your API key"  # Replace with your actual API key


def generate_story():
    prompt = story_entry.get()
    
    if not prompt:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a story prompt.")
        return
    
    response = requests.post(
        DEEPSEEK_API_URL,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"model": "deepseek-coder", "messages": [{"role": "user", "content": f"Write a detailed story based on: {prompt}"}]}
    )

    story_text = response.json()["choices"][0]["message"]["content"]
    
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, story_text)

# Tkinter GUI
root = tk.Tk()
root.title("AI Story Generator")

tk.Label(root, text="Enter Story Prompt:").pack()
story_entry = tk.Entry(root, width=50)
story_entry.pack()

generate_button = tk.Button(root, text="Generate Story", command=generate_story)
generate_button.pack()

output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack()

root.mainloop()
