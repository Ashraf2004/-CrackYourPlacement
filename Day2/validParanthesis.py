
import java.util.*;
public class validParanthesis {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String s = sc.nextLine();
		System.out.print(isValid(s));
	}
	static boolean isValid(String s) {
        char[] arr = s.toCharArray();
        boolean res = true;
        Map<Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');
        Stack<Character> stack = new Stack<>();
        for(char i : arr){
            if(stack.isEmpty()){
                if(i == '}' || i == ']' || i == ')'){
                    return false;
                } 
            }
            if(i == '(' || i == '{' || i == '['){
                stack.push(i);
            }
            else if(map.get(stack.pop()) != i){
                res = false;
                break;
            }
        }
        if(!stack.isEmpty()){
            res = false;
        }
        return res;
    }
}
