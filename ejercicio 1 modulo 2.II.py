def datos():
	h=float(input("Ingrese horas:"))
	m=float(input("Ingrese minutos:"))
	s=float(input("Ingrese segundos:"))
	return h, m, s

def calc_dia(h,m,s):
	return (h/24)+(m/1440)+(s/86400)

def mostrar_dia(dia):
	print(h,":",m,":",s," Es equivalente a", dia,"dias.")   #ten�as 'dias' en vez de 'dia'
	
def calcular_dia():
	h,m,s = datos()
	dia = calc_dia(h,m,s)
	mostrar_dia(dia)

h,m,s= datos()                                                  #si pones return, tiene que guardar los datos en alg�n lado
                                                                #; ah� se guardan corresponientemente horas con horas
                                                                # dias con dias y segundos con segundos
                                                                
dia=calc_dia(h,m,s)                                             # Lo mismo con los d�as, si pones return, tienes que guardar el dato en alg�n lado
mostrar_dia(dia)
calcular_dia() 

