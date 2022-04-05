import random

from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout


class WrappedLabel(Label):
    # Based on Tshirtman's answer
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))


class Notecard(RelativeLayout):

    def __init__(self, header='', body='', w=250, i=True, index=-1, **kwargs):
        super(Notecard, self).__init__(**kwargs)

        # used for window building
        self.typing = 'dynamic'
        self.index = index

        # layout parameters
        self.size_hint_x = None
        self.size_hint_y = None
        self.width = w
        self.height = 140
        self.button_opacity = 0

        # reference images
        self.cards = [['Pink', 'Images/Notecards/Notecard_Pink.png'],
                      ['Green', 'Images/Notecards/Notecard_Green.png'],
                      ['Orange', 'Images/Notecards/Notecard_Orange.png'],
                      ['Blue', 'Images/Notecards/Notecard_Blue.png']]
        # ['Purple','Images/Notecards/Notecard_Purple.png']]

        # data_attributes
        self.card_color = random.randint(0, 3)
        self.title = header

        # card_image
        if i:
            self.nImage = Image(source=self.cards[self.card_color][1],
                                # size_hint=(0.99, 0.99),
                                size_hint_y=None,
                                height=140,
                                pos_hint={'center_x': 0.5})
            self.add_widget(self.nImage)

        # clickability
        self.button = Button(background_color=(1, 1, 1, self.button_opacity),
                             size_hint=(1, 0.99),
                             pos_hint={'center_x': 0.5})
        self.button.bind(on_press=self.btn_click)
        self.add_widget(self.button)

        # title
        self.nTitle = Label(pos_hint={'center_x': 0.5, 'top': 0.84},
                            size_hint=(0.65, 0.165),
                            text=self.title,
                            color=[0, 0, 0, 1],
                            font_size=20,
                            font_name='Fonts/GochiHand-Regular.ttf',
                            underline=True,
                            bold=False)
        self.add_widget(self.nTitle)

        # description
        self.desc_list = []
        self.desc = body + ' '
        desc_chars = [char for char in self.desc]
        temp_str = ''
        # algorithm that breaks up description string into lines of 30 characters or less
        while desc_chars.__len__() != 0:
            if desc_chars[0] != ' ':
                temp_str += desc_chars[0]
                desc_chars.pop(0)
            elif desc_chars[0] == ' ' and desc_chars.count(' ') > 1:
                if desc_chars[1:].index(' ') + temp_str.__len__() >= 30:
                    self.desc_list.append(temp_str)
                    temp_str = ''
                    desc_chars.pop(0)
                else:
                    temp_str += desc_chars[0]
                    desc_chars.pop(0)
            else:
                self.desc_list.append(temp_str)
                temp_str = ''
                desc_chars = []
        line = 0.67
        # creates labels
        for count, i in enumerate(self.desc_list):
            if count < 2 or len(self.desc_list) <= 3:
                self.add_widget(Label(pos_hint={'x': 0.17, 'top': line},
                                      size_hint=(0.65, 0.14),
                                      text=i,
                                      color=[0, 0, 0, 1],
                                      font_size=15,
                                      font_name='Fonts/GochiHand-Regular.ttf'))
            else:
                self.add_widget(Label(pos_hint={'x': 0.17, 'top': line},
                                      size_hint=(0.65, 0.14),
                                      text=i + '...',
                                      color=[0, 0, 0, 1],
                                      font_size=15,
                                      font_name='Fonts/GochiHand-Regular.ttf'))
                break
            line -= 0.14

    def btn_click(self, touch):
        # print(self.cards[self.card_color][0])
        pass

    def get_index(self):
        return self.index

    @staticmethod
    def blank_layout(width=220):
        n = Notecard('', '', width, False)
        n.add_widget(Button())
        n.typing = 'static'
        return n
        # return RelativeLayout(size_hint=(0.33, 0.33))


class Notecard_Divider(RelativeLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # used for window building
        self.typing = 'static'

        # layout parameters   0.03, 1
        self.size_hint = (None, 1)
        self.width = 25

        # self.add_widget(Button())
        #make button size permanent


class Notecard_Button(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint_x = None
        self.size_hint_y = None
        self.width = 250
        self.height = 140
