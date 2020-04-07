#!/bin/bash
# Sending a POST request and setting email and subject
curl -s -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -X POST "$1"
