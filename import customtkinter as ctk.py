import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("dark")


# ================= LOGIN =================
class TelaLogin(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Acessibilidade")
        self.geometry("400x500")
        self.configure(fg_color="#0f172a")  # Azul moderno

        self.criar_interface()

    def criar_interface(self):
        frame = ctk.CTkFrame(self, fg_color="#111827", corner_radius=15)
        frame.pack(expand=True, padx=30, pady=30)

        ctk.CTkLabel(frame, text="♿", font=("Arial", 60)).pack(pady=10)

        ctk.CTkLabel(frame, text="Login Corporativo",
                     font=("Arial", 18, "bold")).pack(pady=10)

        self.user = ctk.CTkEntry(frame, placeholder_text="Usuário")
        self.user.pack(pady=10, padx=20, fill="x")

        self.password = ctk.CTkEntry(frame, placeholder_text="Senha", show="*")
        self.password.pack(pady=10, padx=20, fill="x")

        ctk.CTkButton(frame, text="Entrar",
                      fg_color="#22c55e",
                      hover_color="#16a34a",
                      command=self.login).pack(pady=20)

    def login(self):
        if self.user.get() == "admin" and self.password.get() == "1234":
            self.destroy()
            Sistema().mainloop()
        else:
            messagebox.showerror("Erro", "Login inválido")


# ================= SISTEMA =================
class Sistema(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Portal de Acessibilidade")
        self.geometry("700x800")
        self.configure(fg_color="#0f172a")

        self.cor_verde = "#22c55e"

        self.tela_formulario()

    # -------- LIMPAR --------
    def limpar(self):
        for widget in self.winfo_children():
            widget.destroy()

    # -------- FORMULÁRIO --------
    def tela_formulario(self):
        self.limpar()

        frame = ctk.CTkFrame(self, fg_color="#111827", corner_radius=15)
        frame.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(frame, text="Registrar Problema",
                     font=("Arial", 20, "bold")).pack(pady=15)

        self.problema = ctk.CTkEntry(frame, placeholder_text="Qual o problema?")
        self.problema.pack(pady=10, padx=20, fill="x")

        self.local = ctk.CTkEntry(frame, placeholder_text="Local")
        self.local.pack(pady=10, padx=20, fill="x")

        self.desc = ctk.CTkTextbox(frame, height=120)
        self.desc.pack(pady=10, padx=20, fill="x")

        self.urgencia = ctk.CTkComboBox(
            frame, values=["Baixa", "Média", "Alta", "Crítica"])
        self.urgencia.set("Selecione a urgência")
        self.urgencia.pack(pady=10, padx=20, fill="x")

        ctk.CTkButton(frame, text="Abrir Chat",
                      fg_color=self.cor_verde,
                      command=self.tela_chat).pack(pady=20)

    # -------- CHAT --------
    def tela_chat(self):
        self.limpar()

        problema = self.problema.get()
        urgencia = self.urgencia.get()

        # HEADER
        header = ctk.CTkFrame(self, fg_color="#22c55e", height=60)
        header.pack(fill="x")

        ctk.CTkLabel(header, text="Assistente Virtual",
                     text_color="white",
                     font=("Arial", 16, "bold")).pack(pady=15)

        # ÁREA CHAT
        self.chat = ctk.CTkTextbox(self, fg_color="#020617")
        self.chat.pack(fill="both", expand=True, padx=15, pady=10)

        self.chat.insert("end",
            f"🔎 Problema: {problema}\n"
            f"⚠ Urgência: {urgencia}\n\n"
            "IA: Olá! Já recebi seu relato.\n"
            "Como posso te ajudar agora?\n\n"
        )

        # INPUT
        frame_input = ctk.CTkFrame(self)
        frame_input.pack(fill="x", padx=10, pady=10)

        self.input = ctk.CTkEntry(frame_input, placeholder_text="Digite sua mensagem...")
        self.input.pack(side="left", fill="x", expand=True, padx=10, pady=10)

        ctk.CTkButton(frame_input, text="Enviar",
                      width=80,
                      fg_color=self.cor_verde,
                      command=self.enviar).pack(side="right", padx=10)

    # -------- LÓGICA DO CHAT --------
    def enviar(self):
        msg = self.input.get().strip()

        if not msg:
            return

        # Mostrar mensagem do usuário
        self.chat.insert("end", f"Você: {msg}\n")

        # Resposta simples (simulação de IA)
        resposta = self.resposta_ia(msg)

        self.chat.insert("end", f"IA: {resposta}\n\n")

        self.input.delete(0, "end")
        self.chat.see("end")

    def resposta_ia(self, msg):
        msg = msg.lower()

        if "rampa" in msg:
            return "Entendi. Esse problema pode afetar acessibilidade física. Vamos priorizar isso."
        elif "banheiro" in msg:
            return "Problemas em banheiros acessíveis são críticos. Vou registrar com alta prioridade."
        elif "obrigado" in msg:
            return "De nada! Estou aqui para ajudar 😊"
        else:
            return "Entendi seu ponto. Vou encaminhar essa informação para análise."


# ================= EXECUÇÃO =================
if __name__ == "__main__":
    app = TelaLogin()
    app.mainloop()