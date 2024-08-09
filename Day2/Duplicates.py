# Print all the duplicate characters in a string
import java.util.*;
public class Duplicates{
	public static void main(String[] args) {
		String  str = "test string";
		printDup(str);
	}
	static void printDup(String str) {
		Map<Character, Integer> map = new HashMap<>();
		for(int i=0; i<str.length(); i++) {
			map.put(str.charAt(i), map.getOrDefault(str.charAt(i), 0)+1);
		}
		for(Map.Entry<Character, Integer> entry : map.entrySet()) {
			if(entry.getValue()>1) {
				System.out.print(entry.getKey()+" ");
			}
		}
	}
}