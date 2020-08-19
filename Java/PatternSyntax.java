import java.util.Scanner;
import java.util.regex.*;

public class PatternSyntax
{
    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int testCases = Integer.parseInt(in.nextLine());
        while(testCases>0){
            String pattern = in.nextLine();
            boolean valid = true;
            try {
                Pattern.compile(pattern);
            } catch (Exception e) {
                valid = false;
            }
            if (valid) System.out.println("Valid");
            else System.out.println("Invalid");
            testCases--;
        }
    }
}

