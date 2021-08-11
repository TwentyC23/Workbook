package connectionjdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Connectionjdbc {

    private static Connection connection;

    private Connectionjdbc() {
        try {
            String url = "jdbc:postgresql://localhost:5432/postgres";
            String user ="postgres";
            String password = "postgres";
            connection = DriverManager.getConnection(url,user,password);
        }
        catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static Connection getInstance(){
        if (connection == null)
            new Connectionjdbc();
        return connection;
    }
}
