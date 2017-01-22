import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# import gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Driver Manager") #title
        self.set_border_width(10)

        #self.notebook = Gtk.Notebook()
        #self.set_default_size(500, 300)
        #self.notebook.set_tab_pos(gtk.POS_TOP)
        #self.add(self.notebook)
        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button1 = Gtk.RadioButton.new_with_label_from_widget(None, "Button 1")
        button1.connect("toggled", self.on_button_toggled, "1")
        hbox.pack_start(button1, False, False, 0)

        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("Button 2")
        button2.connect("toggled", self.on_button_toggled, "2")
        hbox.pack_start(button2, False, False, 0)

        button3 = Gtk.RadioButton.new_with_mnemonic_from_widget(button1,
            "B_utton 3")
        button3.connect("toggled", self.on_button_toggled, "3")
        hbox.pack_start(button3, False, False, 0)

    def on_button_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Button", name, "was turned", state)

        #self.notebook.append_page(self.page1, Gtk.Label('Nvidia GPU'))

win = MainWindow() # makes window
win.connect("delete-event", Gtk.main_quit) #delete event to ensure that the application is terminated if we click on the x to close the window.
win.show_all() # display window
Gtk.main() #start the GTK+ processing loop which we quit when the window is closed
