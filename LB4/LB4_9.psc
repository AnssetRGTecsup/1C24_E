Proceso sin_titulo
	Definir n, divisor, suma Como Entero;
	Leer n;
	divisor = 1;
	suma = 0;
	Mientras divisor < n Hacer
		Si n mod divisor == 0 Entonces
			Escribir divisor;
			suma = suma + divisor;
		FinSi
		divisor = divisor + 1;
	FinMientras
	
	Escribir suma;
	
	Si suma == n Entonces
		Escribir "PERFECTO";
	SiNo
		Escribir "NO PERFECTO";
	FinSi
FinProceso
