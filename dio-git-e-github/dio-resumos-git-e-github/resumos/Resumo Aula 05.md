
TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados
$ git clone https://github.com/johanngomig/Dio-Bootcamp-EngDados.git --branch teste --single-branch
Cloning into 'Dio-Bootcamp-EngDados'...
remote: Enumerating objects: 151, done.
remote: Counting objects: 100% (151/151), done.
remote: Compressing objects: 100% (99/99), done.
remote: Total 151 (delta 30), reused 78 (delta 14), pack-reused 0 (from 0)
Receiving objects: 100% (151/151), 31.04 KiB | 7.76 MiB/s, done.
Resolving deltas: 100% (30/30), done.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados
$ ls
Dio-Bootcamp-EngDados/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados
$ cd Dio-Bootcamp-EngDados/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git status
On branch teste
Your branch is up to date with 'origin/teste'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    dio-git-e-github/dio-resumos-git-e-github/arquivo.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git stash
Saved working directory and index state WIP on teste: ffd985f conteúdo do arquivo "committado" na branch remota.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git stash list
stash@{0}: WIP on teste: ffd985f conteúdo do arquivo "committado" na branch remota.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git checkout -b teste-2
Switched to a new branch 'teste-2'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste-2)
$ realizou as alterações necessárias na teste2
bash: realizou: command not found

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste-2)
$ git checkout teste
Switched to branch 'teste'
Your branch is up to date with 'origin/teste'.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git stash list
stash@{0}: WIP on teste: ffd985f conteúdo do arquivo "committado" na branch remota.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git stash pop =se quiser excluir        git stash apply =se quiser manter a alteração para uso posterior
Too many revisions specified: '=se' 'quiser' 'excluir' 'git' 'stash' 'apply' '=se' 'quiser' 'manter' 'a' 'alteração' 'para' 'uso' 'posterior'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (teste)
$ git stash apply
On branch teste
Your branch is up to date with 'origin/teste'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    dio-git-e-github/dio-resumos-git-e-github/arquivo.md

no changes added to commit (use "git add" and/or "git commit -a")
