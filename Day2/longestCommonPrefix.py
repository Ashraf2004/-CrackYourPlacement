
import java.util.*;
public class longestCommonPrefix {
	public static void main(String[] args) {
		String[] strs = {"flower","flow","flight"};
		System.out.print(longestCommonPrefix(strs));
	}
	static String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return ""; // Check for empty or null array
        }

        String res = "";
        int minlen = strs[0].length();
        String minstr = strs[0];

        for (int i = 1; i < strs.length; i++) {
            if (strs[i].isEmpty() || strs[i - 1].isEmpty() || strs[i - 1].charAt(0) != strs[i].charAt(0)) {
                return ""; // Return if any string is empty or first characters don't match
            }
            if (strs[i].length() < minlen) {
                minlen = strs[i].length();
                minstr = strs[i];
            }
        }

        int j = 0;
        boolean flag = true;

        while (j < minlen && flag) {
            for (int i = 0; i < strs.length; i++) {
                if (minstr.charAt(j) != strs[i].charAt(j)) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                res += minstr.charAt(j);
                j++;
            }
        }
        return res;
    }
}
