/*
Asistencia Renzo Viscio mes Noviembre
Arreglos Ejercicio 2
 */
package AsistenciasRenzoViscio;

import java.util.Scanner;

public class Arreglos_Ejercicio_2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float numeros[] = new float[5];
        
        System.out.println("Guardando los elementos del arreglo");
        for(int i=0; i<5;i++){
            System.out.println((i+1) + ". Digite un n�mero: ");
            numeros[i] = entrada.nextFloat();
        }
        
        System.out.println("\nImprimimos los n�meros del arreglo");
        for(int i=4;i>=0;i--){
            System.out.println(" " + numeros[i]);
        }
        System.out.println("\n");
    }
}
