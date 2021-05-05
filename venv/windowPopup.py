import threading
import subprocess
import ctypes
import platform

def showPopup():
    applescript = """
    display dialog "Artikel detected! look at your shopping cart" ¬
    with title "Detecter" ¬
    with icon caution ¬
    buttons {"OK"}
    """

    def macPopup():
        subprocess.call("osascript -e '{}'".format(applescript), shell=True)

    def windowsPopup():
        text = "Artikel detected! look at your shopping cart"
        title = "Detecter"
        ctypes.windll.user32.MessageBoxW(0, text, title, 0x1000)

    def addFoundItemToBasket():
        print("item was added to basket")
        # ActionChains(driver).move_to_element(moveToBtn).click(moveToBtn).perform()

        # # wait for modal and basketBtn to show up
        # WebDriverWait(driver, 3).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="basket"]/div/div[4]/div/button[2]')
        #     )
        # )
        # print("located")

        # # simulate click and add to basket
        # toWarenkorbBtn = driver.find_element_by_xpath(
        #     '//*[@id="basket"]/div/div[4]/div/button[2]'
        # )
        # ActionChains(driver).move_to_element(toWarenkorbBtn).click(
        #     toWarenkorbBtn
        # ).perform()
        # print("item added to basket")

        # self.fillForm()
    
    os = platform.system()
    
    if os == 'Darwin':
        p1 = threading.Thread(target=macPopup)
        p2 = threading.Thread(target=addFoundItemToBasket)
        p1.start()
        p2.start()
    else:
        p1 = threading.Thread(target=windowsPopup)
        p2 = threading.Thread(target=addFoundItemToBasket)
        p1.start()
        p2.start()
    






