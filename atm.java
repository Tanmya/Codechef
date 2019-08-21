/* package codechef; // don't place package name! */

import java.util.*;
import java.lang.*;
import java.io.*;

/* Name of the class has to be "Main" only if the class is public. */
class Codechef
{
	public static void main (String[] args) throws java.lang.Exception{
    Scanner sc=new Scanner(System.in);
    int x=sc.nextInt();
    double y=sc.nextDouble();
    if(x%5==0 && (x+0.5)<y){
        System.out.println((y-x-0.5));
    }else {
        System.out.println(y);
    }   
}
}
    
    
    
    









