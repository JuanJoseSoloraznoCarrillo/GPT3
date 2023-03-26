$key_file = 'api_key.cnf'
$work_path = Get-Location
$work_path = $work_path.Path
Set-location $work_path
$files = Get-ChildItem
try {
    $documets_files = Get-ChildItem $HOME/Documents/
}
catch {
    $documets_files = Get-ChildItem $HOME/Documentos/
}
$ps1_conf = $documets_files.Name.Contains('WindowsPowerShell')
if($ps1_conf)
{
    Write-Host "You are using the latest configuration for PS1 consoles !!!"
    Start-Sleep -Seconds 1.333
}else{
    try {
        cp -Recurse 'WindowsPowerShell' $HOME/Documents/
    }
    catch {
        cp -Recurse 'WindowsPowerShell' $HOME/Documentos/
    }
    echo "coping windows configurations"
    Start-Sleep -Seconds 1.333
}
if($files.Name.Contains($key_file))
{
    $info = Get-Content $key_file
    $name = $info[1]
    $API_KEY = $info[0]
    Set-Location Scripts
    python3.exe ../Lib/GPT3/chatgpt3.py $API_KEY
}else
{
    $name = read-host "What's your name?"
    Clear-Host
    Write-Output "Installation of GPT3 for $name"
    Start-Sleep -Seconds 1
    $API_KEY = Read-Host "Please insert your API KEY from OpenAI "
    echo $API_KEY >> $key_file
    echo $name >> $key_file
    Set-Location Scripts
    python3.exe ../Lib/GPT3/chatgpt3.py $API_KEY
}
Write-Output "
 Nos vemos pronto $name !!!"
Start-Sleep -Seconds 1.333
Set-Location $HOME
