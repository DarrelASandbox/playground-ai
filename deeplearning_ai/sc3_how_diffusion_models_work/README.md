- [About The Project](#about-the-project)
- [Introduction](#introduction)
- [Intuition](#intuition)
  - [Goal](#goal)
  - [Making images useful to a neural network](#making-images-useful-to-a-neural-network)
  - [Training a neural network to make sprites](#training-a-neural-network-to-make-sprites)
- [Sampling](#sampling)

&nbsp;

# About The Project

- [DeepLearning.AI Short Courses](https://learn.deeplearning.ai/)
- How Diffusion Models Work
- Sharon Zhou

&nbsp;

# Introduction

- Midjourney, Stable Diffusion, DALL-E, and others can generate images, sometimes beautiful ones, given only a prompt.
- Diffusion models are becoming a foundation for cutting-edge research in life sciences and other sectors as well. For example, they are used in generating molecules for drug discovery. So, when you understand the technical details of diffusion models, you'll be in a better position to understand and perhaps apply these models yourself.

&nbsp;

# Intuition

## Goal

- You have a lot of sprite images
- You want even more sprite images
- You can use a neural network that generates more sprites for you

## Making images useful to a neural network

- You want a neural network to learn what a sprite is:
  - Fine details
  - General outlines
  - Everything in between
- One way is to add different noise levels to the training data of sprites
  - noising process
  - inspired by diffusion in physics

![add_noise](diagrams/add_noise.png)

- What should the neural network be thinking at each level of noise?
  - If it's Bob the sprite -> Keep Bob as is
  - If it's likely to be Bob -> Suggest possible details to be filled in
  - If it's just an outline of a sprite -> Suggest general details for likely sprites
  - If it looks like nothing -> Suggest an outline of sprite

## Training a neural network to make sprites

- The neural network learns to take different noisy images and turn them back into sprites.
- It learns to remove the noise you added.

![no_idea_level_of_noise](diagrams/no_idea_level_of_noise.png)

- The "No Idea" level of noise is important because it is **normally distributed**.
- So, when you ask the neural network for a new sprite:
  - You can sample noise from the normal distribution
  - Get a completely new sprite by using the net to remove the noise
- Now, you can get even more sprites, beyond your training data

&nbsp;

# Sampling

- NN tries to fully predict the noise at each step. Realistically, it's just a prediction. You need multiple steps to get high quality sprites.

![sampling](diagrams/sampling.png)

![sample](diagrams/sample.png)

```py
# sample using standard DDPM algorithm
# Denoising Diffusion Probabilistic Models
@torch.no_grad()
def sample_ddpm(n_sample, device, save_rate=20):
  # x_T ~ N(0, 1), sample initial noise
  samples = torch.randn(n_sample, 3, height, height).to(device)
  # ...
  for i in range(timesteps, 0, -1):
    # reshape time tensor
    t = torch.tensor([i/timesteps])[:, None, None, None].to(device)

    # sample some random noise to inject back in. For i = 1, don't add back in noise
    z = torch.randn_like(samples) if i > 1 else 0

    eps = nn_model(samples, t) # predict noise e_(x_t,t)
    samples = denoise_add_noise(samples, i, eps, z)
    # ...

  return samples
```

![sampling_iteration_details](diagrams/sampling_iteration_details.png)

- The NN expects a noisy sample as input.
- You can add in additional noise before it gets passed to the next step.
- Empirically, this stabilizes the NN so it doesn't collapse to something closer to the average of the dataset.

![sample_and_noise](diagrams/sample_and_noise.png)

&nbsp;
