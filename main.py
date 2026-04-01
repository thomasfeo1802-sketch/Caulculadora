import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        # 1. Pegar os valores e converter para números
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operacao = opEntry.get()
        
        # 2. Lógica de cálculo
        match operacao:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                if num2 == 0:
                    messagebox.showerror("Erro", "Divisão por zero!")
                    return
                result = num1 / num2
            case _:
                messagebox.showwarning("Aviso", "Operação inválida! Use +, -, * ou /")
                return

        # 3. Atualizar o label de resultado
        resultadoLabel['text'] = f"Resultado: {result}"
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite números válidos.")

# Configuração da Janela
janela = tk.Tk()
janela.title("Calculadora")
janela.geometry("300x400")

# Elementos da Interface
tk.Label(janela, text="Calculadora", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(janela, text="Número 1:").pack()
entry1 = tk.Entry(janela)
entry1.pack()

tk.Label(janela, text="Número 2:").pack()
entry2 = tk.Entry(janela)
entry2.pack()

tk.Label(janela, text="Operação (+, -, *, /):").pack()
opEntry = tk.Entry(janela)
opEntry.pack()

# Botão para disparar o cálculo
btn_calcular = tk.Button(janela, text="Calcular", command=calcular)
btn_calcular.pack(pady=20)

resultadoLabel = tk.Label(janela, text="Resultado: None", font=("Arial", 10, "italic"))
resultadoLabel.pack()

janela.mainloop()