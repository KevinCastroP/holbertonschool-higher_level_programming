#!/bin/bash
# Showing all the methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
