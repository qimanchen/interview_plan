BEGIN{
    printf("|%-8s|\t|%5s|\n","FILE","BYTES")
}
NF==9 &&/^-/{
        sum+=$5
        filenum++
        printf("|%-8s|\t|%5d|\n",$9,$5)
}
NF==9&&/^d/{
    printf("|%-8s|\t|%5s|\n",$9,"<dir>")
}
END{
    printf("Total: %d bytes(%d files)\n",sum,filenum)
}

