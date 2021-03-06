# --------------------------------------------------------
# Fast R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""Factory method for easily getting imdbs by name."""

__sets = {}

from datasets.pascal_voc import pascal_voc
from datasets.coco import coco
from datasets.car_ds import car_ds
from datasets.vehicles import vehicles
import numpy as np

# Set up vehicles dataset version 3 <split>
for split in ['train', 'val', 'test']:
    name = 'vehicles_dataset_v3_{}'.format(split)
    __sets[name] = (lambda split=split: vehicles(split, 3))

# Set up vehicles dataset version 2 <split>
for split in ['train', 'val', 'test']:
    name = 'vehicles_dataset_v2_{}'.format(split)
    __sets[name] = (lambda split=split: vehicles(split, 2))

# Set up cars_<split>
for split in ['train', 'val', 'test', 'trainvaltest']:
    name = 'cars_{}'.format(split)
    __sets[name] = (lambda split=split: car_ds(split))

# Set up voc_<year>_<split> using selective search "fast" mode
for year in ['2007', '2012']:
    for split in ['train', 'val', 'trainval', 'test']:
        name = 'voc_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: pascal_voc(split, year))

# Set up coco_2014_<split>
for year in ['2014']:
    for split in ['train', 'val', 'minival', 'valminusminival']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

# Set up coco_2015_<split>
for year in ['2015']:
    for split in ['test', 'test-dev']:
        name = 'coco_{}_{}'.format(year, split)
        __sets[name] = (lambda split=split, year=year: coco(split, year))

def get_imdb(name):
    """Get an imdb (image database) by name."""
    if not __sets.has_key(name):
        raise KeyError('Unknown dataset: {}'.format(name))
    return __sets[name]()

def list_imdbs():
    """List all registered imdbs."""
    return __sets.keys()
