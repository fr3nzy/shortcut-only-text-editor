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
		""" <Control>I """
		self.accel2 = Gtk.AccelGroup()
		self.accel2.connect(Gdk.keyval_from_name('I'), Gdk.ModifierType.CONTROL_MASK, 0, self.on_i_pressed)
		self.add_accel_group(self.accel2)
		""" <Control>B """
		self.accel3 = Gtk.AccelGroup()
		self.accel3.connect(Gdk.keyval_from_name('B'), Gdk.ModifierType.CONTROL_MASK, 0 , self.on_b_pressed)
		self.add_accel_group(self.accel3)
		""" <Control>U """
		self.accel4 = Gtk.AccelGroup()
		self.accel4.connect(Gdk.keyval_from_name('U'), Gdk.ModifierType.CONTROL_MASK, 0, self.on_u_pressed)

		# grid to organize widgets
		self.box = Gtk.Box()
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
		if self.set_title == (filename + " - DeSedit"):
			print("hmm")
		saveDialog = Gtk.FileChooserDialog("Select folder to save file", self,
			Gtk.FileChooserAction.SAVE,
			(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
			Gtk.STOCK_SAVE, Gtk.ResponseType.OK))
		response = saveDialog.run()
		if response == Gtk.ResponseType.OK:
			filename = saveDialog.get_filename()
			with open(filename, 'w') as fWrite:
				data = self.textbuffer.get_text(self.textbuffer.get_start_iter(),
												self.textbuffer.get_end_iter(), True)
				fWrite.write(data)
				fWrite.close()
			saveDialog.destroy()
		elif response == Gtk.ResponseType.CANCEL:
			saveDialog.destroy()
			
	def on_i_pressed(self, *args):
	    bounds = self.textbuffer.get_selection_bounds()
	    if len(bounds) not 0:
	    	start, end = bounds
	    	self.textbuffer.apply_tag(self.tag_italic, start, end)
	     
	def on_b_pressed(self, *args):
		bounds = self.textbuffer.get_selection_bounds()
	    if len(bounds) not 0:
	    	start, end = bounds
	    	self.textbuffer.apply_tag(self.tag_bold, start, end)
	    
    def on_u_pressed(self, *args):
    	bounds = self.textbuffer.get_selection_bounds()
	    if len(bounds) not 0:
	    	start, end = bounds
	    	self.textbuffer.apply_tag(self.tag_underline, start, end)

window = DeSedit()  # create DeSedit object
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
