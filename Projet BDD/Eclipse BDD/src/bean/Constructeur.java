package bean;

public class Constructeur {
	private String nom_cons="";
	private String d_f_cons="";
	private String adr_cons="";
	
	public Constructeur(String nom_cons, String d_f_cons, String adr_cons) {
		this.nom_cons=nom_cons;
		this.d_f_cons=d_f_cons;
		this.adr_cons=adr_cons;
	}

	public String getNom_cons() {
		return nom_cons;
	}

	public void setNom_cons(String nom_cons) {
		this.nom_cons = nom_cons;
	}

	public String getD_f_cons() {
		return d_f_cons;
	}

	public void setD_f_cons(String d_f_cons) {
		this.d_f_cons = d_f_cons;
	}

	public String getAdr_cons() {
		return adr_cons;
	}

	public void setAdr_cons(String adr_cons) {
		this.adr_cons = adr_cons;
	}

	@Override
	public String toString() {
		return "Constructeur [nom_cons=" + nom_cons + ", d_f_cons=" + d_f_cons + ", adr_cons=" + adr_cons + "]";
	}
}