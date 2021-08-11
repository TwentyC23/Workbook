package modeldao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import bean.Pays;

public class DAOPays extends DAO<Pays>{

	public DAOPays(Connection connection) {
		super(connection);
		// TODO Auto-generated constructor stub
	}

	@Override
	public void create(Pays obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("insert into pays (nom_pays, hbt_pays, cpt_pays) values(?, ?, ?)");
			statement.setString(1, obj.getNom_pays());
			statement.setInt(2, obj.getHbt_pays());
			statement.setString(3, obj.getCpt_pays());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void update(Pays obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("update pays set hbt_pays = ?, cpt_pays = ? where nom_pays = ?");
			statement.setInt(1, obj.getHbt_pays());
			statement.setString(2, obj.getCpt_pays());
			statement.setString(3, obj.getNom_pays());
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public void delete(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("delete from pays where nom_pays = ?");
			statement.setString(1, id);
			statement.execute();
		} catch (SQLException e) {
			e.printStackTrace();
		}
	}

	@Override
	public Pays find(String id, String obj) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection
					.prepareStatement("select " + obj + " from pays where pays_id = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Pays pays = new Pays(id, 0, "");

			while (r.next()) {
				if (obj == "hbt_pays") {
					pays.setHbt_pays(r.getInt("hbt_pays"));
				}
				if (obj == "cpt_pays") {
					pays.setCpt_pays(r.getString("cpt_pays"));
				}
			}
			return pays;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
		}
	}

	@Override
	public Pays findAll(String id) {
		// TODO Auto-generated method stub
		try {
			PreparedStatement statement = connection.prepareStatement("select * from pays where nom_pays = ?");
			statement.setString(1, id);
			ResultSet r = statement.executeQuery();
			Pays pays = new Pays(id, 0, "");

			while (r.next()) {
				pays.setHbt_pays(r.getInt("hbt_pays"));
				pays.setCpt_pays(r.getString("cpt_pays"));
			}
			return pays;

		} catch (SQLException e) {
			e.printStackTrace();
			return null;
	}
	}
}
