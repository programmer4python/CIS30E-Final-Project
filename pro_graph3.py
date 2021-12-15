# https://stackoverflow.com/questions/631524444/how-do-i-create-a-live-graph-with-cpu-data-in-tkinter
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.dates as mdates
from psutil import cpu_percent, virtual_memory
from datetime import datetime, timedelta

LARGE_FONT = ("Verdana", 12)
style.use("ggplot")

class Graphapp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Final Project CIS-30E Live Graph")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, GraphPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CPU % utilization and RAM % utilization", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button3 = ttk.Button(self, text="Live Plot", command=lambda: controller.show_frame(GraphPage))
        button3.pack(fill='x')

class GraphPage(tk.Frame):
    def __init__(self, parent, controller, nb_points=360):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CPU and Ram Live Plotting", font=LARGE_FONT)
        label.pack(pady=10, padx=10, side='top')
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.ax.tick_params(axis='both', which='minor', labelsize=8)
        self.par = self.ax.twiny()
        myFmt = mdates.DateFormatter("%H:%M:%S")
        self.ax.xaxis.set_major_formatter(myFmt)
        # initialize x, y and second y data
        dateTimeObj = datetime.now() + timedelta(seconds=-nb_points)
        self.x_data = [dateTimeObj + timedelta(seconds=i) for i in range(nb_points)]
        self.y_data = [0 for i in range(nb_points)]
        self.par.y_data = [0 for i in range(nb_points)]
        # creating plot
        self.plot = self.ax.plot(self.x_data, self.y_data, label='CPU')[0]
        self.par.plot = self.par.plot(self.x_data, self.par.y_data, label='RAM', color='blue')[0]
        self.par.get_xaxis().set_visible(False)
        self.ax.set_ylim(0,100)
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        button1 = ttk.Button(self, text="Back", command=lambda: controller.show_frame(StartPage))
        button1.pack(side='bottom')
        self.canvas.get_tk_widget().pack(side='top', fill=tk.BOTH, expand=True)
        self.animate()

    def animate(self):
        # append new data point to the x and y data
        self.x_data.append(datetime.now())
        self.y_data.append(cpu_percent())
        self.par.y_data.append(virtual_memory()[2])
        # remove oldest data point
        self.x_data = self.x_data[1:]
        self.y_data = self.y_data[1:]
        self.par.y_data = self.par.y_data[1:]
        # update plot data
        self.plot.set_xdata(self.x_data)
        self.plot.set_ydata(self.y_data)
        self.par.plot.set_ydata(self.par.y_data)
        self.ax.set_ylabel('CPU % utilization',color="red")
        # add secondary axis
        secax=self.ax.secondary_yaxis('right')
        secax.set_ylabel('RAM % utilization', color="blue")
        self.par.set_title('CPU & RAM % utilization')
        self.ax.set_xlim(self.x_data[0], self.x_data[-1])
        self.canvas.draw_idle() # redraw plot
        self.after(1000, self.animate)

app = Graphapp()
app.geometry('700x700')
app.mainloop()
