import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
# import gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Driver Manager") #title
        self.set_border_width(3)


        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('Add radio buttons here'))
        self.notebook.append_page(self.page1, Gtk.Label('Nvidia GPU'))
        '''
        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        self.page2.add(Gtk.Label('A page with an image for a Title.'))
        self.notebook.append_page(
            self.page2,
            Gtk.Image.new_from_icon_name(
                "help-about",
                Gtk.IconSize.MENU
            )
        )
        '''
win = MainWindow() # makes window
win.connect("delete-event", Gtk.main_quit) #delete event to ensure that the application is terminated if we click on the x to close the window.
win.show_all() # display window
Gtk.main() #start the GTK+ processing loop which we quit when the window is closed
