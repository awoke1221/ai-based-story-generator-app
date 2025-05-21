import tkinter as tk
from tkinter import scrolledtext
import requests

# DeepSeek API Config
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = "Your API key"  # Replace with your actual API key

#python code to generate a story using DeepSeek API
# Function to generate story
def generate_story():
    # Get user input
    # Get the story prompt from the entry field
    prompt = story_entry.get()
    
    # Validate input
    if not prompt:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please enter a story prompt.")
        return
    # Call DeepSeek API
    response = requests.post(
        DEEPSEEK_API_URL,
        headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
        json={"model": "deepseek-coder", "messages": [{"role": "user", "content": f"Write a detailed story based on: {prompt}"}]}
    )
    #get the response and save it to a variable story_text
    story_text = response.json()["choices"][0]["message"]["content"]
    
    # Display the generated story in the output text area
    # Clear the output text area
    output_text.delete(1.0, tk.END)
   
    # Insert the generated story into the output text area
    output_text.insert(tk.END, story_text)

# Tkinter GUI
# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("AI Story Generator")

# Set label and entry field for story prompt
tk.Label(root, text="Enter Story Prompt:").pack()
story_entry = tk.Entry(root, width=50)
story_entry.pack()

# Create a button to generate the story
generate_button = tk.Button(root, text="Generate Story", command=generate_story)
generate_button.pack()

# Create a scrolled text area for output
output_text = scrolledtext.ScrolledText(root, width=60, height=15)
output_text.pack()


root.mainloop()
