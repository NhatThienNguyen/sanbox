from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder

class DynamicLabelsApp(App):
    """An app make dynamic labels for name"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Joe", "Amy", "Dave"]


    def build(self):
        """Build kv app from kv file"""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file("dynamic_labels.kv")
        self.create_labels()
        return self.root


    def create_labels(self):
        """Create labels based on name list"""
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)


DynamicLabelsApp().run()