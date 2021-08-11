package bean;

public abstract class Document {
	private String id, title;
	private double price;
	public double repayment;
	public int copy;
	
	public Document(String id, String title, double price) {
		this.id = id;
		this.title = title;
		this.price = price;
	}


	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getTitle() {
		return title;
	}

	public void setTitle(String title) {
		this.title = title;
	}

	public double getPrice() {
		return price;
	}

	public void setPrice(double price) {
		this.price = price;
	}

	public int getCopy() {
		return copy;
	}

	public void setCopy(int copy) {
		this.copy = copy;
	}

	public double getRepayment() {
		return repayment;
	}

	public void setRepayment(double repayment) {
		this.repayment = repayment;
	}


	@Override
	public String toString() {
		return "Document [id=" + id + ", title=" + title + ", price=" + price + ", repayment=" + repayment + ", copy="
				+ copy + "]";
	}
	
}
