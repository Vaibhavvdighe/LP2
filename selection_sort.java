import java.util.*;
public class selection_sort {
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int total,i,j;
        System.out.print("Enter the size:");
        total=sc.nextInt();
        int[] arr=new int[total];
        // accept the elements
        for(i=0;i<total;i++)
        {
            arr[i]=sc.nextInt();
        }
        // print the elements
        System.out.print("Elements in the array:");
        for(i=0;i<total;i++)
        {
            System.out.print(arr[i]+" ");
        }

        //  logic
        int smallest,temp;
        for(i=0;i<total-1;i++)
        {
            smallest=i;
            for(j=i+1;j<total;j++)
            {
                if(arr[j]<arr[smallest])
                {
                    smallest=j;
                }
            }

            temp=arr[i];
            arr[i]=arr[smallest];
            arr[smallest]=temp; // replace
        }
        System.out.println();
        System.out.print("Sorted array:");
        for(i=0;i<total;i++)
        {
            System.out.print(arr[i]+ " ");
        }
    }
}