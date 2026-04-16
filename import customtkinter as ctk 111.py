import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
import threading
import time

ctk.set_appearance_mode("dark")

# -------- TEMA --------
class Tema:
    FUNDO = "#020617"
    CARD = "#0b1220"
    BORDA = "#1e293b"

    ACENTO = "#22c55e"
    ACENTO_HOVER = "#16a34a"

    TEXTO = "#f1f5f9"
    TEXTO_SEC = "#64748b"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("A.AI - Sistema Inteligente")
        self.geometry("1100x850")
        self.configure(fg_color=Tema.FUNDO)

        self.after(300, lambda: self.attributes("-alpha", 0.98))

        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(expand=True, fill="both")

        self.tela_login()

    def limpar(self):
        for w in self.container.winfo_children():
            w.destroy()

    # -------- LOGIN --------
    def tela_login(self):
        self.limpar()

        card = ctk.CTkFrame(self.container,
                            width=380,
                            height=480,
                            fg_color=Tema.CARD,
                            border_width=1,
                            border_color=Tema.BORDA,
                            corner_radius=20)
        card.place(relx=0.5, rely=0.5, anchor="center")

        ctk.CTkLabel(card,
                     text="A.AI",
                     font=("Inter", 40, "bold"),
                     text_color=Tema.ACENTO).pack(pady=(50, 10))

        ctk.CTkLabel(card,
                     text="Acessibilidade Inteligente",
                     text_color=Tema.TEXTO_SEC).pack(pady=(0, 30))

        self.user = ctk.CTkEntry(card, placeholder_text="admin")
        self.user.pack(pady=10, padx=40, fill="x")

        self.senha = ctk.CTkEntry(card, placeholder_text="1234", show="*")
        self.senha.pack(pady=10, padx=40, fill="x")

        ctk.CTkButton(card,
                      text="Entrar",
                      fg_color=Tema.ACENTO,
                      hover_color=Tema.ACENTO_HOVER,
                      command=self.login).pack(pady=40)

    def login(self):
        if self.user.get() == "admin" and self.senha.get() == "1234":
            self.tela_principal()
        else:
            messagebox.showerror("Erro", "Login inválido")

    # -------- FORM PRINCIPAL --------
    def tela_principal(self):
        self.limpar()

        header = ctk.CTkFrame(self.container, height=70, fg_color=Tema.FUNDO)
        header.pack(fill="x")

        ctk.CTkLabel(header,
                     text="A.AI SYSTEM",
                     font=("Inter", 20, "bold"),
                     text_color=Tema.ACENTO).pack(side="left", padx=30)

        ctk.CTkButton(header,
                      text="Sair",
                      fg_color="transparent",
                      border_width=1,
                      border_color=Tema.BORDA,
                      command=self.tela_login).pack(side="right", padx=30)

        scroll = ctk.CTkScrollableFrame(self.container, fg_color="transparent")
        scroll.pack(expand=True, fill="both", padx=30, pady=20)

        grid = ctk.CTkFrame(scroll, fg_color="transparent")
        grid.pack(fill="both", expand=True)

        grid.grid_columnconfigure(0, weight=2)
        grid.grid_columnconfigure(1, weight=1)

        # -------- FORM --------
        form = ctk.CTkFrame(grid,
                            fg_color=Tema.CARD,
                            corner_radius=20,
                            border_width=1,
                            border_color=Tema.BORDA)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 15), pady=10)

        ctk.CTkLabel(form,
                     text="Formulário de Ocorrência",
                     font=("Inter", 20, "bold"),
                     text_color=Tema.ACENTO).pack(pady=(20, 10))

        ctk.CTkLabel(form,
                     text="Preencha as informações abaixo",
                     text_color=Tema.TEXTO_SEC).pack(pady=(0, 20))

        self.problema = self.input(form, "Qual é o problema?")
        self.local = self.input(form, "Local do problema")

        ctk.CTkLabel(form, text="Descrição detalhada",
                     font=("Inter", 12, "bold")).pack(anchor="w", padx=25)

        self.desc = ctk.CTkTextbox(form, height=140, corner_radius=10)
        self.desc.pack(fill="x", padx=25, pady=10)

        ctk.CTkLabel(form, text="Nível de urgência",
                     font=("Inter", 12, "bold")).pack(anchor="w", padx=25)

        self.urg = ctk.CTkSegmentedButton(
            form,
            values=["Baixa", "Média", "Alta", "Crítica"]
        )
        self.urg.pack(fill="x", padx=25, pady=10)
        self.urg.set("Média")

        self.relatado = ctk.CTkCheckBox(form, text="Já foi relatado?")
        self.relatado.pack(anchor="w", padx=25, pady=5)

        self.sugestao = ctk.CTkCheckBox(form, text="Adicionar sugestão?")
        self.sugestao.pack(anchor="w", padx=25)

        self.nome = self.input(form, "Seu nome (opcional)")

        # -------- CHAT --------
        chat_card = ctk.CTkFrame(grid,
                                 fg_color=Tema.CARD,
                                 border_width=1,
                                 border_color=Tema.BORDA)
        chat_card.grid(row=0, column=1, sticky="nsew")

        ctk.CTkLabel(chat_card,
                     text="IA - NBR 9050",
                     text_color=Tema.ACENTO).pack(pady=10)

        self.chat = ctk.CTkTextbox(
            chat_card,
            fg_color="#010409",
            text_color="#22c55e",
            font=("Consolas", 12)
        )
        self.chat.pack(fill="both", expand=True, padx=10, pady=5)

        self.chat.insert("end", "IA: Olá! Pergunte sobre acessibilidade.\n\n")

        self.msg = ctk.CTkEntry(chat_card, placeholder_text="Perguntar...")
        self.msg.pack(fill="x", padx=10, pady=5)
        self.msg.bind("<Return>", lambda e: self.enviar())

        ctk.CTkButton(chat_card,
                      text="Enviar",
                      command=self.enviar).pack(padx=10, pady=5)

        # -------- BOTÃO --------
        ctk.CTkButton(scroll,
                      text="GERAR RELATÓRIO",
                      height=60,
                      font=("Inter", 16, "bold"),
                      fg_color=Tema.ACENTO,
                      hover_color=Tema.ACENTO_HOVER,
                      corner_radius=15,
                      command=self.gerar).pack(pady=25, fill="x", padx=120)

        # RESULTADO
        self.resultado = ctk.CTkTextbox(
            scroll,
            height=250,
            fg_color="#010409",
            text_color="#22c55e",
            font=("Consolas", 13)
        )
        self.resultado.pack(fill="x", padx=40, pady=20)

    def input(self, parent, texto):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=25, pady=8)

        ctk.CTkLabel(frame,
                     text=texto,
                     font=("Inter", 12, "bold")).pack(anchor="w")

        e = ctk.CTkEntry(frame, height=40)
        e.pack(fill="x", pady=5)

        return e

    # -------- CHAT INTELIGENTE --------
    def enviar(self):
        msg = self.msg.get().lower().strip()
        if not msg:
            return

        self.chat.insert("end", f"> {msg}\n")
        self.msg.delete(0, "end")

        def responder():
            time.sleep(1)

            resposta = "IA: Não entendi. Pode reformular?\n\n"

            if "rampa" in msg:
                resposta = "IA: Inclinação máxima de 8,33% (1:12).\n\n"

            elif "porta" in msg:
                resposta = "IA: Largura mínima de 80 cm.\n\n"

            elif "banheiro" in msg:
                resposta = "IA: Deve ter barras de apoio e área de giro de 1,5m.\n\n"

            elif "escada" in msg:
                resposta = "IA: Corrimão duplo e piso antiderrapante.\n\n"

            elif "cadeirante" in msg:
                resposta = "IA: Deve haver rota acessível contínua.\n\n"

            elif "elevador" in msg:
                resposta = "IA: Deve conter braille e altura acessível.\n\n"

            elif "sinalização" in msg:
                resposta = "IA: Deve ter contraste visual e braille.\n\n"

            self.chat.insert("end", resposta)
            self.chat.see("end")

        threading.Thread(target=responder).start()

    # -------- RELATÓRIO --------
    def gerar(self):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")

        texto = f"""
╔══════════════════════════════════════╗
   RELATÓRIO DE ACESSIBILIDADE
╚══════════════════════════════════════╝

Data: {data}
Responsável: {self.nome.get() or "Anônimo"}

Problema: {self.problema.get()}
Local: {self.local.get()}
Urgência: {self.urg.get()}

Relatado antes: {"Sim" if self.relatado.get() else "Não"}
Sugestão: {"Sim" if self.sugestao.get() else "Não"}

Descrição:
{self.desc.get("1.0", "end")}
"""

        self.resultado.delete("1.0", "end")
        self.resultado.insert("1.0", texto)

        messagebox.showinfo("Sucesso", "Relatório gerado!")


# -------- RUN --------
if __name__ == "__main__":
    app = App()
    app.mainloop()
    