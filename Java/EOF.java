import java.util.Scanner;

public class EOF {

    public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    for (int count = 1; scan.hasNext(); count++){
        String text = scan.nextLine();
        System.out.println(count +" "+ text);
    }
    }
}