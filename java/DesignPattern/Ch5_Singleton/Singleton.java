public class Singleton {

	private volatile static Singleton instance;

	private Singleton() {
		System.out.println("Instance Initialized!");
	}

	public static Singleton getInstance(int ID) {
		if(instance == null) {
			synchronized(Singleton.class) {
				System.out.println(ID + ": getInstance()");
				if(instance == null) {
					instance = new Singleton();
				}
			}
		}
		return instance;
	}
	
	public void display(int ID) {
		System.out.println(ID + " display()");
	}
}
