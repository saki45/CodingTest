import java.util.HashMap;

class HashMapTest {
	public static void main(String[] args){
		HashMap<String, Integer> hm = new HashMap<String, Integer>();

		hm.put("one",1);
		hm.put("two",2);
		hm.put("three",3);

		int v = hm.get("one").intValue();
		System.out.println(v);

		for(String str : hm.keySet())
			System.out.println(str);
		hm.remove("one");

		for(String str : hm.keySet())
			System.out.println(str);
	}
}
