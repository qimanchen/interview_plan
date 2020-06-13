set nocompatible
set history=100
filetype on
filetype plugin on
filetype indent on
set autoread
set mouse=a
syntax enable
set cursorline
hi cursorline guibg=#00ff00
hi CursorColumn guibg=#00ff00
set nofen
set fdl=0
set expandtab
set tabstop=4
set shiftwidth=4
set softtabstop=4
set smarttab
set ai
set si
set wrap
set sw=4
set wildmenu
set ruler
set cmdheight=1
set lz
set backspace=eol,start,indent
set whichwrap+=<,>,h,l
set magic
set noerrorbells
set novisualbell
set showmatch
set mat=2
set hlsearch
set ignorecase
set encoding=utf-8
set fileencodings=utf-8
set termencoding=utf-8
set smartindent
set cin
set showmatch
set guioptions-=T
set guioptions-=m
set vb t_vb=
set laststatus=2
set pastetoggle=<F9>
set background=dark
highlight Search ctermbg=black  ctermfg=white guifg=white guibg=black
autocmd BufNewFile *.py,*.cc,*.sh,*.java exec ":call SetTitle()"
func SetTitle()
    if expand("%:e") == 'sh'
        call setline(1, "#!/bin/bash")
        call setline(2, "#Author:chen qiman")
        call setline(3, "#Mail:1033178199@qq.com")
        call setline(4, "#Time:".strftime("%F %T"))
        call setline(5, "#Name:".expand("%"))
        call setline(6, "#Version:V1.0")
        call setline(7, "#Description:This is a test script.")
    endif
    if expand("%:e") == 'py'
        call setline(1, "#!/usr/bin/env python3")
        call setline(2, "#-*- coding: utf-8 -*-")
        call setline(3, "#Author:chen qiman")
        call setline(4, "#Mail:1033178199@qq.com")
        call setline(5, "#Time:".strftime("%F %T"))
        call setline(6, "#Name:".expand("%"))
        call setline(7, "#Version:V1.0")
        call setline(8, "#Description:This is a test script.")
    endif
endfunc
