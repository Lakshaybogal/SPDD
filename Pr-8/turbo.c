#include <dos.h>
#include <conio.h>
#include <graphics.h>
#include <stdio.h>
int initmouse();
void showmouseptr();
void hidemouseptr();
void getmousepos(int *, int *, int *);

union REGS i, o;
int opn1(), opn2(), opn3(), opn4();
main()
{
    int choice, cout;

    do
    {
        clrscr();

        printf("_____MENU_____\n");
        printf("1.Mouse support available or not\n");
        printf("2.Display Mouse Pointer in graphics mode\n");
        printf("3.Which mouse button is clicked\n");
        printf("4.Current position of mouse pointer\n");
        printf("Enter choice:");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            opn1();
            break;
        case 2:
            opn2();
            break;
        case 3:
            opn3();
            break;
        case 4:
            opn4();
            break;
        default:
            printf("Invalid choice..\n");
        }

        printf("Do you want to continue?");
        scanf("%d", &cout);
    } while (cout == 1);
    getch();
    return (0);
}
opn1()
{
    int status;
    clrscr();
    status = initmouse();

    if (status == 0)
        printf("Mouse support not available.\n");
    else
        printf("Mouse support available.\n");
    return 0;
}

int initmouse()
{
    i.x.ax = 0;
    int86(0X33, &i, &o);
    return (o.x.ax);
}

opn4()
{
    int gd = DETECT, gm, status, button, x, y, tempx, tempy;
    char array[50];

    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    settextstyle(DEFAULT_FONT, 0, 2);

    status = initmouse();
    if (status == 0)
        printf("Mouse support not available.\n");
    else
    {
        showmouseptr();

        getmousepos(&button, &x, &y);

        tempx = x;
        tempy = y;

        while (!kbhit())
        {
            getmousepos(&button, &x, &y);

            if (x == tempx && y == tempy)
            {
            }
            else
            {
                cleardevice();
                sprintf(array, "X = %d, Y = %d", x, y);
                outtext(array);
                tempx = x;
                tempy = y;
            }
        }
    }

    getch();
    return 0;
}

void showmouseptr()
{
    i.x.ax = 1;
    int86(0X33, &i, &o);
}

void getmousepos(int *button, int *x, int *y)
{
    i.x.ax = 3;
    int86(0X33, &i, &o);

    *button = o.x.bx;
    *x = o.x.cx;
    *y = o.x.dx;
}

opn3()
{
    int gd = DETECT, gm, status, button, x, y;
    char array[50];

    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    settextstyle(DEFAULT_FONT, 0, 2);

    status = initmouse();

    if (status == 0)
        printf("Mouse support not available.\n");
    else
    {
        showmouseptr();

        getmousepos(&button, &x, &y);

        while (!kbhit())
        {
            getmousepos(&button, &x, &y);

            if (button == 1)
            {
                button = -1;
                cleardevice();
                sprintf(array, "Left Button clicked x = %d y = %d", x, y);
                outtext(array);
            }
            else if (button == 2)
            {
                button = -1;
                cleardevice();
                sprintf(array, "Right Button clicked x = %d y = %d", x, y);
                outtext(array);
            }
        }
    }
    getch();
    return 0;
}

opn2()
{
    int status, gd = DETECT, gm;
    initgraph(&gd, &gm, "C:\\TURBOC3\\BGI");
    status = initmouse();
    if (status == 0)
        printf("Mouse support not available.\n");
    else
        showmouseptr();
    getch();
    return 0;
}