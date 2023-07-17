


import java.util.Scanner;
import java.lang.*;
class Calculator {
    public double add(double a, double b) {
        return a + b;
    }

    public double subtract(double a, double b) {
        return a - b;
    }

    public double multiply(double a, double b) {
        return a * b;
    }

    public double divide(double a, double b) {
        if (b == 0) {
            throw new ArithmeticException("Cannot divide by zero!");
        }
        return a / b;
    }

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        double a = sc.nextDouble();
        double b = sc.nextDouble();
        String operation = sc.next();
        Calculator calculator = new Calculator();

        double result;

        switch (operation) {
            case "addition":
                result = calculator.add(a, b);
                System.out.println("Result of addition: " + result);
                break;
            case "subtraction":
                result = calculator.subtract(a, b);
                System.out.println("Result of subtraction: " + result);
                break;
            case "multiplication":
                result = calculator.multiply(a, b);
                System.out.println("Result of multiplication: " + result);
                break;
            case "division":
                result = calculator.divide(a, b);
                System.out.println("Result of division: " + result);
                break;
            default:
                System.out.println("Invalid operation specified!");
                break;
        }
    }
}
