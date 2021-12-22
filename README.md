# upwork-numpy

The CSV pipeline is as follows.

```shell
cat numpy-numpy.ipynb | main.py > out.csv
```

The JSON pipeline is as follows.

```bash
cat out.csv | make_json_from_csv.py > out.json
```

And the desired notebook pipeline is as follows

```shell
cat numpy-numpy.ipynb | convert.py > desired_nb.ipynb
```
