#!/bin/bash

if  [[ $# -eq 0 ]]; 
then 
    echo "please provide commit message"
    exit 1
else
    git checkout memstrong
    git add -A
    git commit -m "$1"
    git checkout master
    git pull origin --rebase master
    git checkout memstrong
    git pull origin --rebase master
    git push origin memstrong
    exit 0
fi