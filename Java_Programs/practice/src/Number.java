import java.lang.Math;
import java.util.Scanner;

public class Number {

    public static int count_digits(int n){
        int count = 0;
        while(n>0){
            count++;
            n=n/10;
        }
        return count;
    }

    public static int factorial(int n){
        return n==1?1:n*factorial(n-1);
    }

    public static void krishnamurti_number(int n){
        int m=n;
        int temp, sum=0;
        while(n>0){
            temp=n%10;
            sum += factorial(temp);
            n=n/10;
        }
        if(sum==m){
            System.out.println(m+" is a krishnamurti number\n");
        }
        else{
            System.out.println(m+" is not a krishnamurti number\n");
        }
    }

    public static void palindrome_number(int n){
        int m=n;
        int temp, sum=0;
        while(n>0){
            temp=n%10;
            sum = sum*10+temp;
            n=n/10;
        }
        if(sum==m){
            System.out.println(m+" is a palindrome number\n");
        }
        else{
            System.out.println(m+" is not a palindrome number\n");
        }
    }

    public static void armstrong_number(int n){
        int m=n;
        int digits = count_digits(n);
        int digit,sum = 0;
        while(n>0){
            digit=n%10;
            sum+= Math.pow(digit,digits);
            n=n/10;
        }
        if(sum==m){
            System.out.println(m+" is a armstrong number\n");
        }
        else{
            System.out.println(m+" is not a armstrong number\n");
        }
    }

    public static void prime_number(int n){
        int count = 0;
        for(int i=1;i<=n;i++){
            if(n%i==0){
                count++;
            }
        }
        if(count==2){
            System.out.print(n+" is a Prime Number\n");
        }
        else{
            System.out.print(n+" is not a Prime Number\n");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();

        System.out.println("Do u want to check weather a number is prime or not ?");
        String choice = sc.next();

        if (choice == "yes"){
            prime_number(num);
        }
        else if (choice == "no"){
            System.out.println("Do u want to check weather a number is armstrong or not ?");
            choice = sc.next();
            if (choice.equals("yes")){
                armstrong_number(num);
            }
            else if (choice.equals("no")){
                System.out.println("Do u want to check weather a number is palindrome or not ?");
                choice = sc.next();
                if (choice.equals("yes")){
                    palindrome_number(num);
                }
                else if (choice.equals("no")){
                    System.out.println("Do u want to check weather a number is krishnamurti or not ?");
                    choice = sc.next();
                    if (choice.equals("yes")){
                        krishnamurti_number(num);
                    }
                }
            }
        }
        sc.close();
    }
}
