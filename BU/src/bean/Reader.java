package bean;

public abstract class Reader {
	private String name, email, college;
	public int docs, period;
	
	public Reader(String name, String email, String college) {
		this.name = name;
		this.email = email;
		this.college = college;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getCollege() {
		return college;
	}

	public void setCollege(String college) {
		this.college = college;
	}

	public int getDocs() {
		return docs;
	}

	public void setDocs(int docs) {
		this.docs = docs;
	}

	public int getPeriod() {
		return period;
	}

	public void setPeriod(int period) {
		this.period = period;
	}

	@Override
	public String toString() {
		return "Reader [name=" + name + ", email=" + email + ", college=" + college + ", docs=" + docs + ", period="
				+ period + "]";
	}
	
}
