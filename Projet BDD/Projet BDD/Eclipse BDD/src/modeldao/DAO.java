package modeldao;


import java.sql.Connection;

public abstract class DAO<T> {

    protected Connection connection;

    public DAO(Connection connection) {
        this.connection = connection;
    }

    // Méthode permettant de créer un objet d'une classe
    public abstract void create(T obj);

    // Méthode permettant de mettre à jour une classe
    public abstract void update(T obj);

    // Méthode permettant de supprimer un objet d'une classe
    public abstract void delete(String id);

    // Méthode permettant de rechercher un objet d'une classe
    public abstract T find(String id, String obj);

    // Méthode de rechercher tous les objets d'une classe
    public abstract T findAll(String id);

}