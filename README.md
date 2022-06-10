# 🏪 gilded rose 🌹

- [🏪 gilded rose 🌹](#-gilded-rose-)
  - [🤔 Problem Description](#-problem-description)
  - [📖 Manual](#-manual)
  - [🎯 Objectives](#-objectives)
    - [1️⃣ - Code review](#1️⃣---code-review)
    - [2️⃣ - Implementation](#2️⃣---implementation)

## 🤔 Problem Description

Hi and welcome to team Gilded Rose !

🏪 As you know, we are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison.

🛍 We also buy and sell only the finest goods.

![the gilded rose inn](https://static.wikia.nocookie.net/wowwiki/images/8/8b/The_Gilded_Rose.jpg/revision/latest/scale-to-width-down/400)

🙁 Unfortunately, our goods are constantly degrading in quality as they approach their sell by date.
⚙️ We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures.

Your task is to add the new feature to our system **so that we can begin selling a new category of items**.

First an introduction to our system:

- 📆 All items have a `SellIn` value which denotes the number of days we have to sell the item,
- 🏷 All items have a `Quality` value which denotes how valuable the item is,
- 📉 At the end of each day our system lowers both values for every item.

Pretty simple, right ? Well this is where it gets interesting:

- 📉📉 Once the sell by date has passed, `Quality` degrades twice as fast
- ➖ The `Quality` of an item is never negative
- 📈 "Aged Brie" actually increases in `Quality` the older it gets
- 🚧 The `Quality` of an item is never more than 50
- 💫 "Sulfuras", being a legendary item, never has to be sold or decreases in `Quality`
- ⚙️ "Backstage passes", like aged brie, increases in `Quality` as it’s SellIn value approaches; `Quality` increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but `Quality` drops to 0 after the concert.

## 📖 Manual

- 🐍 You can run the unit tests with `python -m unittest test_gilded_rose.py` in a Python 3 environment.
- 🐍 You can run other tests with `python texttest_fixture.py`.

## 🎯 Objectives

### 1️⃣ - Code review

Imagine that we (the examiner(s)) produced this code.

**🎯 Your objective is to give us a feedback on the work we produced.**

- 👀 Take a few minutes to look at the code,
- 🗣 Tell us what you think !
  - 🟢 Is everything OK ?
  - 🔴 Does anything bother you ?
- 🙋 Any suggestion to improve the quality of the code is welcome !

### 2️⃣ - Implementation

**We have recently signed a supplier of conjured items. This requires an update to our system** :

- "Conjured" items degrade in `Quality` twice as fast as normal items 🧙‍♂️

🎯**Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything still works correctly.**

However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesn’t believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, we’ll cover for you).

Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
