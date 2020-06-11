import java.util.Scanner;

class Loops2{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int k=a;
            for(int j=0;j<n;j++)
            {
                k+=b*(int)Math.pow(2,j);
                System.out.print(k+" ");
            }
            System.out.println();
        }
        in.close();
    }
}