public class RemoteLoader {

	public static void main(String[] args) {
		RemoteControl rc = new RemoteControl();

		Light livingRoomLight = new Light("Living Room");
		Light kitchenLight = new Light("Kitchen");

		rc.setCommand(0, new LightOnCommand(livingRoomLight),
					new LightOffCommand(livingRoomLight));
		rc.setCommand(1, new LightOnCommand(kitchenLight),
					new LightOffCommand(kitchenLight));

		System.out.println(rc.toString());

		rc.onCommandButtonPushed(2);
		rc.onCommandButtonPushed(0);
		rc.onCommandButtonPushed(1);
		rc.offCommandButtonPushed(0);
		rc.undoCommandButtonPushed();
	}
}
