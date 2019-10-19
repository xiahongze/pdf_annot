import argparse
import json
from pathlib import Path

import fitz

from .annotation import Annotation, TEXTUAL_ANNOTS


def extract_annotations(doc: fitz.Document):
    for i, page in enumerate(doc):
        page: fitz.Page
        for annot in page.annots(types=TEXTUAL_ANNOTS):
            annot: fitz.Annot
            rect = annot.rect
            yield Annotation(colors=annot.colors, info=annot.info, pageNum=i,
                             annotType=annot.type, vertices=annot.vertices,
                             border=annot.border, lineEnds=annot.lineEnds, opacity=annot.opacity,
                             topLeft=(rect.top_left.x, rect.top_left.y),
                             botRight=(rect.bottom_right.x, rect.bottom_right.y))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pdf', required=True)
    args = parser.parse_args()

    output = Path(args.pdf).with_suffix(".json")
    with output.open('w') as f:
        for annot in extract_annotations(fitz.open(args.pdf)):
            json.dump(annot.to_dict(), f)
            f.write('\n')


if __name__ == "__main__":
    main()
