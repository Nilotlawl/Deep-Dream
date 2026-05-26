Notes :-

- Creative images produced by a neural network..
- Image fed , the program identifies and enhances the patterns which it has learned , through a process called "inceptionism" - it is called that because it maximises the layer activation via gradient ascent on input pixels thus iteratively modifying the input image.
- Maximising the detection of features at various layers, 
- uses a inception_4c cnn , and uses the Caffe deep learnign framework and uses GoogleNET CNN arch model 

Image processing functions 

- preprocess(): It converts the 


TRYING SOMETHING DIFFERENT:-

Input Image → VAE Encode → Latent Space
                      ↓
          [Reverse Diffusion Loop]
                      ↓
   UNet Predicts Noise → Classifier-Free Guidance (CFG)
                      ↓
   Predict Clean Latent → VAE Decode → Pixel Image
                      ↓
   CLIP Vision Encoder + CLIP Text Encoder → Cosine Similarity Loss
                      ↓
   Gradient Backprop to Latents → Adjust Latents
                      ↓
   Scheduler Step → Next Denoising Step
                      ↓
              Final VAE Decode → Dream Image