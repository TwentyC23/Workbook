package bean;

public class Avion {
    private String id_avion = "";
    private int hr_vol= 0;
    private String d_p_vol = "";
    private String nom_cons= "";

    public Avion(String id_avion, int hr_vol, String d_p_vol, String nom_cons) {
        this.id_avion = id_avion;
        this.hr_vol= hr_vol;
        this.d_p_vol = d_p_vol;
        this.nom_cons = nom_cons;
    }

	public String getId_avion() {
		return id_avion;
	}

	public void setId_avion(String id_avion) {
		this.id_avion = id_avion;
	}

	public int getHr_vol() {
		return hr_vol;
	}

	public void setHr_vol(int hr_vol) {
		this.hr_vol = hr_vol;
	}

	public String getD_p_vol() {
		return d_p_vol;
	}

	public void setD_p_vol(String d_p_vol) {
		this.d_p_vol = d_p_vol;
	}

	public String getNom_cons() {
		return nom_cons;
	}

	public void setNom_cons(String nom_cons) {
		this.nom_cons = nom_cons;
	}

	@Override
	public String toString() {
		return "Avion [id_avion=" + id_avion + ", hr_vol=" + hr_vol + ", d_p_vol=" + d_p_vol + ", nom_cons=" + nom_cons
				+ "]";
	}
    

}