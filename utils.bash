#!/bin/bash

function run {
    jupyter lite build --contents content --output-dir dist
    jupyter lite serve --output-dir dist
}
