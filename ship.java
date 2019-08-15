/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{


     Scanner tin=new Scanner(System.in);
        int t=tin.nextInt();
        for(int i=0;i<t+1;i++){
            String a=tin.nextLine();
                switch(a.toLowerCase()){
                    case "f":
                        System.out.println("Frigate");
                            break;
                    case "d":
                        System.out.println("Destroyer");
                            break;
                    case "c":
                        System.out.println("Cruiser");
                            break;
                    case "b":
                        System.out.println("BattleShip");
                            break;
                    
                        
                }
            }
	}
}


    


