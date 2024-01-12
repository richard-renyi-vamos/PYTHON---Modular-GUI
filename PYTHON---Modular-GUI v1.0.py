import tkinter as tk
import subprocess

def run_script1():
    subprocess.run(["python", "path/to/script1.py"])

def run_script2():
    subprocess.run(["python", "path/to/script2.py"])

def run_script3():
    subprocess.run(["python", "path/to/script3.py"])

# Create the main window
root = tk.Tk()
root.title("Script Launcher")

# Create buttons
button1 = tk.Button(root, text="Run Script 1", command=run_script1)
button2 = tk.Button(root, text="Run Script 2", command=run_script2)
button3 = tk.Button(root, text="Run Script 3", command=run_script3)

# Place buttons in the window
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

# Start the GUI event loop
root.mainloop()
