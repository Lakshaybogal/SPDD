
#include <stdio.h>
#include <conio.h>
#include <dos.h>

void main()
{
    int choice, x, y, lines, x1, y1;
    int cont = 1;
    union REGS regs;
    while (cont != 0)
    {
        printf("Enter 1 to set cursor size\nEnter 2 to scroll the window down\nEnter 3 to position the cursor\nEnter 4 to read the cursor position\nEnter your choice :- ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Running test case %d\n", choice);
            printf("Enter upper position of cursor (0-4):- ");
            scanf("%d", &x);
            while (x > 4)
            {
                printf("Enter upper position of cursor (0-4):-");
                scanf("%d", &x);
            }
            printf("Enter lower position of cursor :- ");
            scanf("%d", &y);
            regs.h.ah = 1;
            regs.h.ch = x;
            regs.h.cl = y;
            int86(0x10, &regs, &regs);
            getch();
            break;

        case 2:
            printf("Running test case %d\n", choice);
            printf("Enter no. of lines to scroll :- ");
            scanf("%d", &lines);
            printf("Enter upper row :- ");
            scanf("%d", &x);
            printf("Enter upper column :- ");
            scanf("%d", &y);
            printf("Enter lower row :- ");
            scanf("%d", &x1);
            printf("Enter lower column :- ");
            scanf("%d", &y1);
            regs.h.ah = 7;
            regs.h.al = lines;
            regs.h.bh = 7;
            regs.h.cl = x;
            regs.h.ch = y;
            regs.h.dl = x1;
            regs.h.dh = y1;
            int86(0x10, &regs, &regs);
            getch();
            break;

        case 3:
            printf("Running test case %d\n", choice);
            printf("Enter row :- ");
            scanf("%d", &x);
            printf("Enter column :- ");
            scanf("%d", &y);
            regs.h.ah = 2;
            regs.h.dh = x;
            regs.h.dl = y;
            regs.h.bh = 0;
            int86(0x10, &regs, &regs);
            getch();
            break;

        case 4:
            printf("Running test case %d\n", choice);
            regs.h.ah = 3;
            regs.h.bh = 0;
            int86(0x10, &regs, &regs);
            x = regs.h.dl;
            y = regs.h.dh;
            printf("Cursor position :- %d col, %d row\n", x, y);
            break;
        default:
            printf("Invalid number\n");
            break;
        }
        printf("Do you to continue [1/0] :- ");
        scanf("%d", &cont);
        if (cont == 0)
        {
            break;
        }
    }
}
