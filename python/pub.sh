#!/bin/bash

rm -r dist
rm -r *.egg-info

python3 -m build
twine upload dist/*