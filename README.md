# upwork-numpy

The CSV pipeline is as follows.

```shell
# Make sure you run all cells first
# The CSV pipeline needs the outputs for content
cat numpy-numpy.ipynb | python main.py > out.csv
```

The JSON pipeline is as follows.

```bash
cat out.csv | python make_json_from_csv.py > out.json
```

And the desired notebook pipeline is as follows.

```shell
# Make sure you clear all the cell output first
# The desired nb pipeline does not need cell output, and cannot handle it when there is output
cat numpy-numpy.ipynb | python convert.py > desired_nb.ipynb
```
