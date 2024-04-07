from tkinter import *
from cell import Cell
import utilities
import settings


        
root = Tk()

root.config(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper game test")
root.resizable(True, True)


top_frame = Frame(root,
                  bg="black",
                  width=settings.WIDTH,
                  height=utilities.calculating_height_precentage(20))
side_frame = Frame(root,
                   bg="black",
                   width=utilities.calculating_precentage(25),
                   height=settings.HEIGHT)

main_frame = Frame(root,
                   bg="black",
                   width=utilities.calculating_precentage(75),
                   height=utilities.calculating_height_precentage(80))



top_frame.place(x=0,y=0)
side_frame.place(x=0, y=utilities.calculating_height_precentage(20))
main_frame.place(x=utilities.calculating_precentage(25), y=utilities.calculating_height_precentage(20))



for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_button_object(main_frame)
        c.cell_button_object.grid(row=x, column=y)
        
        
        
Cell.create_self_count_label(top_frame)
Cell.cell_count_label_object.place(x=500, y=35)

Cell.info_label(side_frame)
Cell.create_label_object.place(x=5, y=30)




Cell.randomize_cells()


root.mainloop() 
 