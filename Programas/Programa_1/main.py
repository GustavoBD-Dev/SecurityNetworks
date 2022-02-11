from PyQt5.QtWidgets import QDialog, QMessageBox
from ventana import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwards):
        QtWidgets.QMainWindow.__init__(self, *args, **kwards)
        self.setupUi(self)
        # cuando el boton pushButton es presionado manda a llamar a la 
        self.pushButtonCalculate.clicked.connect(self.validateData)
        self.pushButtonCalculateClear.clicked.connect(self.clearLines)

    # funcion sumar dias
    def sumarDias(self):
        day = self.day_current.currentText() # establece un texto
        time = self.time_current.time() # tiempo actual en horas y minutos 
        timeHour = time.hour() # tiempo actual en horas
        timeMinute = time.minute() # tiempo actual en minutos
        addDays = self.day_input.text() # dias para agregar 
        addHours = self.hour_input.text() # horas para agregar
        addMinutes = self.minutes_input.text() # minutos para agregar 

        #print(day)
        #print(str(timeHour))
        #print(str(timeMinute))
        #print(addDays)
        #print(addHours)
        #print(addMinutes)

        # convertimos dias a semanas y guardamos cociente y residuo 
        var_1Cociente = int(addDays)//7
        var_1Residuo = int(addDays)%7
        # convertims horas a dias y guardamos las horas restantes
        var_2Cociente = int(addHours)//24
        var_2Residuo = int(addHours)%24
        # convertimos minutos a horas y guardamos los minutos restantes 
        var_3Cociente = int(addMinutes)//60
        var_3Residuo = int(addMinutes)%60

        #print(var_1Cociente, var_1Residuo, var_2Cociente, var_2Residuo, var_3Cociente, var_3Residuo)

        varDias = 0 # almacenar el total de dias
        varHoras = 0 # almacenar el total de horas 
        varMinutos = 0 # almacenar el total de minutos 

        # var_1Cociente no cuenta porque son semanas 
        # var_1Residuo siempre debe ser menor a 7
        # agregamos los dias a la variable total
        varDias += var_1Residuo

        # agregamos el cociente a los dias 
        varDias += var_2Cociente
        #agregamos las hiras restantes a la variable
        varHoras += var_2Residuo

        #agregamos el cociente a la variable horas 
        varHoras += var_3Cociente
        #agregamos los minutos (residuo) a la variable minutos 
        varMinutos += var_3Residuo
        
        #print(varDias, varHoras, varMinutos)

        #convertimos las horas a dias y se agregan a los dias 
        varDias += varHoras//24
        #agregamos las horas restantes a la variable horas 
        varHoras = varHoras%24

        #print(varDias, varHoras, varMinutos)
        #convertir los dias a semanas y solo ocupamos los dias restantes (modulo)
        varDias = varDias%7 # debe ser menor a 7

        #print(varDias, varHoras, varMinutos)

        # CODE
        dayCurrent = 0 # variable para dias 
        week = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
        for i in range(len(week)):
            #print(i)
            if week[i] == day:
                #print('i: ', i)
                dayCurrent += i
                #print('dayCurrent: ',dayCurrent)
        """
        1.- Realizamos la suma de los minutos, si es mayor a 60 incrementamos una hora, restamos 60 a variable horas.
        2.- Realizamos la suma de las horas, si es mayor a 24 incrementamos un dia, restamos 24 a variable horas.
        3.- Realizamos la suma de los dias, si es mayor a 7 reiniciamos la semana.
        """
        timeMinute += varMinutos
        if timeMinute >= 60:
            timeHour += 1
            timeMinute -= 60

        timeHour += varHoras
        if timeHour >= 24:
            dayCurrent += 1
            timeHour -= 24
        
        dayCurrent += varDias
        if dayCurrent >= 7:
            dayCurrent -= 7
        print(dayCurrent)
        print(week[dayCurrent], timeHour, timeMinute)
        #asignamos los valores en las celdas
        out = str(week[dayCurrent]) + ' ' + str(timeHour) + ':' + str(timeMinute) #+ ' a.m.' if timeHour<12 else ' p.m.'
        self.values_output.setText(out)
        
    def clearLines(self):
        # clear inputs and outputs
        self.values_output.setText('')
        self.day_input.setText('') 
        self.hour_input.setText('')
        self.minutes_input.setText('') 

    def validateData(self):
        if (not self.day_input.text().isnumeric()) or (not self.hour_input.text().isnumeric()) or (not self.minutes_input.text().isnumeric()):
            self.show_dialog()
        else:
            self.sumarDias()

    def show_dialog(self):
        QMessageBox.about(self, "Alerta!!", "Verificar campos de entrada")

class Dialog(QDialog):
    def __init__(self, *args, **kwards):
        super(Dialog, self).__init__(*args, **kwards)
        self.setWindowTitle('Alerta')
        self.setFixedSize(200, 100)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

