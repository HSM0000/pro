#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(int argc, char **argv){
        FILE *fp;
        char *str="abcdefghijklmnopqrstuvwxyz";
        int i,arr[27];
        char st[27];
        int n=0;

        if ((fp=fopen("testdata","w+"))==NULL)
        {
                perror("error");
                exit(1);
        }

        fwrite(str,sizeof(char),26,fp);
        i=0;
        rewind(fp);
        while(!feof(fp)){
                arr[n]=i*atol(argv[1]);
                fseek(fp,arr[n],SEEK_SET);
                st[n]=fgetc(fp);
                n++;
                i++;
                if(i>26)break;
        }
        if(atoi(argv[1])<=0){
                fclose(fp);
                printf("ERROR\n");
                exit(1);
        }
        else{
                printf("currnet offset : ");
                for(i=0;i<n-1;i++){
                        printf("%d ",arr[i]);
                }
                printf("\ncurrnet data : ");
                for(i=0;i<n-1;i++){printf("%c ",st[i]);
                }
                printf("\n");
                fclose(fp);
        }
}

