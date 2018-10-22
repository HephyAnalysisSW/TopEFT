#!/bin/bash

for x in `ls crab_dim6top*/* -d`;
do
    crab status $x;
done
