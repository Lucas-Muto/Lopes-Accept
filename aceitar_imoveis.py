import pyautogui
import time

# Nomes dos arquivos das imagens dos botões na ordem correta
botoes = ['plus.PNG', 'check.PNG', 'aprovar.PNG', 'ok.PNG']

# Tempo de espera entre as ações (em segundos)
INTERVALO = 8 # Ajuste conforme necessário

def clicar_no_botao(imagem, timeout=15, conf=0.9):
    """Procura e clica no botão na tela."""
    inicio = time.time()
    while time.time() - inicio < timeout:
        try:
            pos = pyautogui.locateCenterOnScreen(imagem, confidence=conf)
        except Exception as e:
            print(f"Erro ao procurar imagem {imagem}: {e}")
            return False
        if pos:
            pyautogui.moveTo(pos)
            pyautogui.click()
            return True
        time.sleep(0.5)
    return False

def scrollar_para_baixo():
    """Rola até o final da página de forma rápida usando a tecla END."""
    pyautogui.press('end')
    time.sleep(0.5)  # Pequena pausa para garantir que tudo carregou

def fluxo_aceitacao():
    while True:
        print("\nProcurando o botão PLUS...")
        if not clicar_no_botao(botoes[0]):
            print("Não encontrou mais solicitações (PLUS). Finalizando script.")
            break
        print("Clicou no botão PLUS. Aguardando...")
        time.sleep(INTERVALO)

        print("Scrollando para baixo para garantir visibilidade dos próximos botões...")
        scrollar_para_baixo()
        time.sleep(1)

        print("Procurando o botão CHECK...")
        if not clicar_no_botao(botoes[1]):
            print("Não encontrou o botão CHECK. Reiniciando fluxo do início...")
            continue  # Volta para o início do loop, procurando o PLUS
        print("Clicou no botão CHECK. Aguardando...")
        time.sleep(INTERVALO)

        print("Procurando o botão APROVAR...")
        if not clicar_no_botao(botoes[2]):
            print("Não encontrou o botão APROVAR. Reiniciando fluxo do início...")
            continue  # Volta para o início do loop, procurando o PLUS
        print("Clicou no botão APROVAR. Aguardando...")
        time.sleep(INTERVALO)

        print("Procurando o botão OK...")
        if not clicar_no_botao(botoes[3]):
            print("Não encontrou o botão OK. Reiniciando fluxo do início...")
            continue  # Volta para o início do loop, procurando o PLUS
        print("Clicou no botão OK. Aguardando...")
        time.sleep(INTERVALO)

        print("Fluxo finalizado para uma solicitação. Reiniciando para próxima...")

if __name__ == "__main__":
    print("O script vai começar em 5 segundos. Deixe a tela pronta!")
    time.sleep(5)
    fluxo_aceitacao()
