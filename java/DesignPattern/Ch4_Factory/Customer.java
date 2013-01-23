public class Customer {

	public static void main(String[] args) {

		System.out.println("\nSimple Factory Pattern:");
		SimpleFactory sf = new SimpleFactory();
		Fruit ap1 = sf.create("Apple");
		ap1.display();
		Fruit or1 = sf.create("Orange");
		or1.display();

		System.out.println("\nFactory Method Pattern:");
		GeneralFactory fa = new AppleFactory();
		GeneralFactory fo = new OrangeFactory();
		Fruit ap2 = fa.create();
		ap2.display();
		Fruit or2 = fo.create();
		or2.display();
		
		System.out.println("\nAbstract Factory Pattern:");
		AbstractFactory afa = new AppleFactory2();
		AbstractFactory afo = new OrangeFactory2();
		Fruit ap3 = afa.create();
		ap3.display();
		OrganicFruit apo = afa.createOrganic();
		apo.display();
		Fruit or3 = afo.create();
		or3.display();
		OrganicFruit oro = afo.createOrganic();
		oro.display();
	}
}
