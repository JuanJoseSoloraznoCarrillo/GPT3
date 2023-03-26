$script:showWindowAsync = Add-Type –memberDefinition @"
[DllImport("C:\Windows\System32\user32.dll")]
public static extern bool ShowWindowAsync(IntPtr hWnd, int nCmdShow);
"@ -name "Win32ShowWindowAsync" -namespace Win32Functions –passThru

function Show-PowerShell() {
     $null = $showWindowAsync::ShowWindowAsync((Get-Process –id $pid).MainWindowHandle, 10)
}

function Hide-PowerShell() {
    $null = $showWindowAsync::ShowWindowAsync((Get-Process –id $pid).MainWindowHandle, 2)
}
