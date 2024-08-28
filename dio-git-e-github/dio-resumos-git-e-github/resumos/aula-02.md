TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ mkdir aulas

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ mkdir resumos

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ touch aulas/.gitkeep

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ touch resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ echo aulas/ > .gitignore

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ touch README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../
        ../../repo-local/

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add .
warning: in the working copy of 'dio-git-e-github/dio-resumos-git-e-github/.gitignore', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   resumos/resumo-aula1.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../../repo-local/


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add ../../repo-local/
error: 'repo-local/' does not have a commit checked out
fatal: adding files failed

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   resumos/resumo-aula1.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit 8220ed2c20b905b736dc31d993258f4233122d0b (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git commit -m"Adequação de arvore para aula"
[main d5930b3] Adequação de arvore para aula
 3 files changed, 19 insertions(+)
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/.gitignore
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/README.md
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit d5930b30df60c75ef9929038937ea004b49d4ee1 (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:15:57 2024 -0300

    Adequação de arvore para aula

commit 8220ed2c20b905b736dc31d993258f4233122d0b
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ mkdir Nova pasta

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ ls
Nova/  README.md  aulas/  pasta/  resumos/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ rmdir Nova pasta

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ ls
README.md  aulas/  resumos/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ mkdir "Nova pasta"

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ ls
'Nova pasta'/   README.md   aulas/   resumos/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ cd "Nova pasta"/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github/Nova pasta (main)
$ git init
Initialized empty Git repository in F:/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github/Nova pasta/.git/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github/Nova pasta (main)
$ rm -rf .git

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github/Nova pasta (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../resumos/resumo-aula1.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github/Nova pasta (main)
$ cd ..

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ ls
'Nova pasta'/   README.md   aulas/   resumos/
k
TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ rm "Nova pasta"/
rm: cannot remove 'Nova pasta/': Is a directory

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ rmdir "Nova pasta"/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ ls
README.md  aulas/  resumos/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   resumos/resumo-aula1.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   resumos/resumo-aula1.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git restore README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   resumos/resumo-aula1.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit d5930b30df60c75ef9929038937ea004b49d4ee1 (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:15:57 2024 -0300

    Adequação de arvore para aula

commit 8220ed2c20b905b736dc31d993258f4233122d0b
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git commit --amend -m"Adiciona gitignore e diretórios aulas e resumos"
[main 7b43d25] Adiciona gitignore e diretórios aulas e resumos
 Date: Wed Aug 28 14:15:57 2024 -0300
 3 files changed, 204 insertions(+)
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/.gitignore
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/README.md
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit 7b43d25fb6f90618140a11306d6db66765c7e43c (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:15:57 2024 -0300

    Adiciona gitignore e diretórios aulas e resumos

commit 8220ed2c20b905b736dc31d993258f4233122d0b
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git commit --amend
[main 1264d5e] Adiciona gitignore e diretórios aulas e resumos xD
 Date: Wed Aug 28 14:15:57 2024 -0300
 3 files changed, 204 insertions(+)
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/.gitignore
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/README.md
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit 1264d5e4bd4ad1df1d7c29fdc7f934fddb2cd37b (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:15:57 2024 -0300

    Adiciona gitignore e diretórios aulas e resumos xD

commit 8220ed2c20b905b736dc31d993258f4233122d0b
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git reset --soft 1264d5e4bd4ad1df1d7c29fdc7f934fddb2cd37b

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git reset --soft 8220ed2c20b905b736dc31d993258f4233122d0b

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   resumos/resumo-aula1.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ commit -m"soft"
bash: commit: command not found

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git commit -m"soft"
[main 268b14c] soft
 3 files changed, 204 insertions(+)
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/.gitignore
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/README.md
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit 268b14cbe003d8c0197c520f1efd925de9d4f379 (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:26:44 2024 -0300

    soft

commit 8220ed2c20b905b736dc31d993258f4233122d0b
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git reset --mixed 8220ed2c20b905b736dc31d993258f4233122d0b

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add .
warning: in the working copy of 'dio-git-e-github/dio-resumos-git-e-github/.gitignore', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   .gitignore
        new file:   README.md
        new file:   resumos/resumo-aula1.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git commit -m"mixed"
[main 3fb9910] mixed
 3 files changed, 204 insertions(+)
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/.gitignore
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/README.md
 create mode 100644 dio-git-e-github/dio-resumos-git-e-github/resumos/resumo-aula1.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 6 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git log
commit 3fb9910be1b754e2909d73dcd5255d2f0d34a8ed (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:28:13 2024 -0300

    mixed

commit 8220ed2c20b905b736dc31d993258f4233122d0b
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:08:46 2024 -0300

    Adequação de ambiente 2

commit 26b07c2874f39001cce0bd63ff413240970410e3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:06:53 2024 -0300

    Adequando ambiente

commit 5bb2376b07466b6826f852104659a3fa83dfc8b1
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:32:17 2024 -0300

    Finalização da aula 1

commit 6f31b826eb21bebf2b36620d359f5dc478ed0c24
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

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git reset --hard 8220ed2c20b905b736dc31d993258f4233122d0b
HEAD is now at 8220ed2 Adequação de ambiente 2

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git reflog
8220ed2 (HEAD -> main) HEAD@{0}: reset: moving to 8220ed2c20b905b736dc31d993258f4233122d0b
3fb9910 HEAD@{1}: commit: mixed
8220ed2 (HEAD -> main) HEAD@{2}: reset: moving to 8220ed2c20b905b736dc31d993258f4233122d0b
268b14c HEAD@{3}: commit: soft
8220ed2 (HEAD -> main) HEAD@{4}: reset: moving to 8220ed2c20b905b736dc31d993258f4233122d0b
1264d5e HEAD@{5}: reset: moving to 1264d5e4bd4ad1df1d7c29fdc7f934fddb2cd37b
1264d5e HEAD@{6}: commit (amend): Adiciona gitignore e diretórios aulas e resumos xD
7b43d25 HEAD@{7}: commit (amend): Adiciona gitignore e diretórios aulas e resumos
d5930b3 HEAD@{8}: commit: Adequação de arvore para aula
8220ed2 (HEAD -> main) HEAD@{9}: commit: Adequação de ambiente 2
26b07c2 HEAD@{10}: commit: Adequando ambiente
5bb2376 HEAD@{11}: commit: Finalização da aula 1
6f31b82 HEAD@{12}: commit: adicionar arquivo git ignore e diretórios de aula e resumos
1aa0681 HEAD@{13}: commit: commit inicial
a7c69a1 (origin/main, origin/HEAD) HEAD@{14}: commit: Preparando o ambiente para o curso de Git/GitHub
dc5a38d HEAD@{15}: clone: from https://github.com/johanngomig/Dio-Bootcamp-EngDados.git

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ ls
aulas/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ mkdir resumos

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ touch resumos/aula-01.md resumos/aula-02.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ../

nothing added to commit but untracked files present (use "git add" to track)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git reset resumos/aula-01.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   aulas/.gitkeep
        new file:   resumos/aula-02.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        resumos/aula-01.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git restore --staged resumos/aula-01.md
error: pathspec 'resumos/aula-01.md' did not match any file(s) known to git

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git restore --staged resumos/aula-02.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/dio-resumos-git-e-github (main)
$ git status
On branch main
Your branch is ahead of 'origin/main' by 5 commits.
  (use "git push" to publish your local commits)

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   aulas/.gitkeep

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        resumos/

