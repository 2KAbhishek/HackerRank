import java.util.Scanner;

public class StringCompare {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = "";
        String largest = "";
        String[] subs = new String[(s.length() - k) + 1];

        for (int i = 0; i <= s.length() - k; i++){
            subs[i] = s.substring(i,i+k);
        }

        smallest = subs[0];
        largest = subs[subs.length - 1];

        for (int i = 0; i < subs.length; i++){
            if (smallest.compareTo(subs[i]) > 0)
                smallest = subs[i];
            if (largest.compareTo(subs[i]) < 0)
                largest = subs[i];
        }
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        int k = scan.nextInt();
        scan.close();

        System.out.println(getSmallestAndLargest(s, k));
    }
}
