import argparse
import json
from pathlib import Path

import fitz

from .annotation import Annotation


def attact_annotation(annot: Annotation, doc: fitz.Document):
    page: fitz.Page = doc.loadPage(annot.pageNum)
    atype = annot.annotType[0]
    ann_new = None
    if atype == fitz.ANNOT_FREETEXT:
        ann_new = page.addFreetextAnnot(annot.rect, annot.info['content'])
    elif atype == fitz.ANNOT_TEXT:
        ann_new = page.addTextAnnot(annot.point, annot.info['content'])
    elif atype == fitz.ANNOT_HIGHLIGHT:
        ann_new = page.addHighlightAnnot(annot.quads)
    elif atype == fitz.ANNOT_STRIKEOUT:
        ann_new = page.addStrikeOUTAnnot(annot.quads)
    elif atype == fitz.ANNOT_SQUIGGLY:
        ann_new = page.addSquigglyAnnot(annot.quads)
    elif atype == fitz.ANNOT_UNDERLINE:
        ann_new = page.addUnderlineAnnot(annot.quads)
    else:
        print(
            f'Annotation type {annot.annotType} is not supported. Ignore: {annot}')

    if ann_new:
        ann_new: fitz.Annot
        ann_new.setInfo(annot.info)
        ann_new.setColors(annot.colors)
        ann_new.setBorder(annot.border)
        if annot.lineEnds:
            ann_new.setLineEnds(*annot.lineEnds)
        ann_new.setOpacity(annot.opacity)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--pdf', required=True)
    parser.add_argument('-a', '--annots', nargs="+",
                        help='annotation jsons, one annotation per line')
    parser.add_argument('--prune', action='store_true',
                        help='prune old annotations from pdf')
    args = parser.parse_args()

    doc: fitz.Document = fitz.open(args.pdf)
    if args.prune:
        for page in doc:
            page: fitz.Page
            for annot in page.annots:
                page.deleteAnnot(annot)

    for filename in args.annots:
        with open(filename) as f:
            for line in f:
                js = json.loads(line)
                annot = Annotation(**js)
                attact_annotation(annot, doc)

    path_pdf = Path(args.pdf)
    path_out = path_pdf.with_name(f"{path_pdf.stem} - annotated.pdf")
    doc.save(path_out.as_posix())


if __name__ == "__main__":
    main()
