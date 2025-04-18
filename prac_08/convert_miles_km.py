from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934
DEFAULT_VALUE = 0

class MilesConverterApp(App):
    """ MilesConverterApp is a Kivy App for converting miles to kilometres """

    output_text = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


    def handle_calculate(self):
        """ handle calculation (could be button press or other call), output result to label widget """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.output_text = str(result)


    def handle_increment(self, change):
        """handle up/down button press, update the text input with new value, call calculation function"""
        value = self.get_validated_miles() + change
        self.root.ids.input_miles.text = str(value)


    def get_validated_miles(self):
        """get text input from text entry widget, convert to float"""
        try:
            value = float(self.root.ids.input_miles.text)
            return value
        except ValueError:
            return DEFAULT_VALUE


MilesConverterApp().run()