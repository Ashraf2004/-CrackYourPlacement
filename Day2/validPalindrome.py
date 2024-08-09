
import java.util.*;
public class validPalindrome {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		System.out.print(check(s));
	}
	static boolean check(String s) {
        int count = 0;
        int i =0 , j = s.length()-1;
        while(i<=j){
            if(s.charAt(i) != s.charAt(j)){
                count ++;
                if(count > 1){
                    return false;
                }else{
                    return isPalindrome(s, i + 1, j) || isPalindrome(s, i, j - 1);
                }
            }else{
            i++;
            j--;
            }
        }
        return true;
    }
    static boolean isPalindrome(String str, int i, int j){
        while(i<j){
            if(str.charAt(i) != str.charAt(j)){
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
