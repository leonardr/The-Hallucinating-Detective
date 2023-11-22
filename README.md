The Hallucinating Detective
===========================

**by [Leonard Richardson](https://www.crummy.com/)  
[NaNoGenMo 2023](https://www.crummy.com/writing/NaNoGenMo/2023/)**

Introduction
------------

One of the most annoying issues with large language models when used seriously--their tendency to confabulate and confidently spout nonsense--becomes a hilarious feature when used for comedic effect. For my 2023 NaNoGenMo project I wanted to create an interplay between two pieces of software: a text generator (written by me) that could reliably induce humorous hallucinations in an LLM (trained on terabytes of human-written text).

My goal was, simply, to invoke the ELIZA effect in an LLM. Models trained on human-written text implicitly assume their input was also human-written. By feeding them automatically generated text instead, I thought I could make them infer connections where none existed.

I simulated a small world full of characters who are always looking at or showing off their posessions. These characters speak in quotes from the same Project Gutenberg texts used, in part, to train LLMs. This simulationist approach is common in NaNoGenMo entries: the text is random and meaningless, but the juxtapositions look like they _ought_ to be meaningful. Humans fall for it, so LLMs, trained on human writings, ought to react similarly.

Unfortunately, today's LLMs are trained to be annoyingly up-front and aggressive about their own limitations. The ones I tried declined to speculate about the meaning of their statistically unlikely input; or else their speculations were wishy-washy to the point of meaninglessness, or at least unfunniness.

So I changed the prompt to goad the LLM into taking action, by casting it as an authority figure in a dangerous and adversarial world. In _The Hallucinating Detective_, the language model is the detective in a murder mystery. The people became suspects or dead bodies; the posessions became clues. The simulated world becomes a text adventure that ignores all player input and keeps moving towards a conclusion, or at least an ending.

Some language models kept their distance from the role of detective, others embraced it, but most of them at least tried to solve the unsolvable mystery.

Table of Contents
-----------------

These twenty-four detective stories, created by a variety of models, are hosted at my personal site.

1.  [_The Mystery of the Foolish Door_](https://www.crummy.com/writing/NaNoGenMo/2023/#foolish-door)  
    starring Roko as "Sleuth Seraphina"
2.  [_The Encrusted Handful Of Change Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#encrusted-handful-of-change)  
    starring gpt4all-falcon-q4\_0
3.  [_The Adventure of the Smothered Egg Beater_](https://www.crummy.com/writing/NaNoGenMo/2023/#smothered-egg-beater)  
    starring replit-code-v1\_5-3b-q4\_0
4.  [_The Adventure of the Workable Scotch Tape_](https://www.crummy.com/writing/NaNoGenMo/2023/#workable-scotch-tape)  
    starring gpt4all-13b-snoozy-q4\_0
5.  [_The Mystery of the Footy Box Of Chocolates_](https://www.crummy.com/writing/NaNoGenMo/2023/#footy-box-of-chocolates)  
    starring nous-hermes-llama2-13b
6.  [_The Adventure of the Healthier Blowdryer_](https://www.crummy.com/writing/NaNoGenMo/2023/#healthier-blowdryer)  
    starring em\_german\_mistral\_v01
7.  [_The Case of the Registering Coffee Pot_](https://www.crummy.com/writing/NaNoGenMo/2023/#registering-coffee-pot)  
    starring rift-coder-v0-7b-q4\_0
8.  [_The Revelatory Tube Of Lip Balm Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#revelatory-tube-of-lip-balm)  
    starring mistral-7b-instruct-v0
9.  [_The Repellent Chocolate Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#repellent-chocolate)  
    starring starcoder-q4\_0
10.  [_The Adventure of the Skeleton Roll Of Gauze_](https://www.crummy.com/writing/NaNoGenMo/2023/#skeleton-roll-of-gauze)  
    starring mistral-7b-openorca
11.  [_The Case of the Uninspired Light_](https://www.crummy.com/writing/NaNoGenMo/2023/#uninspired-light)  
    starring Roko as "The Insightful Enigma"
12.  [_Sherlock Holmes and The Draining Pen Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#draining-pen)  
    starring em\_german\_mistral\_v01
13.  [_The Case of the Prodigious Straw_](https://www.crummy.com/writing/NaNoGenMo/2023/#prodigious-straw)  
    starring wizardlm-13b-v1
14.  [_The Adventure of the Humiliating Zipper_](https://www.crummy.com/writing/NaNoGenMo/2023/#humiliating-zipper)  
    starring rift-coder-v0-7b-q4\_0
15.  [_The Automatic Pants Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#automatic-pants)  
    starring gpt4all-falcon-q4\_0
16.  [_The Case of the Forehand Wedding Ring_](https://www.crummy.com/writing/NaNoGenMo/2023/#forehand-wedding-ring)  
    starring replit-code-v1\_5-3b-q4\_0
17.  [_The Adventure of the Flexible Sword_](https://www.crummy.com/writing/NaNoGenMo/2023/#flexible-sword)  
    starring wizardlm-13b-v1
18.  [_The Case of the Broadest Screw_](https://www.crummy.com/writing/NaNoGenMo/2023/#broadest-screw)  
    starring mistral-7b-openorca
19.  [_The Case of the Neutered Keyboard_](https://www.crummy.com/writing/NaNoGenMo/2023/#neutered-keyboard)  
    starring wizardlm-13b-v1
20.  [_The Case of the Priced Whale_](https://www.crummy.com/writing/NaNoGenMo/2023/#priced-whale)  
    starring nous-hermes-llama2-13b
21.  [_The Case of the Backstage Squirrel_](https://www.crummy.com/writing/NaNoGenMo/2023/#backstage-squirrel)  
    starring wizardlm-13b-v1
22.  [_The Adventure of the Rapid-Fire Squirrel_](https://www.crummy.com/writing/NaNoGenMo/2023/#rapid-fire-squirrel)  
    starring rift-coder-v0-7b-q4\_0
23.  [_The Subjugated Chain Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#subjugated-chain)  
    starring em\_german\_mistral\_v01
24.  [_The Swarthy Dog Affair_](https://www.crummy.com/writing/NaNoGenMo/2023/#swarthy-dog)  
    starring wizardlm-13b-v1

Tools used
----------

*   [Original source code.](https://github.com/leonardr/The-Hallucinating-Detective)
*   The [GPT4All](https://gpt4all.io/index.html) collection of models.
*   The Roko chatbot from the Random Number Venerators Discord server.
*   The [llm](https://llm.datasette.io/en/stable/) and [llm-gpt4all](https://github.com/simonw/llm-gpt4all/) Python libraries.
*   My own [olipy](https://github.com/leonardr/olipy/) library, including the data aggregated from Darius Kazemi's [corpora](https://github.com/dariusk/corpora/)
*   My ol' reliable, the [Project Gutenberg 10K DVD](https://archive.org/details/pgdvd042010).