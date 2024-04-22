Proceso sin_titulo
	Definir n, divisor, contador Como Entero;
	Leer n;
	divisor = 1;
	contador = 0;
	Mientras contador < 2 o divisor < n Hacer
		Si n mod divisor == 0 Entonces
			contador = contador + 1;
		FinSi
		divisor = divisor +1;
	FinMientras
	
	Si contador == 2 Entonces
		Escribir  "ES PRIMO";
	SiNo
		Escribir  "NO ES PRIMO";
	FinSi
FinProceso
