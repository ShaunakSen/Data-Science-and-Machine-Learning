## Learn Git with Bitbucket Cloud

[](https://www.atlassian.com/git/tutorials/learn-git-with-bitbucket-cloud)

### Create a Git repository

As our new Bitbucket space station administrator, you need to be organized. When you make files for your space station, you’ll want to keep them in one place and shareable with teammates, no matter where they are in the universe. With Bitbucket, that means adding everything to a repository. Let’s create one!

- You have access to all files in your local repository, whether you are working on one file or multiple files.
- You can view public repositories without a Bitbucket account if you have the URL for that repository.
- Each repository belongs to a user account or a team. In the case of a user account, that user owns the repository. + In the case of a team, that team owns it.
- The repository owner is the only person who can delete the repository. If the repository belongs to a team, an admin can delete the repository.
- A code project can consist of multiple repositories across multiple accounts but can also be a single repository from a single account.
- Each repository has a 2 GB size limit, but we recommend keeping your repository no larger than 1 GB.

#### Step 1. Create the repository

Initially, the repository you create in Bitbucket is going to be empty without any code in it. That's okay because you will start adding some files to it soon. This Bitbucket repository will be the central repository for your files, which means that others can access that repository if you give them permission. After creating a repository, you'll copy a version to your local system—that way you can update it from one repo, then transfer those changes to the other.

![](https://www.atlassian.com/dam/jcr:a226d62e-3f0f-4c7e-8d99-c3c73188f9f6/01.svg)

### Copy your Git repository and add files

Now that you have a place to add and share your space station files, you need a way to get to it from your local system. To set that up, you want to copy the Bitbucket repository to your system. Git refers to copying a repository as "cloning" it. When you clone a repository, you create a connection between the Bitbucket server (which Git knows as origin) and your local system.

#### Step 1. Clone your repository to your local system

We already know how to do this...


#### Step 2. Add a file to your local repository and put it on Bitbucket

With the repository on your local system, it's time to get to work. You want to start keeping track of all your space station locations. To do so, let's create a file about all your locations.

1. Go to your terminal window and navigate to the top level of your local repository.
`$ cd ~/repos/bitbucketstationlocations/`

2. Enter the following line into your terminal window to create a new file with content.
`$ echo "Earth's Moon" >> locations.txt`

3. Get the status of your local repository. The `git status` command tells you about how your project is progressing in comparison to your Bitbucket repository.
At this point, Git is aware that you created a new file, and you'll see something like this:
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        locations.txt

no changes added to commit (use "git add" and/or "git commit -a")
```
The file is untracked, meaning that Git sees a file not part of a previous commit. The status output also shows you the next step: adding the file.

4. Tell Git to track your new locations.txt file using the `git add` command. Just like when you created a file, the git add command doesn't return anything when you enter it correctly.
`$ git add locations.txt`
The git add command moves changes from the working directory to the Git staging area. The staging area is where you prepare a snapshot of a set of changes before committing them to the official history.
![](https://www.atlassian.com/dam/jcr:dbf0c59f-848d-4814-bfd5-6b190a092963/03.2017-12-12-00-28-24.svg)


5. Check the status of the file.
```
$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   locations.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
```
Now you can see the new file has been added (staged) and you can commit it when you are ready. The git status command displays the state of the working directory and the staged snapshot.

6. Issue the `git commit` command with a commit message, as shown on the next line. The -m indicates that a commit message follows. 
**The git commit takes the staged snapshot and commits it to the project history. Combined with git add, this process defines the basic workflow for all Git users.**
Up until this point, everything you have done is on your local system and invisible to your Bitbucket repository until you push those changes.
- Git's ability to communicate with remote repositories (in your case, Bitbucket is the remote repository) is the foundation of every Git-based collaboration workflow.

- Git's collaboration model gives every developer their own copy of the repository, complete with its own local history and branch structure. Users typically need to share a series of commits rather than a single changeset. Instead of committing a changeset from a working copy to the central repository, Git lets you share entire branches between repositories.

![](https://www.atlassian.com/dam/jcr:c24540ba-3f2b-4697-9fd3-91242f5ac5f2/05.2017-12-12-00-28-23.svg)

7. Go back to your local terminal window and send your committed changes to Bitbucket using `git push origin master`. This command specifies that you are **pushing to the master branch (the branch on Bitbucket) on origin (the Bitbucket server).**
Your commits are now on the remote repository (origin).
![](https://wac-cdn.atlassian.com/dam/jcr:ccfab346-46aa-4677-8469-2e109683bf19/06.2017-12-12-00-28-23.svg)

8. Go to your BitbucketStationLocations repository on Bitbucket.

9. If you click Commits in the sidebar, you'll see a single commit on your repository. Bitbucket combines all the things you just did into that commit and shows it to you. You can see that the Author column shows the value you used when you configured the Git global file ( ~/.gitconfig).
If you click Source in the sidebar, you'll see that you have a single source file in your repository, the locations.txt file you just added.

### Pull changes from your Git repository on Bitbucket Cloud

Next on your list of space station administrator activities, you need a file with more details about your locations. Since you don't have many locations at the moment, you are going to add them right from Bitbucket.

#### Step 1. Create a file in Bitbucket


We go to online bitbucket and create a new file, add in some HTML code and commit the changes
- pretty straightforward

You now have a new file in Bitbucket! You are taken to a page with details of the commit, where you can see the change you just made:

#### Step 2. Pull changes from a remote repository

Now we need to get that new file into your local repository. The process is pretty straight forward, basically just the reverse of the push you used to get the locations.txt file into Bitbucket.

To pull the file into your local repository, do the following:

The git pull command merges the file from your remote repository (Bitbucket) into your local repository with a single command.

When we do `git status` it shows:

```
Your branch is behind 'origin/master' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)
```

Also, in `SourceTree` when we `fetch` we get the following information:

<img src='./diag1.png'>

Here we can see quite clearly that my local copy of the branch master is behind
`origin/master` by 1 commit

According to the tutorial:
Enter the git `pull --all command` to pull all the changes from Bitbucket. (In more complex branching workflows, pulling and merging all changes might not be appropriate .) Enter your Bitbucket password when asked for it.

In SourceTree simply Pull works fine

<img src='./diag2.png'>

Now we can see that, after pulling the local master branch and remote master branch
are at the same level


The git pull command merges the file from your remote repository (Bitbucket) into your local repository with a single command.

![](https://wac-cdn.atlassian.com/dam/jcr:a4d2c201-3486-4f2b-81a9-8ab6b663c9b9/01.2017-12-12-00-28-24.svg)


