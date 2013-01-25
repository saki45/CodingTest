public class ReverseString {

	public static String reverseString(String str) {
		if(str.length() == 0)
			return "";
		else if(str.length() == 1)
			return str;
		else {
			int l = str.length();
			return str.substring(l-1) + reverseString(str.substring(0, l-1));
		}
	}

	public static void main(String[] args) {
		System.out.println(reverseString("abcd"));
		System.out.println(reverseString(""));
		System.out.println(reverseString("a"));
		System.out.println(reverseString("ab"));
		System.out.println(reverseString("  "));
		System.out.println(reverseString("a b"));
	}
}
