import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Start_Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self,title="Antergos Driver Manager") # defining the title
        self.set_border_width(10)
        self.set_default_size(600, 400)


        self.connect('delete-event', Gtk.main_quit)
        icontheme = Gtk.IconTheme.get_default()
        self.icon = icontheme.load_icon(Gtk.STOCK_FLOPPY, 128, 0)
        self.set_icon(self.icon)

        # starting with notebook  from here
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        self.notebook.set_tab_pos(Gtk.PositionType.LEFT) # this part helped by elya5 on stackoverflow
        # nvidia Page / graphic driver later add AMD and others too
        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.notebook.append_page(self.page1, Gtk.Label('Graphic Driver'))
        self.page1.add(Gtk.Label('Nvidia'))

        self.page2 = Gtk.Box()
        self.page2.set_border_width(10)
        #self.notebook.append_page(self.page2,Gtk.Image.new_from_icon_name("wifi",Gtk.IconSize.MENU))
        self.notebook.append_page(self.page2,Gtk.Label('Wifi'))

        self.page3 = Gtk.Box()
        self.page3.set_border_width(10)
        self.notebook.append_page(self.page3,Gtk.Label('About'))
        self.page3.add(Gtk.Label('About'))


win = Start_Window()
win.show_all()
Gtk.main()
