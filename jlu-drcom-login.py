import client
from gi.repository import Gtk

class Handler:
    def onDeleteWindow (self, *args):
        # TODO: kill the backend to close the window
        Gtk.main_quit (*args)

    def onLogin (self, login_button):
        print ("\"login button\" was clicked")
        username = user_entry.get_text ()
        password = pass_entry.get_text ()
        print (username + "\n" + password)
        client.on_login (username, password)

builder = Gtk.Builder ()
builder.add_from_file ("jlu-drcom-login.glade")
builder.connect_signals (Handler ())

user_entry = builder.get_object ("user_entry")
pass_entry = builder.get_object ("pass_entry")
login_button = builder.get_object ("login_button")

window = builder.get_object ("main_window")
window.show_all ()

Gtk.main ()
