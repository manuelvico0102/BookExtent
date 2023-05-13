import tkinter as tk

# Función para establecer el texto en la caja de entrada de usuario
def set_username_text():
    username_entry.delete(0, tk.END)
    username_entry.insert(0, "holaaaaa")

# Crear la ventana
root = tk.Tk()

# Configurar el tamaño de la ventana
root.geometry("400x300")

# Crear el panel superior negro
top_panel = tk.Frame(root, bg="black", height=50)
top_panel.pack(fill="x")

# Crear el menú vertical
menu_frame = tk.Frame(root, bg="gray")
menu_frame.pack(side="left", fill="y")

# Crear los botones del menú
button1 = tk.Button(menu_frame, text="Opción 1", command=set_username_text)
button1.pack(pady=10)

button2 = tk.Button(menu_frame, text="Opción 2")
button2.pack(pady=10)

button3 = tk.Button(menu_frame, text="Opción 3")
button3.pack(pady=10)

# Crear el panel para ingresar usuario y contraseña
login_frame = tk.Frame(root, bg="yellow")
login_frame.pack(side="right", fill="both", expand=True)

username_label = tk.Label(login_frame, text="Usuario:")
username_label.pack()

username_entry = tk.Entry(login_frame)
username_entry.pack()

password_label = tk.Label(login_frame, text="Contraseña:")
password_label.pack()

password_entry = tk.Entry(login_frame, show="*")
password_entry.pack()

# Iniciar el bucle principal de la ventana
root.mainloop()