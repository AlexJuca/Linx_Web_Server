"""
@author: Alexandre Antonio Juca <corextechnologies@gmail.com

Linx Configuration File
"""

class Defaults():

    __DEFAULT_IP__ = "127.0.0.7"
    __DEFAULT__PORT__ = 8080
    __ERROR_MSG_PORT_OR_IP = "Please pleaser a valid IP address or Port number"
    __ERROR_MSG__INVALID_IP = "Please enter a valid I.P address eg.192.168.1.1"
    __ERROR__MSG_GENERAL = "Please enter a valid PORT number. eg 80, 8080"
    __TITLE__ = "Linx Web Server"
    
    __ABOUT__="""   Linx HTTP Server
                    ##############
           @author : Alexandre Antonio Juca
           @version : 0.1
           Info: This is a simple HTTP Server, You should be cautious to not bind
           to an socket that has already beeing taken, so please use the socket 127.0.0.7
           in most cases.

           Also keep in mind the port that you start the Linx server has to be a valid port
           number that the socket can communicate over HTTP, Port 80 in most cases would
           most likely be used by another application like apache or nginx so avoid that.

           Please refrain from using port 40, 113, 445 because they are reserved.
           Please make sure to start the server on a valid I.P address and port.

           Any bugs email: Alexandre Antonio Juca <corextechnologies@gmail.com>



           """

    __DEFAULT_HTML__ = """
            <!DOCTYPE html >
            <html>
            <head>
            <title> Default Linx Server page </title>
            </head>
            <body>


            <h2> Linx Server: If you see this page it is becaue the server is up and running correctly </h2>

            <h6>I.P: 127.0.0.7 Port: 8080 </h6> 


            </body>
            </html>
            """
                  

