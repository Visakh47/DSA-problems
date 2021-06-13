import java.util.Scanner;
class Solution {
    public int[] decode(int[] encoded, int first) {

    Scanner Sc=new Scanner(System.in); 
        int n,i;
        n=encoded.length;
        int arr[]=new int[n+1];
        arr[0]=first;
        for(i=0;i<n;i++)
            arr[i+1]=encoded[i]^arr[i]; 
         return arr;
    }
   
}