import java.util.Scanner;
import java.util.ArrayList;

public class StringTokens {

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.nextLine();
        scan.close();

        ArrayList<String> tokens = new ArrayList<>();
        String temp = "";

        for (char c: s.toCharArray()){
            if (Character.isLetter(c)) {
                temp += c;
                continue;
            }
            if (temp.length() > 0){
                tokens.add(temp);
            }
            temp = "";
        }

            //  Last token is skipped in the loop and for single tokens
            if (temp.length() > 0){
                tokens.add(temp);
            }

        System.out.println(tokens.size());
        tokens.forEach(System.out::println);
    }
}
