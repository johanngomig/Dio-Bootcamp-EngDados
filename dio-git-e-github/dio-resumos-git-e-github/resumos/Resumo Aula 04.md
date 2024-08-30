TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 1.11 KiB | 2.00 KiB/s, done.
From https://github.com/johanngomig/Dio-Bootcamp-EngDados
   32deec2..8e2d790  main       -> origin/main
error: Your local changes to the following files would be overwritten by merge:
        dio-git-e-github/dio-resumos-git-e-github/README.md
Please commit your changes or stash them before you merge.
Aborting
Updating 32deec2..8e2d790

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git status
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git commit -m"atualização README.md'
> ^C

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git commit -m"atualização README.md"
[main afb5e35] atualização README.md
 1 file changed, 1 insertion(+)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git pull
Auto-merging dio-git-e-github/dio-resumos-git-e-github/README.md
Merge made by the 'ort' strategy.
 dio-git-e-github/dio-resumos-git-e-github/README.md | 1 +
 1 file changed, 1 insertion(+)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git log
commit ea6d297203c9920deedb16debda9ba2285b296b9 (HEAD -> main)
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory

commit 70a93ca5ffce704e1024c98d336358dd01a8d921
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:19 2024 -0300

    Update README.md
...skipping...

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory

commit 70a93ca5ffce704e1024c98d336358dd01a8d921
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:19 2024 -0300

    Update README.md

commit f23b2989c52cbad9a34f573791a1f74e8da887ed
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:35:27 2024 -0300

    Commit Final Aula

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

commit a7c69a1a1b52e5a9030a19e85e51587756118906
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ echo "#commit-1-branch-main" > commit-1-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git add .
warning: in the working copy of 'dio-git-e-github/commit-1-branch-main-txt', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git commit -m"commit 1 branch"
[main 690ad53] commit 1 branch
 1 file changed, 1 insertion(+)
 create mode 100644 dio-git-e-github/commit-1-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git log
commit 690ad534804dab6b0a515aed33ca6b927c648e2f (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory
...skipping...

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory

commit 70a93ca5ffce704e1024c98d336358dd01a8d921
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:19 2024 -0300

    Update README.md

commit f23b2989c52cbad9a34f573791a1f74e8da887ed
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:35:27 2024 -0300

    Commit Final Aula

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

commit a7c69a1a1b52e5a9030a19e85e51587756118906
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ echo "#commit-2-branch-main" > commit-2-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git add .
warning: in the working copy of 'dio-git-e-github/commit-2-branch-main-txt', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git commit -m"commit 2 branch"
[main a820f4e] commit 2 branch
 1 file changed, 1 insertion(+)
 create mode 100644 dio-git-e-github/commit-2-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git log
commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md
...skipping...

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory

commit 70a93ca5ffce704e1024c98d336358dd01a8d921
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:19 2024 -0300

    Update README.md

commit f23b2989c52cbad9a34f573791a1f74e8da887ed
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:35:27 2024 -0300

    Commit Final Aula

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

commit a7c69a1a1b52e5a9030a19e85e51587756118906
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (main)
$ git checkout -b teste
Switched to a new branch 'teste'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (teste)
$ git log
commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db (HEAD -> teste, main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

...skipping...

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory

commit 70a93ca5ffce704e1024c98d336358dd01a8d921
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:19 2024 -0300

    Update README.md

commit f23b2989c52cbad9a34f573791a1f74e8da887ed
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:35:27 2024 -0300

    Commit Final Aula

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

commit a7c69a1a1b52e5a9030a19e85e51587756118906
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (teste)
$ echo "#commit-3-branch-main" > commit-3-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (teste)
$ git add .
warning: in the working copy of 'dio-git-e-github/commit-3-branch-main-txt', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (teste)
$ git commit -m"commit 3 branch"
[teste dde9040] commit 3 branch
 1 file changed, 1 insertion(+)
 create mode 100644 dio-git-e-github/commit-3-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (teste)
$ git log
commit dde9040396715412ebb08bd0842601bb055c9a22 (HEAD -> teste)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:51:53 2024 -0300

    commit 3 branch

commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db (main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore
...skipping...

commit 1d4e3113c90ed18d15b8a19974f68710f76d6442
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:44:37 2024 -0300

    Rename aula-02.md to Resumo Aula 02.md

commit 5a62531895454a98c3e13355e2bc73fb4d25f291
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:58 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/.gitignore

commit 622414a21e52ed9911ae9f99a1b9e9f19260df5b
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:43:29 2024 -0300

    Rename aula-01.md to Resumo Aula 01.md

commit e5cd407f12955e83eba5c77a3300ddb6e794c788
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:52 2024 -0300

    Delete dio-git-e-github/dio-resumos-git-e-github/aulas directory

commit 70a93ca5ffce704e1024c98d336358dd01a8d921
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:42:19 2024 -0300

    Update README.md

commit f23b2989c52cbad9a34f573791a1f74e8da887ed
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:35:27 2024 -0300

    Commit Final Aula

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

commit a7c69a1a1b52e5a9030a19e85e51587756118906
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 13:03:52 2024 -0300

    Preparando o ambiente para o curso de Git/GitHub

commit dc5a38d85286b0fa8a876b58b640de1292250573
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Tue Aug 27 22:41:33 2024 -0300

    Initial commit

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github (teste)
$ cd trabalhando-com-branches/

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        ./

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git add .
warning: in the working copy of 'dio-git-e-github/trabalhando-com-branches/commit-1-branch-main-txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'dio-git-e-github/trabalhando-com-branches/commit-2-branch-main-txt', LF will be replaced by CRLF the next time Git touches it
warning: in the working copy of 'dio-git-e-github/trabalhando-com-branches/commit-3-branch-main-txt', LF will be replaced by CRLF the next time Git touches it

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git commit -m"ajustando ambiente de branch"
[teste 6d6f607] ajustando ambiente de branch
 3 files changed, 3 insertions(+)
 create mode 100644 dio-git-e-github/trabalhando-com-branches/commit-1-branch-main-txt
 create mode 100644 dio-git-e-github/trabalhando-com-branches/commit-2-branch-main-txt
 create mode 100644 dio-git-e-github/trabalhando-com-branches/commit-3-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git rm .
fatal: not removing '.' recursively without -r

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git rm . -r
rm 'dio-git-e-github/trabalhando-com-branches/commit-1-branch-main-txt'
rm 'dio-git-e-github/trabalhando-com-branches/commit-2-branch-main-txt'
rm 'dio-git-e-github/trabalhando-com-branches/commit-3-branch-main-txt'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    commit-1-branch-main-txt
        deleted:    commit-2-branch-main-txt
        deleted:    commit-3-branch-main-txt

Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git restore --staged .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt
        deleted:    commit-1-branch-main-txt
        deleted:    commit-2-branch-main-txt
        deleted:    commit-3-branch-main-txt

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git commit -m"Teste de restore e modificação de pasta local"
On branch teste
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt
        deleted:    commit-1-branch-main-txt
        deleted:    commit-2-branch-main-txt
        deleted:    commit-3-branch-main-txt

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt
        deleted:    commit-1-branch-main-txt
        deleted:    commit-2-branch-main-txt
        deleted:    commit-3-branch-main-txt

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git restore commit-1-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git restore commit-2-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git restore commit-3-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git rm ../commit-1-branch-main-txt
rm 'dio-git-e-github/commit-1-branch-main-txt'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git rm ../commit-2-branch-main-txt
rm 'dio-git-e-github/commit-2-branch-main-txt'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git rm ../commit-3-branch-main-txt
rm 'dio-git-e-github/commit-3-branch-main-txt'

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    ../commit-1-branch-main-txt
        deleted:    ../commit-2-branch-main-txt
        deleted:    ../commit-3-branch-main-txt


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git commit -m"Ambiente reorganizado"
[teste c9737de] Ambiente reorganizado
 3 files changed, 3 deletions(-)
 delete mode 100644 dio-git-e-github/commit-1-branch-main-txt
 delete mode 100644 dio-git-e-github/commit-2-branch-main-txt
 delete mode 100644 dio-git-e-github/commit-3-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git status
On branch teste
nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git log
commit c9737de573db6d0b6e7b0af7687ff080a053675a (HEAD -> teste)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:55:54 2024 -0300

    Ambiente reorganizado

commit 6d6f60722a6265954be7e8dc6ca365194eaf67f3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:53:15 2024 -0300

    ajustando ambiente de branch

commit dde9040396715412ebb08bd0842601bb055c9a22
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:51:53 2024 -0300

    commit 3 branch

commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db (main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git chekout main
git: 'chekout' is not a git command. See 'git --help'.

The most similar command is
        checkout

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (teste)
$ git checkout main
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 4 commits.
  (use "git push" to publish your local commits)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git branch -v
* main  a820f4e [ahead 4] commit 2 branch
  teste c9737de Ambiente reorganizado

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git merge teste
Updating a820f4e..c9737de
Fast-forward
 dio-git-e-github/{ => trabalhando-com-branches}/commit-1-branch-main-txt | 0
 dio-git-e-github/{ => trabalhando-com-branches}/commit-2-branch-main-txt | 0
 dio-git-e-github/trabalhando-com-branches/commit-3-branch-main-txt       | 1 +
 3 files changed, 1 insertion(+)
 rename dio-git-e-github/{ => trabalhando-com-branches}/commit-1-branch-main-txt (100%)
 rename dio-git-e-github/{ => trabalhando-com-branches}/commit-2-branch-main-txt (100%)
 create mode 100644 dio-git-e-github/trabalhando-com-branches/commit-3-branch-main-txt

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git branch
* main
  teste

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git branch -d teste
Deleted branch teste (was c9737de).

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git branch
* main

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git pull
Already up to date.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git push
Enumerating objects: 37, done.
Counting objects: 100% (37/37), done.
Delta compression using up to 16 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (29/29), 2.26 KiB | 1.13 MiB/s, done.
Total 29 (delta 8), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (8/8), completed with 1 local object.
To https://github.com/johanngomig/Dio-Bootcamp-EngDados.git
   8e2d790..c9737de  main -> main

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git commit -m"commit feito localmente"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git log
commit c9737de573db6d0b6e7b0af7687ff080a053675a (HEAD -> main, origin/main, origin/HEAD)
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:55:54 2024 -0300

    Ambiente reorganizado

commit 6d6f60722a6265954be7e8dc6ca365194eaf67f3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:53:15 2024 -0300

    ajustando ambiente de branch

commit dde9040396715412ebb08bd0842601bb055c9a22
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:51:53 2024 -0300

    commit 3 branch

commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

commit 8f33899412c8d111cd7fb69b443a841d9fa777d6
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:49:30 2024 -0300

    Update README.md

commit 2f5b4c8be71b70dfc36be34e2c80e7ec6b53b1aa
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:48:41 2024 -0300

    Update README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 1), reused 0 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 1.10 KiB | 11.00 KiB/s, done.
From https://github.com/johanngomig/Dio-Bootcamp-EngDados
   c9737de..514532b  main       -> origin/main
Updating c9737de..514532b
Fast-forward
 dio-git-e-github/dio-resumos-git-e-github/README.md | 1 +
 1 file changed, 1 insertion(+)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git commit -m"commit feito localmente"
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add ../dio-resumos-git-e-github/README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git commit -m"commit feito localmente"
[main 98f11d9] commit feito localmente
 1 file changed, 1 insertion(+)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git log
commit 98f11d981968adb2abe282f6f99f9172cd2e10c6 (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Fri Aug 30 10:58:51 2024 -0300

    commit feito localmente

commit 514532bed7862349c79e29d5a0b93784c31adf73 (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Fri Aug 30 10:52:59 2024 -0300

    commit depois do clone

commit c9737de573db6d0b6e7b0af7687ff080a053675a
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:55:54 2024 -0300

    Ambiente reorganizado

commit 6d6f60722a6265954be7e8dc6ca365194eaf67f3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:53:15 2024 -0300

    ajustando ambiente de branch

commit dde9040396715412ebb08bd0842601bb055c9a22
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:51:53 2024 -0300

    commit 3 branch

commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

commit e80843c40465febd798cf0b18c82d57ecf839d15
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:50:52 2024 -0300

    Update README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git push origin main
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 16 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 466 bytes | 466.00 KiB/s, done.
Total 5 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/johanngomig/Dio-Bootcamp-EngDados.git
   514532b..98f11d9  main -> main

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git add ../dio-resumos-git-e-github/README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   ../dio-resumos-git-e-github/README.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git commit -m"commit local sem realizar pull"
[main 3b597c9] commit local sem realizar pull
 1 file changed, 1 insertion(+), 1 deletion(-)

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git log
commit 3b597c9e6db6f1cb4880d7aa4c849a72d91f41bc (HEAD -> main)
Author: johanngomig <johanngomig@gmail.com>
Date:   Fri Aug 30 11:01:53 2024 -0300

    commit local sem realizar pull

commit 98f11d981968adb2abe282f6f99f9172cd2e10c6 (origin/main, origin/HEAD)
Author: johanngomig <johanngomig@gmail.com>
Date:   Fri Aug 30 10:58:51 2024 -0300

    commit feito localmente

commit 514532bed7862349c79e29d5a0b93784c31adf73
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Fri Aug 30 10:52:59 2024 -0300

    commit depois do clone

commit c9737de573db6d0b6e7b0af7687ff080a053675a
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:55:54 2024 -0300

    Ambiente reorganizado

commit 6d6f60722a6265954be7e8dc6ca365194eaf67f3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:53:15 2024 -0300

    ajustando ambiente de branch

commit dde9040396715412ebb08bd0842601bb055c9a22
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:51:53 2024 -0300

    commit 3 branch

commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300

    Update README.md

commit 32deec29e1bdfb2b9e69ae5e3065fd605f4c8bc7
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 14:57:54 2024 -0300

    Update README.md

commit 7ded0579bd48ffcd3d465eaff23903492e1d2e66
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 14:56:37 2024 -0300

    Adicionando resumo da aula 3

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git push origin main
To https://github.com/johanngomig/Dio-Bootcamp-EngDados.git
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to 'https://github.com/johanngomig/Dio-Bootcamp-EngDados.git'
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git pull
remote: Enumerating objects: 9, done.
remote: Counting objects: 100% (9/9), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 5 (delta 1), reused 2 (delta 0), pack-reused 0 (from 0)
Unpacking objects: 100% (5/5), 1.10 KiB | 49.00 KiB/s, done.
From https://github.com/johanngomig/Dio-Bootcamp-EngDados
   98f11d9..806bd0e  main       -> origin/main
Auto-merging dio-git-e-github/dio-resumos-git-e-github/README.md
CONFLICT (content): Merge conflict in dio-git-e-github/dio-resumos-git-e-github/README.md
Automatic merge failed; fix conflicts and then commit the result.

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$ git add .

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   ../dio-resumos-git-e-github/README.md

no changes added to commit (use "git add" and/or "git commit -a")

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$ git add ../dio-resumos-git-e-github/README.md

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$ git status
On branch main
Your branch and 'origin/main' have diverged,
and have 1 and 1 different commits each, respectively.
  (use "git pull" if you want to integrate the remote branch with yours)

All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
        modified:   ../dio-resumos-git-e-github/README.md


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main|MERGING)
$ git commit -m"commit após o conflito"
[main a1ffdfa] commit após o conflito

TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git log
commit a1ffdfa8e8692a9480935d174eb6809841291760 (HEAD -> main)
Merge: 3b597c9 806bd0e
Author: johanngomig <johanngomig@gmail.com>
Date:   Fri Aug 30 11:05:15 2024 -0300

    commit após o conflito

commit 3b597c9e6db6f1cb4880d7aa4c849a72d91f41bc
Author: johanngomig <johanngomig@gmail.com>
Date:   Fri Aug 30 11:01:53 2024 -0300

    commit local sem realizar pull

commit 806bd0ee0b76f4b6070cc2fd52cefb0106a82d1c (origin/main, origin/HEAD)
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Fri Aug 30 11:00:44 2024 -0300

    commit depois do clone !

commit 98f11d981968adb2abe282f6f99f9172cd2e10c6
Author: johanngomig <johanngomig@gmail.com>
Date:   Fri Aug 30 10:58:51 2024 -0300

    commit feito localmente

commit 514532bed7862349c79e29d5a0b93784c31adf73
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Fri Aug 30 10:52:59 2024 -0300

    commit depois do clone

commit c9737de573db6d0b6e7b0af7687ff080a053675a
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:55:54 2024 -0300

    Ambiente reorganizado

commit 6d6f60722a6265954be7e8dc6ca365194eaf67f3
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:53:15 2024 -0300

    ajustando ambiente de branch

commit dde9040396715412ebb08bd0842601bb055c9a22
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:51:53 2024 -0300

    commit 3 branch

commit a820f4eb1ccbda2ffc7a1d32f3b47bfe4a5332db
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:50:15 2024 -0300

    commit 2 branch

commit 690ad534804dab6b0a515aed33ca6b927c648e2f
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:49:12 2024 -0300

    commit 1 branch

commit ea6d297203c9920deedb16debda9ba2285b296b9
Merge: afb5e35 8e2d790
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:43:00 2024 -0300

    Merge branch 'main' of https://github.com/johanngomig/Dio-Bootcamp-EngDados

commit afb5e3556aee87aee4fa71ef3c63b64460a009df
Author: johanngomig <johanngomig@gmail.com>
Date:   Wed Aug 28 17:42:52 2024 -0300

    atualização README.md

commit 8e2d790ba37901ec0c3f5f7d838d569e73f2be2a
Author: Johann leonhard loureiro gomig <32076028+johanngomig@users.noreply.github.com>
Date:   Wed Aug 28 17:41:09 2024 -0300


TioViking@DESKTOP-9VQ2JFJ MINGW64 /f/Bootcamp-DIO-EngDados/Dio-Bootcamp-EngDados/dio-git-e-github/trabalhando-com-branches (main)
$ git push
Enumerating objects: 18, done.
Counting objects: 100% (18/18), done.
Delta compression using up to 16 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 958 bytes | 958.00 KiB/s, done.
Total 10 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/johanngomig/Dio-Bootcamp-EngDados.git
   806bd0e..a1ffdfa  main -> main
