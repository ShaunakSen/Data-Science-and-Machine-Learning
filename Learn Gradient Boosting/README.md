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

## Creating a forest of stumps using AdaBoost

We start off with some data:

![https://i.imgur.com/8wWu2Dj.png](https://i.imgur.com/8wWu2Dj.png)

We have to predict whether the patient has heart disease or not

1. The first thing we do is assign a weight to each sample, which indicates how important it is for that sample to be correctly classified

    At the start all samples receive same wt = 1/(number of samples) = 1/8

    So all samples are equally important

    But after we make the 1st stump, these wts will change in order to guide how the next stump is created

2. We need to make the first stump in the forest.

    This is done by finding the feature which does the best job at classifying the samples.

    As the wts are same, we can ignore them right now

    We check for each var: first we pick chest pain and check how pure the leaf nodes are based on the values of chest pain

    ![https://i.imgur.com/IjcmO4J.png](https://i.imgur.com/IjcmO4J.png)

    We do the same for blocked arteries and for patient weight

    Then we calculate the Gini Index for the 3 stumps

    The GI for patient wt is the lowest

     

    ![https://i.imgur.com/y33Xeug.png](https://i.imgur.com/y33Xeug.png)

    So this will be the **first stump in the forest**

    ![https://i.imgur.com/ihdbhrT.png](https://i.imgur.com/ihdbhrT.png)

3. Determining the wt of the first stump

    We determine the wt a stump has in the classification decision based on how well it classified the samples

    If we look at the wt stump it made one error for the highlighted patient:

    ![https://i.imgur.com/WEQLMSs.png](https://i.imgur.com/WEQLMSs.png)

    **The Total Error for the stump = the sum of the wts associated with the incorrectly classified samples**

    Here it is 1/8

    NOTE: Because the sample wts always add up to 1, total error is always in range 0→1

    0 → perfect stump

    1 → worst stump

    We use this TE to determine the wt (amount of say)

    ![https://i.imgur.com/9mMjcvD.png](https://i.imgur.com/9mMjcvD.png)

    ![https://i.imgur.com/rGQy4rL.png](https://i.imgur.com/rGQy4rL.png)

    This makes sense, for TE=0, wt is v high, but decreases rapidly as TE inc and decreases then at a slowe rate unitil TE=0.5, at which step wt = 0. This means, that when the stump is no better than random at the decision, it gets 0 wt

    Then the wt decreases at an increasing rate as TE increases (the stump gives the opposite classification) and the wt becomes increasingly negative .

    So of a stump votes for "heart disease" the -ve wt will turn that vote into "not a heart disease"

    In this equation if TE = 1 or 0 the eqn becomes undefined, so in practice a small error term is added to prevent this

    For the stump we have, TE = 1/8, so amount of say (wt) using the equation = 0.97

     

    ![https://i.imgur.com/KgRWdKO.png](https://i.imgur.com/KgRWdKO.png)

4. Similarly we work out the amount of say for the remaining stumps
5.