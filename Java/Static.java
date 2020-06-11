import java.util.Scanner;

public class Static {
    static Scanner scan = new Scanner(System.in);
    static boolean flag = false;
    static int B = scan.nextInt();
    static int H = scan.nextInt();

static {
    if (B <= 0 || H <= 0){
        System.out.println("java.lang.Exception: Breadth and height must be positive");
    }
    else
    {
        flag = true;
    }
}

public static void main(String[] args){
		if(flag){
			int area=B*H;
			System.out.print(area);
		}
	}
}
