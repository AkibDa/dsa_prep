import java.lang.Math;
import java.util.Scanner;

public class Number {

    public static int count_digits(int n){
        int count = 0;
        while(n>0){
            int digit = n%10;
            count++;
            n=n/10;
        }
        return count;
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
        prime_number(num);
        armstrong_number(num);
    }
}
