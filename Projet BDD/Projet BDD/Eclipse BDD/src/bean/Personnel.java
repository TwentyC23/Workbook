package bean;

public class Personnel {
	private String num_pers="";
	private String nom_pers="";
	private String pr�_pers="";
	private String qual_pers="";
	private String num_comp="";
	
	public Personnel(String num_pers, String nom_pers, String pr�_pers,String qual_pers, String num_comp) {
		this.num_pers=num_pers;
		this.nom_pers=nom_pers;
		this.pr�_pers=pr�_pers;
		this.qual_pers=qual_pers;
		this.num_comp=num_comp;
	}

	public String getNum_pers() {
		return num_pers;
	}

	public void setNum_pers(String num_pers) {
		this.num_pers = num_pers;
	}

	public String getNom_pers() {
		return nom_pers;
	}

	public void setNom_pers(String nom_pers) {
		this.nom_pers = nom_pers;
	}

	public String getPr�_pers() {
		return pr�_pers;
	}

	public void setPr�_pers(String pr�_pers) {
		this.pr�_pers = pr�_pers;
	}

	public String getQual_pers() {
		return qual_pers;
	}

	public void setQual_pers(String qual_pers) {
		this.qual_pers = qual_pers;
	}

	@Override
	public String toString() {
		return "Personnel [num_pers=" + num_pers + ", nom_pers=" + nom_pers + ", pr�_pers=" + pr�_pers + ", qual_pers="
				+ qual_pers + ", num_comp=" + num_comp + "]";
	}

	public String getNum_comp() {
		return num_comp;
	}

	public void setNum_comp(String nom_comp) {
		this.num_comp = nom_comp;
	}
	
}

