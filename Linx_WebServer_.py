from gi.repository import Gtk
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import ipaddress
import _thread as thread
import threading


#bug Line 44: Server Hangs when calling start_server method
#bug Line 110: No verification of I.P will cause Exception --FIXED--
#bug -- Dialogs send no close signal




class myHandler(BaseHTTPRequestHandler):
    file_extension_html = '.html'
    file_extension_php = '.php'
    server_on = False
    default_www_path = "/var/www/"
    
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        
        try:
            if (self.path == "/"):
                file = open("/var/www/index.html", 'r')
                raw_data = file.read()
                encoded_data = bytes(raw_data, 'utf-8')
                file.close()
                self.wfile.write(encoded_data)
                print("Started Linx server succesfully...")
        except:
                
                self.get_request()
                error_message = bytes("Could not find default "+file_extension_html+" in current path", 'utf-8')
                self.wfile.write(error_message)

        return
    
    def start_server(ipObject, c_port):
        try:
            
            ip_address = str(ipaddress.IPv4Address(ipObject))
            server = HTTPServer((ip_address, c_port), myHandler)
            
            try:
                
                thread.start_new_thread(server.serve_forever())
                
                
            except RuntimeError as e:
                print("Error initiating thread: %s" %e)    

        except Exception as e:
            print("Error starting Linx server: %s" %e)
                

class LinxWindow(Gtk.Window):
    VERSION = "0.1"
    current_default_server_url = None
    def __init__(self):
        Gtk.Window.__init__(self, title="Linx Web Server v"+self.VERSION+" ",
                           resizable=True, default_height=400, default_width=450)

        #--Widget--Initialization
        box = Gtk.Box(spacing=10, margin_left=10, margin_top=10, margin_right=10)
        self.add(box)
        grid = Gtk.Grid()
        box.pack_start(grid, True, True, 0)
        
        

        ip_label_description = Gtk.Label("Enter I.P address")
        self.ip_Entry = Gtk.Entry()
        self.ip_Entry.set_text("127.0.0.1")
        start_server_button = Gtk.Button(label="Start Server", margin_left=10)
        start_server_button.connect("clicked", self.on_start_server_clicked)

        close_button = Gtk.Button(label="close", margin_left=10, margin_right=10)
        close_button.connect("clicked", self.on_exit)
        
        port_description = Gtk.Label("Port", margin_left=10)
        adjustment = Gtk.Adjustment(0, 8080, 54000, 1, 10, 1)
        self.port = Gtk.SpinButton()
        self.port.set_adjustment(adjustment)
        self.linkbutton = Gtk.LinkButton("http://", "Open test page")
        console = Gtk.TextView(margin=900)
        console.set_border_window_size(Gtk.TextWindowType.TOP, 300)
        
        grid.add(ip_label_description)
        grid.add(self.ip_Entry)
        grid.add(port_description)
        grid.add(self.port)
        grid.add(start_server_button)
        grid.add(close_button)
        grid.add(self.linkbutton)
        hbox = Gtk.Table(margin=10)
        grid.add(hbox)
        

        
        #--End-Widget--Initialization
        
    def on_exit(self, button):
        Gtk.main_quit
        sys.exit()

    
    def on_start_server_clicked(self, button):
        ip = self.ip_Entry.get_text()
        port = self.port.get_text()
        ip_valid = False
        port_valid = False
        
            
        if (ip != ''):
            ip_valid = True
            return ip_valid
        else:
            ip_valid = False
            return ip_valid
        if (type(port) == int):
            port_valid = True
            return port_valid
        else:
            port_valid = False
            return port_valid
       
        if (port_valid == True and ip_valid == True):
            #convert port to type int and ip to type ip object
            print("OK")
            thread.start_new_thread(start_server())
        else:
            Dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL, Gtk.ButtonsType.OK
                                       , Gtk.MessageType.INFO, "Check I.P and Port ")
            Dialog.show()
win = LinxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
