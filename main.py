import tkinter as tk 
from backend import predict
from sklearn.tree import DecisionTreeClassifier
from PIL import ImageTk, Image
root = tk.Tk()
root.geometry("1280x720+30+0")
root.config(bg = "white")
root.title("Placement Prediction")
root.resizable(False, False)



class gui:
    head_font = ("Arial", 36, "bold")
    font = ("Arial", 20, "bold")
    font2 = ("Arial", 16)
    values = range(1,11)
    ex1 = 50
    ex2 = 200
    ex3 = 620
    ex4 = 950
    
    def __init__(self,root):
        frame = tk.Frame(root, bg = "cornsilk2")
        frame.place(x = 0, y = 0, width = 1280, height = 720)
        self.img = ImageTk.PhotoImage(Image.open("college.jpg"))
        tk.Label(frame, image = self.img).place(x = 1050, y = 10)
        tk.Label(frame, text = "STUDENT PLACEMENT PREDICTION", font = self.head_font, bg = "white", borderwidth=2, relief="solid").place(x = 170, y = 50)
        tk.Label(frame, text = "Name", font = self.font, bg = "white").place(x = self.ex1, y = 250)      
        name = tk.Entry(frame, font = self.font2, bg = "silver")
        name.place(x = self.ex2, y = 260, height = 25, width = 300)  
        name.focus()
        tk.Label(frame, text = "Roll no", font = self.font, bg = "white").place(x = self.ex1, y = 300)      
        roll = tk.Entry(frame, font = self.font2, bg = "silver")
        roll.place(x = self.ex2, y = 310, height = 25, width = 300)
        tk.Label(frame, text = "Aggregate", font = self.font, bg = "white").place(x = self.ex1, y = 350)      
        agg = tk.Entry(frame, font = self.font2, bg = "silver")
        agg.place(x = self.ex2, y = 360, height = 25, width = 300)
        tk.Label(frame, text = "%", font = self.font, bg = "white").place(x = self.ex2+300, y = 355)
        tk.Label(frame, text = "Technical Skills", font = self.font, bg = "white").place(x = self.ex3, y = 250)
        techskill = tk.StringVar(frame)
        techskill.set("None")
        drop_down = tk.OptionMenu(root, techskill, *self.values)
        drop_down.place(x = self.ex4, y = 260)
        tk.Label(frame, text = "Communication Skills", font = self.font, bg = "white").place(x = self.ex3, y = 300)
        comskill = tk.StringVar(frame)
        comskill.set("None")
        drop_down = tk.OptionMenu(root, comskill, *self.values)
        drop_down.place(x = self.ex4, y = 310)
        tk.Label(frame, text = "Backlogs", font = self.font, bg = "white").place(x = self.ex3, y = 350)
        backlogs = tk.Entry(frame, font = self.font2, bg = "silver")
        backlogs.place(x = self.ex4, y = 360, height = 25, width = 300)
        answer = tk.Label(frame, font = self.head_font, fg = "green", bg = "white")
        answer.place(x = self.ex1 , y = 500)
        predict = tk.Button(frame, text = "PREDICT", fg = "dark slate gray",  borderwidth=2, relief="raised", font = self.head_font, command = lambda :self.prediction(frame, answer, name, roll, agg, techskill, comskill, backlogs))
        predict.place(x = 970, y = 420, width = 250, height = 100)
        
    
    def prediction(self,frame, answer, name, roll, agg, techskill, comskill, backlogs):
        name.delete(0, "end")
        roll.delete(0, "end")
        x = agg.get()
        agg.delete(0,"end")
        y = techskill.get()
        techskill.set("None")
        z = comskill.get()
        comskill.set("None")
        k = backlogs.get()
        backlogs.delete(0, "end")
        if len(x) == 0 or y == "None" or z == "None" or not k.isdigit():
            answer.config(text = "please fill every field", fg = "red")
        else:
            out = predict(int(float(x)),y,z,k)
            if out:
                answer.config(text = "You might get Selected", fg = "green")
            else:
                answer.config(text = "You might NOT get Selected",fg = "red")

        
    

GUI = gui(root)
root.mainloop()
