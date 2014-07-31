"""
@author: Alexandre Antonio Juca <corextechnologies@gmail.com

Linx Configuration File
"""

class Defaults():
    
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
                  

