TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ gir remote add origin https://github.com/johanngomig/dio-resumos-git-e-github.git
bash: gir: command not found

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git remote add origin https://github.com/johanngomig/dio-resumos-git-e-github.git
error: remote origin already exists.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git remote
origin

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git branch -M main

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git branch
* main

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git push -u origin main
Enumerating objects: 26, done.
Counting objects: 100% (26/26), done.
Delta compression using up to 16 threads
Compressing objects: 100% (18/18), done.
Writing objects: 100% (25/25), 6.07 KiB | 1.52 MiB/s, done.
Total 25 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), done.
To https://github.com/johanngomig/Dio-Bootcamp-EngDados.git
   a7c69a1..f23b298  main -> main
branch 'main' set up to track 'origin/main'.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ "Alterações feitas diretamente no github e agora importando para o git local"
bash: Alterações feitas diretamente no github e agora importando para o git local: command not found

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git pull
remote: Enumerating objects: 43, done.
remote: Counting objects: 100% (43/43), done.
remote: Compressing objects: 100% (30/30), done.
remote: Total 38 (delta 6), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (38/38), 8.54 KiB | 11.00 KiB/s, done.
From https://github.com/johanngomig/Dio-Bootcamp-EngDados
   f23b298..e80843c  main       -> origin/main
Updating f23b298..e80843c
Fast-forward
 dio-git-e-github/dio-resumos-git-e-github/.gitignore              | 1 -
 dio-git-e-github/dio-resumos-git-e-github/README.md               | 8 ++++----
 dio-git-e-github/dio-resumos-git-e-github/aulas/.gitkeep          | 0
 .../resumos/{aula-01.md => Resumo Aula 01.md}                     | 0
 .../resumos/{aula-02.md => Resumo Aula 02.md}                     | 0
 5 files changed, 4 insertions(+), 5 deletions(-)
 delete mode 100644 dio-git-e-github/dio-resumos-git-e-github/.gitignore
 delete mode 100644 dio-git-e-github/dio-resumos-git-e-github/aulas/.gitkeep
 rename dio-git-e-github/dio-resumos-git-e-github/resumos/{aula-01.md => Resumo Aula 01.md} (100%)
 rename dio-git-e-github/dio-resumos-git-e-github/resumos/{aula-02.md => Resumo Aula 02.md} (100%)
