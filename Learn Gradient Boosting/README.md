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

    Lets do this for Chest Pain

    It made 3 errors

    ![https://i.imgur.com/8KNvwH7.png](https://i.imgur.com/8KNvwH7.png)

    Amount of say for chest pain = 0.42

    Similarly we do this for the Blocked Arteries stump

     

    Now we know how the sample weights for the incorrectly classified samples are used to calculate the Amount of say each stump gets

5. Now we need to know how to modify the wts st the next stump will take the errors the current stump made into account

    Lets look at the first stump we made (using wt < 176). When we created this stump, all of the sample wts were same

    This means that classifying all samples was equally important

    But this stump incorrectly classified a sample:

    ![https://i.imgur.com/WEQLMSs.png](https://i.imgur.com/WEQLMSs.png)

    **So we will emphasize the need for the next stump to correctly classify it by increasing its sample wt and decreasing all the other sample wts**

    Lets start by inc the sample wt for this incorrectly classified sample:

    ![https://i.imgur.com/w9gLb5S.png](https://i.imgur.com/w9gLb5S.png)

    Now when the amount of say is high, i.e the TE is less i.e the stump was good, the new sample wt will be raised and will be much larger than the prev one

    ![https://i.imgur.com/NaOnkg7.png](https://i.imgur.com/NaOnkg7.png)

    But if the amount of say is low, i.e the TE is high i.e the stump was not good, the new sample wt will be scaled by a relatively smaller number

    That means that the new sample wt will only be a bit larger than the old one

    An exception to this is if the amount of say is -ve, say -2

    1/8 = 0.125 

    0.125 x e^-2 =  0.09, which is lesser

    In this example, amount of say = 0.97

    e^0.97 = 2.64

    new sample wt = 1/8 * 2.64 = **0.33**

    This is more than the old one

    Now we need to decrease the sample wts for all the correctly classified samples

    ![https://i.imgur.com/9OqlNyQ.png](https://i.imgur.com/9OqlNyQ.png)

    ![https://i.imgur.com/WKbtaxS.png](https://i.imgur.com/WKbtaxS.png)

    Note the -ve sign before the amount of say

    ![https://i.imgur.com/zM5sZXQ.png](https://i.imgur.com/zM5sZXQ.png)

    As we see from the graph, when the amount of say is large, i.e the stump was good we scale by a value close to 0. This will make new sample wt v small

    If amount of say is small, i.e the stump was not good we scale by a value close to 1. This will make new sample wt just a bit smaller

    Here amount of say = 0.97

    e^-0.97 = 0.38

    new sample wt = 1/8 * 0.38 = **0.05**, **which is less than the old one** 

    Note that if the amount of say was -ve say -2

    1/8 x e^2 = 0.92 which is more, so we actually increase the wt.. Why is this?

    Well since the stump was really bad, even on the cases where it actually predicted correctly, it probably did so by chance and not because it learned something useful,

    So we do want these cases to be more important to be classified correctly by the future stumps, so we increase the weight (probably)

     In this way we plug in the new sample wts

    ![https://i.imgur.com/Cg092BJ.png](https://i.imgur.com/Cg092BJ.png)

    The correct cases get lower wts while the incorrect one gets higher wt

6. Normalize the new wts so that they add upto 1

    Right now sum is 0.68

    So we divide each wt by 0.68 to get the normalized values

    ![https://i.imgur.com/ibEzR2w.png](https://i.imgur.com/ibEzR2w.png)

    Now we just use these normalized wts as the sample wts columns, since these are the ons we will use for the next stump

7. Now we use the modified sample wts to make the second stump in the forest. Recall, when we made the first stump using weight, we did not have to worry about this as all the wts were same and we simply chose the least value of Gini Index.

    Here we take the sample wts and calculate the **Weighted Gini Index** to determine which variable should be the next stump

    The WGI would put more emphasis on classifying the sample with the highest wt (the one that was mis-classified by the last stump) 

    Alternatively, instead of using WGI we can make a **new** collection of samples that contain duplicate copies of samples with the largest sample wts

    1. We start by making a new and empty dataset that is the same size as the original one
    2. Remember that the sum of sample wts always equals 1
    3. So we pick a number randomly (say x) bw 0 and 1
    4. We check where that number falls when we use sample wts as a distribution
        1. For eg: if 0≤x≤0.07, we put the first sample into the new collection of samples
        2. If 0.07≤x≤0.07+0.07(0.14) we put the second sample into the new collection of samples
        3. If 0.14≤x≤0.14+0.07(0.21) we put the third sample into the new collection of samples
        4. If 0.21≤x≤0.21+0.49(0.70) we put the fourth sample into the new collection of samples
        5. .... and so on ...
    5. Note how the interval is equal to the sample wt and if the sample wt is large so is the interval and so is the probability that the random number picked is in that interval and that sample will be selected
    6. For eg if x = 0.72 we pick the fifth sample and put it in the new collection:

        ![https://i.imgur.com/fys0VL0.png](https://i.imgur.com/fys0VL0.png)

    7. Then we pick another random no x = 0.42 so we pick the fourth sample and put it in the new collection
    8. Then we pick 0.83 and we put the sixth one
    9. Then 0.51, again we pick fourth one 
    10. We continue to do this until size of new collection == size of original

        ![https://i.imgur.com/MUeUH3M.png](https://i.imgur.com/MUeUH3M.png)

    11. Now we get rid of the original samples and use this new collection of samples
8. We assign equal wts to these samples, just as before. But this does not mean that the next stump will not emphasize the need to correctly classify the previously miss-classified sample. This sample will be treated as a block, creating a large penalty for being miss-classified

    Basically this block has same values of features and same target, so the effective wt becomes 1*4/8 = 1/2 

    ![https://i.imgur.com/k7QvtwD.png](https://i.imgur.com/k7QvtwD.png)

9. Now we go back to the beginning and try to find the stump that does the best job classifying the new collection of samples
10. This is how the errors that the first tree (stump) makes influences how the second is made. How the errors the 2nd one makes influences how the 3rd is made and so on...
11. How does a forest of stumps created by AdaBoost makes classifications
    1. Say that the stumps on the LHS of the below diag predicted heart disease and the ones on the RHS predicted not
    2. Since the sum of amounts of say for the 1st class is higher we predict that patient has heart disease

        ![https://i.imgur.com/E0B49LJ.png](https://i.imgur.com/E0B49LJ.png)

---