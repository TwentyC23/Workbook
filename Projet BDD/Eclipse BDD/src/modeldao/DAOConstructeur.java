package modeldao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import bean.Constructeur;



public class DAOConstructeur extends DAO<Constructeur>{

	public DAOConstructeur(Connection connection) {
		super(connection);
		// TODO Auto-generated constructor stub
		
	}

	@Override
	public void create(Constructeur obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("insert into constructeur(nom_cons, d_f_cons, adr_cons) values(?, ?, ?)");
			statement.setString(1, obj.getNom_cons());
			statement.setString(2, obj.getD_f_cons());
			statement.setString(3, obj.getAdr_cons());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void update(Constructeur obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("update constructeur set d_f_cons= ?, adr_cons = ? where nom_cons= ?");
			
			statement.setString(1, obj.getD_f_cons());
			statement.setString(2, obj.getAdr_cons());
			statement.setString(3, obj.getNom_cons());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void delete(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("delete from constructeur where Nom_cons = ?");
			statement.setString(1, id);
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public Constructeur find(String id, String obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("select " + obj + " from constructeur where nom_cons = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Constructeur constructeur = new Constructeur(id, "", "");

			while (r.next()) {
				if (obj == "hbt_pays") {
					constructeur.setD_f_cons(r.getString("D_f_cons"));
				}
				if (obj == "adr_cons") {
					constructeur.setAdr_cons(r.getString("adr_cons"));
				}
			}
			return constructeur;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public Constructeur findAll(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("select * from constructeur where nom_cons = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Constructeur constructeur = new Constructeur(id, "", "");

			while (r.next()) {
				constructeur.setD_f_cons(r.getString("d_f_cons"));
				constructeur.setAdr_cons(r.getString("adr_cons"));
			}
			return constructeur;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
	}
	}
}
