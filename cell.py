
import tkinter as tk
from tkinter import Button, Label
import random
import settings
import sys

class Cell:
    
    all_instances = []
    cell_count_label_object = False
    create_label_object = False
    
    def __init__(self,x, y,  is_mine=False,):
        self.is_mine = is_mine
        self.cell_button_object = None
        self.x = x
        self.y = y
        self.is_open = False
        self.is_mine_marker = False
        
        Cell.all_instances.append(self)
        
        
        
    def create_button_object(self, location):
        btn = Button(
            location,
            bg="gray",
            width=8,
            height=3
        )
        btn.bind('<Button-1>', self.left_click_actions) 
        btn.bind("<Button-3>", self.right_click_action)
        self.cell_button_object = btn
    
    
    
    @staticmethod
    def create_self_count_label(location):
        label = Label(
            location,
            text=f"Cells remaining: {settings.ALL_CELLS}",
            width=18,
            height=3,
            bg="yellow",
            fg="black",
            font=("", 12)
        )
        Cell.cell_count_label_object = label
    
    @staticmethod
    def info_label(location):
        label = Label(
            location,
            bg="white",
            fg="black",
            width=32,
            height=15,
            font=("", 10),
            text="To mark a cell, right click on it! .\n .To unmark it, right click again!"
        )
        Cell.create_label_object = label
    
    
        


    def left_click_actions(self, event):
        self.cell_button_object.configure(
            bg="gray"
        )
        if self.is_mine:
            self.show_mine()
        else:
            
            if self.mines_surrounding_cell == 0:
                for cell_object in self.surroinding_cells:
                    cell_object.show_cell()
            
            self.show_cell()
        
        self.cell_button_object.unbind("<Button-1>")
        self.cell_button_object.unbind("<Button-3>")
        
            
            
            
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all_instances:
            if cell.x == x and cell.y == y:
                return cell
                
    
    @property
    def surroinding_cells(self):
        cells_around = [
            
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x + 1, self.y-1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
            
            
        ]

        cells_around = [cell for cell in cells_around if cell is not None]
        return cells_around
    
    @property
    def mines_surrounding_cell(self):
        count = 0
        for cell in self.surroinding_cells:
            if cell.is_mine:
                count += 1
        return count
            
    
            
    def show_cell(self):
        if not self.is_open:
            settings.ALL_CELLS -= 1
            self.cell_button_object.configure(text=self.mines_surrounding_cell)  
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"cells remaining: {settings.ALL_CELLS}")
        
        self.is_open = True             
    
    
    def show_mine(self):
        self.cell_button_object.configure(bg="red")
        self.create_label_object.configure(text="You exploded!", bg="orange", font=("", 12))
        
        self.after(5000, self.exit_application)
    
    def exit_application(self):
        sys.exit()
    
    def not_mine(self):
        self.cell_button_object.configure(bg="blue")


    def right_click_action(self, event):
        if not self.is_mine_marker:
            self.cell_button_object.configure(
                bg="orange"
            )    
            self.is_mine_marker = True
        else:
            self.cell_button_object.configure(
                bg="gray"
            )
            self.is_mine_marker = False
    
    
    
    @staticmethod
    def randomize_cells():
        mine_cells = random.sample(Cell.all_instances, settings.MINES_COUNT)
        for mine_cell in mine_cells:
            mine_cell.is_mine = True
        
    
    
    def __repr__(self):
        return f"Cell({self.x, self.y})"
    
        


