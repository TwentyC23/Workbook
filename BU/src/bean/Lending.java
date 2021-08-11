package bean;

import java.util.Date;

public class Lending {
	private Reader name;
	private Document id;
	private Date date;
	private int period;
	
	public Lending(Reader name, Document id, Date date) {
		this.name = name;
		this.id = id;
		this.date = date;
		this.period = this.name.getPeriod();
	}
	
	// lending of a document
	public Lending lend() {
		name.setDocs(name.getDocs() - 1);
		id.setCopy(id.getCopy() - 1);
		return new Lending(name, id, date);
	}
	
	// check if lending is possible
	public boolean check_lending() {
		return check_copy() && check_docs();
	}
	
	// check if enough copy
	private boolean check_copy() {
		return id.getCopy() > 0;
	}
	
	// check if the reader can borrow more documents
	private boolean check_docs() {
		return name.getDocs() > 0;
	}
	
	// return document
	public void return_doc() {
		name.setDocs(name.getDocs() + 1);
		id.setCopy(id.getCopy() + 1);
	}
	
	// return delay is over
	public boolean warning() {
		Date dateAfter = new Date();
		long diff = dateAfter.getTime() - date.getTime();
		float res = diff / (1000*60*60*24);
		
		if (res > period) {
			return true;
		}
		else {
			return false;
		}
	}
	
	// document lost
	public double lost() {
		name.setDocs(name.getDocs() + 1);
		return (id.getPrice() * id.getRepayment()) / 100;
	}

	public Reader getName() {
		return name;
	}

	public void setName(Reader name) {
		this.name = name;
	}

	public Document getId() {
		return id;
	}

	public void setId(Document id) {
		this.id = id;
	}

	public Date getDate() {
		return date;
	}

	public void setDate(Date date) {
		this.date = date;
	}

	public int getPeriod() {
		return period;
	}

	public void setPeriod(int period) {
		this.period = period;
	}

	@Override
	public String toString() {
		return "Lending [name=" + name.getName() + "address=" + name.getEmail() +", title=" + id.getTitle() + ", date=" + date + ", period=" + period + "]";
	}

}
