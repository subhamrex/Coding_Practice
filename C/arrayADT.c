#include<stdio.h>
#include<stdlib.h>
struct arrayADT
{
    int total_size;
    int use_size;
    int *ptr;
};

void create_arr(struct arrayADT *a,int tsize,int usize)
{
    (*a).total_size = tsize;// a->totalsize = tsize
    (*a).use_size = usize;
    (*a).ptr = (int *) malloc(tsize*sizeof(int));
}
void set_array(struct arrayADT *a)
{  
    for (int i = 0; i < a->use_size; i++)
    {    
        scanf("%d",&((a->ptr)[i]));
    }
    
}
void show(struct arrayADT *a)
{
    for (int i = 0; i < a->use_size; i++)
    {
        printf("Element %d -> %d\n",i,(a->ptr)[i] );
    }
    
}

int main()
{
    struct arrayADT arr1,arr2;
    create_arr(&arr1,10,3);
    printf("Add Elements in c :\n");
    set_array(&arr1);
    show(&arr1);
    create_arr(&arr2,10,3);
    printf("Add Elements in c :\n");
    set_array(&arr2);
    show(&arr2);

    return 0;
}