#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

#define NAMELENGTH 64

char namebuf[NAMELENGTH];
char namebuf2[NAMELENGTH];
int infile = -1;

int main(int argc, char **argv) {

        off_t offset1,offset2;
        ssize_t nread;
        int i = 0;
        if (infile == -1 && (infile = open("residents", O_RDWR|O_CREAT,0644)) == -1) {

                exit(1);
        }
        offset1 = (atoi(argv[1])-1) * NAMELENGTH;
        if (lseek(infile, offset1, SEEK_SET) == -1) {
            perror("Seek error");
            exit(1);
        }
        if ((nread = read(infile, namebuf, sizeof(namebuf))) <= 0) {
            perror("Read error");
            exit(1);
        }
        offset2 = (atoi(argv[2])-1) * NAMELENGTH;
        if (lseek(infile, offset2, SEEK_SET) == -1) {
            perror("Seek error");
            exit(1);
        }
        if ((nread = read(infile, namebuf2, sizeof(namebuf2))) <= 0) {
            perror("Read error");
            exit(1);
        }
        printf("before\n");
        printf("room %d = %s\n",atoi(argv[1]),namebuf);
        printf("room %d = %s\n",atoi(argv[2]),namebuf2);
        lseek(infile,offset1,SEEK_SET);
        write(infile,namebuf2,sizeof(namebuf2));
        lseek(infile,offset2,SEEK_SET);
        write(infile,namebuf,sizeof(namebuf));
        lseek(infile,0,SEEK_SET);
        printf("after\n");
        for(i=0;i<12;i++)
        {
                read(infile,namebuf,sizeof(namebuf));
                printf("room %d = %s\n",i+1,namebuf);

        }


        close(infile);
}