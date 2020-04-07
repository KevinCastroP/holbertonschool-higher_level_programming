#!/bin/bash
# Displaying the size of the bofy of the response
curl -s "$1" | wc -c
