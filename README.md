# jack_connection_manager

Classes for managing jack client connections.

These differ from the JACK Client for Python (jack), in that it makes possible
connecting and disconnecting ports which are not "owned" by a client created in
your process.

There is also an (optionally installed) QtJackConnectionManager which emits
signals when events of interest happen. In order to use the
QtJackConnectionManager class, you must install with the "\[Qt\]" option, like so:

	$ pip install jack_connection_manager[Qt]

### Using the plain (non-Qt) version

Import JackConnectionManager:

	from jack_connection_manager import JackConnectionManager

Create an instance using standard constructor syntax ...

	self.conn_man = JackConnectionManager()

... or use it as a context manage:

	with JackConnectionManager() as conn_man:

The non-Qt version uses callbacks to inform your program when events of
interest happen. Register your functions as callbacks using the "on_<event>"
methods:

	self.conn_man.on_client_registration(self.jack_client_reg)
	self.conn_man.on_port_registration(self.jack_port_reg)
	self.conn_man.on_shutdown(self.close)

### Using the Qt version:

In order to use the Qt version, you must import "QtJackConnectionManager" from
the jack_connection_manager.qt module.

	from jack_connection_manager.qt import QtJackConnectionManager
	self.conn_man = QtJackConnectionManager(client_name = "DescriptiveClientName")

The Qt version forsakes callbacks for the Qt signal/slot mechanism. To
subscribe signals which are generated on events of interest:

	self.conn_man.sig_client_registration.connect(self.slot_client_registration)
	self.conn_man.sig_port_registration.connect(self.slot_port_registration)
	self.conn_man.sig_shutdown.connect(self.slot_shutdown)

Refer to the help text to determine the function arguments to use in the callbacks or slots.

## Help

Refer to the help for jack_connection_manager. From python:

	>>> import jack_connection_manager
	>>> help(jack_connection_manager)

	>>> import jack_connection_manager.qt
	>>> help(jack_connection_manager.qt)

