#!/usr/bin/env bash

python3 -m venv venv
source venv/bin/activate

az webapp up -n flaskpt2

az webapp log tail
