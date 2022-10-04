# Copyright (c) Facebook, Inc. and its affiliates.
from detic.modeling.meta_arch import custom_rcnn
from detic.modeling.roi_heads import detic_roi_heads
from detic.modeling.roi_heads import res5_roi_heads
from detic.modeling.backbone import swintransformer
from detic.modeling.backbone import timm


from detic.data.datasets import lvis_v1
from detic.data.datasets import imagenet
from detic.data.datasets import cc
from detic.data.datasets import objects365
from detic.data.datasets import oid
from detic.data.datasets import coco_zeroshot

try:
    from detic.modeling.meta_arch import d2_deformable_detr
except:
    pass