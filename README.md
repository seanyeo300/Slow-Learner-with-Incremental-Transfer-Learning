<h1>Slow Learner with Incremental Transfer Learning</h1>

<h2>Description</h2>


This project consists of a simple approach to incorporating external datasets into pre-trained models. The approach was adapted from the continual learning approach by [Zhang et al.](https://arxiv.org/abs/2303.05118) In this adaptation, the use of transfer learning bypasses the need for classifier alignment due to the re-initialization of the classification head. The model backbone uses the Patchout faSt Spectrogram Transformer ([PaSST](https://arxiv.org/abs/2110.05069)) model pre-trained with AudioSet.
<br/>

The external dataset used is the [CochlScene](https://arxiv.org/abs/2211.02289) dataset, an acoustic scene classification dataset obtained via crowdsourcing in South Korea. The final task dataset is the TAU 2022 urban acoustic scenes mobile development dataset, which has been a mainstay in the DCASE Task 1 challenges since 2022.


<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>Pytorch</b>

<h2>Environments Used </h2>

- <b>Windows 10</b> (21H2)

<h2>Datasets Used</h2>

- <b>TAU 2022 Urban Acoustic Scenes Mobile Development</b> 
- <b>CochlScene</b>

<h2>Getting Started:</h2>


Follow the setup instructions for the PaSST models found [here](https://github.com/fschmid56/cpjku_dcase23).



Prepare the Datasets: <br/>

1. Download the CochlScene dataset [here](https://github.com/cochlearai/cochlscene).
2. Extract the files to your dataset path
3. Run the [filename cleaner](utils/rename_csfiles.py)

Implememting SIT: <br/>
<img src="https://i.imgur.com/nCIbXbg.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Confirm your selection:  <br/>
<img src="https://i.imgur.com/cdFHBiU.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Wait for process to complete (may take some time):  <br/>
<img src="https://i.imgur.com/JL945Ga.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Sanitization complete:  <br/>
<img src="https://i.imgur.com/K71yaM2.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Observe the wiped disk:  <br/>
<img src="https://i.imgur.com/AeZkvFQ.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
</p>

<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
