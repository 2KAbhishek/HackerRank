import java.util.Scanner;

public class Anagrams {

    static boolean isAnagram(String a, String b) {
        if (a.length() != b.length())
            return false;

        int [] countsA = new int[26];
        int [] countsB = new int[26];
        a = a.toLowerCase();
        b = b.toLowerCase();

        for (int i = 0; i < a.length(); i++){
            countsA[a.charAt(i) - 'a']++;
            countsB[b.charAt(i) - 'a']++;
        }
        
        for (int i = 0; i < countsA.length; i++){
            if (countsA[i] != countsB[i])
                return false;
        }
        
        return true;
    }

  public static void main(String[] args) {
    
        Scanner scan = new Scanner(System.in);
        String a = scan.next();
        String b = scan.next();
        scan.close();
        boolean ret = isAnagram(a, b);
        System.out.println( (ret) ? "Anagrams" : "Not Anagrams" );
    }
}
