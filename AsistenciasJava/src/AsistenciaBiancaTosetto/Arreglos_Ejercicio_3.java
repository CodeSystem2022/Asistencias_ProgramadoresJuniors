/*
Ejercicio 3: leer 5 numeros por teclado, almacenarlos en un arreglo y a continuacion
realizar la media de los numeros positivos, la media de los numeros negativos y contar
el numero de ceros.
*/
package AsistenciaBiancaTosetto;

import java.util.Scanner;


public class Arreglos_Ejercicio_3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        float negativos = 0, positivos = 0, mediaNegativos, mediaPositivos;
        int conteo0 = 0, conteoNegativos = 0, conteoPositivos = 0;
        
        System.out.println("Guardamos los elementos del arreglo: ");
        for(int i = 0; i < 5; i++){
            System.out.println((i+i) + ". Digite un numero: ");
            numeros[i] = entrada.nextFloat();
            if(numeros[i] > 0){
                positivos += numeros[i];
                conteoPositivos++;
            }
            else if(numeros[i] < 0){
                negativos += numeros[i];
                conteoNegativos++;
            }
            else{
                conteo0++;
            } 
        }
        
        if(conteoPositivos == 0){
            System.out.println("\nNo se puede sacar la media de los numeros positivos");
        }
        else{
            mediaPositivos = positivos/conteoPositivos;
            System.out.println("\nLa media de los numeros positivos es: " + mediaPositivos);
        }
        
        if(conteoNegativos == 0){
            System.out.println("\nNo se puede sacar la media de los numeros negativos");
        }
        else{
            mediaNegativos = negativos/conteoNegativos;
            System.out.println("La media de los numeros negativos es: " + mediaNegativos);
        }
        
        System.out.println("La cantidad de ceros es: " + conteo0);
    }
}
