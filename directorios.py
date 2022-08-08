from importlib.resources import path
import sys, os, re
from PyQt5.QtWidgets import QAction, QApplication, QFileDialog, QMainWindow
from CreadorPlantilla import CreadorPlantilla


class CreadorPlantillaAplicacion(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = CreadorPlantilla()
        self.ui.setupUi(self)

        self.ui.Boton_Seleccionar.clicked.connect(self.fileManager)
        self.ui.Boton_Ejecutar.clicked.connect(self.CreateDir)
        self.ui.actionSalir.triggered.connect(lambda: self.Salir())
    
    def fileManager(self):
        folder = str(QFileDialog.getExistingDirectory(None, "Select Directory"))
        #nombre = QFileDialog.getOpenFileName(self, 'seleccion de archivo', 'C:/')
        #ruta = nombre[0]
        self.ui.Seleccion.setText(folder)
        print(folder)
    

    def CreateDir(self): 
       
       NumCarpetas = self.ui.carpetas.value()
       NumSubCarpetas = self.ui.subcarpetas.value()
       #guardar ruta y separarla en trozos

       ruta = self.ui.Seleccion.text()

       #comprueba que se a seleccionado un directorio
       if ruta == "":
        self.ui.aviso_error.setText('Por favor, seleccione un directorio')
        return

       resultado = re.split('[/]+', ruta)

       #nombre para directorios a crear
       
       ind_resultado = resultado.__len__()
       directorios = re.split('[.]+', resultado[ind_resultado -1])
       rutaNueva = ''

       for i in range(ind_resultado - 1):
        rutaNueva += resultado[i] + '/'

       #crea carpetas

       if NumCarpetas > 0 :
        for cantidad_carpetas in range(NumCarpetas):
            rutaCarpetaPrincipal = rutaNueva + directorios[0] + '_' + str(cantidad_carpetas)
            if os.path.exists(rutaCarpetaPrincipal):
                self.ui.aviso_error.setText('Las carpetas ya existen. Borrelas si desea continuar')
                return
            os.mkdir(rutaCarpetaPrincipal)
            if NumSubCarpetas > 0:
                for cantidad_subcarpetas in range(NumSubCarpetas):
                    os.mkdir(rutaCarpetaPrincipal + '/' + 'subcarpeta_' + str(cantidad_subcarpetas))
                    print(rutaCarpetaPrincipal + '/' + 'subcarpeta_' + str(cantidad_subcarpetas))

        

    def Salir(self):
        sys.exit()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CreadorPlantillaAplicacion()
    ventana.show()
    sys.exit(app.exec())