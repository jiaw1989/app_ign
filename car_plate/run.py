from car_plate_letter_numbers import *

from Tkinter import *
class car_plate_ui:
    '''A simple counter GUI using object-oriented programming.'''
    def __init__(self, parent):
        '''Create the GUI.'''
        # Framework.
        self.parent = parent
        self.frame = Frame(parent)
        self.frame.pack()
        # Model.
        self.pop = StringVar()
        self.pat = StringVar()
        self.total= StringVar()
        self.excess = StringVar()
        # Label displaying current state.
        
        self.label0 = Label(self.frame, text='Input population to calculate pattern of plates:')
        self.label0.pack()  
        
        self.text = Text(self.frame, height=10, width=20)
        self.text.pack()        
        

        # Buttons to control application.
        self.up = Button(self.frame, text='Calculate', command=self.count_plate)
        self.up.pack()
        self.right = Button(self.frame, text='quit', command=self.quitClick)
        self.right.pack()
        self.label1 = Label(self.frame, text='population:')
        self.label1.pack()   
        self.label11 = Label(self.frame, textvariable=self.pop)
        self.label11.pack()  
        self.label2 = Label(self.frame, text='pattern: ')
        self.label2.pack()           
        self.label21 = Label(self.frame,textvariable=self.pat)
        self.label21.pack()  
        self.label3 = Label(self.frame, text='total plate: ')
        self.label3.pack()           
        self.label31 = Label(self.frame, textvariable=self.total)
        self.label31.pack()     
        self.label4 = Label(self.frame, text='excess plate: ')
        self.label4.pack()                           
        self.label41 = Label(self.frame, textvariable=self.excess)
        self.label41.pack()                   
        
   

    def count_plate(self):
        '''Handle click on 'count_plate' button.'''
        population = int(self.text.get(1.0,END))
        # set all the caculated values
        self.pop.set(str(population))
        self.pat.set(str(car_plate(population)[0])+" letters "+str(car_plate(population)[1])+" numbers")
        self.total.set(str(car_plate(population)[2]))
        self.excess.set(str(car_plate(population)[3]))
        
        
    def quitClick(self):
        '''Handle click on 'quit' button.'''
        self.parent.destroy()
        
        
        
if __name__ == '__main__':
    window = Tk()
    myapp = car_plate_ui(window)
    window.mainloop()