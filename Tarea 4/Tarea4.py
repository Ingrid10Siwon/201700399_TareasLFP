import webbrowser
import sys
import os
from string import Template
print("TAREA NO 4")



def reporte():
    filein = open('tarea4.html')

    src=Template(filein.read())
    #lista =['Carlos','23','true','0','lore','21','false','0']
#    lista = [
#        {
#        'nombre':'Carlos',
#        'edad': 21,
#        'activo':'true',
#        'saldo':'0'
#        },
#        {
#        'nombre':'Carlos',
#        'edad': 21,
#        'activo':'true',
#        'saldo':'0'
#        },
#        {
#        'nombre':'Carlos',
#        'edad': 21,
#        'activo':'true',
#        'saldo':'0'
#        },
#        {
#        'nombre':'Carlos',
#        'edad': 21,
#        'activo':'true',
#        'saldo':'0'
#        }
#    ]
    d = {'nombre':'Carlos', 'edad':'21','activo':'true','saldo':'10','nombre2':'Priscyla','edad2':'17','activo2':'false','saldo2':'50', 'nombre3':'Mauricio','edad3':'25','activo3':'true','saldo3':'90', 'nombre4':'Daniela','edad4':'16','activo4':'false','saldo4':'250',
    'nombre5':'Juan','edad5':'30','activo5':'false','saldo5':'100', 'nombre6':'Cristina','edad6':'19','activo6':'true','saldo6':'200', 'nombre7':'Irma','edad7':'27','activo7':'false','saldo7':'1000', 'nombre8':'David','edad8':'31','activo8':'true','saldo8':'40',
    'nombre9':'Lesly','edad9':'24','activo9':'true','saldo9':'25', 'nombre10':'Alejandra','edad10':'45','activo10':'false','saldo10':'85'}
    result = src.substitute(d)

    try:
        os.mkdir("Tarea4")
        filein2= open('Tarea4/'+'201700399'+'.html','a')
        filein2.writelines(result)
        print("Creando")
    except OSError:
        if os.path.exists('Tarea4'):

            filein2= open('Tarea4/'+'201700399'+'.html','a')
            filein2.writelines(result)
    nombreArchivo = "file:///C:/Users/logas/Documents/python/Tarea4/201700399.html"
    webbrowser.open_new_tab(nombreArchivo)



    #d = {'nombre':'Carlos', 'edad':'21','activo':'true','saldo':'0','nombre':'Lore','edad':'21','activo':'false','saldo':'0'}
     
    #f=open('Tarea4.html','w')
    #mensaje=""""<html>
    #<head></head>
    #<body><p>Tarea4</p></body>
    #</html>"""
    #f.write(mensaje)
    #f.close()
    #nombreArchivo='C://Users/logas/Documents/python/'+'Tarea4.html'
    #webbrowser.open_new_tab(nombreArchivo)


    