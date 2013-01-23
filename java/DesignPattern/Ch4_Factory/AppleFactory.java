public class AppleFactory implements GeneralFactory {

	public Fruit create() {
		return new Apple();
	}
}
