import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class RegexTest {

	public static void main(String[] args) {

		Pattern p = Pattern.compile("\\d{3}");
		
		try {
			BufferedReader br = new BufferedReader(
						new FileReader("test.txt"));
			String str;
			while((str = br.readLine()) != null) {
				System.out.println(str);
				Matcher m = p.matcher(str);
				while(m.find()){
					System.out.println(m.group());
				}
			}
			br.close();
		}
		catch(FileNotFoundException ex) {
			ex.printStackTrace();
		}
		catch(IOException ex) {
			ex.printStackTrace();
		}
	}
}
