from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

class DynamicLabelsApp(App):
    text = StringProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Joe", "Amy", "Dave"]


    def build(self):
        self.title = "Dynamic Labels"
        self.root = "dynamic_labels.kv"
        return self.root


    def create_labels(self):
        for name in self.names:
            name_label = Label(text=name)