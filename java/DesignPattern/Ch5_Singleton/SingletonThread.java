public class SingletonThread implements Runnable {

	int ID;
	public SingletonThread(int ID) {
		this.ID = ID;
	}

	public void run() {
		Singleton sl = Singleton.getInstance(ID);
		sl.display(ID);
	}
}
