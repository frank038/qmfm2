# qmfm2
File manager for Linux in PyQt5.

Version 2 014

This is an enhanced and experimental version of qmfm version 1.
This version supports comments and emblems with some limitations: 
they will be lost after all file operations except renaming within 
this program; the comments and emblems are stored with the item full path.
This version support file, not folder, filtering; a combobox store the path of all 
the opened folders; each element in the main view can show additional custom text 
by modifying the custom_icon_text.py module; the mimetype info and label can be 
fully customized by modifying the custom_text.py module.

The zip package is just for the checksums and contains all the project files.

This program has absolutely no warranty.

Required: 
base module: Python3 (min. 3.3), Pyqt5, PyXdg, xdg-utils
optional media module: python3-dbus.
optional assmime.py in utility folder: Pyqt5, PyXdg, xdg-utils

Just launch the file qmfm2.py from the project directory to open the home folder,
or open a different folder from the command line or by chancing the config file.

------------

The optional disks and trash modules do not track any changes while their tabs are open.

The disks tab let user manage the recycle bin of every partitions, if supported.
This means the home recycle bin is indipendent from the recycle bin of the other
storage masses.

The program support custom scripts and custom thumbnailers.
Thumbnailers for images, videos (using ffmpegthumbnailer), and pdf files 
(using pdftocairo) are provided.
At the moment, the following script are provided: open xterm in the current directory (if
xterm is installed); calculate the checksum of the selected items (if the checksums
are installed); extract the content of the selected archive, alse with password 
(if 7z is installed); create a tar or tar.gz archive (if tar and gzip are installed).

Drag and Drop is supported.

The program also support the default templates directory, or a generic Templates
folder.

At the moment the hidden features are:
- CTRL+s : the window size is saved; in fullscreen mode only this state is saved.
- The program accept a folder or a file path as argument.
- When html/htm files are copied or dropped into this program the associated 
folders will be copied too, and viceversa.
- Recycle bin tabs: the files have a contextual menu; folders can be opened in a
new tab, and files opened with the default program, if any, with a double click.
- Progress dialog during copying operations: the current copying operation cannot be
interrupted, only the following ones can be interrupted.
- Delete (canc) key: selected items into the recycle bin if choosen so in the config file.

![My image](https://github.com/frank038/qmfm2/blob/master/screenshot.png)

![My image](https://github.com/frank038/qmfm2/blob/master/screenshot2.png)

This is the dialog that appears when the 'Paste and Merge' action is called.
The difference between 'Automatic' and 'Backup': both add a suffix to a file or folder if another item with the same name already exists at destination, Automatic add it to the item to be copied, Backup add it to the item at destination.
![My image](https://github.com/frank038/qmfm2/blob/master/screenshot3.png)
