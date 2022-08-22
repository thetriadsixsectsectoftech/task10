import java.util.Objects;
import java.util.Scanner;

public class PoisedProjectmain {

    public static void main(String[] args) {

        PoisedProjectClass project = projectdetails();
        //The code starts by creating an instance of the class, which is called project.
        System.out.println(project);
        // The main method then prints out the contents of the object that was created in step 1.

        Scanner menu_input = new Scanner(System.in);





        while(true){
            System.out.println("""
                would you like to change the due date of a project?,type pdd
                would you like to change the amount paid to date? type apd
                would you like to update a contractors detals? type ud
                type exit to exit the programm
                """);
            //The code is designed to ask the user if they would like to change the due date of a project.
            // The code is designed to ask the user if they would like to change the amount paid to date?
            //The code is designed to ask the user if they would like to update a contractors detals?

            String projectMenu = menu_input.nextLine();

            if(Objects.equals(projectMenu, "exit")){
                break;

            }//break statement

            else if (Objects.equals(projectMenu, "pdd")) {
                Scanner pdd = new Scanner(System.in);
                System.out.println("please enter the new date");
                String user_edit = pdd.nextLine();
                project.setDate(user_edit);
                System.out.println("the new date is.");
                System.out.println(project);

            }//else if to set new project due date

            else if (Objects.equals(projectMenu, "apd")) {
                Scanner apd = new Scanner(System.in);
                System.out.println("please enter the new amount paid to date");
                String newmount = apd.nextLine();
                project.setAmountpaidtodate(newmount);
                System.out.println("the new amount paid to date is");
                System.out.println(project);
            }// else if to set new amount paid to date

            else if (Objects.equals(projectMenu, "ud")) {

                Scanner ud = new Scanner(System.in);

                while (true){

                    System.out.println("""
                    please enter which detail you would like to update,
                    n = name 
                    t = telephone
                    e = email 
                    a = address
                    d = done """);

                    String userEdit = ud.nextLine();

                    if (Objects.equals(userEdit, "d")){
                        break;
                    }// break statement

                    else if (Objects.equals(userEdit, "n")) {
                        System.out.println("please enter the new name of the contractor");


                        String newName = ud.nextLine();

                        project.getContractor().setName(newName);



                        System.out.println(project);


                    }// set method for the contractors new name

                    else if (Objects.equals(userEdit, "t")) {
                        System.out.println("please enter the new telephone of the contractor");

                        new Scanner(System.in);

                        long newTele = Long.parseLong(ud.nextLine());

                        project.getContractor().setTelenum(newTele);



                        System.out.println(project);


                    }// set method for the contractors new telephone

                    else if (Objects.equals(userEdit, "e")) {
                        System.out.println("please enter the new email of the contractor");

                        new Scanner(System.in);

                        String newEmail = ud.nextLine();

                        project.getContractor().setEmail(newEmail);



                        System.out.println(project);


                    }// set method for the contractors new email

                    else if (Objects.equals(userEdit, "a")) {
                        System.out.println("please enter the new addres of the contractor");

                        new Scanner(System.in);

                        String newAddy = ud.nextLine();

                        project.getContractor().setAddress(newAddy);



                        System.out.println(project);


                    }// set method for the contractors new address





                }// while loop menu if the user chooses to edit contractor details

            }

        }
    }

    public static PoisedProjectClass projectdetails() {
        Scanner input = new Scanner(System.in);

        System.out.println("please enter the project number\n");

        int projectnum = Integer.parseInt(input.nextLine());

        input = new Scanner(System.in);

        System.out.println("please enter the project name\n");

        String projectname = input.nextLine();

        input = new Scanner(System.in);

        System.out.println("please enter what type of building it is");
        String buildingtype = input.nextLine();

        input = new Scanner(System.in);
        System.out.println("please enter the physical address");
        String physicaladd = input.nextLine();

        input = new Scanner(System.in);
        System.out.println("please enter the ERF number");
        int erfnumb = input.nextInt();

        input = new Scanner(System.in);
        System.out.println("please enter the total fee being charged for the project");
        int totalfee = Integer.parseInt(input.nextLine());

        input = new Scanner(System.in);
        System.out.println("please enter the amount paid to date");
        int amountpaid = Integer.parseInt(input.nextLine());

        input = new Scanner(System.in);
        System.out.println(" please enter the project deadline. in this format YYYY,MM,DD seperated by a comma.");
        String projectdeadline = input.nextLine();

        PoisedPersonClass contractor = peopledetails();
        PoisedPersonClass architect = peopledetails();
        PoisedPersonClass customer = peopledetails();


        return new PoisedProjectClass(projectnum, projectname, buildingtype, erfnumb, totalfee, amountpaid, projectdeadline, physicaladd ,architect,contractor,customer);


    }// project method used to create a project object

    public static PoisedPersonClass peopledetails() {
        Scanner input1 = new Scanner(System.in);
        System.out.println("please enter your name");
        String name = input1.nextLine();

        input1 = new Scanner(System.in);
        System.out.println("please enter your telephone");
        long tele = input1.nextLong();

        input1 = new Scanner(System.in);
        System.out.println("please enter your email");
        String mail = input1.nextLine();

        input1 = new Scanner(System.in);
        System.out.println("please enter your address");
        String addy = input1.nextLine();

        return new PoisedPersonClass(name, tele, mail, addy);


    }// perso method used to create a new person object


}
