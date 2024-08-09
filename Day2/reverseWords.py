
import java.util.Scanner;

public class reverseWords {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		System.out.print(reverse(str));
	}
	static String reverse(String s) {
        String[] arr = s.trim().split("\\s+");
        String str = "";
        for (int i = arr.length - 1; i > 0; i--) {
            str += arr[i] + " ";
        }
        str += arr[0]; 
        return str;
    }
}
