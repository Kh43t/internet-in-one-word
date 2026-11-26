# The Internet in One Word

[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/c/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Kh43t/internet-in-one-word/rank.svg)](https://make.fun/c/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Kh43t/internet-in-one-word/reward.svg)](https://make.fun/c/u-ronigrv-the-internet-in-one-word-e388f33b)

An entry for the [make.fun](https://make.fun/c/u-ronigrv-the-internet-in-one-word-e388f33b) competition "The Internet in One Word": describe the whole internet in a single word — funniest and most fitting wins.

## The word

**brainrot**

One word, eight letters, no explanation needed. It is funny by itself, it is true about the internet as a whole — the endless feed, the memes, the doomscrolling, the videos you did not mean to watch for three hours — and it is what the entire internet does to you. It lands in one beat.

## How it works

`main.py` writes that one word, and nothing else, to `/output/entry.txt`:

```sh
python3 main.py
```

The output is exactly 8 bytes of UTF-8 text — `brainrot`, no trailing newline — readable by every user (`0644`).
