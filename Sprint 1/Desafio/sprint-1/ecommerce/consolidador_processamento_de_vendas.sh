#!/bin/bash

# Criando ou limpando o arquivo de relatório final
> vendas/backup/relatorio-final.txt

# Consolidando relatórios em um único arquivo
for relatorio in vendas/backup/relatorios-*.txt; do
    echo "Relatório: $relatorio" >> vendas/backup/relatorio-final.txt
    echo "" >> vendas/backup/relatorio-final.txt
    cat "$relatorio" >> vendas/backup/relatorio-final.txt
    echo "" >> vendas/backup/relatorio-final.txt
    echo "-----------------------------------------------" >> vendas/backup/relatorio-final.txt
    echo "" >> vendas/backup/relatorio-final.txt
done
