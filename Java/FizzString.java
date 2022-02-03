# Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" return "Buzz". If both the "f" and "b" conditions are true, return "FizzBuzz". In all other cases, return the string unchanged.

#fizzString("fig") → "Fizz"
#fizzString("dib") → "Buzz"
#fizzString("fib") → "FizzBuzz"


public class FizzString {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		String word = "facebook";
		String otherWord = "Github";
		String both = "facehub";
		
		System.out.println(typeofString(word));
		System.out.println(typeofString(otherWord));
		System.out.println(typeofString(both));

	}
	
	public static String typeofString(String word) {
		
		if (word.charAt(0) == 'f' && word.charAt(word.length()-1) == 'b') {
			return "FizzBuzz";
		}
		
		else if (word.charAt(0) == 'f') {
			return "Fizz";
		}
		
		else if (word.charAt(word.length()-1) == 'b') {
			return "Buzz";
		}
		
		return null;
	}

}
