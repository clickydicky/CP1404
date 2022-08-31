"""
Display name as separate labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class DynamicLabels(App):
    """Main program - Kivy app to demo static widget creation."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.name_display = {"Bob Brown": "1", "Ironman": "2", "Bill Gates": "3", "Mickey Mouse": "4"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.load_widgets()
        return self.root

    def load_widgets(self):
        """Load names from dictionary entries and display them on the GUI."""
        for name in self.name_display:
            temp_label = Label(text=name)
            self.root.ids.main_box.add_widget(temp_label)


DynamicLabels().run()
