package modeldao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;


import bean.Compagnie;


public class DAOCompagnie extends DAO<Compagnie>{

	public DAOCompagnie(Connection connection) {
		super(connection);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void create(Compagnie obj) {
		try {
			PreparedStatement statement = connection
					.prepareStatement("insert into compagnie(num_comp,nom_comp, creat_comp, nom_pays) values(?, ?, ?,?)");
			statement.setString(1, obj.getNum_comp());
			statement.setString(2, obj.getNom_comp());
			statement.setString(3, obj.getCreat_comp());
			statement.setString(4, obj.getNom_pays());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		// TODO Auto-generated method stub
		
	}

	@Override
	public void update(Compagnie obj) {
		try {
			PreparedStatement statement = connection
					.prepareStatement("update compagnie set nom_comp = ? , creat_comp = ?, nom_pays = ? where num_comp = ?" );
			statement.setString(1, obj.getNom_comp());
			statement.setString(2, obj.getCreat_comp());
			statement.setString(3, obj.getNom_pays());
			statement.setString(4, obj.getNum_comp());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		// TODO Auto-generated method stub
		
	}

	@Override
	public void delete(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("delete from compagnie where num_comp = ?");
			statement.setString(1, id);
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public Compagnie find(String id, String obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("select " + obj + " from compagnie where nom_comp = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Compagnie compagnie = new Compagnie(id, "", "","");

			while (r.next()) {
				if (obj == "nom_comp") {
					compagnie.setNom_comp(r.getString("nom_comp"));
				}
				if (obj == "creat_comp") {
					compagnie.setCreat_comp(r.getString("creat_comp"));
				}
				if (obj == "nom_pays") {
					compagnie.setNom_pays(r.getString("nom_pays"));
				}
			}
			return 	compagnie;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public Compagnie findAll(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("select * from compagnie where num_comp = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Compagnie compagnie = new Compagnie(id, "","","");

			while (r.next()) {
				compagnie.setNom_comp(r.getString("nom_comp"));
				compagnie.setCreat_comp(r.getString("creat_comp"));
				compagnie.setNom_pays(r.getString("nom_pays"));
			}
			return compagnie;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
	}
	}


}
