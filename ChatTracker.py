from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from engine import FileReader


class FeedScreen(Screen):
    pass


class SettingsScreen(Screen):

    file_path = ''
    report = ''
    mention = ''

    def save(self, file_path, report, mention):
        self.file_path = file_path
        self.report = report
        self.mention = mention


class ScreenManagement(ScreenManager):
    pass


sm = Builder.load_file('ui/chattracker.kv')


class ChatTrackerApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    ChatTrackerApp().run()
