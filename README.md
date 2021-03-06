# πͺ gilded rose πΉ

- [πͺ gilded rose πΉ](#-gilded-rose-)
  - [π€ Problem Description](#-problem-description)
  - [π Manual](#-manual)
  - [π― Objectives](#-objectives)
    - [1οΈβ£ - Code review](#1οΈβ£---code-review)
    - [2οΈβ£ - Implementation](#2οΈβ£---implementation)

## π€ Problem Description

Hi and welcome to team Gilded Rose !

πͺ As you know, we are a small inn with a prime location in a prominent city ran by a friendly innkeeper named Allison.

π We also buy and sell only the finest goods.

![the gilded rose inn](https://static.wikia.nocookie.net/wowwiki/images/8/8b/The_Gilded_Rose.jpg/revision/latest/scale-to-width-down/400)

π Unfortunately, our goods are constantly degrading in quality as they approach their sell by date.
βοΈ We have a system in place that updates our inventory for us. It was developed by a no-nonsense type named Leeroy, who has moved on to new adventures.

Your task is to add the new feature to our system **so that we can begin selling a new category of items**.

First an introduction to our system:

- π All items have a `SellIn` value which denotes the number of days we have to sell the item,
- π· All items have a `Quality` value which denotes how valuable the item is,
- π At the end of each day our system lowers both values for every item.

Pretty simple, right ? Well this is where it gets interesting:

- ππ Once the sell by date has passed, `Quality` degrades twice as fast
- β The `Quality` of an item is never negative
- π "Aged Brie" actually increases in `Quality` the older it gets
- π§ The `Quality` of an item is never more than 50
- π« "Sulfuras", being a legendary item, never has to be sold or decreases in `Quality`
- βοΈ "Backstage passes", like aged brie, increases in `Quality` as itβs SellIn value approaches; `Quality` increases by 2 when there are 10 days or less and by 3 when there are 5 days or less but `Quality` drops to 0 after the concert.

## π Manual

- π You can run the unit tests with `python -m unittest test_gilded_rose.py` in a Python 3 environment.
- π You can run other tests with `python texttest_fixture.py`.

## π― Objectives

### 1οΈβ£ - Code review

Imagine that we (the examiner(s)) produced this code.

**π― Your objective is to give us a feedback on the work we produced.**

- π Take a few minutes to look at the code,
- π£ Tell us what you think !
  - π’ Is everything OK ?
  - π΄ Does anything bother you ?
- π Any suggestion to improve the quality of the code is welcome !

### 2οΈβ£ - Implementation

**We have recently signed a supplier of conjured items. This requires an update to our system** :

- "Conjured" items degrade in `Quality` twice as fast as normal items π§ββοΈ

π―**Feel free to make any changes to the `UpdateQuality` method and add any new code as long as everything still works correctly.**

However, do not alter the Item class or Items property as those belong to the goblin in the corner who will insta-rage and one-shot you as he doesnβt believe in shared code ownership (you can make the UpdateQuality method and Items property static if you like, weβll cover for you).

Just for clarification, an item can never have its Quality increase above 50, however "Sulfuras" is a legendary item and as such its Quality is 80 and it never alters.
