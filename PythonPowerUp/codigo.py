# 1° Abrir o sistema da empresa: https://dlp.hashtagtreinamentos.com/python/intensivao/login
    # pyautogui
    # pyautogui.hotkey() -> atalho de teclado (crtl, C)

import pyautogui
import time

pyautogui.PAUSE = 0.5
pyautogui.press("win")   
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# tempo de carregamento do site:
time.sleep(2)

# 2° Fazer login
pyautogui.click(x=412, y=339)
pyautogui.write("teste@gmail.com")

pyautogui.press("tab")
pyautogui.write("123")      

pyautogui.press("tab")
pyautogui.press("enter")

# 3° Importar a base de dados dos produtos
    #pandas openpyxl
import pandas as pd

tb_produtos = pd.read_csv('produtos.csv')

# 4° Cadastrar um produto

for linha in tb_produtos.index:
    pyautogui.press("tab")
    # codigo prod
    codigo = tb_produtos.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tb_produtos.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = tb_produtos.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = tb_produtos.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preço
    preco_unitario = tb_produtos.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tb_produtos.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tb_produtos.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000)