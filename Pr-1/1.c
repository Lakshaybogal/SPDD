#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int _stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdLine, int nCmdShow)

{
  HWND h;
  h = CreateWindow("BUTTON", "Hit Me", WS_THICKFRAME, 10, 10, 250, 250, 0, 0, 0, 0);
  ShowWindow(h, nCmdShow);
  MessageBox(0, "Hi !", "Waiting", MB_OK);
  return 0;
}

