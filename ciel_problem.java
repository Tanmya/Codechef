/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception
	{
    Scanner sc=new Scanner(System.in); 
    int A=sc.nextInt();
    int B=sc.nextInt();
    int C=A-B;
    if(C%10==9){
        System.out.println(C-1);
    }else{
        System.out.println(C+1);
    }   
    }
}

