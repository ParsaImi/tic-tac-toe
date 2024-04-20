import tkinter as tk
window = tk.Tk()
current_ch = "X"
o_corrects = []
x_corrects = []
played_set_x = set()
played_set_o = set()
win_poses = [[(1,1) , (2,2) , (3,3)] , [(1,3) , (2,2) , (3,1)] , [(1,1) , (1,2) , (1,3)] , [(2,1) , (2,2) , (2,3)] , [(3,1) , (3,2) ,(3,3)] , [(1,1) , (2,1) , (3,1)] , [(1,2) ,(2,2) , (3,2) ] , [(1,3) , (2,3) , (3,3)]]
class XOPoint():
    def __init__(self , x , y):
        self.x = x
        self.y = y
        self.value = None
        self.btn = tk.Button(window, text = '', width=20 , height=5 , command = self.set)
        self.btn.grid(row=x , column=y)
    def set(self):
        if not self.value:
            global current_ch
            self.value = current_ch
            self.btn.config(text=current_ch)
            if current_ch == "O":
                played_set_o.add((self.x , self.y))
                current_ch = "X"
                self.checkforo()
            elif current_ch == "X":
                played_set_x.add((self.x , self.y))
                current_ch = "O"
                self.checkforx()
    def checkforx(self):
        global x_corrects
        if len(played_set_x) >= 3:
            for i in win_poses:
                for j in i :
                    if j in played_set_x:
                        x_corrects.append(j)    
                    else:
                        x_corrects = []
                        break
                if len(x_corrects) == 3:
                    window.destroy()            
    def checkforo(self):
        global o_corrects
        if len(played_set_o) >= 3:
            for i in win_poses:
                for j in i :
                    if j in played_set_o:                        
                        o_corrects.append(j)    
                    else:
                        o_corrects = []
                        break
                if len(o_corrects) == 3:
                    window.destroy()           
    def ending(self , ch):
        self.btn.config(state="disabled")
    def reset(self):
        self.btn.configure(text = "" , bg="white")
        self.value = None
for x in range(1 , 4):
    for y in range(1 , 4):
        XOPoint(x,y)
window.mainloop()