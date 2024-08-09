import java.util.*;
public class firstOccurance {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String haystack = sc.nextLine();
		String needle = sc.nextLine();
		strStr(haystack, needle);
	}
	static int strStr(String haystack, String needle) {
        return haystack.indexOf(needle);
    }
}
