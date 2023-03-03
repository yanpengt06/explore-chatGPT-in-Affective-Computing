# Explore ChatGPT in Affective Computing
## Introduction
We want to test the capacity of ChatGPT on Affective Computing
This repository contains the result of Dialogue Act Classification(DAC) for now
## Result for DAC

| Model                                                        | Acc  | weighted-F1 |
| ------------------------------------------------------------ | :--: | :---------: |
| [Co-GAT](https://ojs.aaai.org/index.php/AAAI/article/view/17616) |  -   |  **79.4**   |
| ChatGPT, oneshot                                             | 0.67 |    0.65     |
| ChatGPT, oneshot+prompt-engineering                          | 0.71 |    0.70     |
| ChatGPT, fewshot                                             | 0.73 |    0.72     |
| ChatGPT, fewshot+prompt-engineering                          | 0.74 |    0.73     |

## Project Structure

- cal_prf.py

  `input`: two label files which are chatGPT prediction and golden answer file

  `output`: the classification report using sklearn

-  check_utts

​		`input`: output file of chatGPT and golden answer file

​		`output`: the indexes of dialogue which are obviously wrongly annotated. 

- dd_label_extract.py: extract the labels from output file of chatGPT into a label file.
- dd-dialogue-act.py: sample 64 dialogs in daily dialogue and transform the data format.

- main.py: use ReverseChatGPT API to use chatGPT
