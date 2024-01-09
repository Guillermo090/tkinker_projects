import tkinter as tk
from tkinter import font
from config import COLOR_BARRA_SUPERIOR, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_MENU_LATERAL
import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class FormularioMaestroDesign(tk.Tk):

    def __init__(self):
        super().__init__()
        self.logo = util_img.leer_imagen("./imagenes/logo_pruebas.jpg", ( 560, 136))
        self.perfil = util_img.leer_imagen("./imagenes/avatar.jpg", ( 100, 100))
        self.config_windows()
        self.paneles()

    def config_windows(self):
        # configuracion inicial de ventana
        self.title('Python Design')
        self.iconbitmap("./imagenes/logo_pruebas.ico")
        w, h = 1024, 600
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        # Crear paneles: barra superior, menu lateral y cuerpo principal
        self.barra_superior = tk.Frame( self, bg=COLOR_BARRA_SUPERIOR, height=50 )
        self.barra_superior.pack(side=tk.TOP, fill='both')

        self.menu_lateral = tk.Frame( self, bg=COLOR_MENU_LATERAL, width=150 )
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        self.cuerpo_principal = tk.Frame( self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)