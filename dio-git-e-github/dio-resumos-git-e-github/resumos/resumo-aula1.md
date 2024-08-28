TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ touch README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ touch BATATA.txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        BATATA.txt

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git pull
Already up to date.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit -a
Aborting commit due to empty commit message.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git rm README.MD
fatal: pathspec 'README.MD' did not match any files

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git add READM.md
fatal: pathspec 'READM.md' did not match any files

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git rm README.md
rm 'README.md'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit
Aborting commit due to empty commit message.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    README.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit
[main a7c69a1] Preparando o ambiente para o curso de Git/GitHub
 1 file changed, 1 deletion(-)
 delete mode 100644 README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git push
Enumerating objects: 3, done.
Counting objects: 100% (3/3), done.
Writing objects: 100% (2/2), 219 bytes | 219.00 KiB/s, done.
Total 2 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/johanngomig/Dio-Bootcamp-EngDados.git
   dc5a38d..a7c69a1  main -> main

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ touch README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        README.md

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ touch RESUMO.txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git add README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        RESUMO.txt


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git add RESUMO.txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   README.md
        new file:   RESUMO.txt


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit -m"commit inicial"
[main 1aa0681] commit inicial
 2 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
 create mode 100644 RESUMO.txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git log
commit 1aa0681b50a5fdc4da7746424c80c1da20b3b901 (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:21:32 2024 -0300

    commit inicial

commit a7c69a1a1b52e5a9030a19e85e51587756118906 (origin/main, origin/HEAD)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ mkdir resumos

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ touch resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        resumos/

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ echo resumos/ > .gitignore

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ echo > .gitignore

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        resumos/

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ mkdir aulas

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        resumos/

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ touch aulas/.gitkeep

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore
        aulas/
        resumos/

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git add .
warning: in the working copy of '.gitignore', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   aulas/.gitkeep
        new file:   resumos/resumo-aula1.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git commit -m"adicionar arquivo git ignore e diretórios de aula e resumos"
[main 6f31b82] adicionar arquivo git ignore e diretórios de aula e resumos
 3 files changed, 1 insertion(+)
 create mode 100644 .gitignore
 create mode 100644 aulas/.gitkeep
 create mode 100644 resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados (main)
$ git log
commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24 (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:28:23 2024 -0300

    adicionar arquivo git ignore e diretórios de aula e resumos

commit 1aa0681b50a5fdc4da7746424c80c1da20b3b901
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:21:32 2024 -0300

    commit inicial

commit a7c69a1a1b52e5a9030a19e85e51587756118906 (origin/main, origin/HEAD)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

