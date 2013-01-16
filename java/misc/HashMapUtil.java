import java.util.HashMap;
import java.util.Iterator;

class HashMapUtil {

	HashMap<String, Integer> hm;

	public HashMapUtil() {

		hm = new HashMap<String, Integer>();

		hm.put("one", 1);
		hm.put("two", 2);
		hm.put("three", 3);
		hm.put("four", 4);
		hm.put("five", 5);

		Iterator<String> iterKey = hm.keySet().iterator();

		while(iterKey.hasNext()) {

			String tmpKey = iterKey.next();
			System.out.print(tmpKey + " :");
			int tmpValue = hm.get(tmpKey).intValue();
			System.out.println(tmpValue);

		}
	}

	public static void main(String[] args) {

		new HashMapUtil();

	}
}
