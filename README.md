<h1>Slow Learner with Incremental Transfer Learning</h1>

<h2>Description</h2>


This repository consists of a simple approach to incorporating external datasets into pre-trained models. The approach was adapted from the continual learning approach by [Zhang et al.](https://arxiv.org/abs/2303.05118) [1]. In this adaptation, the use of transfer learning bypasses the need for classifier alignment due to the re-initialization of the classification head. The model backbone uses the Patchout faSt Spectrogram Transformer ([PaSST](https://arxiv.org/abs/2110.05069)) [2] model pre-trained with AudioSet [3].
<br/>

The external dataset used is the [CochlScene](https://arxiv.org/abs/2211.02289) [4] dataset, an acoustic scene classification dataset obtained via crowdsourcing in South Korea. The final task dataset is the TAU 2022 urban acoustic scenes mobile development dataset, which has been a mainstay in the DCASE Task 1 challenges since 2022.


<br />


<h2>Languages and Utilities Used</h2>

The important packages and libraries required for reproducing this experiment are:

- <b>Python = 3.7.9 </b> 
- <b>Pytorch = 1.13.1+cu117 </b>

For exact requirements, see [here](https://github.com/fschmid56/cpjku_dcase23).

<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Datasets Used</h2>

- <b>TAU 2022 Urban Acoustic Scenes Mobile Development [5] </b> 
- <b>CochlScene</b>
- <b>AudioSet</b>

<h2>Getting Started:</h2>


Follow the setup instructions for the PaSST models found [here](https://github.com/fschmid56/cpjku_dcase23).

Prepare the Datasets: <br/>

1. Download the CochlScene dataset [here](https://github.com/cochlearai/cochlscene).
2. Extract the files to your dataset path.
3. Run [rename_csfiles.py](utils/rename_csfiles.py) to generate the meta and training split csv for the CS dataset.

Prepare the resource and metadata files: <br/>

1. Create a separate instance of [dcase23.py](https://github.com/fschmid56/cpjku_dcase23/blob/main/datasets/dcase23.py) for use on the CS dataset.
2. Adjust the paths for the TAU and CS meta files accordingly.
3. Configure the get_training_set function show below to take the CS training split.

![Adjust training set retrieval function in run_passt_training.py.](https://github.com/seanyeo300/Slow-Learner-with-Incremental-Transfer-Learning/blob/main/images/configure_training_set.png)

Implememting SIT: <br/>
Adjust optimizer function in run_passt_training.py.<br />

![Adjust optimizer function in run_passt_training.py.](https://github.com/seanyeo300/Slow-Learner-with-Incremental-Transfer-Learning/blob/main/images/configure_optimizer.png)

<br />
<br />

Adjust the representation layer Learning Rate:  <br/>

For use with the CS dataset, setting 1e-4 for the representation layer yielded the best performance for our system configuration.

![Adjust learning rate arguments in run_passt_training.py.](https://github.com/seanyeo300/Slow-Learner-with-Incremental-Transfer-Learning/blob/main/images/configure_learning_rate.png)

<br />

Perform SIT training for CochlScene:  <br/>

- Set the default value of --subset to cochl
- Set the default value of --n_classes to 13
- Set the default value of --resample_rate to 44100
- Reduce batch size until the samples fit into GPU memory
- For windows users, set the default value of num_workers to 0

Peform SIT training for TAU:  <br/>

- Set the default value of --ckpt_id to the model trained with the CS dataset
- Set the default value of --subset between 5 to 100
- Set the default value of --n_classes to 10
- Set the default value of --resample_rate to 44100
- Set the default value of --batch_size to 256 or 128, depending on size of GPU memory
- For windows users, set the default value of num_workers to 0

Train a PaSST model with TAU only:  <br/>

- Set the default value of --ckpt_id to None
- Set the default value of --subset between 5 to 100
- Set the default value of --n_classes to 10
- Set the default value of --resample_rate to 44100
- Set the default value of --batch_size to 256 or 128, depending on size of GPU memory
- For windows users, set the default value of num_workers to 0

<h2>Comparing your results:</h2>

Compare the results of the SIT trained model and the one trained with standard fine-tuning. Seq-FT refers to a model trained using standard fine-tuning for the CS and TAU dataset. i.e. No SIT training.

<p align="center">
 <img src="https://github.com/seanyeo300/Slow-Learner-with-Incremental-Transfer-Learning/blob/main/images/result_comparison.png" height="50%" width="50%" alt="Table of Results"/>


<h2>References:</h2>

[1] Zhang, G., Wang, L., Kang, G., Chen, L., & Wei, Y. (2023). Slca: Slow learner with classifier alignment for continual learning on a pre-trained model. In Proceedings of the IEEE/CVF International Conference on Computer Vision (pp. 19148-19158).

[2] Koutini, K., Schlüter, J., Eghbal-Zadeh, H., & Widmer, G. (2021). Efficient training of audio transformers with patchout. arXiv preprint arXiv:2110.05069.

[3] Gemmeke, J. F., Ellis, D. P., Freedman, D., Jansen, A., Lawrence, W., Moore, R. C., ... & Ritter, M. (2017, March). Audio set: An ontology and human-labeled dataset for audio events. In 2017 IEEE international conference on acoustics, speech and signal processing (ICASSP) (pp. 776-780). IEEE.

[4] Jeong, I. Y., & Park, J. (2022, November). Cochlscene: Acquisition of acoustic scene data using crowdsourcing. In 2022 Asia-Pacific Signal and Information Processing Association Annual Summit and Conference (APSIPA ASC) (pp. 17-21). IEEE.

[5] T. Heittola, A. Mesarosand T. Virtanen, “TAU Urban Acoustic Scenes 2022 Mobile, Development dataset”. Zenodo, Mar. 08, 2022. doi: 10.5281/zenodo.6337421.






<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
