"""

@author: Alexandre Antonio Juca <corextechnologies@gmail.com


Linx HTTP Server: A simple HTTP Server for serving html web pages




"""


#bug Line 44: Server Hangs when calling start_server() method
#bug Line 110: No verification of I.P will cause Exception --FIXED--
#bug -- Dialogs send no close signal --FIXED--
#TODO -- ADD CONSOLE WINDOW with green text and background set to #000 --DONE--
#TODO -- Change index page ip and port to current values


from gi.repository import Gtk, Gdk
import sys
import socketserver
from http.server import BaseHTTPRequestHandler, HTTPServer
import ipaddress
import _thread as thread
import Defaults


""" Default values """

__ABOUT__= Defaults.Defaults.__ABOUT__


class indexPageWriter():

    def __init__(self, ipObject, port):
        ip = ipaddress.Ipv4Address(ipObject)
        cport = str(port)
        indexpage = open(myHandler.get_default_path(), 'w')
        
class myHandler(BaseHTTPRequestHandler):
    """ Later these configuration options will have to be set in a seperate config file """
    file_extension_html = '.html'
    file_extension_php = '.php'
    server_on = False
    default_www_path = "/var/www/"
    """ --------------------------------------------------------------------------------"""
    
    def get_default_path(self):
        full_default_path = self.default_www_path+self.file_extension_html
        return full_default_path
    
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        try:
            if (self.path == "/"):
                file = open("/var/www/index.html", 'r')
                raw_data = file.read()
                #convert binary data to utf-8 for display in browser
                encoded_data = bytes(raw_data, 'utf-8')
                file.close()
                #print content sto web browser
                self.wfile.write(encoded_data)
        except:
                #self.get_request()
                error_message = bytes("Could not find default "+file_extension_html+" in current path", 'utf-8')
                self.wfile.write(error_message)
        return
    # args
    def start_server(ipObject, c_port):
        """Start the Linx HTTP Server"""
   
        try:
            ip_address = str(ipaddress.IPv4Address(ipObject))#convert IPv4 object to str
            server = HTTPServer((ip_address, c_port), myHandler)
            try:
                print("Started Linx server succesfully...")
                server.serve_forever()
                
            except Exception as e:
                win = Gtk.Window()
                LinxWindow.exceptionDialog(win, e)
        except Exception as e:
            
            win = Gtk.Window()#window object to pass to method to properly display Dialog
            LinxWindow.exceptionDialog(win, e)#call method to handle Dialog messages created with no Gtk.Window instance  
            
                
class LinxWindow(Gtk.Window):
    VERSION = "0.1"
    current_default_server_url = None
    
    def __init__(self):
        win = Gtk.Window.__init__(self, title="Linx Web Server v"+self.VERSION+" ",
                           resizable=True, default_height=400, default_width=450)
        #--Begin-Widget--Initialization
        box = Gtk.Box(spacing=10, margin_left=10, margin_top=10, margin_right=10)
        self.add(box)
        grid = Gtk.Grid()
        box.pack_start(grid, True, True, 0)
        ip_label_description = Gtk.Label("Enter I.P address")
        self.ip_Entry = Gtk.Entry()
        self.ip_Entry.set_text("127.0.0.7")
        start_server_button = Gtk.Button(label="Start Server", margin_left=10)
        start_server_button.connect("clicked", self.on_start_server_clicked)
        close_button = Gtk.Button(label="close", margin_left=10, margin_right=10)
        close_button.connect("clicked", self.on_exit)
        port_description = Gtk.Label("Port", margin_left=10)
        adjustment = Gtk.Adjustment(0, 0, 54000, 1, 10, 1)
        self.port = Gtk.SpinButton()
        self.port.set_adjustment(adjustment)
        self.linkbutton = Gtk.LinkButton("http://", "see test page")
        
        #Change TextView Color properties
        bg = Gdk.Color(0, 2000, 1000)
        text_color = Gdk.Color(0, 42000, 0)
        textbuf = Gtk.TextBuffer(text=__ABOUT__) 
        self.console = Gtk.TextView( margin=10, buffer=textbuf)
        self.console.set_size_request(400, 400)
        self.console.modify_bg(Gtk.StateType.NORMAL, bg)
        self.console.modify_fg(Gtk.StateType.NORMAL, text_color)
        #Change TextView Color properties
        self.console.set_border_window_size(Gtk.TextWindowType.BOTTOM, 10)
        
        
        
        
        box.pack_start(self.console, False, False, 0)
        grid.add(ip_label_description)
        grid.add(self.ip_Entry)
        grid.add(port_description)
        grid.add(self.port)
        grid.add(start_server_button)
        grid.add(close_button)
        grid.add(self.linkbutton)
        #--End-Widget--Initialization

    def writeToConsole (self, text):		
        """
          This function will be used to append text into the consoles textBuffer
        """
        textBuff = Gtk.TextBuffer(text=text)
        self.console.set_buffer(textBuff)
        
    def exceptionDialog (win, e):
        Dialog = Gtk.MessageDialog(win, Gtk.DialogFlags.MODAL, Gtk.MessageType.ERROR, Gtk.ButtonsType.OK,
                                   "Error starting Linx: %s" %e)
        Gtk.Dialog.run(Dialog)
        Gtk.Widget.destroy(Dialog)
        
    def on_exit(self, button):
        Gtk.main_quit
        sys.exit()
        
    def on_start_server_clicked(self, button):
        
        ip = self.ip_Entry.get_text()
        port = self.port.get_text()    
        if (ip != ''):
            try:
                try:
                    ip_x = ipaddress.ip_address(ip)
                    xport = int(port)
                    if (type(xport) == int):
                
                        self.linkbutton.set_uri("http://"+ip+":"+str(xport))
                        ip_x = ipaddress.ip_address(ip)
                        try:
                            myHandler.start_server(ip_x, xport)
                        except Exception as e:
                            print(" %s " %e)
                            Dialog = Gtk.MessageDialog(self,Gtk.DialogFlags.MODAL,
                                                   Gtk.MessageType.ERROR,
                                                   Gtk.ButtonsType.OK, "Error creating server: %s" %e)
                            Gtk.Dialog.run(Dialog)
                            Gtk.Widget.destroy(Dialog)
                    
                    else:
                        Dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL,
                                               Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "Please enter a valid PORT number. eg 80, 8080")
                    
                        Gtk.Dialog.run(Dialog)
                        Gtk.Widget.destroy(Dialog)
                except:
                    Dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL, Gtk.MessageType.INFO, Gtk.ButtonsType.OK,
                                               "Please pleaser a valid IP address or Port number")
                    Dialog.run()
                    Gtk.Widget.destroy(Dialog)
                
                    return
                
                
            except:
                Dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL
                                  ,Gtk.MessageType.INFO, Gtk.ButtonsType.OK,"Please enter a valid I.P address eg.192.168.1.1")
                
                Gtk.Dialog.run(Dialog)
                Gtk.Widget.destroy(Dialog)
                
                
        else:
            Dialog = Gtk.MessageDialog(self, Gtk.DialogFlags.MODAL
                                  ,Gtk.MessageType.INFO, Gtk.ButtonsType.OK,"Please enter a valid I.P address eg.192.168.1.2")
            Gtk.Dialog.run(Dialog)
            Gtk.Widget.destroy(Dialog)
            
            
win = LinxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
