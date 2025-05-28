import time
from datetime import datetime
import pyautogui
import tkinter as tk
from tkinter import simpledialog, messagebox

# Oculta a janela principal
root = tk.Tk()
root.withdraw()

def solicitar_data(msg):
    while True:
        data = simpledialog.askstring("Data", msg)
        if data is None:
            messagebox.showwarning("Aviso", "Operação cancelada.")
            exit()
        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data
        except ValueError:
            messagebox.showerror("Erro", "Data inválida. Use o formato dd/mm/yyyy.")

check_in = solicitar_data("Data de check-in (dd/mm/yyyy):")
check_out = solicitar_data("Data de check-out (dd/mm/yyyy):")
nome = simpledialog.askstring("Hóspede", "Nome do hóspede:")
tem_cadastro = simpledialog.askstring("Cadastro", "Tem cadastro? (sim/não):").strip().lower()
valor_por_dia = int(simpledialog.askstring("Valor", "Valor da diária (apenas números): R$ "))
categoria_quarto = simpledialog.askstring("Categoria", "Categoria do quarto (STD4, STD6, SUI):").strip().upper()
quarto = int(simpledialog.askstring("Quarto", "Qual o número do quarto?"))
pax = int(simpledialog.askstring("Pessoas", "Quantas pessoas tem no quarto?"))
venda = simpledialog.askstring("Venda", "De quem é a venda?")

dias = (datetime.strptime(check_out, "%d/%m/%Y") - datetime.strptime(check_in, "%d/%m/%Y")).days
valor_total = valor_por_dia * dias if dias > 0 else valor_total

resumo = f"""
Check-in: {check_in}
Check-out: {check_out}
Hóspede: {nome}
Cadastro: {tem_cadastro}
Categoria: {categoria_quarto}
Quarto: {quarto}
Valor total: R$ {valor_total} (R$ {valor_por_dia:.2f}/dia)
"""
messagebox.showinfo("Resumo da Reserva", resumo)

messagebox.showinfo("Atenção", "Você tem 5 segundos para posicionar o mouse...")
time.sleep(5)


# Automatização com PyAutoGUI
pyautogui.click(x=1170, y=487)
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)

pyautogui.press("tab")
time.sleep(1)

pyautogui.write("PARTICULAR", interval=0.1)
pyautogui.press("tab")
time.sleep(1)

pyautogui.doubleClick(x=137, y=395)
pyautogui.doubleClick(x=589, y=353)
time.sleep(1)

pyautogui.press("down")
pyautogui.press("tab")
pyautogui.press("left")

for _ in range(7):
    pyautogui.press("tab")

# Check-in
pyautogui.write(check_in, interval=0.1)
pyautogui.press("tab")

# Check-out
pyautogui.write(check_out, interval=0.1)

for _ in range(6):
    pyautogui.press("tab")
pyautogui.press("enter")

# Define número de TABs conforme categoria
if categoria_quarto == 'STD4':
    down_count = 4
elif categoria_quarto == 'STD6':
    down_count = 5
elif categoria_quarto == 'SUI':
    down_count = 6
else:
    down_count = 0  # padrão caso categoria inválida

# Pressiona a tecla "down" o número de vezes necessário
for _ in range(down_count):
    pyautogui.press("down")

pyautogui.press("enter")

for _ in range(4):
    pyautogui.press("tab")
pyautogui.press("enter")

if pax == 1:
    down_count = 1
elif pax == 2:
    down_count = 2
elif pax == 3:
    down_count = 3
elif pax == 4:
    down_count = 4
elif pax == 5:
    down_count = 5
elif pax == 6:
    down_count = 6
else:
    down_count = 0  # padrão caso categoria inválida

for _ in range(down_count):
   pyautogui.press("down")

pyautogui.press("enter")

for _ in range(4):
   pyautogui.press("tab")
pyautogui.press("enter")

if quarto == 1:
    down_count = 1
elif quarto == 2:
    down_count = 2
elif quarto == 3:
    down_count = 3
elif quarto == 4:
    down_count = 4
elif quarto == 5:
    down_count = 5
elif quarto == 6:
    down_count = 6
elif quarto == 7:
    down_count = 7
elif quarto == 8:
    down_count = 8
elif quarto == 12:
    down_count = 9
else:
    down_count = 0  # padrão caso categoria inválida

for _ in range(down_count):
   pyautogui.press("down")

pyautogui.press("enter")

pyautogui.press("tab")
pyautogui.press("down")
pyautogui.press("enter")

pyautogui.click(x=446, y=523)

pyautogui.write(str(valor_por_dia), interval=0.1)

pyautogui.click(x=893, y=506)
time.sleep(1)

pyautogui.click(x=57, y=554)
time.sleep(1)

pyautogui.write(nome, interval=0.1)
pyautogui.press("tab")
time.sleep(1)

pyautogui.doubleClick(x=439, y=415)
pyautogui.doubleClick(x=924, y=372)
time.sleep(1)

pyautogui.click(x=960, y=493)
time.sleep(1)

pyautogui.press("pagedown")

pyautogui.click(x=406, y=203)
time.sleep(1)

pyautogui.write(venda, interval=0.1)

pyautogui.press("tab")
pyautogui.press("enter")

for _ in range(2):
    pyautogui.press("down")
time.sleep(1)
  
pyautogui.press("enter")

pyautogui.click(x=1023, y=334)
pyautogui.press("pagedown")

pyautogui.doubleClick(x=223, y=174)
pyautogui.doubleClick(x=223, y=174)
time.sleep(1)

# Nome do hóspede já informado anteriormente
pyautogui.write(nome, interval=0.1)

for _ in range(4):
    pyautogui.press("tab")
time.sleep(1)

# Celular
pyautogui.write("22992219769", interval=0.1)

for _ in range(4):
    pyautogui.press("tab")
time.sleep(1)

#email
pyautogui.write("email@exemplo.com", interval=0.1)

for _ in range(7):
    pyautogui.press("tab")
time.sleep(1)

pyautogui.write(f"DIARIAS: {dias}\nValor total: R$ {valor_total}\nPax: {pax}", interval=0.1)

pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')

pyautogui.press("tab")

pyautogui.hotkey('ctrl', 'v')

# pyautogui.click(x=1150, y=700)
