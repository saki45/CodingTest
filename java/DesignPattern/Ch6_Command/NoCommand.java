public class NoCommand implements Command {
	public void execute() {
		System.out.println("Command not defined!");
	}

	public void undo() {
		System.out.println("Command not defined!");
	}
}
