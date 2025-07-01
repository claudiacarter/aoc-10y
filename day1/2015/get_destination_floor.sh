#!/usr/bin/env bash

input_file="$1"

num_open_bracket=$(grep -o "(" "$input_file" | wc -l)
num_close_bracket=$(grep -o ")" "$input_file" | wc -l)

target_floor=$((num_open_bracket - num_close_bracket))

echo "$target_floor"
