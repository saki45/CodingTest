public class SimpleFactory {

	public Fruit create(String fruit) {
		switch(fruit){
			case "Apple":
				return new Apple();
			case "Orange":
				return new Orange();
		}
		return null;
	}
}
