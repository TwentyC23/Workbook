package modeldao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import bean.Avion;



public class DAOAvion extends DAO<Avion>{

	public DAOAvion(Connection connection) {
		super(connection);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void create(Avion obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("insert into avion(id_avion, nom_cons, d_p_vol,hr_vol) values(?, ?, ?,?)");
			statement.setString(1, obj.getId_avion());
			statement.setString(2, obj.getNom_cons());
			statement.setString(3, obj.getD_p_vol());
			statement.setInt(4, obj.getHr_vol());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}		
	}

	@Override
	public void update(Avion obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("update avion set nom_cons = ?, d_p_vol = ? ,hr_vol= ? where id_avion = ?");
			statement.setString(1, obj.getNom_cons());
			statement.setString(2, obj.getD_p_vol());
			statement.setInt(3, obj.getHr_vol());
			statement.setString(4, obj.getId_avion());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void delete(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("delete from avion where id_avion = ?");
			statement.setString(1, id);
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public Avion find(String id, String obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("select " + obj + " from avion where id_avion = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Avion avion = new Avion(id, 0, "","");

			while (r.next()) {
				if (obj == "hr_pays") {
					avion.setHr_vol(r.getInt("hr_pays"));
				}
				if (obj == "d_p_vol") {
					avion.setD_p_vol(r.getString("d_p_vol"));
				}
				if (obj == "nom_cons") {
					avion.setNom_cons(r.getString("nom_cons"));
				}
			}
			return 	avion;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public Avion findAll(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("select * from avion where id_avion = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Avion avion = new Avion(id, 0,"","");

			while (r.next()) {
				avion.setHr_vol(r.getInt("hr_vol"));
				avion.setD_p_vol(r.getString("d_p_vol"));
				avion.setNom_cons(r.getString("nom_cons"));
			}
			return avion;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
	}
	
	}

	
	
}
