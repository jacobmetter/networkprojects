name: Python Package using Conda

on: [push]

jobs:
  build-linux:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 5

    steps:
    1) first I do this
    2) then I do this
    3) next this
    
