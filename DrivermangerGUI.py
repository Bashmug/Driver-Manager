import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 
# import gtk 

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")


win = MyWindow() # makes window
win.connect("delete-event", Gtk.main_quit) #delete event to ensure that the application is terminated if we click on the x to close the window.
win.show_all() # display window
Gtk.main() #start the GTK+ processing loop which we quit when the window is closed

