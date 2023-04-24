from breezypythongui import EasyFrame

class TextFieldDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Text Field Demo",width=300, height=200, background="light green")
        self.addLabel(text="Input", row=0, column=0)
        self.inputField = self.addTextField(text="", row=0, column=1)
        self.addLabel(text="Output", row=1, column=0)
        self.outputField = self.addTextField(text="", row=1, column=1)
        self.addButton(text="Convert", row=2, column=0,columnspan=2, command=self.convert)

    # The event handling method for the button
    def convert(self):
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)


TextFieldDemo().mainloop()
