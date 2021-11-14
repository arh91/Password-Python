'''
Created on 15 may. 2020

@author: PackardBell
'''


def main():
    
    contador = [0]
    correcto = False
    
    while (True):
        print("A continuacion usted debe introducir una contrasenha.")
        print("Para que sea valida, la contrasenha debera tener una longitud de minimo 6 caracteres y maximo 20")
        print("Tambien debera contener como minimo 1 letra mayuscula, y como minimo 2 numeros")
        print("Y por ultimo, tambien debera contener uno de los siguientes caracteres especiales")
        print("(_, #, $, &)")
        tecla = input("Si lo ha entendido pulse la tecla Enter, e iremos al siguiente paso")
        print("")
        if(tecla==''):
            break
        
        
    while(True):
        
        password = input("Por favor, introduzca una contrasenha.")
        longitud = len(password)-1        
        password = list(password)
        
        
        """Contamos cuantas mayusculas hay"""
        mayusculas = len([c for c in password if c.isupper()])        
        
        """Contamos cuantos numeros hay"""
        numeros = len([c for c in password if c.isdigit()])
        
                  
        def buscarCaracteres(list, list2):
            for caracter in list:
                if caracter=="_" or caracter=="#" or caracter=="$" or caracter=="&":
                    list2[0]=1
                    break
              
        buscarCaracteres(password, contador)
        
        """Convertimos la lista Contador en un entero c"""
        c = int("".join(map(str, contador)))           
        
        if longitud>=6 and longitud<=20 and mayusculas>0 and numeros>1 and c==1:
            correcto = True
            print(correcto)
            break
        else:
            print("Formato de contrasenha incorrecto")
            print("")
    
        
main() 