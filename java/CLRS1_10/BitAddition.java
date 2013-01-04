public class BitAddition {
	public static void main(String[] args) {
		int a = Integer.parseInt(args[0]);
		int b = Integer.parseInt(args[1]);

		int c, d;

		while(b != 0) {
			c = a ^ b;
			d = (a & b)<<1;
			a = c;
			b = d;
		}

		System.out.println(a);
	}
}
