# Setup window development environment

## Requirements
- `WSL2`
- `Visual Studio Code`

## Steps
1. Download `Ubuntu 20.04.4 LTS` in Microsoft Store
2. Check `WSL` version
    if version is `1` please set version to `2` using `wsl --set-version 2` command
```powershell
PS C:> wsl -l -v
 NAME            STATE           VERSION
* Ubuntu-20.04    Running         2
```
3. Install VSCode extension `Remote - WSL` and Run VSCode with WSL
4. Run `WSL` in your `powershell` or `CMD`
5. clone this repository and run comamnd `make init`

## Customizing
If you want to automatically make your custom window environment
1. run `setup-window.sh` located this directory with administor authorized state
2. after finish 1. run `install-dependency.sh`
