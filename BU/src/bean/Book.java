package bean;

public class Book extends Document {
	private String author;
	
	public Book(String id, String title, double price, String author, double repayment, int copy) {
		super(id, title, price);
		this.repayment = repayment;
		this.author = author;
		this.copy = copy;
	}

	public String getAuthor() {
		return author;
	}

	public void setAuthor(String author) {
		this.author = author;
	}

	@Override
	public String toString() {
		return super.toString() + " is a Book [author=" + author + "]";
	}
	
}
