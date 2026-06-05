import java.util.Scanner;

public class Q3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter first integer: ");
        int a = sc.nextInt();

        System.out.print("Enter second integer: ");
        int b = sc.nextInt();

        System.out.print("Enter a float number: ");
        float c = sc.nextFloat();

        float average = ((float)a + (float)b + c) / 3;

        System.out.println("Average = " + average);
    }
}
