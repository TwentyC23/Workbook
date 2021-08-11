package bean;

public class Teacher extends Reader {
	private String phone;
	
	public Teacher(String name, String email, String college, String phone) {
		super(name, email, college);
		this.docs = 5;
		this.period = 14;
		this.phone = phone;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	@Override
	public String toString() {
		return  super.toString() + " is a Teacher [phone=" + phone + "]";  
	}
	
}
