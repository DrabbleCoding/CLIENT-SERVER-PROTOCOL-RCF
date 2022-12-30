"""
Shima Iraniparast, Tino Nyakurerwa
"""


# Import socket module
from socket import * 
import sys # In order to terminate the program
from threading import Thread 
from SocketServer import ThreadingMixIn 

# Create a TCP server socket
#(AF_INET is used for IPv4 protocols)
#(SOCK_STREAM is used for TCP)
serverName = "localhost"

serverSocket = socket(AF_INET, SOCK_STREAM)

portLocation = 3333
boardWidth = 200
boardHeight = 100

# Assign a port number
serverPort = 6789

# Bind the socket to server address and server port
serverSocket.bind((serserverName,serverPort))

# Listen to at most 1 connection at a time
serverSocket.listen(1)

print ('The server is ready to receive')

# Server should be up and running and listening to the incoming connections

while True:
	print('The server is ready to receive')

	# Set up a new connection from the client
	connectionSocket, addr = serverSocket.accept()

	
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()



serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data



# Multithreaded Python server : TCP Server Socket Thread Pool
class ClientThread(Thread): 
 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print "[+] New server socket thread started for " + ip + ":" + str(port) 
 
    def run(self): 
        while True : 
            data = conn.recv(2048) 
            print "Server received data:", data
            MESSAGE = raw_input("Multithreaded Python server : Enter Response from Server/Enter exit:")
            if MESSAGE == 'exit':
                break
            conn.send(MESSAGE)  # echo 

# Multithreaded Python server : TCP Server Socket Program Stub
TCP_IP = '0.0.0.0' 
TCP_PORT = 2004 
BUFFER_SIZE = 20  # Usually 1024, but we need quick response 

tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
tcpServer.bind((TCP_IP, TCP_PORT)) 
threads = [] 
 
while True: 
    tcpServer.listen(4) 
    print "Multithreaded Python server : Waiting for connections from TCP clients..." 
    (conn, (ip,port)) = tcpServer.accept() 
    newthread = ClientThread(ip,port) 
    newthread.start() 
    threads.append(newthread) 
 
for t in threads: 
    t.join() 


import tkinter 
#import tkSimpleDialog
from tkinter import *


#main application window creation
class TCPGUI:

    def __init__(self, master):
        self.master = master
        master.title("Client GUI")

        #initoialising user given values
        #setting lables
        self.message = "Welcome hope you have a good time"
        self.label_text= StringVar()
        self.label_text.set(self.message)
        self.label=Label(master, textvariable= self.label_text)
        
        self.label_IPadd=Label(master, text="IP Address: ").grid(row=1)
        self.label_port_num= Label(master, text="Port Number: ").grid(row=2)
        self.label_post_info=Label(master, text="Post Text in the form of coord1 coord2 width height colour text: ").grid(row=3)

        #text area to get the values
        self.IPaddress = Entry(master)
        self.Port_num = Entry(master)
        self.post_text = Entry(master)
        self.post_cord1 = Entry(master)
        self.post_cord2 = Entry(master)
        self.post_width= Entry(master)
        self.post_height= Entry(master)
        self.post_colour= Entry(master)

        self.label.grid(row= 0)
        self.IPaddress.grid(row = 1, column=1 )
        self.Port_num.grid(row= 2, column = 1)
        #you can change cord 1 and two if you need to and then just remove one of the text fields
        self.post_cord1.grid(row=3, column=1)
        self.post_cord2.grid(row=3, column = 2)
        self.post_width.grid(row=3, column = 3)
        self.post_height.grid(row=3, column = 4)
        self.post_colour.grid(row=3, column = 5)
        self.post_text.grid(row = 3, column =6)

        #creating buttons - to have them connect to the function use command = self.function name
        self.connect_button = Button(master, text="Connect", command = self.connect_event, width = 10)
        self.disconnect_button= Button(master, text="Disconncet", command = self.disconnect, width = 10, state = DISABLED)
        
        #GET NEEDS TO BRING UP DIALOGUE
        self.get_button = Button(master, text = "GET",command = self.get_for_get, width = 10, state= DISABLED)
        self.pin_button =  Button(master, text = "PIN",command = self.get_pin_coord, width = 10,state = DISABLED)
        self.unpin_button =  Button(master, text = "UNPIN",command = self.get_unpin_coord, width = 10,state = DISABLED)
        
        #putting buttons in the grid
        self.connect_button.grid(row= 5, column= 0, sticky = W)
        self.get_button.grid(row = 5, column= 1, sticky= W)
        self.pin_button.grid(row = 5, column = 2,sticky= W)
        self.unpin_button.grid(row = 5, column = 3,sticky= W)
        self.disconnect_button.grid(row = 5, column = 4,sticky= W)
        
        self.coord2= None
        self.coord1= None
        self.get_color = None
        self.get_coord1= None
        self.get_coord2= None
        self.get_refersTo = None

        self.get_message=None
        #self.norm_message= None
    
    #pin/unpin popup
    def get_pin_coord(self):
        top = self.top = Toplevel(self.master)
        
        self.top_label=Label(top, text="Enter coordinates of pin to be pinned: ").grid(row=0)
        self.coord1 = Entry(top)
        self.coord2= Entry(top)
        self.coord1.grid(row = 1,column = 0)
        self.coord2.grid(row=1, column=1 )
        self.ok_button= Button(top, text="OK", command= self.ok_pin)
        self.ok_button.grid(row= 3, column= 0)

    def get_unpin_coord(self):
        top = self.top = Toplevel(self.master)
        
        self.top_label=Label(top, text="Enter coordinates of pin to be  unpinned: ").grid(row=0)
        self.coord1 = Entry(top)
        self.coord2= Entry(top)
        self.coord1.grid(row = 1,column = 0)
        self.coord2.grid(row=1, column=1 )
        self.ok_button= Button(top, text="OK", command= self.ok_unpin)
        self.ok_button.grid(row= 3, column= 0)

    
    def ok_pin(self):
    
        if self.coord1 is not None  and self.coord2 is not None :
            self.message= "The post has been pinned" 
             #can call fnction using int(self.coord1.get())
        else:
            self.message = "Could not process request"
        self.label_text.set(self.message)
        self.top.destroy()

    def ok_unpin(self):
        
        if self.coord1 is None  and self.coord2 is None :
            self.message = "Could not process request"
             #can call fnction using int(self.coord1.get())
        else:
            self.message= "The post has been unpinned" 
            
        self.label_text.set(self.message)
        self.top.destroy() 
    
    #get attribute

    def get_for_get(self):

        top = self.top = Toplevel(self.master)

        self.top_label=Label(top, text="Enter attributes of post to be retrieved: ").grid(row=0)
        self.get_color = Entry(top)
        self.get_coord1= Entry(top)
        self.get_coord2= Entry(top)
        self.get_refersTo = Entry(top)
        self.get_color_label= Label(top, text= "Colour:").grid(row=1)
        self.get_color.grid(row=1, column = 1)
        self.get_coord_label= Label(top, text= "Coordinates").grid(row=2)
        self.get_coord1.grid(row = 2,column = 1)
        self.get_coord2.grid(row=2, column=2)
        self.get_refersTo_label= Label(top, text= "Refers To:").grid(row= 3)
        self.get_refersTo.grid(row=3, column= 1)
        self.ok_button= Button(top, text="OK", command= self.ok_get)
        self.ok_button.grid(row= 4, column= 1)
    
    def ok_get(self):

        self.message= "Your get request has been processed"
        self.label_text.set(self.message)
        self.top.destroy()
        # didn't know how to handle this part because don't kow your code as yet.
    def connect_event(self):

        top = self.top = Toplevel(self.master)

        self.top_label=Label(top, text="Enter conecttion values: ").grid(row=0)
        self.connect_values = Entry(top)
        self.connect_values.grid(row=1, column =0, columnspan= 10 )
        self.ok_button= Button(top, text="OK", command= self.ok_connect)
        self.ok_button.grid(row= 2, column= 0)
    
    def connect_event(self):
        self.connect_button.configure( state= DISABLED)
        self.disconnect_button.configure( state= NORMAL)
        
        self.get_button.configure( state= NORMAL)
        self.pin_button.configure( state= NORMAL)
        self.unpin_button.configure( state= NORMAL)
        self.message= "You are now connected to the server "
        self.label_text.set(self.message)
        #self.change_buttons
        self.top.destroy()
    
    def disconnect(self):
        # call function

        self.master.destroy()
        
        
        


root= Tk()
tcp_gui= TCPGUI(root)
root.mainloop()

"""   
mainWindow=tk.Tk()

mainWindow.title('CP372 ASSIGNMENT ONE')
mainFrame = Frame(mainWindow)
mainFrame.pack()

mainLabel = Label(mainFrame, text= 'Let us get that sexy A')
mainLabel.pack()


pinButton= tk.Button(mainFrame, text='Pin', width = 25, command= mainWindow.destroy)
connectButton= tk.Button(mainFrame, text='Connect', width = 25,command= mainWindow.destroy)
connectButton.pack(side= LEFT)

pinButton.pack(side= RIGHT)

mainWindow.mainloop()
"""
