#!/bin/sh

mkdir $HOME/pipes/

mkfifo $HOME/pipes/pipereader
mkfifo $HOME/pipes/mpipereader
