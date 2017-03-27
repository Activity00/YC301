#-*-coding:utf-8-*-

import matplotlib.pyplot as plt
import numpy as np
import xlrd

workbook=xlrd.open_workbook(r'info.xls')


def hist():
    sheet=workbook.sheet_by_name(workbook.sheet_names()[5])
    coln=sheet.col_values(2)
    coln=coln[1:]
    plt.hist(coln,30)
    ax.set_yticks(len(coln))
    ax.set_yticklabels('a','b','c')
    plt.show()

def barh():
    sheet=workbook.sheet_by_name(workbook.sheet_names()[5])
    coln=sheet.col_values(2)
    coln=coln[1:]
    
    plt.barh(100, 100)
    #ax.set_yticklabels('a','b','c')
    plt.show()
barh()
"""
Simple demo of a horizontal bar chart.
"""

plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))
# 
# ax.barh(y_pos, performance, xerr=error, align='center',
#         color='green', ecolor='black')
# ax.set_yticks(y_pos)
# ax.set_yticklabels(people)
# 
# plt.show()


