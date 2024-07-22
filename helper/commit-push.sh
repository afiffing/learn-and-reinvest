#!/bin/bash

if  [[ $# -eq 0 ]]; 
then 
    echo "please provide commit message"
    exit 1
else
    git checkout memstrong
    git add -A
    git commit -m "$1"
    git pull origin --rebase memstrong
    git checkout master
    git pull origin --rebase master
    git checkout memstrong
    git pull origin --rebase master
    git push origin memstrong -f
    exit 0
fi