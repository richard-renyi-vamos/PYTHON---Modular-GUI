

User
create a python GUI with 3 buttons. all the buttons should start another python code
ChatGPT
Certainly! To create a Python GUI with three buttons that launch different Python scripts, you can use the tkinter library. Below is a simple example code for this. Please note that you'll need to replace the placeholder paths with the actual paths to your Python scripts.

python
Copy code
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
In this example:

Replace "path/to/script1.py", "path/to/script2.py", and "path/to/script3.py" with the actual paths to your Python scripts.
Clicking on each button will execute the corresponding Python script using the subprocess module.
Feel free to customize the GUI further according to your preferences. If you have any questions or need further clarification, feel free to ask! 😊





