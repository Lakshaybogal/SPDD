#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int _stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)

{
  HWND h[10];
  int x;
  for (x = 0; x <= 9; x++)
  {
    h[x] = CreateWindow("BUTTON", "PRESS Me", WS_ACTIVECAPTION, 20 * x, 20 * x, 250, 100, 0, 0, 0, 0);
    ShowWindow(h[x], nCmdShow);
  }

  MessageBox(0, "Hi !", "Waiting", MB_OK);

  return 0;
}