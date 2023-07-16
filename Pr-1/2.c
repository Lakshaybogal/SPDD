#include <windows.h>
#include "helper.h"
#define IDM_FILE_NEW 1
#define IDM_FILE_OPEN 2
#define IDM_FILE_QUIT 3
#define IDM_FILE_UNDO 4

void OnDestroy(HWND);
LRESULT CALLBACK WndProc(HWND, UINT, WPARAM, LPARAM);
void AddMenus(HWND);
int _stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInst, LPSTR arg, int nCmdShow)
{
  MSG m;
  InitInstance(hInstance, nCmdShow, "title");
  while (GetMessage(&m, 0, 0, 0))
  {
    TranslateMessage(&m);
    DispatchMessage(&m);
  }

  return (int)m.wParam;
}
LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM IParam)
{
  switch (message)
  {
  case WM_CREATE:

    AddMenus(hWnd);
    break;

  case WM_COMMAND:

    switch (LOWORD(wParam))
    {

    case IDM_FILE_NEW:
      MessageBeep(MB_ICONINFORMATION);
      break;
    case IDM_FILE_OPEN:
      MessageBeep(MB_ICONINFORMATION);
      break;
    case IDM_FILE_QUIT:
      SendMessage(hWnd, WM_CLOSE, 0, 0);
      break;

    case IDM_FILE_UNDO:
      MessageBeep(MB_ICONINFORMATION);
      break;
    }

    break;

  case WM_DESTROY:
    OnDestroy(hWnd);
    break;

  default:
    return DefWindowProc(hWnd, message, wParam, IParam);
  }
  return 0;
}
void OnDestroy(HWND hWnd)
{
  PostQuitMessage(0);
}
void AddMenus(HWND hwnd)
{

  HMENU hMenubar;
  HMENU hMenu, hMenu1;

  hMenubar = CreateMenu();
  hMenu = CreateMenu();

  hMenu1 = CreateMenu();
  HMENU hSubMenu = CreatePopupMenu();

  AppendMenuW(hMenu, MF_STRING | MF_POPUP, (UINT_PTR)hSubMenu, L"&New");
  AppendMenuW(hSubMenu, MF_STRING, IDM_FILE_NEW, L"Empty &File");
  AppendMenuW(hSubMenu, MF_SEPARATOR, 0, NULL);
  AppendMenuW(hSubMenu, MF_STRING, IDM_FILE_NEW, L"Class..");
  AppendMenuW(hMenu, MF_STRING, IDM_FILE_OPEN, L"&Open");

  AppendMenuW(hMenu, MF_SEPARATOR, 0, NULL);
  AppendMenuW(hMenu, MF_STRING, IDM_FILE_QUIT, L"&Quit");

  AppendMenuW(hMenubar, MF_POPUP, (UINT_PTR)hMenu, L"&File");

  AppendMenuW(hMenu1, MF_STRING, IDM_FILE_UNDO, L"&Undo");
  AppendMenuW(hMenubar, MF_POPUP, (UINT_PTR)hMenu1, L"&Edit");
 
  SetMenu(hwnd, hMenubar);
}