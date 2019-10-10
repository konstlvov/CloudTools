" use `set filetype` to override default filetype=xml for *.ts files
autocmd BufNewFile,BufRead *.ts,*.tsx set filetype=typescript|
                               \ silent execute ":e ++enc=utf-8"
