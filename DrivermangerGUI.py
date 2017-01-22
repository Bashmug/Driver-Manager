import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk 
# import gtk 

win = Gtk.Window() # makes empty window
win.connect("delete-event", Gtk.main_quit) #delete event to ensure that the application is terminated if we click on the x to close the window.
win.show_all() # display window
Gtk.main() #start the GTK+ processing loop which we quit when the window is closed

