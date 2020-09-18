# All about Gradient Boosting

# Understanding AdaBoost

Notes on the video by Josh Starmer (StatQuest): https://www.youtube.com/watch?v=LsK-xG1cLYA

## Key ideas

In DTs when we make trees they are usually full, some may be bigger than others but there is no pre-determined max depth

In AdaBoost, a forest of trees is made and the trees usually comprise a node and 2 leaves

A tree with one node and 2 leaves is called a **Stump**

So its rather a forest of stumps

![https://i.imgur.com/ZMWoPgF.png](https://i.imgur.com/ZMWoPgF.png)

These simple stumps are not great at making accurate decisions as it considers only one variable at a time to make a decision

So stumps are **Weak Learners**

In RF each tree has an equal vote on the final classification

In contrast in a forest of stumps made by AdaBoost, some stumps may get more/less vote than the others

![https://i.imgur.com/tIJ8oV1.png](https://i.imgur.com/tIJ8oV1.png)

Also in RF each DT is made independently of the others. But in AdaBoost order is important

The error that the first stump makes influences how the second stump is made and so on...

To summarize the key ideas:

![https://i.imgur.com/TjRAX67.png](https://i.imgur.com/TjRAX67.png)