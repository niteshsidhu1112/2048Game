#from future.moves import tkinter
#import tkinter as tk
from tkinter import Frame,Label,CENTER

import LogicsFinal
import constants as c
class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title('2048')
        self.master.bind('<Key>',self.key_down)
        self.comands={c.KEY_UP:LogicsFinal.moveup,c.KEY_DOWN:LogicsFinal.movedown,c.KEY_LEFT:LogicsFinal.moveleft,c.KEY_RIGHT:LogicsFinal.moveright}
        self.grid_cells=[]
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()
        self.mainloop()

    def init_grid(self):
        background=Frame(self,bg=c.BACKGROUND_COLOR_GAME,width=c.Size,height=c.Size)
        background.grid()
        for i in range(c.GRIDLEN):
            grid_row=[]
            for j in range(c.GRIDLEN):
                cell=Frame(background,bg=c.BACKGROUND_COLOR_CELL_EMPTY,width=c.Size/c.GRIDLEN,height=c.Size/c.GRIDLEN)
                cell.grid(row=i,column=j,padx=c.GRID_PADDING,pady=c.GRID_PADDING)
                t=Label(master=cell,text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY,justify=CENTER,font=c.FONT,width=5,height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)


    def init_matrix(self):
        self.matrix=LogicsFinal.gameStart()
        LogicsFinal.add_random2(self.matrix)
        LogicsFinal.add_random2(self.matrix)

    def update_grid_cells(self):
        for i in range(c.GRIDLEN):
            for j in range(c.GRIDLEN):
                new_number=self.matrix[i][j]
                if new_number==0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(new_number),bg=c.BACKGROUND_COLOR_DICT[new_number],fg=c.CELL_COLOR_DICT[new_number])
        self.update_idletasks()

    def key_down(self,event):
        key=repr(event.char)
        if key in self.comands:
            self.matrix,changed=self.comands[repr(event.char)](self.matrix)

            if changed:
                LogicsFinal.add_random2(self.matrix)
                self.update_grid_cells()
                changed=False
                if LogicsFinal.get_current_state(self.matrix)=="WON":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="WON",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                if LogicsFinal.get_current_state(self.matrix)=="LOST":
                    self.grid_cells[1][1].configure(text="YOU",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(text="LOSE",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
gamegrid=Game2048()











