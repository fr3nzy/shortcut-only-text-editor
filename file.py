#!/usr/bin/env python3

from gi.repository import Gtk, Gdk

class DeSedit(Gtk.Window):
	def __init__(self):
		Gtk.Window.__init__(self, title="DeSedit")

		self.set_default_size(650, 500)

		# keyboard shortcuts
		""" <Control>O """
		accel = Gtk.AccelGroup()
		accel.connect(Gdk.keyval_from_name('O'), Gdk.ModifierType.CONTROL_MASK, 0, self.on_o_pressed)
		self.add_accel_group(accel)
		""" <Control>S """
		accel1 = Gtk.AccelGroup()
		accel1.connect(Gdk.keyval_from_name('S'), Gdk.ModifierType.CONTROL_MASK, 0, self.on_s_pressed)
		self.add_accel_group(accel1)

		# grid to organize widgets
		self.box = Gtk.Box()
		self.box.set_orientation(Gtk.Orientation.VERTICAL)
		self.add(self.box)
		# text view
		self.textview = Gtk.TextView()
		self.textview.set_wrap_mode(True)
		self.textbuffer = self.textview.get_buffer()
		# scroll bar
		scrollwindow = Gtk.ScrolledWindow()
		scrollwindow.add(self.textview)
		self.box.pack_start(scrollwindow, True, True, 0)

	# open file dialog
	def on_o_pressed(self, *args):
		openDialog = Gtk.FileChooserDialog("Select file to be opened", self,
			Gtk.FileChooserAction.OPEN,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
		response = openDialog.run()
		if response == Gtk.ResponseType.OK:
			filename = openDialog.get_filename()
			with open(filename, 'r') as fRead:
				data = fRead.read()
				self.textbuffer.set_text(data)
				self.set_title(filename + " - DeSedit")
				fRead.close()
			openDialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			openDialog.destroy()

	# save file dialog
	def on_s_pressed(self, *args):
		saveDialog = Gtk.FileChooserDialog("Select folder to save file", self,
			Gtk.FileChooserAction.SAVE,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		filename = saveDialog.get_filename()
		if not filename:
			print("no file slected for saving")
		response = saveDialog.run()

		if response == Gtk.ResponseType.OK:
			with open(filename, 'w') as fWrite:
				data = self.textbuffer.get_text(self.textbuffer.get_start_iter(),
												self.textbuffer.get_end_iter(), True)
				fWrite.write(data)
				fWrite.close()
			saveDialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			saveDialog.destroy()



window = DeSedit()  # create DeSedit object
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
