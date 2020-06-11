import java.util.Scanner;

public class Printf {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                String str=sc.next();
                int x=sc.nextInt();
                System.out.printf("%-15s%03d%n", str, x);
            }
            System.out.println("================================");

    }
}

