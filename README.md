pdf_annot
=========

Utilities to extract and merge PDF annotations

## Installation

```bash
python setup.py install # or pip install pdf_annot
```

## Usage

### extract annotations from PDF and save as JSON

```shell
python -m pdf_annot.extract --pdf "path/to/pdf"
```

### cmd usage
```
python -m pdf_annot.extract -h
usage: extract annotations from PDF and save as JSON in the same folder
       [-h] -p PDF

optional arguments:
  -h, --help         show this help message and exit
  -p PDF, --pdf PDF
```

### attach JSON annotations to an exsiting PDF

```shell
python -m pdf_annot.attach -p "path/to/pdf" -a "path/to/first/annot/json" ["path/to/second/annot/json"] ...
```

### cmd usage

```
python -m pdf_annot.attach -h
usage: attach JSON annotations to a PDF and save a new PDF in the same folder (with '- annotated' appended)
       [-h] -p PDF [-a ANNOTS [ANNOTS ...]] [--prune]

optional arguments:
  -h, --help            show this help message and exit
  -p PDF, --pdf PDF
  -a ANNOTS [ANNOTS ...], --annots ANNOTS [ANNOTS ...]
                        annotation jsons, one annotation per line
  --prune               prune old annotations from the pdf
```

## Notes

At the moment, only textual kind of annotations are supported. For more information, please view `annotation.py`.