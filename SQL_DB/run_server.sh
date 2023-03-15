#!/bin/zsh

brew update

isPackageNotInstalled() {
if brew ls --versions postgresql@14 > /dev/null; then
  echo The package is installed

else
  brew install postgresql@14
fi
}

isPackageNotInstalled

