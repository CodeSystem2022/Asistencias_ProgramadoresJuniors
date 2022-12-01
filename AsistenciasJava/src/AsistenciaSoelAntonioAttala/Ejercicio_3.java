//Ejecutar una matriz de 3x3, transponerla y mostrarla
package matriz_ejercicio_3;
import java.util.Scanner;
public class Matriz_Ejercicio_3{
    public static void main(String[]args){
        Scanner entrada = new Scanner(Systemn.in);
        int matriz [] [] = new int [3] [3];
        System.out.println("LLenamos Matriz");
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print("Matriz ["+i+"]["+j+"]: ");
                matriz [i] [j] = entrada.nextInt();
            }
        }
        System.out.println();

        System.out.println("matriz original: ");
        for(int i=0;i<3;i++){
            for(int j=0;j<3;j++){
                System.out.print(matriz[i] [j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
}