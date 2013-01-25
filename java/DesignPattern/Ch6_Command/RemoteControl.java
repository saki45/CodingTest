public class RemoteControl {

	Command[] onCommands;
	Command[] offCommands;
	Command undoCommand;

	public RemoteControl() {
		onCommands = new Command[3];
		offCommands = new Command[3];

		Command noCommand = new NoCommand();

		for(int i=0; i<3; i++) {
			onCommands[i] = noCommand;
			offCommands[i] = noCommand;
		}
		undoCommand = noCommand;
	}

	public void setCommand(int slot, Command onCommand, Command offCommand) {
		onCommands[slot] = onCommand;
		offCommands[slot] = offCommand;
	}

	public void onCommandButtonPushed(int slot){
		onCommands[slot].execute();
		undoCommand = onCommands[slot];
	}

	public void offCommandButtonPushed(int slot) {
		offCommands[slot].execute();
		undoCommand = offCommands[slot];
	}

	public void undoCommandButtonPushed() {
		undoCommand.undo();
	}

	public String toString() {
		StringBuffer sb = new StringBuffer();
		sb.append("\n----- Remote Control -----\n");
		for(int i=0;i<onCommands.length;i++) {
			sb.append("[slot " + i + "] " + onCommands[i].getClass().getName() + "\t" + offCommands[i].getClass().getName() + "\n");
		}

		return sb.toString();
	}
}
