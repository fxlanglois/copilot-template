$ErrorActionPreference = 'Stop'

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = 'C:\utils\python.exe'
if (-not (Test-Path $pythonExe)) {
    $pythonExe = 'python'
}

$pythonArgs = @(
    (Join-Path $scriptDir 'compare_folders.py'),
    '--config',
    (Join-Path $scriptDir 'compare_folders.config.txt'),
    '--output',
    (Join-Path $scriptDir 'matches.csv'),
    '--folder-output',
    (Join-Path $scriptDir 'folder_matches.csv')
)

& $pythonExe $pythonArgs
if ($LASTEXITCODE -ne 0) {
    exit $LASTEXITCODE
}
