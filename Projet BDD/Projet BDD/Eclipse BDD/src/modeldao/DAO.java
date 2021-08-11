package modeldao;


import java.sql.Connection;

public abstract class DAO<T> {

    protected Connection connection;

    public DAO(Connection connection) {
        this.connection = connection;
    }

    // M�thode permettant de cr�er un objet d'une classe
    public abstract void create(T obj);

    // M�thode permettant de mettre � jour une classe
    public abstract void update(T obj);

    // M�thode permettant de supprimer un objet d'une classe
    public abstract void delete(String id);

    // M�thode permettant de rechercher un objet d'une classe
    public abstract T find(String id, String obj);

    // M�thode de rechercher tous les objets d'une classe
    public abstract T findAll(String id);

}