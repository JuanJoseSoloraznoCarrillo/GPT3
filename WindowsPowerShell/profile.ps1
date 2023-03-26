Clear-Host # clear current console.
function prompt
{
    Set-PSReadLineOption -Color @{ command = 'green'}
    $currentDir = (Convert-Path .)
    if($currentDir.Contains($HOME))
    {
        $currentDir = $currentDir.Replace($HOME, '~ ')
    }
    if(Test-Path .git)
    {
       Write-Host ("" + $currentDir + "\\") -NoNewLine `
       -ForegroundColor 13
       Write-BranchName
       Write-Host("-->") -NoNewLine `
       -ForegroundColor 10
            return " "
    }
    else{
        Write-Host(""+$currentDir+"\\") -NoNewLine `
        -ForegroundColor 13
        Write-Host("-->") -NoNewLine `
        -ForegroundColor 10
            return " "
    }
}
function Write-BranchName()
{
    try{
        $branch = git rev-parse --abbrev-ref HEAD 

        if($branch -eq "HEAD")
        {
            $branch = git rev-parse --short HEAD
            Write-Host "<$branch>" -ForegroundColor "red" -NoNewLine `
        }
        else{
            
            Write-Host "<$branch>" -ForegroundColor "blue" -NoNewLine `
        }
    }catch{
        Write-Host "<no branches yer>" -ForegroundColor "yellow" -NoNewLine `
    }
}