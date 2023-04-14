#words = ["apple", "banana", "cherry", "date", "elderberry", "elderberry"]
#print(words)

#sdfi = list(dict.fromkeys(words))
#print(sdfi)

#a_words = list(filter(lambda x: x.__contains__("a"), words))
#print(a_words)

#tfa = list(filter(lambda d: d.endswith("a"), a_words))
#print(tfa)

import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk    
from tkinter.filedialog import askopenfilename
import pandas as pd

finishList = []


def questionChanged(event):  

    dubs = event.widget.get()

    question = list(filter(lambda i: i[0] == dubs, finishList))

    if question[0][1].isdigit():
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = []

        for num in x:
            y.append(question[0].count(str(num)))       

        fig, ax = plt.subplots()
        ax.bar(x, y)        
        ax.set_xlabel(question[0][0])        

        
        ax.bar_label(ax.containers[0], labels=y)               
        
        
        plt.show()
        
    else:
        x = []
        y = []
        skip = True
        for i in list(dict.fromkeys(question[0])):
            

            if skip:
                skip = False
                continue
            else:
                x.append(i)


        for num in x:
            y.append(question[0].count(str(num)))        
        
        lables = []

        for i in range(x.__len__()):
            lables.append(str(x[i]) + " | " + str(y[i]))

        fig, ax = plt.subplots()
        ax.pie(y, labels=lables)              
        plt.show()
    

    

def makeQuetsionPick(questions):
    current_var = StringVar()
    combobox = ttk.Combobox(frm, textvariable=current_var, values=questions)
    combobox.grid(column=4, row=0)  
    combobox.bind("<<ComboboxSelected>>", questionChanged)

def GetFile():    
    if finishList.__len__() != 0:
        finishList.clear()

    df = pd.read_csv(askopenfilename(), sep=",", encoding='utf-8')
    quest = list(dict.fromkeys(df['Fokus']))

    for i in quest:
        questList = []
        questList.append(i)
        for j in filter(lambda d: d[1]['Fokus'] == i, df.iterrows()):
            questList.append(j[1]['Spørgsmålstype'])
        finishList.append(questList)
    makeQuetsionPick(quest)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Pick File", command=GetFile).grid(column=3, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=6, row=0)
root.mainloop()







#fig, ax = plt.subplots()
#ax.bar(x = x, height = y)


#for k in finishList:
    #if k[1].isdigit():
        #number = []
        #for num in x:
            #number.append(k.count(str(num)))
        #y.append(number)

#for i in y:
    #print(i)



#for row in df:
    #print(', '.join(row))

#with open(filename, newline='') as csvfile:
#    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    

#for row in reader:
#    print(', '.join(row['FirstName']))