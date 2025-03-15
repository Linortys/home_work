class Button:
        def __init__(self, text):
            self.text = text
            self.loc = ""
            self.type = "Кнопка"

        def click(self):
            print(f"Клик по кнопке {self.text}")

textybox = Button("Text Box")
checkybox = Button("Check Box")
radio = Button("Radio Button")
web = Button("Web Tables")
butt = Button("Buttons")
link = Button("Links")
brok = Button("Broken Links - Images")
upp = Button("Upload and Download")
dyno = Button("Dynamic Properties")

textybox.click()
checkybox.click()
radio.click()
web.click()
butt.click()
link.click()
brok.click()
upp.click()
dyno.click()
