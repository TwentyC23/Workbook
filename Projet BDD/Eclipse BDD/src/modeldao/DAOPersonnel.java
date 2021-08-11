package modeldao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


import bean.Personnel;

public class DAOPersonnel extends DAO<Personnel>{

	public DAOPersonnel(Connection connection) {
		super(connection);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void create(Personnel obj) {

		try {
			PreparedStatement statement = connection
					.prepareStatement("insert into personnel(num_pers,nom_pers, pré_pers, qual_pers,num_comp) values(?, ?, ?,?,?)");
			statement.setString(1, obj.getNum_pers());
			statement.setString(2, obj.getNom_pers());
			statement.setString(3, obj.getPré_pers());
			statement.setString(4, obj.getQual_pers());
			statement.setString(5, obj.getNum_comp());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void update(Personnel obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("update compagnie set nom_pers = ?, pré_pers = ?, qual_pers = ?, num_comp=? where num_pers = ? ");
			statement.setString(1, obj.getNom_pers());
			statement.setString(2, obj.getPré_pers());
			statement.setString(3, obj.getQual_pers());
			statement.setString(4, obj.getNum_comp());
			statement.setString(5, obj.getNum_pers());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}		
	}

	@Override
	public void delete(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("delete from personnel where num_pers = ?");
			statement.setString(1, id);
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public Personnel find(String id, String obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("select " + obj + " from personnel where num_pers= ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Personnel personnel = new Personnel(id, "", "","","");

			while (r.next()) {
				if (obj == "nom_pers") {
					personnel.setNom_pers(r.getString("nom_pers"));
				}
				if (obj == "pré_pers") {
					personnel.setPré_pers(r.getString("pré_pers"));
				}
				if (obj == "qual_pers") {
					personnel.setQual_pers(r.getString("qual_pers"));
				}
				if (obj == "num_comp") {
					personnel.setNum_comp(r.getString("num_comp"));
				}
			}
			return 	personnel;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public Personnel findAll(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("select * from personnel where num_pers = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Personnel personnel = new Personnel(id, "","","","");

			while (r.next()) {
				personnel.setNom_pers(r.getString("nom_pers"));
				personnel.setPré_pers(r.getString("pré_pers"));
				personnel.setQual_pers(r.getString("qual_pers"));
				personnel.setNum_comp(r.getString("num_comp"));
			}
			return personnel;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
	}
	}

}
