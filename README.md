Linx_Web_Server
===============

A simple python HTTP Web Server

This script creates an HTTP Server to server pages. It will only server one page which is the index page.
Make sure you start it on an available port and I.P (Loopback will work, obviously) 

Make sure you have GTK installed before you run the script. You can download GTK here http://www.pygtk.org/.

Still work in progress though.

To run script: sudo python3.4 Linx_WebServer.py.

NOTE: GUI will lock while lock while doing ayncronous work using select[, , , ] until I find a work around. That does not mean the app hanged. The server thread will still be running until you send an interupt.
