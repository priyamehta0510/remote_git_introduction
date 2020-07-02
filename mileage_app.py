import tkinter as tk
import pickle

print("*********loading model**********")
with open('mil.pkl', 'rb') as fp:
   new_model = pickle.load(fp)
   fp.close()
print("***********successfully loaded**********")

root = tk.Tk()
horsepower = tk.DoubleVar()
displacement = tk.DoubleVar()
weight = tk.DoubleVar()
predict = ''

def clear():
    horsepower.set('')
    displacement.set('')
    weight.set('')
    
clear()
  
f1 = tk.Frame(root)
l1 = tk.Label(f1, text=" HORSEPOWER".center(20)+" : " )
l1.config(bg ='#123456', fg ='#eeeeee', font = ('monospace', 20,'bold') )
l1.pack(side = tk.LEFT, fill =tk.X, expand = tk.YES)

e1 = tk.Entry(f1, textvariable = horsepower)
e1.config(bg="#eeeeee", fg ="#333333", font=('times', 25, 'bold'))
e1.pack(side = tk.LEFT, fill =tk.X, expand = tk.YES)
e1.focus()
f1.pack(fill = tk.BOTH, expand = tk.YES, padx =20, pady =20)

f2 = tk.Frame(root)
l2 = tk.Label(f2, text="DISPLACEMENT".center(20)+" : ")
l2.config(bg ='#123456', fg ='#eeeeee', font = ('monospace', 20,'bold') )
l2.pack(side = tk.LEFT, fill =tk.X, expand = tk.YES)

e2 = tk.Entry(f2, textvariable = displacement)
e2.config(bg="#eeeeee", fg ="#333333", font=('times', 25, 'bold'))
e2.pack(side = tk.LEFT, fill =tk.X, expand = tk.YES)
f2.pack(fill = tk.BOTH, expand = tk.YES, padx =20, pady =20)

f3 = tk.Frame(root)
l3 = tk.Label(f3, text="WEIGHT".center(20)+" : ")
l3.config(bg ='#123456', fg ='#eeeeee', font = ('monospace', 20,'bold') )
l3.pack(side = tk.LEFT, fill =tk.X, expand = tk.YES)

e3 = tk.Entry(f3, textvariable = weight)
e3.config(bg="#eeeeee", fg ="#333333", font=('times', 25, 'bold'))
e3.pack(side = tk.LEFT, fill =tk.X, expand = tk.YES)
f3.pack(fill = tk.BOTH, expand = tk.YES, padx =20, pady =20)

b1 = tk.Button(root, text = 'PREDICT', command = lambda : predict())
b1.config(bg='purple', fg = 'white', font = ('courier', 25, 'italic'))
b1.pack(fill = tk.X, expand = tk.YES)



#frame 5 to display output
f5=tk.Frame(root)
l5=tk.Label(f5,text="""
 Prediction






""",height=10,font=('monospace', 18, 'bold'))
l5.pack()
f5.pack(fill=tk.BOTH, expand=tk.YES, padx=20, pady=5)

def show(mil):
    global l5
    l5.pack_forget()
    l5=tk.Label(f5,text=f"""
Prediction
________________________________
horsepower    : {float(horsepower.get()):.2f}
Displacement  : {float(displacement.get()):.2f}
Weight        : {float(weight.get()):.2f}
________________________________   
Mileage       : {float(mil):2f}""",height=10,font=('monospace', 18, 'bold'))   
    
    l5.pack()


def predict():

    d = displacement.get()
    h = horsepower.get()
    w = weight.get()
    features = [ [ d,h,w ] ]
    mil = new_model.predict(features)[0]
    show(mil)    
    clear()
    
    
b2 = tk.Button(root, text = 'EXIT', command = root.quit)
b2.config(bg='purple', fg = 'white', font = ('courier', 25, 'italic'))
b2.pack(fill = tk.X, expand = tk.YES)
    
    
root.title('mileage prediction')
root.minsize(100,400)
root.mainloop()
