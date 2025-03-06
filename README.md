<h1>Slow Learner with Incremental Transfer Learning</h1>

<h2>Description</h2>


This project consists of a simple approach to incorporating external datasets into pre-trained models. The approach was adapted from the continual learning approach by [Zhang et al.](https://arxiv.org/abs/2303.05118) In this adaptation, the use of transfer learning bypasses the need for classifier alignment due to the re-initialization of the classification head. The model backbone uses the Patchout faSt Spectrogram Transformer ([PaSST](https://arxiv.org/abs/2110.05069)) model pre-trained with AudioSet.
<br/>

The external dataset used is the [CochlScene](https://arxiv.org/abs/2211.02289) dataset, an acoustic scene classification dataset obtained via crowdsourcing in South Korea. The final task dataset is the TAU 2022 urban acoustic scenes mobile development dataset, which has been a mainstay in the DCASE Task 1 challenges since 2022.


<br />


<h2>Languages and Utilities Used</h2>

The important packages and libraries required for reproducing this experiment are:

- <b>Python = 3.7.9 </b> 
- <b>Pytorch = 1.13.1+cu117 </b>

For exact requirements, see [here](https://github.com/fschmid56/cpjku_dcase23).

<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Datasets Used</h2>

- <b>TAU 2022 Urban Acoustic Scenes Mobile Development</b> 
- <b>CochlScene</b>

<h2>Getting Started:</h2>


Follow the setup instructions for the PaSST models found [here](https://github.com/fschmid56/cpjku_dcase23).

Prepare the Datasets: <br/>

1. Download the CochlScene dataset [here](https://github.com/cochlearai/cochlscene).
2. Extract the files to your dataset path
3. Run the [filename cleaner](utils/rename_csfiles.py)

Prepare the resource and metadata files: <br/>

1. Create a separate instance of [dcase23.py](datasets/dcase23.py) for use on the CS dataset.
2. Generate the meta and training split csv for the CS dataset using [create_meta.py](utils/create_meta.py).
3. Adjust the paths for the TAU and CS meta files accordingly
4. Configure the get_training_set function show below to take the CS training split.

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

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
