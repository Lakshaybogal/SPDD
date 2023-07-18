

#include <windows.h>
int _stdcall WinMain(HINSTANCE hinstance, HINSTANCE hPrevinstance, LPSTR IpszCmdline, int nCmdShow)
{
  HWND h[5];
  h[0] = CreateWindow("BUTTON", "HSCROLL", WS_HSCROLL, 10, 10, 150, 100, 0, 0, hinstance, 0);
  ShowWindow(h[0], nCmdShow);
  h[1] = CreateWindow("BUTTON", "MAXIMIZEBOX", WS_OVERLAPPEDWINDOW | WS_MAXIMIZEBOX, 100, 100, 150, 100, 0, 0, hinstance, 0);
  ShowWindow(h[1], nCmdShow);
  h[2] = CreateWindow("BUTTON", "MINIMIZEBOX", WS_OVERLAPPEDWINDOW | WS_MINIMIZEBOX, 200, 200, 150, 100, 0, 0, hinstance, 0);
  ShowWindow(h[2], nCmdShow);
  h[3] = CreateWindow("BUTTON", "VSCROLL", WS_VSCROLL, 300, 300, 150, 100, 0, 0, hinstance, 0);
  ShowWindow(h[3], nCmdShow);
  h[4] = CreateWindow("BUTTON", "SYSMENU", WS_SYSMENU, 400, 400, 150, 100, 0, 0, hinstance, 0);
  ShowWindow(h[4], nCmdShow);
  MessageBox(0, " name !", "Waiting", MB_OK);
}
