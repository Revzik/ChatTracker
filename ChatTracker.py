from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class FeedScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    pass


sm = Builder.load_file('ui/chattracker.kv')


class ChatTrackerApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    ChatTrackerApp().run()
