import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math as mt
from tkinter import *
import pygame
# from PySide6.QtWidgets import QApplication, QDialog
#
# from tims_interface import Ui_Dialog
# import sys
# from scipy.optimize import fsolve


class Main:
    def read_from_file(self):
        with open("Data.txt") as f:
            lines = f.readlines()
            lines = [i.replace("\n", "") for i in lines]
            matrix = [[float(j) for j in i.split(",")] for i in lines]
        return matrix

    def get_x_i(self):
        return self.read_from_file()[0][1:]

    def get_y_i(self):
        matrix = self.read_from_file()
        return [matrix[i][0] for i in range(1, len(matrix))]

    def get_n_i(self):
        matrix = self.read_from_file()
        return [sum([matrix[i][j] for i in range(1, len(matrix))]) for j in range(1, len(matrix[0]))]

    def get_m_i(self):
        matrix = self.read_from_file()
        return [sum(matrix[i][1:]) for i in range(1, len(matrix))]

    def Y_vybirkove(self):
        yi, arrX, arrY, arrN, matrix = [], self.get_x_i(), self.get_y_i(), self.get_n_i(), self.read_from_file()

        for i in range(len(arrY)+1):
            elems = []
            for j in range(len(arrX) - 1):
                elem = matrix[j + 1][i + 1] * arrY[j]
                elems.append(elem)
            yi.append(sum(elems))

        result = [y / arrN[i] for i, y in enumerate(yi)]
        return result

    def Table(self):
        arrY = self.Y_vybirkove()
        new_y = [round(i, 3) for i in arrY]
        return pd.DataFrame({'X': self.get_x_i(), '-Y': new_y, 'Ni': self.get_n_i()})


    # Обчислення значень показникової функції для кожного x
    def GraphicM3(self):
        arrxi = self.get_x_i()
        arryi = self.Y_vybirkove()

        arrx = np.linspace(min(arrxi), max(arrxi)+1, 1000)
        y = 2.75*np.exp(arrx)
        yy = [i**2 for i in arrx]
        a_ = 0  # Параметр a
        b_ = 1  # Параметр b
        y1 = [np.sqrt(a_**2 + (b_*x)**2) for x in arrx]  # Верхня гілка гіперболи
        y2 = [-np.sqrt(a_**2 + (b_*x)**2) for x in arrx]   # Нижня гілка гіперболи
        yyy = [x**0.5 for x in arrx]
        plt.close("all")
        fig5, ax5 = plt.subplots()
        ax5.plot(arrxi, arryi, marker='o', linestyle='-', color='blue', label='Графік моєї функції')
        ax5.plot(arrx, yy, color='red', label='Парабола')
        ax5.plot(arrx, y, color='green', label='Експонента')
        ax5.plot(arrx, y1, color='orange', label='Верхня гілка гіперболи')
        ax5.plot(arrx, y2, color='orange', label='Нижня гілка гіперболи')
        ax5.plot(arrx, yyy, color='purple', label='Коренева функція')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік точок Mi(x,y-)')
        plt.grid(True)
        sound2 = pygame.mixer.Sound('графік.mp3')
        sound2.play()
        plt.legend()
        plt.show()


    # 1) Parabola fx= ax^2+bx+c
    def GraphicM(self):
        arrxi = self.get_x_i()
        arryi = self.Y_vybirkove()

        arrx = np.linspace(min(arrxi), max(arrxi)+1, 1000)
        # y = 2.75*np.exp(arrx)
        yy = [i**2 for i in arrx]
        # a_ = 0  # Параметр a
        # b_ = 1  # Параметр b
        # y1 = [np.sqrt(a_**2 + (b_*x)**2) for x in arrx]  # Верхня гілка гіперболи
        # y2 = [-np.sqrt(a_**2 + (b_*x)**2) for x in arrx]   # Нижня гілка гіперболи
        # yyy = [x**0.5 for x in arrx]
        plt.close("all")
        fig4, ax4 = plt.subplots()
        ax4.plot(arrxi, arryi, marker='o', linestyle='-', color='blue', label='Графік моєї функції')
        ax4.plot(arrx, yy, color='red', label='Парабола')
        # plt.plot(arrx, y, color='green', label='Експонента')
        # plt.plot(arrx, y1, color='orange', label='Верхня гілка гіперболи')
        # plt.plot(arrx, y2, color='orange', label='Нижня гілка гіперболи')
        # plt.plot(arrx, yyy, color='purple', label='Коренева функція')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік точок Mi(x,y-)')
        plt.grid(True)

        plt.legend()
        plt.show()


    def Sum(self):
        arr = self.get_n_i()
        arrx = self.get_x_i()
        y_vybirkove = self.Y_vybirkove()
        sum1_ = sum([arr[i] * (arrx[i] ** 4) for i in range(len(arr))])
        sum2_ = sum([arr[i] * (arrx[i] ** 3) for i in range(len(arr))])
        sum3_ = sum([arr[i] * (arrx[i] ** 2) for i in range(len(arr))])
        sum4_ = sum([arr[i] * y_vybirkove[i] * arrx[i] ** 2 for i in range(len(arr))])
        sum5_ = sum([arr[i] * arrx[i] for i in range(len(arr))])
        sum6_ = sum([arr[i] * y_vybirkove[i] * arrx[i] for i in range(len(arr))])
        sum7_ = sum([arr[i] * y_vybirkove[i] for i in range(len(arr))])
        n = sum(arr)
        return sum1_, sum2_, sum3_, sum4_, sum5_, sum6_, sum7_, n

    def system_eq(self):
        sum1, sum2, sum3, sum4, sum5, sum6, sum7, n = self.Sum()
        return f'{round(sum1, 3)}*A + {round(sum2, 3)}*B + {round(sum3, 3)}*C = {round(sum4, 3)}\n\n{round(sum2, 3)}*A + {round(sum3, 3)}*B + {round(sum5, 3)}*C = {round(sum6, 3)}\n\n{round(sum3, 3)}*A + {round(sum5, 3)}*B + {round(n, 3)}*C = {round(sum7, 3)}'

    def gauss_elimination(self):
        a11, a12, a13, b1, a32, b2, b3, a33 = self.Sum()
        a21 = a12
        a22 = a13
        a23 = a32
        a31 = a13

        # Elimination steps
        factor1 = a21 / a11
        factor2 = a31 / a11
        a22 -= factor1 * a12
        a23 -= factor1 * a13
        a32 -= factor2 * a12
        a33 -= factor2 * a13
        b2 -= factor1 * b1
        b3 -= factor2 * b1

        factor3 = a32 / a22
        a33 -= factor3 * a23
        b3 -= factor3 * b2

        # Back substitution
        C = b3 / a33
        B = (b2 - a23 * C) / a22
        A = (b1 - a12 * B - a13 * C) / a11


        return A, B, C

    def Solve_pow(self):
        A, B, C = self.gauss_elimination()
        return [A * (i ** 2) + B * i + C for i in self.get_x_i()], A, B, C

    def A_value(self):
        fx, A, B, C = self.Solve_pow()
        return f'{round(A, 3)}'

    def B_value(self):
        fx, A, B, C = self.Solve_pow()
        return f'{round(B, 3)}'

    def C_value(self):
        fx, A, B, C = self.Solve_pow()
        return f'{round(C, 3)}'

    def fx_value(self):
        fx, A, B, C = self.Solve_pow()
        return f'{round(A, 3)} * х^2 + {round(B, 3)} * x + {round(C, 3)}'

    def Sigma(self):
        temps = []
        arr = self.get_n_i()
        arry = self.get_y_i()

        n = sum(arr)
        fx, A, B, C = self.Solve_pow()
        matrix = self.MatrixWithout_xy()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j] * (abs(arry[i] - fx[j])) ** 2
                temps.append(temp)
        return sum(temps) / n

    def Delta(self):
        temps = []
        arr = self.get_n_i()

        y_vybirkove = self.Y_vybirkove()
        fx, A, B, C = self.Solve_pow()
        for i in range(0, len(y_vybirkove)):
            temp = arr[i] * ((abs(y_vybirkove[i] - fx[i])) ** 2)
            temps.append(temp)

        return sum(temps)

    def Sigma_value(self):
        return f'{round(self.Sigma(), 3)}'

    def Delta_value(self):
        return f'{round(self.Delta(), 3)}'


    def Graphic_fx(self):
        fx, A, B, C = self.Solve_pow()
        plt.close("all")
        fig10, ax10 = plt.subplots()
        ax10.plot(self.get_x_i(), fx, linestyle=':', color='black', label='Крива регресії f(x)')  # крива регресії
        ax10.plot(self.get_x_i(), self.Y_vybirkove(), marker='o', linestyle=':', color='blue', label='M(xi,y_)')  # моя функція
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік f(x) для параболічної кореляції')
        plt.grid(True)
        plt.legend()
        plt.show()

    #2) hyperbola fx = a\x + b
    def Sum2(self):
        arr = self.get_n_i()
        arrx = self.get_x_i()
        y_vybirkove = self.Y_vybirkove()
        sum1_ = sum([arr[i] / arrx[i] if arrx[i] != 0 else 0 for i in range(len(arr))])
        sum2_ = sum([arr[i] * y_vybirkove[i] for i in range(len(arr))])
        sum3_ = sum([arr[i] / (arrx[i]) ** 2 if arrx[i] != 0 else 0 for i in range(len(arr))])
        sum4_ = sum([arr[i] * y_vybirkove[i] / arrx[i] if arrx[i] != 0 else 0 for i in range(len(arr))])
        n = sum(arr)
        return sum1_, sum2_, sum3_, sum4_, n

    def system_eq2(self):
        sum1, sum2, sum3, sum4, n = self.Sum2()
        return f'A*{round(sum1,3)} + {n}*B = {round(sum2,3)} \n\nA*{round(sum3,3)} + B*{round(sum1,3)} = {round(sum4,3)}'

    def gauss_elimination2(self):
        sum1, sum2, sum3, sum4, n = self.Sum2()
        a11 = sum1
        a12 = n
        a21 = sum3
        a22 = sum1
        b1 = sum2
        b2 = sum4

        # Elimination steps
        factor = a21 / a11
        a22 -= factor * a12
        b2 -= factor * b1

        # Back substitution
        B = b2 / a22
        A = (b1 - a12 * B) / a11

        return A, B

    def Solve_pow2(self):
        A, B = self.gauss_elimination2()
        arrX = self.get_x_i()
        results = []
        for i in arrX:
            if i != 0:
                result = A / i + B
            else:
                result = 0
            results.append(result)
        return results, A, B


    def A_value2(self):
        fx, A, B = self.Solve_pow2()
        return f'{round(A, 3)}'

    def B_value2(self):
        fx, A, B = self.Solve_pow2()
        return f'{round(B, 3)}'

    def fx_value2(self):
        fx, A, B = self.Solve_pow2()
        return f'{round(A, 3)}/x + {round(B, 3)}'


    def GraphicM2(self):
        arrxi = self.get_x_i()
        arryi = self.Y_vybirkove()

        arrx = np.linspace(min(arrxi), max(arrxi) + 1, 1000)
        # y = 2.75 * np.exp(arrx)
        # yy = [i ** 2 for i in arrx]
        a_ = 0  # Параметр a
        b_ = 1  # Параметр b
        y1 = [np.sqrt(a_ ** 2 + (b_ * x) ** 2) for x in arrx]  # Верхня гілка гіперболи
        y2 = [-np.sqrt(a_ ** 2 + (b_ * x) ** 2) for x in arrx]  # Нижня гілка гіперболи
        # yyy = [x ** 0.5 for x in arrx]
        plt.close("all")
        fig3, ax3 = plt.subplots()
        plt.plot(arrxi, arryi, marker='o', linestyle='-', color='blue', label='Графік моєї функції')
        #ax3.plot(arrx, yy, color='red', label='Парабола')
        #ax3.plot(arrx, y, color='green', label='Експонента')
        ax3.plot(arrx, y1, color='orange', label='Верхня гілка гіперболи')
        ax3.plot(arrx, y2, color='orange', label='Нижня гілка гіперболи')
        #ax3.plot(arrx, yyy, color='purple', label='Коренева функція')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік точок Mi(x,y-)')
        plt.grid(True)
        plt.legend()

        plt.show()


    def Graphic_fx2(self):
        fx, A, B = self.Solve_pow2()
        arrX = self.get_x_i()
        plt.close("all")
        fig11, ax11 = plt.subplots()
        ax11.plot(arrX,fx, linestyle=':', color='black', label='Крива регресії f(x)' )  # крива регресії
        ax11.plot(arrX, self.Y_vybirkove(), marker='o', linestyle=':', color='blue', label='M(xi,y_)') # моя функція
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік f(x) для гіперболічної кореляції')
        plt.grid(True)
        plt.legend()
        plt.show()


    def Sigma2(self):
        temps = []
        arry = self.get_y_i()
        sum1, sum2, sum3, sum4, n = self.Sum2()
        fx, A, B = self.Solve_pow2()
        matrix = self.MatrixWithout_xy()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j]*(abs(arry[i]-fx[j]))**2
                temps.append(temp)
        return sum(temps) / n


    def Sigma_value2(self):
        return f'{round(self.Sigma2(),3)}'

    def Delta2(self):
        temps = []
        arrn = self.get_n_i()
        arry = self.Y_vybirkove()
        fx, A, B = self.Solve_pow2()
        for i in range(0,len(arry)):
            temp = arrn[i]*(abs(arry[i]-fx[i]))**2
            temps.append(temp)

        return sum(temps)


    def Delta_value2(self):
        return f'{round(self.Delta2(),3)}'


    #3) exponent corelation fx = ba^x,  a,b -?

    def Sum3(self):
        arr = self.get_n_i()
        arrx = self.get_x_i()
        arry = self.Y_vybirkove()

        sum1 = sum([arr[i] * (arrx[i]) for i in range(len(arr))])
        sum2 = sum([arr[i] * mt.log10(arry[i]) for i in range(len(arr))])
        sum3 = sum([arr[i] * (arrx[i])**2 for i in range(len(arr))])
        sum4 = sum([arr[i] * (arrx[i]) * mt.log10(arry[i])  for i in range(len(arr))])

        n = sum(arr)
        return sum1, sum2, sum3, sum4, n



    def system_eq3(self):
        sum1,sum2,sum3,sum4,n = self.Sum3()
        return f'lg(a)*{round(sum1,3)} + {n}*lg(b) = {round(sum2,3)} \n\nlg(a)*{round(sum3,3)} + lg(b)*{round(sum1,3)} = {round(sum4,3)}'


    def gauss_elimination3(self):
        sum1, sum2, sum3, sum4, n = self.Sum3()
        a11 = sum1
        a12 = n
        a21 = sum3
        a22 = sum1
        b1 = sum2
        b2 = sum4

        # Elimination steps
        factor = a21 / a11
        a22 -= factor * a12
        b2 -= factor * b1

        # Back substitution
        B = b2 / a22
        A = (b1 - a12 * B) / a11

        return A, B

    def Solve_pow3(self):
        A, B = self.gauss_elimination3()
        arrX = self.get_x_i()
        A, B = 10 ** A, 10 ** B
        return [B * A ** i for i in arrX], A, B

    # fx,A,B = Solve_pow()

    def A_value3(self):
        fx, A, B = self.Solve_pow3()
        return f'{round(A,3)}'

    def B_value3(self):
        fx, A, B = self.Solve_pow3()
        return f'{round(B,3)}'


    def fx_value3(self):
        fx, A, B = self.Solve_pow3()
        return f'{round(B,3)}*{round(A,3)}^x'


    def Graphic_fx3(self):
        fx, A, B = self.Solve_pow3()
        arrX = self.get_x_i()
        plt.close("all")
        fig12, ax12 = plt.subplots()
        ax12.plot(arrX,fx, linestyle=':', color='black', label='Крива регресії f(x)' )  # крива регресії
        ax12.plot(arrX, self.Y_vybirkove(), marker='o', linestyle=':', color='blue', label='M(xi,y_)') # моя функція
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік f(x) для показникової кореляції')
        plt.grid(True)
        plt.legend()
        plt.show()

    def MatrixWithout_xy(self):
        matrix_without_xy = self.read_from_file().copy()
        return [row[1:] for row in matrix_without_xy[1:]]


    def Sigma3(self):
        temps = []
        arry = self.get_y_i()
        sum1, sum2, sum3, sum4, n = self.Sum3()
        fx, A, B = self.Solve_pow3()
        matrix = self.MatrixWithout_xy()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j]*(abs(arry[i]-fx[j]))**2
                temps.append(temp)
        return sum(temps) / n


    def Sigma_value3(self):
        return f'{round(self.Sigma3(),3)}'

    def Delta3(self):
        temps = []
        arrn = self.get_n_i()
        arry = self.Y_vybirkove()
        fx, A, B = self.Solve_pow3()
        for i in range(0,len(arry)):
            temp = arrn[i]*(abs(arry[i]-fx[i]))**2
            temps.append(temp)

        return sum(temps)


    def Delta_value3(self):
        return f'{round(self.Delta3(),3)}'


#----------------------------------------------------------------
#4) sqrt corelation fx = a*x**0.5+b  a,b -?

    def Sum4(self):
        arr = self.get_n_i()
        arrx = self.get_x_i()
        arry = self.Y_vybirkove()
        sum1_ = sum([arr[i] * np.sqrt(arrx[i]) for i in range(len(arr))])
        sum2_ = sum([arr[i] * arry[i] for i in range(len(arr))])
        sum3_ = sum([arr[i] * arrx[i] for i in range(len(arr))])
        sum4_ = sum([arr[i] * arry[i] * np.sqrt(arrx[i]) for i in range(len(arr))])
        n = sum(arr)
        return sum1_, sum2_, sum3_,sum4_, n

    def system_eq4(self):
        sum1, sum2, sum3, sum4, n = self.Sum4()
        return f'A*{round(sum1,3)} + {n}*B = {round(sum2,3)} \n\nA*{round(sum3,3)} + B*{round(sum1,3)} = {round(sum4,3)}'

    def gauss_elimination4(self):
        a11, b1, a21, b2, a12 = self.Sum4()
        a22 = a11

        # Elimination steps
        factor = a21 / a11
        a22 -= factor * a12
        b2 -= factor * b1

        # Back substitution
        B = b2 / a22
        A = (b1 - a12 * B) / a11

        return A, B


    def Solve_pow4(self):
        A, B = self.gauss_elimination4()
        arryx = self.get_x_i()
        return [A*np.sqrt(i)+B for i in arryx], A, B

    def A_value4(self):
        fx, A, B = self.Solve_pow4()
        return f'{round(A,3)}'

    def B_value4(self):
        fx, A, B = self.Solve_pow4()
        return f'{round(B,3)}'

    def fx_value4(self):
        fx, A, B = self.Solve_pow4()
        return f'{round(A,3)}*√х+{round(B,3)}'


    def GraphicM4(self):
        arryx = self.get_x_i()
        plt.close("all")
        fig1, ax1 = plt.subplots()
        y = np.sqrt(arryx)
        yy = [i ** 2 for i in arryx]
        ax1.plot(arryx, self.Y_vybirkove(), marker='o', linestyle='-', color='blue')
        # ax1.plot(x_values,yy, color='red')
        ax1.plot(arryx, y, color='green')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік точок(x,y-)')
        plt.grid(True)
        plt.show()


    def Graphic_fx4(self):
        arryx = self.get_x_i()
        plt.close("all")
        fx, A, B = self.Solve_pow4()
        fig2, ax2 = plt.subplots()
        ax2.plot(arryx,fx, color='black')
        ax2.plot(arryx, self.Y_vybirkove() , marker='o', linestyle='-', color='blue')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Графік f(x) для кореневої гіперболяції')
        plt.grid(True)
        plt.show()

    def Sigma4(self):
        temps = []
        arry = self.get_y_i()
        sum1, sum2, sum3, sum4, n = self.Sum4()
        fx, A, B = self.Solve_pow4()
        matrix = self.MatrixWithout_xy()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = matrix[i][j] * (abs(arry[i] - fx[j])) ** 2
                temps.append(temp)
        return sum(temps) / n


    def Delta4(self):
        temps, arrn, arry = [], self.get_n_i(), self.Y_vybirkove()
        fx, A, B = self.Solve_pow4()
        for i in range(0, len(self.Y_vybirkove())):
            temp = arrn[i] * (abs(arry[i] - fx[i])) ** 2
            temps.append(temp)

        return sum(temps)

    def Sigma_value4(self):
        return f'{round(self.Sigma4(),3)}'

    def Delta_value4(self):
        return f'{round(self.Delta4(),3)}'



    def EditFile(self):
        from os import startfile
        startfile('Data.txt')


#   terrible  retry for treanslition






