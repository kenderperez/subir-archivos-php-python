import sys
import zipfile



argumentos = sys.argv
argumento1 = str(argumentos[1])
punto = argumento1.find('.')
nombre = argumento1[:punto]
#CREAR ARCHIVO ZIP

archivoZip = zipfile.ZipFile(f'{nombre}.zip','w') #abre un nuevo archivo zip con  permisos de escritura --mirar: segundo parametro
archivoZip.write(f'archivos/{argumento1}', compress_type=zipfile.ZIP_DEFLATED) #este archivo es el que se comprimira y ya tiene que estar en la carpeta raiz del programa
archivoZip.close()

#devolver la ruta del archivo zip creado
ruta = f'http://localhost/{nombre}.zip'
print(ruta)
