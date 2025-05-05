#  jack_connection_manager/qt.py
#
#  Copyright 2025 liyang <liyang@veronica>
#
"""
PyQt wrapper for using JackConnectionManager in Qt applications.
"""
from PyQt5.QtCore import QObject, pyqtSignal
from jack_connection_manager import _JackConnectionManager, JackPort


class QtJackConnectionManager(QObject, _JackConnectionManager):
	"""
	Class which provides PyQt signals when jack connection graph changes occur.
	"""

	sig_error = pyqtSignal(str)
	sig_port_registration = pyqtSignal(JackPort, int)
	sig_port_connect = pyqtSignal(JackPort, JackPort, bool)
	sig_port_rename = pyqtSignal(JackPort, str, str)
	sig_shutdown = pyqtSignal()

	def _error_callback(self, error):
		self.sig_error.emit(error.decode(jacklib.ENCODING, errors='ignore'))

	def _port_registration_callback(self, port_id, action, *args):
		self.sig_port_registration.emit(self.get_port_by_id(port_id), action)

	def _port_connect_callback(self, port_a_id, port_b_id, connect, *args):
		self.sig_port_connect.emit(
			self.get_port_by_id(port_a_id),
			self.get_port_by_id(port_b_id),
			bool(connect)
		)

	def _port_rename_callback(self, port_id, old_name, new_name, *args):
		self.sig_port_rename.emit(
			self.get_port_by_id(port_id),
			old_name.decode(jacklib.ENCODING, errors='ignore') if old_name else 'NO_OLD_NAME',
			new_name.decode(jacklib.ENCODING, errors='ignore') if new_name else 'NO_NEW_NAME'
		)

	def _xrun_callback(self, arg):
		self.xruns += 1
		return 0

	def _shutdown_callback(self, *args):
		self.sig_shutdown.emit()
		self.client = None


#  end jack_connection_manager/qt.py
