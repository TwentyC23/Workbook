package MainApp;

import java.util.Date;
import java.util.Iterator;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Scanner;

import bean.Book;
import bean.Document;
import bean.Lending;
import bean.PeriodicReview;
import bean.Reader;
import bean.Student;
import bean.Teacher;

public class MainApp {
	
	public static int menu() {
		
		System.out.println("Choose an action to perform");
		System.out.println("---------------------------\n");
		System.out.println("1 - add reader");
		System.out.println("2 - delete reader");
		System.out.println("3 - add document");
		System.out.println("4 - delete document");
		System.out.println("5 - show all readers");
		System.out.println("6 - show all documents");
		System.out.println("7 - lend a document");
		System.out.println("8 - return a document");
		System.out.println("9 - warn readers");
		System.out.println("10 - lost document");
		System.out.println("11 - modify reader privilege");
		System.out.println("12 - add time");
		System.out.println("13 - export data");
		System.out.println("0 - Quit\n");
		System.out.println("Enter choice: ");

		Scanner scanner = new Scanner(System.in);
		int selection = scanner.nextInt();
		return selection;
		
	}
	
	
   public static void main(String args[]) throws ParseException {
	   
	   boolean quit = false;
	   ArrayList<Reader> reader = new ArrayList<Reader>();
	   ArrayList<Document> document = new ArrayList<Document>();
	   ArrayList<Lending> lending = new ArrayList<Lending>();
	   
	   do {
		   
		   int menu = menu();
		   
		   switch (menu) {
		   
		   // quit menu
		   case 0:
			   quit = true;
			   break;
		   
		   // add reader
		   case 1:
			   Scanner sc_menu1 = new Scanner(System.in);
			   
			   System.out.println("Profession");
			   System.out.println("----------\n");
			   System.out.println("1 - teacher");
			   System.out.println("2 - student");
			   int value1 = sc_menu1.nextInt();
			   sc_menu1.nextLine();
			   
			   System.out.println("name: ");
			   String name1 = sc_menu1.nextLine();
			   
			   System.out.println("email: ");
			   String email1 = sc_menu1.nextLine();
			   
			   System.out.println("college: ");
			   String college1 = sc_menu1.nextLine();
			   
			   if (value1 == 1) {
				   System.out.println("phone number: ");
				   String phone1 = sc_menu1.nextLine();
				   reader.add(new Teacher(name1, email1, college1, phone1));
			   } else {
				   
				   System.out.println("address: ");
				   String address1 = sc_menu1.nextLine();
				   Student test = new Student(name1, email1, college1, address1);
				   reader.add(test);
			   }   
			   System.out.println("Reader added successfully\n");
			   break;
			   
		   // delete reader
		   case 2:
			   Scanner sc_menu2 = new Scanner(System.in);
			   
			   System.out.println("name: ");
			   String name2 = sc_menu2.nextLine();
			   
			   Iterator<Reader> iter2 = reader.iterator();
			   while (iter2.hasNext()) {
				   Reader r2 = iter2.next();
				   if (r2.getName().equals(name2)) {
					   iter2.remove();
					   System.out.println("Reader deleted successfully\n");
				   } else if (reader.indexOf(r2) == reader.size() - 1) {
					   System.out.println("Reader not found\n");
				   }
			   }
			   if (reader.isEmpty()) {
				   System.out.println("Reader data empty\n");
			   }
			   
			   break;
			   
		   // add document
		   case 3:
			   Scanner sc_menu3 = new Scanner(System.in);
			   
			   System.out.println("Document type");
			   System.out.println("-------------\n");
			   System.out.println("1 - periodic review");
			   System.out.println("2 - book");
			   int value3 = sc_menu3.nextInt();
			   sc_menu3.nextLine();
			   
			   System.out.println("id: ");
			   String id3 = sc_menu3.nextLine();
			   
			   System.out.println("title: ");
			   String title3 =sc_menu3.nextLine();
			   
			   System.out.println("price: ");
			   double price3 = sc_menu3.nextDouble();
			   sc_menu3.nextLine();
			   
			   if (value3 == 1) {
				   System.out.println("number: ");
				   int number3 = sc_menu3.nextInt();
				   sc_menu3.nextLine();
				   
				   System.out.println("year: ");
				   int year3 = sc_menu3.nextInt();
				   sc_menu3.nextLine();
				   
				   document.add(new PeriodicReview(id3, title3, price3, number3, year3));
			   } else {
				   System.out.println("author: ");
				   String author3 = sc_menu3.nextLine();
				   
				   System.out.println("repayment (%): ");
				   double repayment3 = sc_menu3.nextDouble();
				   sc_menu3.nextLine();
				   
				   System.out.println("copy: ");
				   int copy3 = sc_menu3.nextInt();
				   sc_menu3.nextLine();
				   
				   document.add(new Book(id3, title3, price3, author3, repayment3, copy3));
			   }
			   System.out.println("Document added successfully\n");
			   break;
			   
		   // delete document
		   case 4:
			   Scanner sc_menu4 = new Scanner(System.in);
			   
			   System.out.println("id: ");
			   String id4 = sc_menu4.nextLine();
			   
			   Iterator<Document> iter4 = document.iterator();
			   while (iter4.hasNext()) {
				   Document d4 = iter4.next();
				   if (d4.getId().equals(id4)) {
					   iter4.remove();
					   System.out.println("Document deleted successfully\n");
				   } else if (document.indexOf(d4) == document.size() - 1) {
					   System.out.println("Document not found\n");
				   }
			   }
			   if (document.isEmpty()) {
				   System.out.println("Document data empty\n");
			   }
			   break;
			   
		   // show all readers
		   case 5:
			   for (Reader i : reader) {
				   System.out.println(i);
			   }
			   if (reader.isEmpty()) {
				   System.out.println("Reader data empty\n");
			   }
			   break;
			   
		   // show all documents
		   case 6:
			   for (Document i : document) {
				   System.out.println(i);
			   }
			   if (document.isEmpty()) {
				   System.out.println("Document data empty\n");
			   }
			   break;
			   
		   // lend a document
		   case 7:
			   Scanner sc_menu7 = new Scanner(System.in);
			   
			   System.out.println("name: ");
			   String name7 = sc_menu7.nextLine();
			   
			   System.out.println("id: ");
			   String id7 = sc_menu7.nextLine();
			   
			   System.out.println("date (dd/MM/yyyy): ");
			   SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
			   Date date7 = sdf.parse(sc_menu7.nextLine());
			   
			   for (Reader i : reader) {
				   if (i.getName().equals(name7)) {
				
					   for (Document j : document) {
						   if (j.getId().equals(id7)) {
							   
							   if (new Lending(i, j, date7).check_lending()) {
								   lending.add(new Lending(i, j, date7).lend());
								   System.out.println("Lending added successfully\n");
							   } else {
								   System.out.println("Not enough copies of the document or Reader is not allowed to borrow more\n");
							   }
							   
						   } else if (document.indexOf(j) == document.size() - 1) {
							   System.out.println("Document not found\n");
						   }
					   }
				   } else if (reader.indexOf(i) == reader.size() - 1) {
					   System.out.println("Reader not found\n");
				   }
			   }
			   if (reader.isEmpty() || document.isEmpty()) {
				   System.out.println("Reader or document data empty\n");
			   }
			   break;
			   
		   // return a document
		   case 8:
			   Scanner sc_menu8 = new Scanner(System.in);
			   
			   System.out.println("name: ");
			   String name8 = sc_menu8.nextLine();
			   
			   System.out.println("id: ");
			   String id8 = sc_menu8.nextLine();
			   
			   Iterator<Lending> iter8 = lending.iterator();
			   while (iter8.hasNext()) {
				   Lending l8 = iter8.next();
				   if (l8.getId().getId().equals(id8) && l8.getName().getName().equals(name8)) {
					   l8.return_doc();
					   iter8.remove();
					   System.out.println("Document returned successfully\n");
				   } else if (lending.indexOf(l8) == lending.size() - 1) {
					   System.out.println("Lending not found\n");
				   }
			   }
			   if (lending.isEmpty()) {
				   System.out.println("Lending data empty\n");
			   }
			   break;
			   
		   // warn readers
		   case 9:
			   for (Lending i : lending) {
				   if (i.warning()) {
					   System.out.println(i);
				   } 
			   }
			   if (lending.isEmpty()) {
				   System.out.println("Lending data empty\n");
			   }
			   break;
			   
		   // lost document
		   case 10:
			   Scanner sc_menu10 = new Scanner(System.in);
			   
			   System.out.println("name: ");
			   String name10 = sc_menu10.nextLine();
			   
			   System.out.println("id: ");
			   String id10 = sc_menu10.nextLine();
			   		 
			   Iterator<Lending> iter10 = lending.iterator();
			   while (iter10.hasNext()) {
				   Lending l10 = iter10.next();
				   if (l10.getId().getId().equals(id10) && l10.getName().getName().equals(name10)) {
					   System.out.println("Repayment: " + l10.lost() + "€\n");
					   iter10.remove();
					   
				   } else if (lending.indexOf(l10) == lending.size() - 1) {
					   System.out.println("Lending not found\n");
				   }
			   }
			   if (lending.isEmpty()) {
				   System.out.println("Lending data empty\n");
			   }
			   break;
			   
		   // modify reader privilege
		   case 11:
			   Scanner sc_menu11 = new Scanner(System.in);
			   
			   System.out.println("name: ");
			   String name11 = sc_menu11.nextLine();
			   
			   for (Reader i : reader) {
				   if (i.getName().equals(name11)) {
					   
					   System.out.println("Documents allowed: " + i.getDocs());
					   System.out.println("Period allowed: " + i.getPeriod());
					   
					   System.out.println("documents: ");
					   int docs11 = sc_menu11.nextInt();
					   
					   System.out.println("period: ");
					   int period11 = sc_menu11.nextInt();
					   
					   i.setDocs(docs11);
					   i.setPeriod(period11);
					   
					   System.out.println("Modification added successfully\n");
					   
				   } else if (reader.indexOf(i) == reader.size() - 1) {
					   System.out.println("Reader not found\n");
				   } 
			   }
			   break;
			   
		   // add time  
		   case 12:
			   Scanner sc_menu12 = new Scanner(System.in);
			   
			   System.out.println("name: ");
			   String name12 = sc_menu12.nextLine();
			   
			   System.out.println("id: ");
			   String id12 = sc_menu12.nextLine();							   
			   for (Lending i : lending) {
				   if (i.getId().getId().equals(id12) && i.getName().getName().equals(name12)) {
					   System.out.println("add time (dd): ");
					   int period12 = sc_menu12.nextInt();
					   i.setPeriod(i.getPeriod() + period12);
					   System.out.println("Added time successfully\n");
					   									  
				   } else if (lending.indexOf(i) == lending.size() - 1) {
					   System.out.println("Lending not found\n");
				   }
			   }
			   break;
			   
		   // export data 
		   case 13:
			   try {
				   File file = new File("data.txt");
				   file.createNewFile();
				   FileWriter filewriter = new FileWriter("data.txt");
				   filewriter.write("Readers: \n");
				   for (Reader i : reader) {
					   filewriter.write(i + "\n");
				   }
				   filewriter.write("\nDocuments: \n");
				   for (Document j : document) {
					   filewriter.write(j + "\n");
				   }
				   filewriter.write("\nLendings: \n");
				   for (Lending k : lending) {
					   filewriter.write(k + "\n");
				   }
				   filewriter.close();
				   System.out.println("data exported to data.txt\n");
			   } catch (IOException e) {
				   System.out.println("An error occurred\n");
				   e.printStackTrace();
			   }
			   break;
			   
		   // unsupported keystroke   
		   default:
			   System.out.println("keystroke not supported\n");		   
		   }
		   
	   } while (!quit);   
   }
}