#!/bin/bash

function create(){
  cd
  python mycode.py $1
  cd C:/Users/ksr20/PycharmProjects/$1
  git init
  git remote add origin https://github.com/YOUR_GITHUB_USERNAME/$1.git
  touch README.md
  git add .
  git commit -m "Initial commit"
  git push -u origin master
}
