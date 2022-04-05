from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.image import Image


class paper_scrap(RelativeLayout):

    scrap = ['Images/PaperScraps/PaperScrap_Subtitle.PNG']

    def __init__(self, time = 'not set', **kwargs):
        super(paper_scrap, self).__init__(**kwargs)

        # used for window building
        self.typing = 'header'

        # layout parameters
        self.title = time
        self.width = 250
        self.height = 90
        self.size_hint = (None, None)
        self.pTitle = Label(text=self.title, color=[0, 0, 0, 1],
                            font_name='Fonts/GochiHand-Regular.ttf',
                            font_size='20',
                            pos_hint={'center_x': 0.504, 'top': 0.97})
        self.pImage = Image(source=self.scrap[0],
                            size_hint=(0.75, 0.75),
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.button = Button(background_color=(0, 0, 0, 0))
        self.button.bind(on_press=self.clicked)
        self.add_widget(self.pImage)
        self.add_widget(self.pTitle)

    def clicked(self, touch):
        print(self.title)
