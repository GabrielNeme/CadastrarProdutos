import pyautogui, time, pandas

pyautogui.press("win")
time.sleep(0.7)

pyautogui.write("chrome")
time.sleep(0.7)

pyautogui.press("enter")
time.sleep(0.7)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(0.7)

pyautogui.press("enter")
time.sleep(1)

pyautogui.click(x=797, y=410)

pyautogui.write("Teste@email.com")
time.sleep(0.7)

pyautogui.press("tab")
time.sleep(0.7)

pyautogui.write("TestePython")

pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)

tabela = pandas.read_csv("produtos.csv")

time.sleep(1)

for linha in tabela.index:
    pyautogui.click(x=806, y=294)

    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.press("pageup")