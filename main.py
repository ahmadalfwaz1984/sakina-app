import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SakinaApp(App):
    def build(self):
        Window.clearcolor = get_color_from_hex('#1A1A24')
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        title_label = Label(text="تطبيق سَكِينَة", font_size='32sp', color=get_color_from_hex('#E2E8F0'), bold=True)
        status_label = Label(text="أهلاً بك في بيئة السكينة والطمأنينة", font_size='18sp', color=get_color_from_hex('#94A3B8'))
        action_btn = Button(text="ابدأ الجلسة", font_size='20sp', size_hint=(1, 0.2), background_color=get_color_from_hex('#3B82F6'), color=get_color_from_hex('#FFFFFF'))
        layout.add_widget(title_label)
        layout.add_widget(status_label)
        layout.add_widget(action_btn)
        return layout

if __name__ == '__main__':
    SakinaApp().run()
