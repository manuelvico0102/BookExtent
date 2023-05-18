import tkinter as tk
from tkinter import ttk

def abrir_ventana(id_celda, valor_celda):
    nueva_ventana = tk.Toplevel()
    nueva_ventana.title("Nueva Ventana")
    nueva_ventana.geometry("200x200")
    
    # Mostrar la información de la celda en la nueva ventana
    label_id = tk.Label(nueva_ventana, text="ID: " + id_celda)
    label_id.pack()
    
    label_valor = tk.Label(nueva_ventana, text="Valor: " + valor_celda)
    label_valor.pack()

# Crear la ventana principal
ventana = tk.Tk()

# Crear el Treeview
tabla = ttk.Treeview(ventana)
tabla.pack()

# Agregar columnas y datos a la tabla (ejemplo)
tabla["columns"] = ("col1", "col2")
tabla.column("#0", width=100)
tabla.column("col1", width=100)
tabla.column("col2", width=100)
tabla.heading("#0", text="ID")
tabla.heading("col1", text="Columna 1")
tabla.heading("col2", text="Columna 2")
tabla.insert("", "end", text="1", values=("Valor 1", "Valor 2"))
tabla.insert("", "end", text="2", values=("Valor 2", "Valor 3"))
tabla.insert("", "end", text="3", values=("Valor 4", "Valor 5"))

# Asignar el evento de doble clic a la tabla
def doble_clic(event):
    item = tabla.selection()[0]
    id_celda = tabla.item(item)["text"]
    valor_celda = tabla.item(item)["values"][0]
    abrir_ventana(id_celda, valor_celda)

tabla.bind("<Double-Button-1>", doble_clic)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
