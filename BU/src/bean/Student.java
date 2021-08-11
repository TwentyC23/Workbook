package bean;

public class Student extends Reader {
	private String address;
	
	public Student(String name, String email, String college, String address) {
		super(name, email, college);
		this.docs = 3;
		this.period = 10;
		this.address = address;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return super.toString() + " is a Student [address=" + address + "]";
	}

}
