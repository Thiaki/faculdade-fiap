package br.com.fiap.aula08;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class conexao {

  public static void main(String[] args) {
    try {
      //Registra o Driver
      Class.forName("oracle.jdbc.driver.OracleDriver");

      //Abre uma conexão
      Connection conexao = DriverManager.getConnection(
          "jdbc:oracle:thin:@192.168.60.15:1521:ORCL", "OPS$PF0392", "123456");
      
      System.out.println("Conectado!");
      
      Statement stmt = conexao.createStatement();
      stmt.executeUpdate("INSERT INTO TAB_COLABORADOR(CODIGO_COLABORADOR, NOME, EMAIL, SALARIO, DATA_CONTRATACAO)"
      		+ "VALUES (SQ_COLABORADOR.NEXTVAL, 'Leandro', 'leandro@gmail.com', 1500, TO_DATE('10/12/2009','dd/mm/yyyy'))");
      
      PreparedStatement stmt2 = conexao.prepareStatement("INSERT INTO TAB_COLABORADOR(CODIGO_COLABORADOR, NOME, EMAIL, SALARIO, DATA_CONTRATACAO)"
      		+ "VALUES (SQ_COLABORADOR.NEXTVAL, ?, ?, ?, ?)");
      stmt2.setString(1, "Thiago"); //Primero parâmetro (Nome)
      stmt2.setString(2, "thiago@gmail.com");//Segundo parâmetro (Email)
      stmt2.setDouble(3, 5000); //Terceiro parâmetro (Salário)
      //Instancia um objeto do tipo java.sql.Date com a data atual
      java.sql.Date data = new java.sql.Date(new java.util.Date().getTime());
      stmt2.setDate(4,data);//Quarto parâmetro (data contratação)
            
      stmt2.executeUpdate();
      
      //Fecha a conexão
      conexao.close();
      
    //Tratamento de erro  
    } catch (SQLException e) {
      System.err.println("Não foi possível conectar no Banco de Dados");
      e.printStackTrace();
    } catch (ClassNotFoundException e) {
      System.err.println("O Driver JDBC não foi encontrado!");
      e.printStackTrace();
    }
  }
}