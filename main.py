import sys
import time
import pyperclip
import pyautogui
import pandas as pd

# Configuração de pausa do pyautogui
pyautogui.PAUSE = 1

print(f"Interpretador Python em uso: {sys.executable}")

# Passo 1: Entrar no sistema da empresa (Google Drive)
pyautogui.hotkey("command", "space")
pyautogui.write("safari")
pyautogui.press("enter")
time.sleep(2)

link = "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

# Passo 2: Navegar no sistema para encontrar a base de dados
pyautogui.click(x=365, y=445, clicks=2)
time.sleep(2)
pyautogui.press("enter")
time.sleep(1)

# Passo 3: Exportar a base de dados (Download do arquivo)
pyautogui.click(x=1334, y=451)
pyautogui.click(x=1054, y=163)
time.sleep(2)

# Passo 4: Calcular os indicadores (Faturamento e Quantidade)
# Atenção: Ajuste o caminho do arquivo conforme o seu usuário/sistema operacional
caminho_arquivo = "/Users/zeluc4x/Downloads/Vendas - Dez.xlsx"
tabela = pd.read_excel(caminho_arquivo)

faturamento = tabela["Valor Final"].sum()
qtde_produtos = tabela["Quantidade"].sum()

print(f"Faturamento calculado: R$ {faturamento:,.2f}")
print(f"Quantidade de produtos: {qtde_produtos:,}")

# Passo 5: Enviar um e-mail pelo Gmail com os indicadores
pyautogui.hotkey("command", "t")
pyautogui.write("https://mail.google.com")
pyautogui.press("enter")
time.sleep(5)

# Clicar no botão 'Escrever'
pyautogui.click(x=56, y=220)
time.sleep(3)

# Destinatário
pyautogui.write("joselucas2santos+codigo@gmail.com")
pyautogui.press("tab")
pyautogui.press("tab")

# Assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("command", "v")
pyautogui.press("tab")

# Corpo do e-mail
texto = f"""
Prezados,

Segue o relatório de vendas de hoje.

Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {qtde_produtos:,}

Qualquer dúvida estou à disposição.
Abs,
Lira Python
"""
pyperclip.copy(texto)
pyautogui.hotkey("command", "v")

# Enviar o e-mail
pyautogui.click(x=858, y=782)