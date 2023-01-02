# Copyright (c) OpenMMLab. All rights reserved.
from argparse import ArgumentParser

import mmcv

import mmcv_custom   # noqa: F401,F403
import mmseg_custom   # noqa: F401,F403
from mmseg.apis import inference_segmentor, init_segmentor, show_result_pyplot
from mmseg.core.evaluation import get_palette
from mmcv.runner import load_checkpoint
from mmseg.core import get_classes
import cv2
import numpy as np
import os.path as osp
import os


def main():
    parser = ArgumentParser()
    parser.add_argument('config', help='Config file')
    parser.add_argument('checkpoint', help='Checkpoint file')
    parser.add_argument('--scans_dir', help='directory containing scans')
    parser.add_argument('--color_dirname', help='name of image directory')
    parser.add_argument('--skip_freq', help='frame sampling frequence')
    parser.add_argument(
        '--device', default='cuda:0', help='Device used for inference')
    args = parser.parse_args()

    # build the model from a config file and a checkpoint file
    
    model = init_segmentor(args.config, checkpoint=None, device=args.device)
    checkpoint = load_checkpoint(model, args.checkpoint, map_location='cpu')
    if 'CLASSES' in checkpoint.get('meta', {}):
        model.CLASSES = checkpoint['meta']['CLASSES']
    else:
        model.CLASSES = get_classes(args.palette)
        
    # inference on all scans
    for scan_id in os.listdir(args.scans_dir):
        img_dir = osp.join(args.scans_dir, scan_id, args.color_dirname)
        for img_id in os.listdir(img_dir):
            
            if not int(img_id.split(".")[0]) % int(args.skip_freq) == 0:
                continue
        
            img_path = osp.join(img_dir, img_id)
            result = inference_segmentor(model, img_path)
            result = result[0] + 1   # add 1 to labels such that 0 == ignored

            # save the results
            mask_dir = osp.join(args.scans_dir, scan_id, 'ViT_masks')
            mmcv.mkdir_or_exist(mask_dir)
            out_path = osp.join(mask_dir, img_id)
            cv2.imwrite(out_path, result)
            print(f"Result is save at {out_path}")


if __name__ == '__main__':
    main()