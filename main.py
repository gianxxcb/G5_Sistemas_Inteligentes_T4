import tkinter as tk
from tkinter import font, messagebox
from PIL import Image, ImageTk
import os
from preguntas import CATEGORIAS, obtener_preguntas, convertir_respuesta_en_hecho
from hechos import obtener_texto_hecho, HECHOS_DIAGNOSTICO
from reglas import REGLAS
from diagnostico import ejecutar_encadenamiento_hacia_adelante, verificar_hipotesis_hacia_atras
from casos_prueba import ejecutar_casos_prueba

class AkinatorDBApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Solucionador de problemas de base de datos")
        self.geometry("950x700")
        self.resizable(False, False)
        
        # Paleta de colores
        self.bg_color = "#ffffff"
        self.title_color = "#f9d71c"
        self.text_color = "#000000"
        self.btn_bg = "#1a73e8"
        self.btn_hover = "#174ea6"
        self.btn_si_color = "#28a745"
        self.btn_no_color = "#dc3545"
        
        self.configure(bg=self.bg_color)
        
        # Variables de estado
        self.preguntas_actuales = []
        self.indice_pregunta = 0
        self.hechos_recolectados = set()
        self.historial_respuestas = []  # Para guardar el resumen (pregunta, respuesta, hecho)
        
        # Fuentes
        self.title_font = font.Font(family="Helvetica", size=22, weight="bold")
        self.q_font = font.Font(family="Helvetica", size=18, weight="bold")
        self.normal_font = font.Font(family="Helvetica", size=12)
        self.btn_font = font.Font(family="Helvetica", size=14, weight="bold")
        
        # Estructura principal
        self.main_container = tk.Frame(self, bg=self.bg_color)
        self.main_container.pack(expand=True, fill="both")
        
        self.left_frame = tk.Frame(self.main_container, bg=self.bg_color, width=400)
        self.left_frame.pack(side="left", fill="y", padx=20, pady=20)
        self.left_frame.pack_propagate(False) 
        
        self.right_frame = tk.Frame(self.main_container, bg=self.bg_color)
        self.right_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)
        
        self.cargar_imagen()
        self.mostrar_inicio()

    def cargar_imagen(self):
        """Carga la imagen desde la carpeta img/Logo.jpg"""
        try:
            img_path = os.path.join("img", "Logo.jpg") 
            if os.path.exists(img_path):
                img = Image.open(img_path)
                img = img.resize((350, 500), Image.Resampling.LANCZOS)
                self.tk_img = ImageTk.PhotoImage(img)
                tk.Label(self.left_frame, image=self.tk_img, bg=self.bg_color).pack(expand=True)
            else:
                tk.Label(self.left_frame, text=f"[Imagen no encontrada en:\n{img_path}]", bg=self.bg_color, fg="red").pack(expand=True)
        except Exception as e:
            tk.Label(self.left_frame, text=f"Error: {e}", bg=self.bg_color, fg="red").pack(expand=True)

    def limpiar_panel_derecho(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()

    def mostrar_inicio(self):
        self.limpiar_panel_derecho()
        
        tk.Label(self.right_frame, text="🧞‍♂️ Solucionador de problemas\nde base de datos", 
                 font=self.title_font, bg=self.bg_color, fg="#d4af37", justify="center").pack(pady=(10, 20))
        
        tk.Label(self.right_frame, text="Selecciona la categoría del problema que estás experimentando:", 
                 font=self.normal_font, bg=self.bg_color, fg=self.text_color, wraplength=450).pack(pady=(0, 15))
        
        for key, cat in CATEGORIAS.items():
            btn = tk.Button(self.right_frame, text=cat["nombre"], font=self.btn_font,
                            bg=self.btn_bg, fg="white", activebackground=self.btn_hover,
                            cursor="hand2", relief="flat", padx=10, pady=5,
                            command=lambda c=cat["codigo"]: self.iniciar_diagnostico(c))
            btn.pack(pady=5, fill="x", padx=30)
            
        btn_pruebas = tk.Button(self.right_frame, text="🧪 Ejecutar Casos de Prueba (CP01-CP08)", font=self.normal_font,
                                bg="#6c757d", fg="white", activebackground="#5a6268", cursor="hand2", relief="flat",
                                command=self.ejecutar_pruebas_integracion)
        btn_pruebas.pack(pady=20, fill="x", padx=30)

    def ejecutar_pruebas_integracion(self):
        try:
            resultados = ejecutar_casos_prueba()
            messagebox.showinfo("Suite de Pruebas Exitosa", "Todos los casos (CP01-CP08) pasaron:\n\n" + resultados)
        except AssertionError as e:
            messagebox.showerror("Fallo en Prueba", f"Un caso falló:\n{e}")

    def iniciar_diagnostico(self, codigo_categoria):
        self.preguntas_actuales = obtener_preguntas(codigo_categoria)
        self.indice_pregunta = 0
        self.hechos_recolectados = set()
        self.historial_respuestas = []
        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.limpiar_panel_derecho()
        
        if self.indice_pregunta < len(self.preguntas_actuales):
            pregunta = self.preguntas_actuales[self.indice_pregunta]
            
            # Parte superior: Indicador
            tk.Label(self.right_frame, text=f"Pregunta {self.indice_pregunta + 1} de {len(self.preguntas_actuales)}",
                     font=self.normal_font, bg=self.bg_color, fg="#666666").pack(pady=(10, 10))
            
            # Centro: Pregunta y Botones de respuesta
            q_frame = tk.Frame(self.right_frame, bg=self.btn_bg, bd=0, padx=20, pady=30)
            q_frame.pack(fill="x", padx=20, pady=10)
            
            tk.Label(q_frame, text=pregunta["texto"], font=self.q_font, bg=self.btn_bg, fg="white", 
                     wraplength=400, justify="center").pack(expand=True)
            
            btn_frame = tk.Frame(self.right_frame, bg=self.bg_color)
            btn_frame.pack(pady=20)
            
            tk.Button(btn_frame, text="👍 Sí", font=self.title_font, width=6, bg=self.btn_si_color, fg="white",
                      cursor="hand2", relief="flat", command=lambda p=pregunta: self.procesar_respuesta(p, "s")).pack(side="left", padx=20)
            
            tk.Button(btn_frame, text="👎 No", font=self.title_font, width=6, bg=self.btn_no_color, fg="white",
                      cursor="hand2", relief="flat", command=lambda p=pregunta: self.procesar_respuesta(p, "n")).pack(side="right", padx=20)
            
            # Inferior: Botón de Volver a la derecha
            bottom_frame = tk.Frame(self.right_frame, bg=self.bg_color)
            bottom_frame.pack(side="bottom", fill="x", pady=20)
            
            tk.Button(bottom_frame, text="⬅️ Volver", font=self.normal_font, bg="#6c757d", fg="white", 
                      cursor="hand2", relief="flat", padx=10, command=self.retroceder_pregunta).pack(side="right", padx=20)
            
        else:
            self.mostrar_resultados()

    def procesar_respuesta(self, pregunta, respuesta):
        texto_resp = "Sí" if respuesta == "s" else "No"
        hecho = convertir_respuesta_en_hecho(pregunta, respuesta)
        
        if hecho:
            self.hechos_recolectados.add(hecho)
            
        # Guardar en el historial para el resumen y para poder retroceder
        self.historial_respuestas.append({
            "pregunta": pregunta["texto"], 
            "respuesta": texto_resp, 
            "hecho": hecho
        })
        
        self.indice_pregunta += 1
        self.mostrar_pregunta()

    def retroceder_pregunta(self):
        """Retrocede una pregunta eliminando el último hecho y respuesta."""
        if self.indice_pregunta > 0:
            self.indice_pregunta -= 1
            ultimo = self.historial_respuestas.pop()
            
            if ultimo["hecho"] and ultimo["hecho"] in self.hechos_recolectados:
                self.hechos_recolectados.remove(ultimo["hecho"])
                
            self.mostrar_pregunta()
        else:
            self.mostrar_inicio()

    def mostrar_resultados(self):
        self.limpiar_panel_derecho()
        
        tk.Label(self.right_frame, text="✨ Resultados del Diagnóstico ✨", font=self.normal_font, bg=self.bg_color, fg="#d4af37").pack(pady=(10, 5))
        
        # Frame inferior para el botón de Regresar
        bottom_frame = tk.Frame(self.right_frame, bg=self.bg_color)
        bottom_frame.pack(side="bottom", fill="x", pady=10)
        
        tk.Button(bottom_frame, text="🏠 Regresar al menú principal", font=self.normal_font,
                  bg=self.btn_bg, fg="white", cursor="hand2", relief="flat", padx=15, pady=5, 
                  command=self.mostrar_inicio).pack(side="right", padx=20)
                  
        # Ejecución y Área de texto
        resultado = ejecutar_encadenamiento_hacia_adelante(self.hechos_recolectados, REGLAS)
        txt_resultado = tk.Text(self.right_frame, font=self.normal_font, bg="#f8f9fa", fg="black", wrap="word", relief="groove", bd=2, padx=15, pady=15)
        txt_resultado.pack(expand=True, fill="both", padx=20, pady=5)
        
        # --- 1. RESUMEN DE PREGUNTAS Y RESPUESTAS ---
        txt_resultado.insert(tk.END, "📝 RESUMEN DE RESPUESTAS:\n")
        for item in self.historial_respuestas:
            txt_resultado.insert(tk.END, f" P: {item['pregunta']}\n")
            txt_resultado.insert(tk.END, f" R: {item['respuesta']}\n\n")
        txt_resultado.insert(tk.END, "-"*50 + "\n\n")
        
        # --- 2. DIAGNÓSTICO Y RECOMENDACIONES ---
        if not resultado["diagnosticos"]:
            txt_resultado.insert(tk.END, "⚠️ INFORMACIÓN INSUFICIENTE\nNo se activaron reglas concluyentes con las respuestas proporcionadas.")
        else:
            txt_resultado.insert(tk.END, "🛑 DIAGNÓSTICO:\n")
            for d in resultado["diagnosticos"]: 
                txt_resultado.insert(tk.END, f" ✔️ {obtener_texto_hecho(d)}\n")
                
            txt_resultado.insert(tk.END, "\n💡 RECOMENDACIONES:\n")
            for r in resultado["recomendaciones"]: 
                txt_resultado.insert(tk.END, f" 👉 {obtener_texto_hecho(r)}\n")
                
        txt_resultado.config(state="disabled") # Hacerlo de solo lectura

if __name__ == "__main__":
    app = AkinatorDBApp()
    app.mainloop()