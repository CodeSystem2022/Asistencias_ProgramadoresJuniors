/*
Ejercicio: LEER 5 NUMEROS, GUARDARLOS EN UN ARREGLO Y MOSTRARLOS EN EL MISMO ORDEN INTRODUCIDOS
 */
package AsistenciaEmirMaya;

import java.util.Scanner;

/**
 *
 */
public class Ejercicio {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float[] arreglo = new float[5];

        System.out.println("Gurdando los datos en el arreglo");
        for (int i = 0; i < 5; i++) {
            System.out.print("Dugute un número: ");
            arreglo[i] = sc.nextFloat();
        }

        System.out.println("\nImprimir los elementos del arreglo");
        for (float i : arreglo) {
            System.out.print(i + " ");
        }
        System.out.println("\n");

    }

}
