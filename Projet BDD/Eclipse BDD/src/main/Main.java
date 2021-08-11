package main;

import java.util.Scanner;
import bean.Constructeur;
import bean.Pays;
import bean.Compagnie;
import bean.Avion;
import bean.Personnel;
import modeldao.DAO;
import modeldao.DAOFactory;

public class Main {
	private static DAO<Constructeur>ConstructeurDAO=DAOFactory.getDAOConstructeur();
	private static DAO<Pays>PaysDAO=DAOFactory.getDAOPays();
	private static DAO<Compagnie>CompagnieDAO=DAOFactory.getDAOCompagnie();
	private static DAO<Avion>AvionDAO=DAOFactory.getDAOAvion();
	private static DAO<Personnel>PersonnelDAO=DAOFactory.getDAOPersonnel();

	
	public static void main(String[] args) {
    
		boolean quit=(false);
		boolean back1=(false);
		boolean back2=(false);
		boolean back3=(false);
		boolean back4=(false);
		boolean back5=(false);
		System.out.println("Choisisez une table de donnée à éxaminer/modifier:");
		System.out.println("1- Constructeur");
		System.out.println("2- Pays");
		System.out.println("3- Compagnie");
		System.out.println("4-Avion");
		System.out.println("5-Personnel");
		System.out.println("6-Quitter le programme");

		Scanner scanner = new Scanner(System.in);
		int choice = scanner.nextInt();
		
		do {
			switch (choice) {
	    		case 1:
	    			do {
	    				System.out.println("Choisissez une action à effectuer avec la table de donnée Constructeur:");
	    				System.out.println("1-Ajouter un élément à la table");
	    				System.out.println("2-Modifier un élément de la table");
	    				System.out.println("3-Suprimer un élément de la table");
	    				System.out.println("4-Trouver un élément de la table");
	    				System.out.println("5-Trouver tout les éléments de la table");
	    				Scanner scanner1 = new Scanner(System.in);
	    				int choice1 = scanner1.nextInt();
	    				
	    				switch (choice1) {
	    				
		    				case 1:
		    					Scanner scanner1_1_1 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur:");
		    					String nom_cons1 = scanner1_1_1.next();
		    					
		    					Scanner scanner1_1_2 = new Scanner(System.in);
		    					System.out.println("Date de fondation du constructeur:");
		    					String d_f_cons1 = scanner1_1_2.next();
		    					
		    					Scanner scanner1_1_3 = new Scanner(System.in);
		    					System.out.println("Adresse du constructeur:");
		    					String adr_cons1 = scanner1_1_3.next();
		    					
		    					Constructeur constructeur1 = new Constructeur (nom_cons1, d_f_cons1 , adr_cons1);
		    					ConstructeurDAO.create(constructeur1);
		    					break;
	    				
	    				
			    			case 2:
		    					Scanner scanner1_2_1 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur:");
		    					String nom_cons2 = scanner1_2_1.next();
		    					
		    					Scanner scanner1_2_2 = new Scanner(System.in);
		    					System.out.println("Date de fondation du constructeur:");
		    					String d_f_cons2 = scanner1_2_2.next();
		    					
		    					Scanner scanner1_2_3 = new Scanner(System.in);
		    					System.out.println("Adresse du constructeur:");
		    					String adr_cons2 = scanner1_2_3.next();
		    					
		    					Constructeur constructeur2 = new Constructeur (nom_cons2, d_f_cons2 , adr_cons2);
		    					ConstructeurDAO.update(constructeur2);
		    					break;
		    					
			    			case 3:
			    				Scanner scanner1_3_1 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur à supprimer:");
		    					String nom_cons3 = scanner1_3_1.next();
		    					
		    					ConstructeurDAO.delete(nom_cons3);
		    					break;
		    					
		    				
			    			case 4:
			    				Scanner scanner1_4_1 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur a afficher:");
		    					String nom_cons4 = scanner1_4_1.next();
		    					
		    					Scanner scanner1_4_2 = new Scanner(System.in);
		    					System.out.println("Objet à afficher (adr_cons, d_f_cons:");
		    					String obj1 = scanner1_4_2.next();
		    					
		    					
		    					System.out.println(ConstructeurDAO.find(nom_cons4,obj1));
		    					break;
		    					
			    			case 5:
			    				Scanner scanner1_5_1 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur à afficher:");
		    					String nom_cons5 = scanner1_5_1.next();
		    					
		    					System.out.println(ConstructeurDAO.findAll(nom_cons5));
		    					break;
		    					
			    			case 6: back1=true;	
			    			break;
			    			
			    			default:{
				       			System.out.println("Entrez un cas valable");
	    				}
	    				}
	    				
	    			}while(!back1);
	    			break;
	    		
	    		
	    		case 2:
	    			do {
	    				System.out.println("Choisissez une action à effectuer avec la table de donnée Constructeur:");
	    				System.out.println("1-Ajouter un élément à la table");
	    				System.out.println("2-Modifier un élément de la table");
	    				System.out.println("3-Suprimer un élément de la table");
	    				System.out.println("4-Trouver un élément de la table");
	    				System.out.println("5-Trouver tout les éléments de la table");
	    				Scanner scanner2 = new Scanner(System.in);
	    				int choice2 = scanner2.nextInt();
	    				switch (choice2) {
	    				case 1:
	    					Scanner scanner2_1_1 = new Scanner(System.in);
	    					System.out.println("Nom du pays:");
	    					String nom_pays1 = scanner2_1_1.next();
	    					
	    					Scanner scanner2_1_2 = new Scanner(System.in);
	    					System.out.println("Nombre d'habitant du pays:");
	    					int hbt_pays1 = scanner2_1_2.nextInt();
	    					
	    					Scanner scanner2_1_3 = new Scanner(System.in);
	    					System.out.println("Capitale du pays:");
	    					String cpt_pays1 = scanner2_1_3.next();
	    					
	    					Pays pays1 = new Pays (nom_pays1, hbt_pays1 , cpt_pays1);
	    					PaysDAO.create(pays1);
	    					break;
    				
    				
		    			case 2:
	    					Scanner scanner2_2_1 = new Scanner(System.in);
	    					System.out.println("Nom du pays:");
	    					String nom_pays2 = scanner2_2_1.next();
	    					
	    					Scanner scanner2_2_2 = new Scanner(System.in);
	    					System.out.println("Nombre d'habitant du pays:");
	    					int hbt_pays2 = scanner2_2_2.nextInt();
	    					
	    					Scanner scanner2_2_3 = new Scanner(System.in);
	    					System.out.println("Capitale du Pays:");
	    					String cpt_pays2 = scanner2_2_3.next();
	    					
	    					Pays pays2 = new Pays (nom_pays2, hbt_pays2, cpt_pays2);
	    					PaysDAO.update(pays2);
	    					break;
	    					
		    			case 3:
		    				Scanner scanner2_3_1 = new Scanner(System.in);
	    					System.out.println("Nom du pays à supprimer:");
	    					String nom_pays3 = scanner2_3_1.next();
	    					
	    					PaysDAO.delete(nom_pays3);
	    					break;
	    					
	    				
		    			case 4:
		    				Scanner scanner2_4_1 = new Scanner(System.in);
	    					System.out.println("Nom du pays a afficher:");
	    					String nom_pays4 = scanner2_4_1.next();
	    					
	    					Scanner scanner2_4_2 = new Scanner(System.in);
	    					System.out.println("Objet à afficher (hbt_pays, cpt_pays):");
	    					String obj2 = scanner2_4_2.next();
	    					
	    					
	    					System.out.println(PaysDAO.find(nom_pays4,obj2));
	    					break;
	    					
		    			case 5:
		    				Scanner scanner2_5_1 = new Scanner(System.in);
	    					System.out.println("Nom du pays à afficher:");
	    					String nom_pays5 = scanner2_5_1.next();
	    					
	    					System.out.println(PaysDAO.findAll(nom_pays5));
	    					break;
	    					
		    			case 6: back2=true;	
		    			break;
		    			
		    			default:{
			       			System.out.println("Entrez un cas valable");
    				}
    				}
	    			
	    			}while(!back2);
	    			
	    			break;
	    			
	    			
	       		case 3:
	       			do {
	       				System.out.println("Choisissez une action à effectuer avec la table de donnée Constructeur:");
	    				System.out.println("1-Ajouter un élément à la table");
	    				System.out.println("2-Modifier un élément de la table");
	    				System.out.println("3-Suprimer un élément de la table");
	    				System.out.println("4-Trouver un élément de la table");
	    				System.out.println("5-Trouver tout les éléments de la table");
	       				Scanner scanner3 = new Scanner(System.in);
    				int choice3 = scanner3.nextInt();
	       				switch (choice3) {
	       				
		       				case 1:
		    					Scanner scanner3_1_1 = new Scanner(System.in);
		    					System.out.println("Numéro de la compagnie:");
		    					String num_comp1 = scanner3_1_1.next();
		    					
		    					Scanner scanner3_1_2 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie:");
		    					String nom_comp1 = scanner3_1_2.next();
		    					
		    					Scanner scanner3_1_3 = new Scanner(System.in);
		    					System.out.println("Date de création de la compagnie:");
		    					String creat_comp1 = scanner3_1_3.next();
	
		    					Scanner scanner3_1_4 = new Scanner(System.in);
		    					System.out.println("Pays d'origine de la compagnie:");
		    					String nom_pays4 = scanner3_1_4.next();
		    					
		    					Compagnie compagnie1 = new Compagnie (num_comp1, nom_comp1, creat_comp1, nom_pays4);
		    					CompagnieDAO.create(compagnie1);
		    					break;
	    				
	    				
			    			case 2:
			    				Scanner scanner3_2_1 = new Scanner(System.in);
		    					System.out.println("Numéro de la compagnie:");
		    					String num_comp2 = scanner3_2_1.next();
		    					
		    					Scanner scanner3_2_2 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie:");
		    					String nom_comp2 = scanner3_2_2.next();
		    					
		    					Scanner scanner3_2_3 = new Scanner(System.in);
		    					System.out.println("Date de création de la compagnie:");
		    					String creat_comp2 = scanner3_2_3.next();
	
		    					Scanner scanner3_2_4 = new Scanner(System.in);
		    					System.out.println("Pays d'origine de la compagnie:");
		    					String nom_pays5 = scanner3_2_4.next();
		    					
		    					Compagnie compagnie2 = new Compagnie (num_comp2, nom_comp2, creat_comp2, nom_pays5);
		    					CompagnieDAO.update(compagnie2);
		    					break;
		    					
			    			case 3:
			    				Scanner scanner3_3_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie à supprimer:");
		    					String num_comp3 = scanner3_3_1.next();
		    					
		    					CompagnieDAO.delete(num_comp3);
		    					break;
		    					
		    				
			    			case 4:
			    				Scanner scanner3_4_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie a afficher:");
		    					String num_comp4 = scanner3_4_1.next();
		    					
		    					Scanner scanner3_4_2 = new Scanner(System.in);
		    					System.out.println("Objet à afficher (nom_comp, creat_comp,nom_pays):");
		    					String obj3 = scanner3_4_2.next();
		    					
		    					
		    					System.out.println(CompagnieDAO.find(num_comp4,obj3));
		    					break;
		    					
			    			case 5:
			    				Scanner scanner3_5_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie à afficher:");
		    					String num_comp5 = scanner3_5_1.next();
		    					
		    					System.out.println(CompagnieDAO.findAll(num_comp5));
		    					break;
		    					
			    			case 6: back3=true;	
			    			break;
			    			
			    			default:{
				       			System.out.println("Entrez un cas valable");
    				}
	    			} 
	       			}while(!back3);
	       			
	       			break;
	       			
	       			
	       		case 4:
	       			
	       			do {
	       				System.out.println("Choisissez une action à effectuer avec la table de donnée Constructeur:");
	    				System.out.println("1-Ajouter un élément à la table");
	    				System.out.println("2-Modifier un élément de la table");
	    				System.out.println("3-Suprimer un élément de la table");
	    				System.out.println("4-Trouver un élément de la table");
	    				System.out.println("5-Trouver tout les éléments de la table");
	       				Scanner scanner4 = new Scanner(System.in);
    				int choice4 = scanner4.nextInt();
	       				switch (choice4) {
	       				
		       				case 1:
		    					Scanner scanner4_1_1 = new Scanner(System.in);
		    					System.out.println("Identifiant de l'avion:");
		    					String id_avion1= scanner4_1_1.next();
		    					
		    					Scanner scanner4_1_2 = new Scanner(System.in);
		    					System.out.println("Nombre d'heur de vol de l'avion:");
		    					int hr_vol1 = scanner4_1_2.nextInt();
		    					
		    					Scanner scanner4_1_3 = new Scanner(System.in);
		    					System.out.println("Date de premier vol de l'avion:");
		    					String d_p_vol1= scanner4_1_3.next();
	
		    					Scanner scanner4_1_4 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur de l'avion:");
		    					String nom_cons4 = scanner4_1_4.next();
		    					
		    					Avion avion1= new Avion (id_avion1, hr_vol1, d_p_vol1, nom_cons4);
		    					AvionDAO.create(avion1);
		    					break;
	    				
	    				
			    			case 2:
			    				Scanner scanner4_2_1 = new Scanner(System.in);
		    					System.out.println("Identifiant de l'avion:");
		    					String id_avion2= scanner4_2_1.next();
		    					
		    					Scanner scanner4_2_2 = new Scanner(System.in);
		    					System.out.println("Nombre d'heur de vol de l'avion:");
		    					int hr_vol2 = scanner4_2_2.nextInt();
		    					
		    					Scanner scanner4_2_3 = new Scanner(System.in);
		    					System.out.println("Date de premier vol de l'avion:");
		    					String d_p_vol2= scanner4_2_3.next();
	
		    					Scanner scanner4_2_4 = new Scanner(System.in);
		    					System.out.println("Nom du constructeur de l'avion:");
		    					String nom_cons5 = scanner4_2_4.next();
		    					
		    					Avion avion2= new Avion (id_avion2, hr_vol2, d_p_vol2, nom_cons5);
		    					AvionDAO.update(avion2);
		    					break;
		    					
			    			case 3:
			    				Scanner scanner4_3_1 = new Scanner(System.in);
		    					System.out.println("Nom de l'avion à supprimer:");
		    					String id_avion3= scanner4_3_1.next();
		    					
		    					AvionDAO.delete(id_avion3);
		    					break;
		    					
		    				
			    			case 4:
			    				Scanner scanner4_4_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie a afficher:");
		    					String id_avion4 = scanner4_4_1.next();
		    					
		    					Scanner scanner4_4_2 = new Scanner(System.in);
		    					System.out.println("Objet à afficher (hr_vol, d_p_vol,nom_cons):");
		    					String obj4 = scanner4_4_2.next();
		    					
		    					
		    					System.out.println(AvionDAO.find(id_avion4,obj4));
		    					break;
		    					
			    			case 5:
			    				Scanner scanner4_5_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie à afficher:");
		    					String id_avion5 = scanner4_5_1.next();
		    					
		    					System.out.println(AvionDAO.findAll(id_avion5));
		    					break;
		    					
			    			case 6: back4=true;	
			    			break;
			    			
			    			default:{
				       			System.out.println("Entrez un cas valable");
    				}
	    			} 
	       			}while(!back4);
	       			break;

	       			
	       			
	       		case 5:
	       			do {
	       				System.out.println("Choisissez une action à effectuer avec la table de donnée Constructeur:");
	    				System.out.println("1-Ajouter un élément à la table");
	    				System.out.println("2-Modifier un élément de la table");
	    				System.out.println("3-Suprimer un élément de la table");
	    				System.out.println("4-Trouver un élément de la table");
	    				System.out.println("5-Trouver tout les éléments de la table");
	       				Scanner scanner5 = new Scanner(System.in);
    				int choice5 = scanner5.nextInt();
	       				switch (choice5) {
	       				
		       				case 1:
		    					Scanner scanner5_1_1 = new Scanner(System.in);
		    					System.out.println("Numéro de passeport:");
		    					String num_pers1= scanner5_1_1.next();
		    					
		    					Scanner scanner5_1_2 = new Scanner(System.in);
		    					System.out.println("Nom:");
		    					String nom_pers1 = scanner5_1_2.next();
		    					
		    					Scanner scanner5_1_3 = new Scanner(System.in);
		    					System.out.println("Prénom:");
		    					String pre_pers1= scanner5_1_3.next();
	
		    					Scanner scanner5_1_4 = new Scanner(System.in);
		    					System.out.println("Qualité:");
		    					String qual_pers1 = scanner5_1_4.next();
		    					
		    					Scanner scanner5_1_5 = new Scanner(System.in);
		    					System.out.println("Numéro de compagnie affilié:");
		    					String num_comp4 = scanner5_1_5.next();
		    					
		    					Personnel personnel1= new Personnel(num_pers1, nom_pers1, pre_pers1, qual_pers1, num_comp4);
		    					PersonnelDAO.create(personnel1);
		    					break;
	    				
	    				
			    			case 2:
			    				Scanner scanner5_2_1 = new Scanner(System.in);
		    					System.out.println("Numéro de passeport:");
		    					String num_pers2= scanner5_2_1.next();
		    					
		    					Scanner scanner5_2_2 = new Scanner(System.in);
		    					System.out.println("Nom:");
		    					String nom_pers2 = scanner5_2_2.next();
		    					
		    					Scanner scanner5_2_3 = new Scanner(System.in);
		    					System.out.println("Prénom:");
		    					String pre_pers2= scanner5_2_3.next();
	
		    					Scanner scanner5_2_4 = new Scanner(System.in);
		    					System.out.println("Qualité:");
		    					String qual_pers2 = scanner5_2_4.next();
		    					
		    					Scanner scanner5_2_5 = new Scanner(System.in);
		    					System.out.println("Numéro de compagnie affilié:");
		    					String num_comp5 = scanner5_2_5.next();
		    					
		    					Personnel personnel5= new Personnel(num_pers2, nom_pers2, pre_pers2, qual_pers2, num_comp5);
		    					PersonnelDAO.update(personnel5);
		    					break;
		    					
			    			case 3:
			    				Scanner scanner5_3_1 = new Scanner(System.in);
		    					System.out.println("Numéro du personnel à supprimer:");
		    					String num_pers3= scanner5_3_1.next();
		    					
		    					PersonnelDAO.delete(num_pers3);
		    					break;
		    					
		    				
			    			case 4:
			    				Scanner scanner5_4_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie a afficher:");
		    					String num_pers4 = scanner5_4_1.next();
		    					
		    					Scanner scanner5_4_2 = new Scanner(System.in);
		    					System.out.println("Objet à afficher (nom_pers, pré_pers ,qual_pers, num_comp):");
		    					String obj5 = scanner5_4_2.next();
		    					
		    					
		    					System.out.println(PersonnelDAO.find(num_pers4,obj5));
		    					break;
		    					
			    			case 5:
			    				Scanner scanner5_5_1 = new Scanner(System.in);
		    					System.out.println("Nom de la compagnie à afficher:");
		    					String num_pers5 = scanner5_5_1.next();
		    					
		    					System.out.println(PersonnelDAO.findAll(num_pers5));
		    					break;
		    					
			    			case 6: back5=true;	
			    			break;
			    			
			    			default:{
				       			System.out.println("Entrez un cas valable");
    				}
	    			} 
	       			}while(!back5);

	       			break;
	       			
	       			
	       		case 6:
	       			quit=true;
	       			break;
	       			
	       			
	       		default:{
	       			System.out.println("Entrez un cas valable");
				}
			}
		}while(!quit);
	}
}
	