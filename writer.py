import pyautogui
import time
def scrivi_su_applicazione(messaggio):
         
        pyautogui.write(messaggio)
        pyautogui.press('enter')
if __name__ == "__main__":
    messaggio_da_scrivere = "plain text"
    time.sleep(2)
    for i in range(100):
        time.sleep(1)
        scrivi_su_applicazione(messaggio_da_scrivere)
