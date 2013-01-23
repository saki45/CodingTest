public class AppleFactory2 implements AbstractFactory {

	public Fruit create() {
		return new Apple();
	}

	public OrganicFruit createOrganic() {
		return new OrganicApple();
	}
}
