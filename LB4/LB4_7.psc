Proceso sin_titulo
	Definir n, divisor Como Entero;
	Leer n;
	divisor = 1;
	Mientras divisor <= n Hacer
		Si n mod divisor == 0 Entonces
			Escribir divisor;
		FinSi
		divisor = divisor + 1;
	FinMientras
FinProceso
