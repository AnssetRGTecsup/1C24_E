Proceso sin_titulo
	Definir n, divisor, suma Como Entero;
	Leer n;
	suma = 0;
	
	Para divisor <- 1 Hasta n - 1 Con Paso 1 Hacer
		Si n mod divisor == 0 Entonces
			Escribir divisor;
			suma = suma + divisor;
		FinSi
	FinPara
	
	Escribir suma;
	
	Si suma == n Entonces
		Escribir "PERFECTO";
	SiNo
		Escribir "NO PERFECTO";
	FinSi
FinProceso
