package numero_perfecto;

import java.util.Scanner;

/**
 *
 * @author serra
 */
public class Numero_perfecto {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int num, divisor, sumadivisores;
        divisor = 1;
        sumadivisores = 0;
        Scanner entrada = new Scanner(System.in);
        System.out.print ("Introduzca un número mayor que 0: ");
        num = entrada.nextInt();
        while (divisor <= num/2)
        {   if (num % divisor == 0)
                sumadivisores = sumadivisores + divisor;
            divisor++;
        }    
        if (num == sumadivisores)
            System.out.println("El número " + num + " es un número perfecto");
        else
            System.out.println("El número " + num + " no es número perfecto ");
        
        
       
    }
    
}
