package bean;

public class Pays {
	private String nom_pays="";
	private int hbt_pays=0;
	private String cpt_pays="";
	
	public Pays(String nom_pays, int hbt_pays, String cpt_pays) {
		this.nom_pays=nom_pays;
		this.hbt_pays=hbt_pays;
		this.cpt_pays=cpt_pays;
	}

	public String getNom_pays() {
		return nom_pays;
	}

	public void setNom_pays(String nom_pays) {
		this.nom_pays = nom_pays;
	}

	public int getHbt_pays() {
		return hbt_pays;
	}

	public void setHbt_pays(int hbt_pays) {
		this.hbt_pays = hbt_pays;
	}

	public String getCpt_pays() {
		return cpt_pays;
	}

	public void setCpt_pays(String cpt_pays) {
		this.cpt_pays = cpt_pays;
	}

	@Override
	public String toString() {
		return "Pays [nom_pays=" + nom_pays + ", hbt_pays=" + hbt_pays + ", cpt_pays=" + cpt_pays + "]";
	}
	
}

