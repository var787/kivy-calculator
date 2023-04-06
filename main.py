from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

Window.size = (350, 500)  # Increase the size of the window
Builder.load_string("""
<Calculator>:
    cols: 4
    spacing: 5
    padding: [5, 5, 5, 5]
    canvas.before:
        Color:
            rgba: 0.678, 0.847, 0.902, 1  # Light blue background
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        id: display
        text: root.display_text
        font_size: 32
        size_hint_y: 0.25
        halign: "right"
        valign: "middle"
        text_size: self.size
        padding_x: 20
        canvas.before:
            Color:
                rgba: (0.8, 0.8, 0.8, 1)
            Rectangle:
                pos: self.pos
                size: self.size

    Button:
        text: "C"
        on_press: root.clear()
    Button:
        text: "/"
        on_press: root.append_operator(self.text)
    Button:
        text: "*"
        on_press: root.append_operator(self.text)
    Button:
        text: "-"
        on_press: root.append_operator(self.text)
    Button:
        text: "7"
        on_press: root.append_number(self.text)
    Button:
        text: "8"
        on_press: root.append_number(self.text)
    Button:
        text: "9"
        on_press: root.append_number(self.text)
    Button:
        text: "+"
        on_press: root.append_operator(self.text)
    Button:
        text: "4"
        on_press: root.append_number(self.text)
    Button:
        text: "5"
        on_press: root.append_number(self.text)
    Button:
        text: "6"
        on_press: root.append_number(self.text)
    Button:
        text: "="
        on_press: root.calculate()
    Button:
        text: "1"
        on_press: root.append_number(self.text)
    Button:
        text: "2"
        on_press: root.append_number(self.text)
    Button:
        text: "3"
        on_press: root.append_number(self.text)
    Button:
        text: "0"
        size_hint_y: None
        height: self.width
        on_press: root.append_number(self.text)
    Button:
        text: "."
        on_press: root.append_decimal()
""")


class Calculator(GridLayout):
    display_text = StringProperty()

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)
        self.expression = ""

    def update_display(self):
        self.display_text = self.expression

    def append_number(self, number):
        self.expression += number
        self.update_display()

    def append_operator(self, operator):
        if self.expression and self.expression[-1] not in "+-*/":
            self.expression += operator
            self.update_display()

    def append_decimal(self):
        if self.expression and self.expression[-1] != "." and self.expression[-1] not in "+-*/":
            self.expression += "."
            self.update_display()

    def clear(self):
        self.expression = ""
        self.update_display()

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self.update_display()


class SimpleCalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == '__main__':
    SimpleCalculatorApp().run()
