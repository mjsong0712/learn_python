# include <stdio.h>
# define MAX_SIZE 1000001
# define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp) )

int partition(int list[], int left, int right){
  int pivot, temp;
  int low, high;

  low = left;
  high = right + 1;
  pivot = list[left]; 

  do{
    do {
      low++;
    } while (low<=right && list[low]<pivot);

    do {
      high--;
    } while (high>=left && list[high]>pivot);

    if(low<high){
      SWAP(list[low], list[high], temp);
    }
  } while (low<high);

  SWAP(list[left], list[high], temp);

  return high;
}

void quick_sort(int list[], int left, int right){

  if(left<right){

    int q = partition(list, left, right);

    quick_sort(list, left, q-1);
    quick_sort(list, q+1, right);
  }

}

void main(){
  int i;
  int n = MAX_SIZE;
  int list[1000001] = {0,};
  int l = 0;

  scanf("%d",&l);

  for(i=0; i<l; i++){
    scanf("%d", &list[i]);
  }

  quick_sort(list, 0, l-1);

  // 정렬 결과 출력
  for(i=0; i<l; i++){
    printf("%d\n", list[i]);
  }
}
