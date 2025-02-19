from gi import require_versions
require_versions({"Gtk": "4.0", "Adw": "1"})
from gi.repository import Gtk
import fdb

class Window(Gtk.ApplicationWindow):

    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Hello World")
        con = fdb.connect(dsn="DSN", user="FBTEST_USER", password="FBTEST_PASSWORD")
        # Attach to 'employee' database/alias using embedded server connecti
