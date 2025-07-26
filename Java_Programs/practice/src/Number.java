import java.util.Scanner;
public class Number {
    public static void prime_number(int n){
        int count = 0;
        for(int i=1;i<=n;i++){
            if(n%i==0){
                count++;
            }
        }
        if(count==2){
            System.out.print(n+" is a Prime Number");
        }
        else{
            System.out.print(n+" is not a Prime Number");
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int num = sc.nextInt();
        prime_number(num);
    }
}
