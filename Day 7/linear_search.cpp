#include<iostream>
using namespace std;

int linear_search(int arr[],int n,int x)
{
   int i;
	 for(i =0;i<n;i++)
	 {
	 	if (arr[i]==x)
		{
			return i;
		}
	 }
	return -1;
}
int main()
{	
	int n,x;
	cout<<"Enter Number of elements in array: ";
	cin>>n;
	int arr[n];
	for(int i=0;i<n;i++)
	{
		cout<<"Enter element "<<i+1<<": ";
		cin>>arr[i];
	}
	cout<<"Enter element to search: ";
	cin>>x;
	cout<<linear_search(arr,n,x);
	return 0;
}
