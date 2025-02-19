from gi import require_versions
require_versions({"Gtk": "4.0", "Adw": "1"})
from gi.repository import Gtk
from firebird.driver import connect

class Window(Gtk.ApplicationWindow):

    def __init__(self, app):
        super().__init__(application=app)
        self.set_title("Hello World")

        # Attach to 'employee' database/alias using embedded server connection
        con = connect('employee', user='sysdba', password='masterkey')

        # Attach to 'employee' database/alias using local server connection
        from firebird.driver import driver_config
        driver_config.server_defaults.host.value = 'localhost'
        con = connect('employee', user='sysdba', password='masterkey')

        # Set 'user' and 'password' via configuration
        driver_config.server_defaults.user.value = 'SYSDBA'
        driver_config.server_defaults.password.value = 'masterkey'
        con = connect('employee')
