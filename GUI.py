import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from applogic import PathFound, Graph
'''
Class defining the GUI Elements.

'''
class MapPathfindingApp:
    def __init__(self, master, pointNames):
        self.master = master
        self.master.title("Map Pathfinding Program")
        self.pointNames:list[str] = pointNames

        # Point and Algo Options
        self.start_label = ttk.Label(master, text="Start Point:")
        self.start_label.grid(row=0, column=0)
        self.start_combobox = ttk.Combobox(master, values=self.pointNames)
        self.start_combobox.grid(row=0, column=1)
        self.start_combobox.current(0)

        self.end_label = ttk.Label(master, text="End Point:")
        self.end_label.grid(row=1, column=0)
        self.end_combobox = ttk.Combobox(master, values=self.pointNames)
        self.end_combobox.grid(row=1, column=1)
        self.end_combobox.current(1)

        self.algorithm_label = ttk.Label(master, text="Algorithm:")
        self.algorithm_label.grid(row=2, column=0)
        self.algorithm_combobox = ttk.Combobox(master, values=["Shortest way", "least outdoors", "least crowded"])
        self.algorithm_combobox.grid(row=2, column=1)
        self.algorithm_combobox.current(0)

        #time

        self.time_label = ttk.Label(master, text="Time:[Hours][Minutes] in 24 hour clock")
        self.time_label.grid(row=3, column=0)
        self.time_combobox_hour = ttk.Combobox(master, values=[i for i in range(0,20)])
        self.time_combobox_hour.current(10)
        self.time_combobox_hour.grid(row=3, column=1)
        self.time_combobox_minutes = ttk.Combobox(master, values=[i for i in range(0,60)])
        self.time_combobox_minutes.current(0)
        self.time_combobox_minutes.grid(row=3, column=2,columnspan=2)
        

        # Start Button
        self.find_button = ttk.Button(master, text="Find Path", command=self.find_path)
        self.find_button.grid(row=4, column=0, columnspan=2)

        # Map png display
        self.image_label = tk.Label(master)
        self.image_label.grid(row=6, column=0, columnspan=2)

        # Path description label
        self.path_label = ttk.Label(master, text="")
        self.path_label.grid(row=5, column=0, columnspan=2)


    def find_path(self):
        '''Takes input from the GUI and calls PathFound(see applogic.py)'''
        start_point = self.start_combobox.get()
        end_point = self.end_combobox.get()
        algorithm = self.algorithm_combobox.get()
        time =(int(self.time_combobox_hour.get()) + (int(self.time_combobox_minutes.get())/60))
        path = PathFound(start_point,end_point,algorithm,time)

        #print(path)
        #updates path label using path obtained from PathFound
        self.path_label.configure(text=path)

        # Load and display the map image for reference
        map_image = Image.open("campusMap_CS2002A5.png")
        map_image = map_image.resize((710, 830))  # Resize as needed(depends on the resolution of the map image file, keep aspect ratio)
        map_image = ImageTk.PhotoImage(map_image)
        self.image_label.configure(image=map_image,background="pink") # :D
        self.image_label.image = map_image

        


def main():
    root = tk.Tk()
    MapPathfindingApp(root,list(Graph.Nodes.keys()))
    root.mainloop()

if __name__ == "__main__":
    
    main()