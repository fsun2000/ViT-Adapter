# from mmseg.datasets.builder import DATASETS
# from mmseg.datasets.custom import CustomDataset


# @DATASETS.register_module()
# class ScannetDataset(CustomDataset):
#     """ScannetDataset.

#     In segmentation map annotation for Potsdam dataset, 0 is the ignore index.
#     ``reduce_zero_label`` should be set to True. The ``img_suffix`` and
#     ``seg_map_suffix`` are both fixed to '.png'.
#     """
#     CLASSES = (
#         'ignored',
#         'wall',
#         'floor',
#         'cabinet',
#         'bed',
#         'chair',
#         'sofa',
#         'table',
#         'door',
#         'window',
#         'bookshelf',
#         'picture',
#         'counter',
#         'desk',
#         'curtain',
#         'refrigerator',
#         'shower curtain',
#         'toilet',
#         'sink',
#         'bathtub',
#         'otherfurniture',
#    )

#     PALETTE = [
#         [0, 0, 0],
#         [174, 199, 232],
#         [152, 223, 138],
#         [31, 119, 180],
#         [255, 187, 120],
#         [188, 189, 34],
#         [140, 86, 75],
#         [255, 152, 150],
#         [214, 39, 40],
#         [197, 176, 213],
#         [148, 103, 189],
#         [196, 156, 148],
#         [23, 190, 207],
#         [247, 182, 210],
#         [219, 219, 141],
#         [255, 127, 14],
#         [158, 218, 229],
#         [44, 160, 44],
#         [112, 128, 144],
#         [227, 119, 194],
#         [82, 84, 163]
#     ]

#     def __init__(self, **kwargs):
#         super(ScannetDataset, self).__init__(
#             img_suffix='.png',
#             seg_map_suffix='.png',
#             reduce_zero_label=True,
#             **kwargs)