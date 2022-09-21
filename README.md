# Leetcode Challenge Generator
- [Leetcode Challenge Generator](#leetcode-challenge-generator)
  - [Introduction](#introduction)
  - [How it Works](#how-it-works)
  - [Upcoming](#upcoming)
  - [How to run](#how-to-run)
    - [Dependencies](#dependencies)
## Introduction
This python script uses selenium and the Microsoft Edge webdriver to scare the [Leetcode](https://leetcode.com/problems) for the first 5 challenges. 

## How it Works
- Get the top 5 challenges, their title and the link
- Go to the challenge page and take a screenshot of the challenge decription

## Upcoming
- get input from the user to select what level of problems to generate
[x] Upload the images to a CDN (cloudinary?)
[x] Send the challenges to a slack channel

## How to run
### Dependencies
- Microsoft Edge - [Download Here](https://www.microsoft.com/en-us/edge)
- Microsoft Edge Webdriver - [Download Here](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
```sh
# clone the repo into a virtual environment
# activate the virtual environment
> pip install -r requirements.txt

> python3 findChallenge.py
```