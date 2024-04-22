Proceso sin_titulo
	Definir n, iterad Como Entero;
	Repetir
		Escribir "Escribir un número positivo:";
		Leer n;
		Si n < 0 Entonces
			Escribir "NUMERO INCORRECTO";
		FinSi
	Hasta Que n > 0;
	
	Definir iterador, maxMulti Como Entero;
	
	Repetir
		Escribir "Escribir cuántas veces iterar:";
		Leer maxMulti;
		Si maxMulti < 0 Entonces
			Escribir "NUMERO INCORRECTO";
		FinSi
	Hasta Que maxMulti > 0
	
	iterador = 0;
	
	Mientras iterador <= maxMulti Hacer
		Escribir iterador * n;
		iterador = iterador + 1;
	FinMientras
FinProceso
