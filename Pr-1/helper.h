LRESULT CALLBACK WndProc ( HWND, UINT, WPARAM, LPARAM ) ;

HINSTANCE hInst ; 
BOOL InitInstance ( HINSTANCE hInstance, int nCmdShow, char* pTitle )
{
 char classname[ ] = "MyWindowClass" ;
 HWND hWnd ;

 WNDCLASSEX wcex ;
 wcex.cbSize   = sizeof ( WNDCLASSEX ) ;
 wcex.style   = CS_HREDRAW | CS_VREDRAW ;
 wcex.lpfnWndProc = ( WNDPROC ) WndProc ;
 wcex.cbClsExtra  = 0 ;
 wcex.cbWndExtra = 0 ;
 wcex.hInstance  = hInstance ;
 wcex.hIcon   = NULL ;
 wcex.hCursor  = LoadCursor ( NULL, IDC_ARROW ) ;
 wcex.hbrBackground = ( HBRUSH )( COLOR_WINDOW + 1 ) ;
 wcex.lpszMenuName = NULL ;
 wcex.lpszClassName = classname ;
 wcex.hIconSm  = NULL ;

 if ( !RegisterClassEx ( &wcex ) )
  return FALSE ;

 hInst = hInstance ; // Store instance handle in our global variable
 hWnd = CreateWindow ( classname, pTitle,
     WS_OVERLAPPEDWINDOW,
     CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, NULL,
     NULL, hInstance, NULL ) ;
if ( !hWnd )
     return FALSE ;

 ShowWindow ( hWnd, nCmdShow ) ;
 UpdateWindow ( hWnd ) ;

 return TRUE ;
}


