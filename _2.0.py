# coding: utf-8

from tkinter import *

from tkinter import messagebox



def s_Up(s):

    '''

    Convert every string including empty string to numbers

    '''



    if s == '':

        return None

    else:

        return float(s)






def roundUp(a, num_bit):

    ''' 
    
    Round the numbers

    '''



    n = 10 ** num_bit

    a1 = float(int(a * n))

    tag = a * n - a1

    if tag >= 0.5:

        return (a1 + 1) / float(n)

    else:

        return a1 / float(n)






def get_vol(V0, ssc, Gram_oil, acid):

    '''

    Calculate the volume of standard solutions

    '''



    if V0 == None or Gram_oil == None or ssc == None or acid == None or ssc == 0:

        return None

    else:

        volume = acid * Gram_oil / ssc / 56.1 + V0

        # volume_round = roundUp(volume, 4)
        volume_round = "%.4f" % volume

        return volume_round





# CREATE A GUI TO CONTAIN THE CALCULATING COMPONENTS

root = Tk()

root.title('Acid Value Calculating')

frame_root = Frame(root)




# CREATE A FRAME TO CONTAIN THE COMPONENTS OF EVERY UNITS

frame_cal = Frame(frame_root)



list_vol_emp_variables = []

list_ssc_variables = []

list_oil_variables = []

list_acid_variables = []

list_var_variables = []






for i in range(0, 10):

    list_vol_emp_variables.append('e_vol_emp_' + str(i))

    list_ssc_variables.append('e_ssc_' + str(i))

    list_oil_variables.append('e_oil_' + str(i))

    list_acid_variables.append('e_acid_' + str(i))

    list_var_variables.append('var_' + str(i))


# the ten units to calculating the volumne of standard solution

for i in range(0, 10):

    exec('%s = Entry(frame_cal)' % list_vol_emp_variables[i])

    exec('%s = Entry(frame_cal)' % list_ssc_variables[i])

    exec('%s = Entry(frame_cal)' % list_oil_variables[i])

    exec('%s = Entry(frame_cal)' % list_acid_variables[i])

    Label(frame_cal, text = '空白体积(mL):').grid(row = i)

    Label(frame_cal, text = '标准溶液浓度(mol/L):').grid(row = i, column = 2)

    Label(frame_cal, text = '油样质量(g):').grid(row = i, column = 4)

    Label(frame_cal, text = '酸值(mgKOH/g):').grid(row = i, column = 6)

    # create a process symbol

    Label(frame_cal, text = '===>>').grid(row = i, column = 8)

    Label(frame_cal, text = '标液体积(mL):').grid(row = i, column = 9)


for i in range(0, 10):

    exec('%s.grid(row = i, column = 1, padx = 10, pady = 2)' % list_vol_emp_variables[i])  

    exec('%s.grid(row = i, column = 3, padx = 10, pady = 2)' % list_ssc_variables[i])

    exec('%s.grid(row = i, column = 5, padx = 10, pady = 2)' % list_oil_variables[i])

    exec('%s.grid(row = i, column = 7, padx = 10, pady = 2)' % list_acid_variables[i])







def cal():

    '''

    Calculate the results

    '''


    for i in range(0, 10):

        exec('V0 = s_Up(%s.get())' % list_vol_emp_variables[i])

        exec('SSC = s_Up(%s.get())' % list_ssc_variables[i])

        exec('Gram_oil = s_Up(%s.get())' % list_oil_variables[i])

        exec('acid = s_Up(%s.get())' % list_acid_variables[i])

        exec('%s = StringVar()' % list_var_variables[i])

        exec('%s.set(str(get_vol(V0, SSC, Gram_oil, acid)))' % list_var_variables[i])

        exec('Label(frame_cal, textvariable = %s).grid(row = i, column = 10)' % list_var_variables[i])





# define a function to clear the contents of the components

def clr():

    '''

    clear the contents of the components

   
    '''


    for i in range(0, 10):

        exec('%s.delete(0, END)' % list_vol_emp_variables[i])

        exec('%s.delete(0, END)' % list_ssc_variables[i])

        exec('%s.delete(0, END)' % list_oil_variables[i])

        exec('%s.delete(0, END)' % list_acid_variables[i])

        exec('%s = StringVar()' % list_var_variables[i])

        exec('%s.set(\'\')' % list_var_variables[i])

        exec('Label(frame_cal, textvariable = %s).grid(row = i, column = 10)' % list_var_variables[i])




Button(frame_cal, text = '计算', command = cal, padx = 10, pady = 2).grid(row = 12, column =2, padx = 10, pady = 5)

Button(frame_cal, text = '清空', command = clr, padx = 10, pady = 2).grid(row = 12, column = 4, padx = 10, pady = 5)

Button(frame_cal, text = '退出', command = root.quit, padx = 10, pady = 2).grid(row = 12, column = 6, padx = 10, pady = 5)


frame_root.pack()

frame_cal.pack()

mainloop()



