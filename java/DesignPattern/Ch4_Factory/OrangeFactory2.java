public class OrangeFactory2 implements AbstractFactory {

	public Fruit create() {
		return new Orange();
	}

	public OrganicFruit createOrganic() {
		return new OrganicOrange();
	}
}
