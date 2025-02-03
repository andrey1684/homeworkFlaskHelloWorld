#!/usr/bin/env just --justfile

import 'just/homework.just'
import 'just/environment.just'
import 'just/other.just'
###
# List of all commands
[private]
@list:
    just --list --justfile {{ justfile() }}

hello:
  echo "hello world"