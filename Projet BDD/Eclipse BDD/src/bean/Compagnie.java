package bean;

public class Compagnie {
	private String num_comp="";
	private String nom_comp="";
	private String creat_comp="";
	private String nom_pays="";
	
	public Compagnie(String num_comp , String nom_comp, String creat_comp, String nom_pays) {
		this.num_comp=num_comp;
		this.nom_comp=nom_comp;
		this.creat_comp=creat_comp;
		this.nom_pays=nom_pays;	
	}

	public String getNum_comp() {
		return num_comp;
	}

	public void setNum_comp(String num_comp) {
		this.num_comp = num_comp;
	}

	public String getNom_comp() {
		return nom_comp;
	}

	public void setNom_comp(String nom_comp) {
		this.nom_comp = nom_comp;
	}

	public String getCreat_comp() {
		return creat_comp;
	}

	public void setCreat_comp(String creat_comp) {
		this.creat_comp = creat_comp;
	}

	public String getNom_pays() {
		return nom_pays;
	}

	public void setNom_pays(String nom_pays) {
		this.nom_pays = nom_pays;
	}

	@Override
	public String toString() {
		return "Compagnie [num_comp=" + num_comp + ", nom_comp=" + nom_comp + ", creat_comp=" + creat_comp
				+ ", nom_pays=" + nom_pays + "]";
	}
	
}
