from functools import partial

from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition, CardTransition
from kivy.uix.stacklayout import StackLayout

from kivy.animation import Animation

from database import database

Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '600')


class MainGrid(Screen):
    button_press = True

    mid_button_source = ""
    temp_bool = True
    mid_an_pos = NumericProperty(0.52)

    def bulletin_click(self):
        print('MidButtonClicked')
        self.button_press = False
        if self.temp_bool:
            self.mid_an_pos = 0.50075
            self.temp_bool = False
        else:
            self.mid_an_pos = 0.52
            self.temp_bool = True

    def left_click(self):
        print("left button clicked")

    def right_click(self):
        print("right button clicked")

    @staticmethod
    def animate_button(widget, *args):
        animate = Animation(
            duration=0.1,
            pos_hint={"center_y": 0.50075}
        )
        animate += Animation(
            duration=0.1,
            pos_hint={"center_y": 0.52}
        )
        # start animation
        animate.start(widget)


class Screen_Bulletin(Screen):

    def __init__(self):
        super(Screen_Bulletin, self).__init__()

        # database
        self.db = database()
        self.db.grab_schedule()
        self.element_list = self.db.get_bulletin()
        self.bindings = []

        # initialize
        n_count = 0
        for count, i in enumerate(self.element_list):
            if type(i) == int:
                continue
            if i.typing == 'static' and self.element_list.__len__() > count + 2 and self.element_list[count + 2].typing != 'dynamic':
                continue
            if i.typing == 'header' and self.check_blanks(self.element_list[count + 1:]):
                self.ids.bulletin_board.add_widget(i)
            elif i.typing == 'dynamic':
                self.bindings.append(partial(self.button_press, count))
                i.button.bind(on_press=self.bindings[n_count])
                # i.button.bind(on_press=self.print_hi)
                self.ids.bulletin_board.add_widget(i)
                n_count += 1
            elif i.typing == 'static':
                self.ids.bulletin_board.add_widget(i)

    def refresh(self):
        self.bindings = []
        n_count = 0

        for count, i in enumerate(self.element_list):
            if type(i) == int:
                continue
            if i.typing == 'static' and self.element_list.__len__() > count + 2 and self.element_list[count + 2].typing != 'dynamic':
                continue
            if i.typing == 'header' and self.check_blanks(self.element_list[count + 1:]):
                self.ids.bulletin_board.add_widget(i)
            elif i.typing == 'dynamic':
                self.bindings.append(partial(self.button_press, count))
                i.button.bind(on_press=self.bindings[n_count])
                self.ids.bulletin_board.add_widget(i)
                n_count += 1
            elif i.typing == 'static':
                self.ids.bulletin_board.add_widget(i)

    @staticmethod
    def check_blanks(partial_list):
        for i in partial_list:
            if i == 0 or i.typing == 'static':
                continue
            elif i.typing == 'header':
                return False
            else:
                return True
            return False

    @staticmethod
    def print_hi(self):
        print('hi')

    def button_press(self, index, instance):
        self.unbind_buttons()
        self.element_list.remove(self.element_list[index])
        self.ids.bulletin_board.clear_widgets()
        self.refresh()

    def unbind_buttons(self):
        print(self.bindings.__len__())
        n_count = 0
        for i in self.element_list:
            if i.typing == 'dynamic':
                i.button.unbind(on_press=self.bindings[n_count])
                n_count += 1

    @staticmethod
    def animate_notecard(self, notecard, *args):
        animate = Animation(
            duration=0.1,
            background_color=(1,1,1,0)
        )
        # start animation
        animate.start(notecard)


class Screen3(Screen):
    pass


class Screen4(Screen):
    pass


class CareManagementSystem(App):

    def build(self):
        root = ScreenManager(transition=CardTransition())

        root.add_widget(MainGrid())
        # root.add_widget(BulletinInterface())
        # root.add_widget(Screen3())
        root.add_widget(Screen4())
        root.add_widget(Screen_Bulletin())

        return root


CareManagementSystem().run()
