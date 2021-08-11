package modeldao;


import java.sql.Connection;

import bean.Avion;
import bean.Compagnie;
import bean.Constructeur;
import bean.Pays;
import bean.Personnel;
import connectionjdbc.Connectionjdbc;

public class DAOFactory {

    private static final Connection connection = Connectionjdbc.getInstance();

    public static DAO<Avion> getDAOAvion() {
        return new DAOAvion(connection);
    }
    public static DAO<Compagnie> getDAOCompagnie() {
    	return new DAOCompagnie(connection);
    }
    public static DAO<Personnel> getDAOPersonnel() {
    	return new DAOPersonnel(connection);
    }
    public static DAO<Pays> getDAOPays() {
    	return new DAOPays(connection);
    }
    public static DAO<Constructeur> getDAOConstructeur(){
    	return new DAOConstructeur(connection);
    }
}