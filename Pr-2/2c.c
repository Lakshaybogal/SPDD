#include <windows.h>
WNDCLASS wc;
#define ID_FILE_NEW 1
#define ID_FILE_OPEN 2
#define ID_FILE_EXIT 3
void addMenu(HWND h);

long _stdcall myfunc(HWND w, UINT x, UINT y, long z)
{
  switch (x)
  {
  case WM_DESTROY:
    PostQuitMessage(0);
    printf("Executed Successfully");
    break;

  case WM_CREATE:
    addMenu(w);
    break;

  case WM_COMMAND:
    switch (y)
    {
    case ID_FILE_NEW:
      MessageBox(0, "New button clicked", "File", MB_OK);
      break;

    case ID_FILE_OPEN:
      MessageBox(0, "Open button clicked", "File", MB_OK);
      break;

    case ID_FILE_EXIT:
      MessageBox(0, "Exit button clicked", "File", MB_OK);
      break;
    }
  default:
    return DefWindowProc(w, x, y, z);
  }
  return 0;
}

void addMenu(HWND h)
{
  HMENU hMenubar;
  HMENU hMenu, hMenu1;

  hMenubar = CreateMenu();
  hMenu = CreateMenu();

  // hMenubar1 = CreateMenu();
  hMenu1 = CreateMenu();
  HMENU hSubMenu = CreatePopupMenu();

  AppendMenuW(hMenu, MF_STRING | MF_POPUP, (UINT_PTR)hSubMenu, L"&New");
  AppendMenuW(hSubMenu, MF_STRING, ID_FILE_NEW, L"Empty &File");
  AppendMenuW(hSubMenu, MF_SEPARATOR, 0, NULL);
  AppendMenuW(hSubMenu, MF_STRING, ID_FILE_NEW, L"Class..");
  AppendMenuW(hMenu, MF_STRING, ID_FILE_OPEN, L"&Open");

  AppendMenuW(hMenu, MF_SEPARATOR, 0, NULL);
  AppendMenuW(hMenu, MF_STRING, ID_FILE_EXIT, L"&Quit");
  AppendMenuW(hMenubar, MF_POPUP, (UINT_PTR)hMenu, L"&File");
  AppendMenuW(hMenu1, MF_STRING, ID_FILE_EXIT, L"&Undo");
  AppendMenuW(hMenubar, MF_POPUP, (UINT_PTR)hMenu1, L"&Edit");
  SetMenu(h, hMenubar);
}

int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpszCmdline, int nCmdShow)
{
  HINSTANCE hinst;
  HWND hwndMain;
  MSG msg;
  wc.lpfnWndProc = myfunc;
  wc.hInstance = hInstance;
  wc.lpszClassName = "Main Class";
  wc.lpszMenuName = "First Menue";
  RegisterClass(&wc);
  hwndMain = CreateWindow("Main Class", "Name", WS_OVERLAPPEDWINDOW, 0, 0, 300, 300, 0, 0, hInstance, 0);
  ShowWindow(hwndMain, SW_NORMAL);
  while (GetMessage(&msg, 0, 0, 0))
  {
    DispatchMessage(&msg);
  }
  return 0;
}
