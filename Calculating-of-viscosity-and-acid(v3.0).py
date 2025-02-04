#!usr/bin/env python2.7

# coding: utf-8

# import modules

from tkinter import *

from tkinter import messagebox







def roundUp(a, num_bits):

    '''

    Round numbers

    '''


    n = 10 ** num_bits

    a1 = float(int(a * n))

    tag = a * n - a1

    if tag >= 0.5:

        return (a1 + 1) / float(n)

    else:

        return a1 / float(n)





# CREATE A FRAME TO CONTAIN THE viscosity AND emulsify COMPONENTS


root = Tk()

frame_root = Frame(root)

frame_nd_pr = Frame(frame_root)




# input time and the number of pipes

Label(frame_nd_pr, text = 'Time(s):', justify = RIGHT).grid(row = 0, padx = 1, pady = 5)

Label(frame_nd_pr, text = 'PIPE-NUMBER:', justify = RIGHT).grid(row = 2)

e_AT = Entry(frame_nd_pr)

e_NP = Entry(frame_nd_pr)

e_AT.grid(row = 0, column = 1, padx = 1, pady = 1)

e_NP.grid(row = 2, column = 1, padx = 1, pady = 1)



# create a symbol to show the process of calculating    

Label(frame_nd_pr, text = '===>>').grid(row = 1, column = 2)



# show the coefficient the pipes matched and exam the result

Label(frame_nd_pr, text = 'Coeff-matched(mm2/s2):').grid(row = 0, column = 3)

Label(frame_nd_pr, text = 'Coeff-refered(mm2/s2):').grid(row = 2, column = 3)



# create a symbol to show the process of calculating

Label(frame_nd_pr, text = '===>>').grid(row = 1, column = 5)



# show the calculated results of viscosity and viscosity pushed back

Label(frame_nd_pr, text = 'Actual-Viscosity(mm2/s):').grid(row = 0, column = 6)

Label(frame_nd_pr, text = 'TIME-PUSHBACK(s):').grid(row = 1, column = 6)

Label(frame_nd_pr, text = 'Viscosity-PUSHBACK(mm2/s):').grid(row = 2, column = 6)


# create a symbol to show the process of calculating

Label(frame_nd_pr, text = '===>>').grid(row = 1, column = 8)

Label(frame_nd_pr, text = 'AVERAGE-VISCOSITY(mm2/s):').grid(row = 1, column = 9)



# Calculating and change the time of Emulsified to 'xxx'(min)

Label(frame_nd_pr, text = 'Emulsified-time:').grid(row = 3, padx = 1, pady = 5)

e_ET = Entry(frame_nd_pr)

e_ET.grid(row = 3, column = 1)

Label(frame_nd_pr, text = '===>>').grid(row = 3, column = 2)

Label(frame_nd_pr, text = 'Change-to-min(min):').grid(row = 3, column = 3)


# create a dict containing the coefficient according to the number of pipes

dict_coefficient_pipes = {'817': 1.288, '791': 0.8198, '794': 1.086, '641': 0.9190, '756': 1.090, '709': 1.108, '782': 0.9699,

                          '714': 0.9129, '721': 0.9358, '752': 1.173, '788': 1.245, '703': 0.8565, '785': 0.8962, '764': 0.9777,

                          '754': 0.8891, '812': 0.7765, '802': 1.097, '444': 0.8498, '749': 0.8457, '825': 0.8337, '759': 0.8547,

                          '841': 0.9635, '774': 1.146, '751': 1.255, '762': 0.9424, '730': 0.8304, '843': 0.9551, '119': 0.1429,

                          '208': 0.1591, '178': 0.1573, '283': 0.1441, '60': 0.1426, '109': 0.1800, '145': 0.1840, '132': 0.1835,

                          '206': 0.1742, '204': 0.1810, '186': 0.1597, '179': 0.1763, '150': 0.1881, '138': 0.1557, '192n': 0.1808,

                          '205n': 0.1899, '141n': 0.1792, '217': 0.1778, '131': 0.1512, '174n': 0.1602, '116': 0.1512, '152': 0.1512,

                          '428': 0.1836, '77': 0.1854, '272': 0.1592, '134': 0.1409, '311': 0.1510, '112': 0.1572, '113': 0.1894,

                          '235n': 0.1663, '411': 0.1454, '225': 0.1795, '442': 0.1791, '281': 0.1607, '393': 0.1517, '418': 0.1665,

                          '280': 0.1557, '284': 0.1793, '157': 0.1836, '360': 0.1523, '368': 0.1567, '208': 0.1826, '327': 0.1486,

                          '375': 0.1651, '416': 0.1716, '108': 0.1821, '233': 0.1571, '297': 0.1616, '235o': 0.1578, '192o': 0.1554, 

                          '147': 0.1609, '66': 0.1776, '97': 0.1580, '177o': 0.1581, '174o': 0.1403, '121': 0.1626, '92': 0.1407, '167': 0.1500,

                          '176': 0.1532, '271': 0.1451, '212': 0.1638, '17': 0.1828, '115': 0.1711, '207': 0.1593, '227': 0.1607, 

                          '247': 0.1465, '286': 0.1435, '184': 0.1562, '96': 0.1425, '93': 0.1495, '222': 0.1607, '185': 0.1466, 

                          '141o': 0.1536, '26': 0.1406, '205o': 0.1539, '736': 0.2834, '190': 0.1557, '587': 0.1496, '628': 0.1407,

                          '734': 0.1377, '509': 0.1463, '563': 0.1339, '661': 0.1484, '23': 0.02958, '164': 0.1825, '210': 0.1882,

                          '177n': 0.1834, '173': 0.1833, '344':0.1428, '168':0.1893, '169':0.1833, '273':0.1514, '407': 0.1535, 

                          '446': 0.1472, '441':0.1561, '422': 0.1700, '351': 0.1781, '396': 0.1574, '381': 0.1783}



# create a list containing the coefficients which is used to give a reference to practical calculating in '1.2' series

list_coefficient_reference = [0.1493, 0.1358, 0.1435, 0.1444, 0.1499, 0.1246, 0.1460, 0.1482, 0.02364, 0.2064, 0.01756, 0.1024, 0.08530, 0.1898, 0.1514, 0.1140]






def get_coefficients(num):


    '''

    Get the coefficient of viscosity


    '''



    coeff = dict_coefficient_pipes['%s' % num]

    list_coefficient = []

    d_abs = {}



    # if the number of pipes belong to '2.0' series, then execute the follow methods to find the coefficient and the Coefficient of reference

    if coeff > 0.2:

        for key, value in dict_coefficient_pipes.items():

            if value > 0.2 and not abs(coeff - value) == 0:        

                d_abs[key] = abs(coeff - value)

                list_coefficient.append(abs(coeff - value))

        list_coefficient.sort()

        for d_abs_key in d_abs:

            if d_abs[d_abs_key] == list_coefficient[0]:
  
                return coeff, dict_coefficient_pipes[d_abs_key]


               
    # if the number of pipes belong to '1.2' series, then execute the follow methods to find the coefficient and the Coefficient of reference

    elif 0.15 < coeff < 0.2:

        return coeff, 0.1514

    elif coeff < 0.15:

        for co_refer in list_coefficient_reference:

            d_abs[co_refer] = abs(coeff - co_refer)

            list_coefficient.append(abs(coeff - co_refer))

        list_coefficient.sort()

        for d_abs_key in d_abs:
        
            if d_abs[d_abs_key] == list_coefficient[0]:

                return coeff, d_abs_key  



var_coeff = StringVar()

var_coeff_refer = StringVar()

var_viscosity = StringVar()

var_time_repushed = StringVar()

var_viscosity_repushed = StringVar()

var_average_viscosity = StringVar()

var_emulsified_time = StringVar()






def show_viscosity(x):


    '''

    Show the coefficient, coefficient refered, time_repushed, 

    viscosity calculated, viscosity refered, average viscosity, and emulsified time


    '''



    if e_NP.get() == '' or e_AT.get() == '' :

        messagebox.showinfo(title = 'Error Warning', message = 'Some EMPTY, Try again!')

    if  int(e_AT.get()) < 200 and (not e_AT.get() == ''):

        messagebox.showinfo(title = 'Error Warning', message = 'Time should > 200s!')


    var_coeff.set(str(get_coefficients(e_NP.get())[0]))

    var_coeff_refer.set(str(get_coefficients(e_NP.get())[1]))
    
    Label(frame_nd_pr, textvariable = var_coeff).grid(row = 0, column = 4)  # the coefficient according to the number of pipes

    Label(frame_nd_pr, textvariable = var_coeff_refer).grid(row = 2, column = 4)  # the coefficient referred by coefficient above

    # calculate the viscosity, repushed time and viscosity and the average between viscosity and refered viscosity

    v = int(e_AT.get()) * get_coefficients(e_NP.get())[0]

    v_round = roundUp(v, 2)

    time_repushed = round(v_round / get_coefficients(e_NP.get())[1], 0)

    v_repushed = time_repushed * get_coefficients(e_NP.get())[1]

    v_repushed_round = roundUp(v_repushed, 2)

    v_average = (v_round + v_repushed_round) / 2.00

    v_average_round = roundUp(v_average, 3)

    # make the label components' text content changeable

    var_viscosity.set(str(v_round))

    var_time_repushed.set(str(time_repushed))

    var_viscosity_repushed.set(str(v_repushed_round))

    var_average_viscosity.set(str(v_average_round))

    # show the results above using label components

    Label(frame_nd_pr, textvariable = var_viscosity).grid(row = 0, column = 7)

    Label(frame_nd_pr, textvariable = var_time_repushed).grid(row = 1, column = 7)

    Label(frame_nd_pr, textvariable = var_viscosity_repushed).grid(row = 2, column = 7)

    Label(frame_nd_pr, textvariable = var_average_viscosity).grid(row = 1, column = 10)







def show_emulsitime(y):

    
    '''

    Show the emulsified time

    '''




    if e_ET.get() == '':

        messagebox.showinfo(title = 'Error Warning', message = 'Should not empty, try again!')
 
    # calculate the Emulsified time which is changed to 'min'

    time_str = e_ET.get()

    time_inte = int(time_str[0:2]) + int(time_str[2:]) / 60.0

    emulsified_time = roundUp(time_inte, 2)

    var_emulsified_time.set(str(emulsified_time))

    # show the result time using label components

    Label(frame_nd_pr, textvariable = var_emulsified_time).grid(row = 3, column = 4)






def clr_nd():

    '''

    clear the contents of viscosity calculating components

    '''



    e_AT.delete(0, END)

    e_NP.delete(0, END)

    # make the label components' text content changable

    var_coeff.set('')

    var_coeff_refer.set('')

    var_viscosity.set('')

    var_time_repushed.set('')

    var_viscosity_repushed.set('')

    var_average_viscosity.set('')

    # show the results above using label components

    Label(frame_nd_pr, textvariable = var_coeff).grid(row = 0, column = 4)  # the coefficient according to the number of pipes

    Label(frame_nd_pr, textvariable = var_coeff_refer).grid(row = 2, column = 4)  # the coefficient referred by coefficient above

    Label(frame_nd_pr, textvariable = var_viscosity).grid(row = 0, column = 7)

    Label(frame_nd_pr, textvariable = var_time_repushed).grid(row = 1, column = 7)

    Label(frame_nd_pr, textvariable = var_viscosity_repushed).grid(row = 2, column = 7)

    Label(frame_nd_pr, textvariable = var_average_viscosity).grid(row = 1, column = 10)





def clr_emul_time():

    '''

    Clear the emulsified time 

    '''


    e_ET.delete(0, END)

    var_emulsified_time.set('')

    Label(frame_nd_pr, textvariable = var_emulsified_time).grid(row = 3, column = 4)



# bind 'enter' event with Entry of time

e_AT.bind('<Return>', show_viscosity)  

e_NP.bind('<Return>', show_viscosity)

e_ET.bind('<Return>', show_emulsitime)

Button(frame_nd_pr, text = 'Clear-viscosity', command = clr_nd, padx = 10, pady = 3).grid(row = 5, column = 2, padx = 10, pady = 5)

Button(frame_nd_pr, text = 'Clear-emulsifiy', command = clr_emul_time, padx = 10, pady= 3).grid(row = 5, column = 5, padx = 10, pady = 5)

Button(frame_nd_pr, text = 'QUIT', command = root.quit, padx = 10, pady = 3).grid(row = 5, column = 8, padx = 10, pady = 5)



# CREATE A LINE TO SEPARATE THE TWO FRAMES----frame_nd_pr, frame_acd

frame_sep_line = Frame(frame_root)

Label(frame_sep_line, text = '--' * 100).grid(row = 0, column = 5)

Label(frame_sep_line, text = 'Caution: 1. While inputing pipe\'s number, if the pipe is old, then add \'o\' behind the pipe number; if the pipe is new, add \'n\' behind the pipe number;').grid(row = 1, column = 5)

Label(frame_sep_line, text = 'Example: the pipe number is 177, both old  and new exist, if is new one, then input \'177n\', else input\'177o\'').grid(row = 2, column = 5)

Label(frame_sep_line, text = '2. So far the same numbers in both old and new pipes are: 177, 141, 192, 205, 174, 235').grid(row = 3, column = 5)

Label(frame_sep_line, text = '3. If Emulsified time is 2\'2\'\', then input 0202').grid(row = 4, column = 5)

Label(frame_sep_line, text = '--' * 100).grid(row = 5, column = 5)




# CREATE A FRAME TO CONTAIN Acid value Components

frame_acd = Frame(frame_root)

Label(frame_acd, text = 'Volume-empty(mL):').grid(row = 0, padx = 10, pady = 5)

e_VE = Entry(frame_acd)

e_VE.grid(row = 0, column = 1)

Label(frame_acd, text = 'SSC(mol/L):').grid(row = 1, padx = 10, pady = 5)

e_SSC = Entry(frame_acd)

e_SSC.grid(row = 1, column = 1)

Label(frame_acd, text = 'Gram-oil(g):').grid(row = 2, padx = 10, pady = 5)

e_OG = Entry(frame_acd)

e_OG.grid(row = 2, column = 1)

Label(frame_acd, text = 'Volume-KOH(mL):').grid(row = 3, padx = 10, pady = 5)

e_VKOH = Entry(frame_acd)

e_VKOH.grid(row = 3, column = 1)

Label(frame_acd, text = '===>>').grid(row = 2, column = 2)

Label(frame_acd, text = 'Acid-value(mgKOH/g):').grid(row = 2, column = 3, padx = 10, pady = 5)

Label(frame_acd, text = '===>>').grid(row = 2, column = 5)

Label(frame_acd, text = 'SSV(mL):').grid(row = 2, column = 6, padx = 10, pady = 5)


var_acid = StringVar()

var_volume_of_standard_solution = StringVar()






def cal_acid_and_volume_standard(z):

    '''

    Calculate the acid value

    '''



    if e_VKOH.get() == '' or e_VE.get() == '' or e_SSC.get() == '':

        messagebox.showinfo(title = 'Error Warning', message = 'Should not empty, try again!')

    Vi = float(e_VKOH.get())

    V0 = float(e_VE.get())

    c = float(e_SSC.get())

    mi = float(e_OG.get()) 

    acid_value = (Vi - V0) * 56.1 * c / mi

    # acid_value_round = roundUp(acid_value, 4)
    acid_value_round = "%.4f" % acid_value

    V_standard = float(acid_value_round) * 10.00 / c / 56.1 + V0

    # V_standard_round = roundUp(V_standard, 3)
    V_standard_round = "%.4f" % V_standard

    # make the label components' contents changeable

    var_acid.set(str(acid_value_round))

    var_volume_of_standard_solution.set(str(V_standard_round))

    Label(frame_acd, textvariable = var_acid).grid(row = 2, column = 4)

    Label(frame_acd, textvariable = var_volume_of_standard_solution).grid(row = 2, column = 7)






def clr_acd():

    '''

    Clear the content of the component

    '''


    e_VE.delete(0, END)

    e_VKOH.delete(0, END)

    e_SSC.delete(0, END)

    e_OG.delete(0, END)

    var_acid.set('')

    var_volume_of_standard_solution.set('')

    Label(frame_acd, textvariable = var_acid).grid(row = 2, column = 4)

    Label(frame_acd, textvariable = var_volume_of_standard_solution).grid(row = 2, column = 7)

     


# bind 'enter' event with Entry of time

e_VE.bind('<Return>', cal_acid_and_volume_standard)

e_SSC.bind('<Return>', cal_acid_and_volume_standard)

e_VKOH.bind('<Return>', cal_acid_and_volume_standard)

e_OG.bind('<Return>', cal_acid_and_volume_standard)



Button(frame_acd, text = 'Clear-acid-value', command = clr_acd, padx = 10, pady = 3).grid(row = 4, column = 1, padx = 10, pady = 5)

Button(frame_acd, text = 'QUIT', command = root.quit, padx = 10, pady = 3).grid(row = 4, column = 4, padx = 10, pady = 5)




frame_nd_pr.pack(padx = 10, pady = 5)

frame_sep_line.pack(padx = 10, pady = 5)

frame_acd.pack(padx = 10, pady = 15)



frame_root.pack()

mainloop()

