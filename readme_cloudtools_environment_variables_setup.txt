В USER (не SYSTEM) environment variables надо добавить:

CT=%USERPROFILE%\CloudTools (или куда скачан репозиторий)
PATH=%CT%\TOOLS

Чтобы появилось меню в Far (по F2), надо пойти в Far Manager\Profile и скопировать файл
FarMenu.ini.sample в файл FarMenu.ini. Так сделано потому, что файл FarMenu.ini больше не находится
под контролем Git-а.
