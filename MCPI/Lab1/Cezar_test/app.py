import encrypt
import main
import sys




class MW:

    def main(self):
        ui = main.Ui_MainWindow()
        ui.setupUi(ui.MainWindow)
        ui.MainWindow.show()
        sys.exit(ui.app.exec_())


        
tmp = MW()
tmp.main()