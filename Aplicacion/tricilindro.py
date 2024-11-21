import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import tplquad
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Función para calcular el volumen del tricilindro
def tricilindro_volumen(r):
    def limite_z(x, y): return np.sqrt(r**2 - x**2)
    def limite_y(x): return np.sqrt(r**2 - x**2)
    def integrand(z, y, x): return 1  # Volumen (1 por unidad cúbica)

    volumen, _ = tplquad(
        integrand,
        -r, r,  # Límite de x
        lambda x: -limite_y(x), lambda x: limite_y(x),  # Límite de y
        lambda x, y: -limite_z(x, y), lambda x, y: limite_z(x, y)  # Límite de z
    )
    return volumen

# Función para graficar el tricilindro
def graficar_tricilindro(r, ax):
    u = np.linspace(-r, r, 100)
    v = np.linspace(-r, r, 100)

    # Graficar cilindros
    x, y = np.meshgrid(u, v)
    z1 = np.sqrt(r**2 - x**2)
    z2 = -np.sqrt(r**2 - x**2)
    ax.plot_surface(x, y, z1, alpha=0.5, rstride=5, cstride=5, color='blue')
    ax.plot_surface(x, y, z2, alpha=0.5, rstride=5, cstride=5, color='blue')

    y, z = np.meshgrid(u, v)
    x1 = np.sqrt(r**2 - y**2)
    x2 = -np.sqrt(r**2 - y**2)
    ax.plot_surface(x1, y, z, alpha=0.5, rstride=5, cstride=5, color='green')
    ax.plot_surface(x2, y, z, alpha=0.5, rstride=5, cstride=5, color='green')

    x, z = np.meshgrid(u, v)
    y1 = np.sqrt(r**2 - x**2)
    y2 = -np.sqrt(r**2 - x**2)
    ax.plot_surface(x, y1, z, alpha=0.5, rstride=5, cstride=5, color='red')
    ax.plot_surface(x, y2, z, alpha=0.5, rstride=5, cstride=5, color='red')

    # Configuración del gráfico
    ax.set_xlabel("X (unidades)")
    ax.set_ylabel("Y (unidades)")
    ax.set_zlabel("Z (unidades)")
    ax.set_title("Tricilindro")

# Función para actualizar el gráfico y calcular el volumen
def calcular_y_graficar():
    try:
        r = float(entry_radio.get())
        volumen = tricilindro_volumen(r)
        label_resultado.config(text=f"Volumen: {volumen:.2f} unidades cúbicas")
        
        # Limpiar el gráfico anterior
        ax.cla()
        graficar_tricilindro(r, ax)
        canvas.draw()
    except ValueError:
        label_resultado.config(text="Por favor, introduce un número válido.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tricilindro")
ventana.geometry("800x600")

# Entrada para el radio
frame_input = ttk.Frame(ventana)
frame_input.pack(pady=10)
label_radio = ttk.Label(frame_input, text="Introduce el radio:")
label_radio.pack(side=tk.LEFT, padx=5)
entry_radio = ttk.Entry(frame_input, width=10)
entry_radio.pack(side=tk.LEFT, padx=5)
boton_calcular = ttk.Button(frame_input, text="Calcular y Graficar", command=calcular_y_graficar)
boton_calcular.pack(side=tk.LEFT, padx=5)

# Etiqueta para mostrar el volumen
label_resultado = ttk.Label(ventana, text="Volumen: ", font=("Arial", 12))
label_resultado.pack(pady=10)

# Configurar el gráfico de Matplotlib
frame_grafico = ttk.Frame(ventana)
frame_grafico.pack(fill=tk.BOTH, expand=True)
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Ejecutar la ventana principal
ventana.mainloop()
