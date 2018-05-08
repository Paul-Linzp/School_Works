package test;

public class TEST {
	public static void main(String[] args) {
		StringBuffer test = new StringBuffer();
		test.append('1');
		test.append('a');
		if(test.toString().charAt(0) >= 39) {
			System.out.println("success");
		}
		System.out.println(test.toString().charAt(1));
	}
	
}
