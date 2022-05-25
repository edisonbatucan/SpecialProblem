# Special Problem (Repo for our special problem 1 and 2)

## Dataset
<b>From SPIE-AAPM-NCI PROSTATEx Challenges (PROSTATEx)</b>
* https://wiki.cancerimagingarchive.net/pages/viewpage.action?pageId=23691656

## Data Preparation
<b>dicom to tiff conversion</b>
```
pip install dicom2jpg
```
```
dicom_path = '../dicom'
output_path = '../out_dicom'
dicom2jpg.dicom2tiff(dicom_path, target_root=output_path, anonymous=False, multiprocessing=True)
```
<b>Read Data</b>
<p align="center">
  <img src="./SHOWING/data.gif" width="350">
</p>
## Pre-processing

<b>Run dataprep.py</b>

<b> Prostate : </b> <i>Read -> Resize -> Histogram Equalization</i>
<p align="center">
  <img src="./SHOWING/prostate.gif" width="350">
</p>
<b> Mask : </b> <i>Read -> Resize and Grayscale</i>
<p align="center">
  <img src="./SHOWING/mask.gif" width="350">
</p>
## Model Accuracy and Loss
<p align="center">
  <img src="./SHOWING/accuracy.png" width="350" title="hover text">
  <img src="./SHOWING/loss.png" width="350">
</p>

## References

* https://pyimagesearch.com/2022/02/21/u-net-image-segmentation-in-keras/
* https://github.com/jocicmarko/ultrasound-nerve-segmentation.git
* https://towardsdatascience.com/metrics-to-evaluate-your-semantic-segmentation-model-6bcb99639aa2#
