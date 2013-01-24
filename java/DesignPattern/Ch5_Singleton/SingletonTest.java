
public class SingletonTest {

	public static void main(String[] args) {

		Runnable[] re = new SingletonThread[3];
		Thread[] threads = new Thread[3];
		for(int i=0; i<3; i++) {
			re[i] = new SingletonThread(i);
			threads[i] = new Thread(re[i]);
		}

		for(Thread t : threads) {
			t.start();
		}

		for(Thread t : threads) {
			t.yield();
		}
		
	}
}
			
