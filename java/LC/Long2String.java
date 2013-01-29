public class Long2String {

	public static void long2String(long num) {
		if(num < 0) {
			System.out.print('-');
			long2String(-num);
		}
		else if(num < 10) {
			System.out.print(num);
		}
		else {
			long2String(num/10);
			System.out.print(num % 10);
		}
	}

	public static void main(String[] args) {
		long2String(0);
		System.out.println();
		long2String(5);
		System.out.println();
		long2String(-5);
		System.out.println();
		long2String(233);
		System.out.println();
		long2String(-233);
		System.out.println();
		long2String(123456789012345L);
		System.out.println();
		long2String(-123456789012345L);
		System.out.println();
	}
}
