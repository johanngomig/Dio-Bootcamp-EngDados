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
