#include <stdio.h>

/*Step 1 - divide the list into n sublists of size 1 
Base case  - a sublist of size 1 is sorted
Maintain - dividing a list recursively into sublists of size n/2 at every call,
            eventually resulting in a sublist of 1 element
Termination - If left > right, then terminate, as then we have reached size 1.*/

void mergesort(int arr[], int l, int r) {
    if (l < r) {
        int m = l + (r - l) / 2;

        mergesort(arr, l, m);
        mergesort(arr, m + 1, r);
        /* this call in memory will first execute "mergesort(Arr,l,m)" recursively, 
        and first 2 halves will be formed, then it will divide the left half first,
        so the first sublist of size 1 will be of the first element at the left most.*/
        merge(arr, l, m, r); //we will define this now
    }
}

/*We */


void merge(int arr[], int left , int mid , int right){

}
