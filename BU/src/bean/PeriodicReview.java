package bean;

public class PeriodicReview extends Document {
	private int number, year;
	
	public PeriodicReview(String id, String title, double price, int number, int year) {
		super(id, title, price);
		this.copy = 1;
		this.repayment = 100;
		this.number = number;
		this.year = year;
	}

	public int getNumber() {
		return number;
	}

	public void setNumber(int number) {
		this.number = number;
	}

	public int getYear() {
		return year;
	}

	public void setYear(int year) {
		this.year = year;
	}

	@Override
	public String toString() {
		return super.toString() + " is a PeriodicReview [number=" + number + ", year=" + year + "]";
	}
	
}
