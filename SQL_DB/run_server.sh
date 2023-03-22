#!/bin/zsh

brew update

isPackageNotInstalled() {
if brew ls --versions postgresql@14 > /dev/null; then
  echo "$1 is installed"

else
  brew install postgresql@14
fi
}

isPackageNotInstalled postgresql@14

pg_ctl -D /Users/wojciechflak/Library/Application\ Support/Postgres/var-15/ start

