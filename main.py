from kivy.app import App
 fr om kivy.uix.boxlayout import BoxLayout
 fr om kivy.uix.label import Label
 fr om kivy.uix.switch import Switch
 fr om kivy.uix.slider import Slider
 fr om kivy.uix.button import Button

class NexoOSApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 25
        self.spacing = 20
        
        # Título
        self.add_widget(Label(text="Nexo-OS Personalización", font_size=28, bold=True, color=(0.3, 0.8, 1, 1)))
        
        # Sección 1: Tema oscuro
        self.add_widget(Label(text="Tema Oscuro", font_size=20))
        switch_dark = Switch(active=True)
        switch_dark.bind(active=self.on_dark_mode)
        self.add_widget(switch_dark)
        
        # Sección 2: Brillo
        self.add_widget(Label(text="Brillo de pantalla", font_size=20))
        slider = Slider(min=0, max=100, value=70)
        slider.bind(value=self.on_brightness)
        self.add_widget(slider)
        self.brightness_label = Label(text="70%")
        self.add_widget(self.brightness_label)
        
        # Sección 3: Animaciones
        self.add_widget(Label(text="Animaciones activadas", font_size=20))
        switch_anim = Switch(active=True)
        self.add_widget(switch_anim)
        
        # Botón aplicar
        btn = Button(text="Aplicar cambios", size_hint_y=None, height=60, background_color=(0.2, 0.6, 1, 1))
        btn.bind(on_press=self.apply_changes)
        self.add_widget(btn)
        
        self.status = Label(text="Listo para personalizar", font_size=16)
        self.add_widget(self.status)
    
    def on_dark_mode(self, instance, value):
        self.status.text = "Tema oscuro: " + ("Activado" if value else "Desactivado")
    
    def on_brightness(self, instance, value):
        self.brightness_label.text = f"{int(value)}%"
    
    def apply_changes(self, instance):
        self.status.text = "✅ Cambios aplicados correctamente!"

class NexoOSAndroidApp(App):
    def build(self):
        return NexoOSApp()

if __name__ == "__main__":
    NexoOSAndroidApp().run()