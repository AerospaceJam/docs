---
sidebar_position: 4
---

# Project Setup

Now that we have the SDK running and we know how to use it, we have to set up our project structure and learn how to extend the example.

:::note

This guide once again only deals with the example code that's provided out-of-the-box in the SDK. If you'd like, you can feel free to use any project structure you'd like.

:::

## Prerequisites

- A Pi, running the Aerospace Jam SDK, connected to a monitor, keyboard, and mouse, in Development Mode
- The `teamCode` folder opened in Thonny, as described in the [SDK intro](/getting-started/sdk-intro#writing-code)
- (Optional) A GitHub account. If you don't have one, you can sign up for free at [GitHub](https://github.com/signup).

## Project structure

As you look at the template project already located in `teamCode`, you'll notice some basic folder and files that already exist:

- `main.py` is the main [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) file that runs the entry point of your code. This is where you write most of your code, unless you split it into separate modules. The example file here is pretty well-commented, and reading those should help you understand approximately what the code is doing. If you need any more support with code, please ask in the [Discord](https://discord.com/invite/ShsPVMzpyW)!
- `pyproject.toml` is the Python project file that defines your project. You can modify this a bit, but for the most part, the only thing you want to change here is the `description`.
- `.python-version` defines the Python version that your project uses. With `uv`, you can change this, but in 99% of cases you should just leave this at its default, `3.11`.
- `README.md` is the [README](https://en.wikipedia.org/wiki/README) of your project. A README tells people looking at your code what it does, what it needs to run, and more. This should be the primary source of documentation for your project, unless you want to make a separate folder for it. This will be submitted with your codebase, so make sure to write at least something in it to be judged.
  - The format that your README uses is called [Markdown](https://en.wikipedia.org/wiki/Markdown). You can see some [basic formatting examples here](https://www.markdownguide.org/basic-syntax/).
- `templates` is a folder that stores your website's "templates". These are [HTML](https://en.wikipedia.org/wiki/HTML) files that define pages - realistically, though, you'll only need one.
  - `index.html` is the main home page of your site. This is served by the following code in the template `main.py`:

    ```py
    # When someone requests the root page from our web server, we return 'index.html'.
    @app.route('/')
    def index():
        return render_template('index.html')
    ```

- `static` is where other files that your website needs to serve up that *aren't* pages go. The only file in here is `js/socket.io.js`, which is a library that allows you to communicate back and forth with your server from your website and ground control station in real time without having to worry about any complicated code. You won't EVER need to modify this code, and if you ever are instructed to manually modify it, disregard the instructions to do so.
  - You can add other files to this folder in any structure that you like and load them from templates with `{{ url_for('static', filename='<path to your file>') }}`, where `<path to your file>` is the file you added.

## Configuring git

Now that you have a handle on the project structure, it's time to set up version control. This will allow you to track your changes, collaborate with your team, and revert to previous versions of your code if something goes wrong. For this, we'll use git, a popular version control system, and, optionally, GitHub, a platform for hosting your git repositories.

Before you start using git, you need to configure your username and email address. This information will be associated with every commit you make. Open a terminal and run the following commands, replacing "Your Name" and "youremail@example.com" with your own information:

```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"
git config --global init.defaultBranch main
```

:::warning

If you chose to sign up for and use GitHub, then make sure that "Your Name" matches your GitHub username, and that "youremail@example.com" matches the email address you used to sign up for GitHub.

:::

## Creating a repository

A repository, or "repo," is a folder that contains all the files for your project and the entire history of changes.

1. Open a terminal and navigate to your `teamCode` folder:

    ```bash
    cd ~/teamCode
    ```

2. Initialize a new Git repository:

    ```bash
    git init
    ```

## Using git

### The importance of committing your work

A "commit" is a snapshot of your files at a specific point in time. It's crucial to commit your changes frequently for several reasons:

- **Tracking Progress:** Commits create a historical log of your project, making it easy to see how it has evolved.
- **Safety Net:** If you make a mistake, you can easily revert to a previous working version of your code.
- **Collaboration:** Frequent commits keep your teammates updated on your progress and help to avoid merge conflicts, which is when git has to reconcile two different versions of a codebase.

A good rule of thumb is to make a commit after you complete a small, logical task, such as fixing a bug or adding a new feature.

### Writing good commit messages

A good commit message is as important as the code itself. It helps your future self and your teammates understand the changes you made and why, and it assists you in writing your engineering notebook later on. A good rule of thumb when writing commit messages is to imagine your future self trying to understand why you changed something. Here are some gentle suggestions for writing great commit messages:

- **Separate the subject from the body with a blank line.**
- **Limit the subject line to 50 characters.** This keeps it concise and readable.
- **Capitalize the subject line.**
- **Do not end the subject line with a period.**
- **Use the imperative mood in the subject line.** For example, use "Fix bug" instead of "Fixed bug" or "Fixes bug."
- **If you need more space, write in the body.**

Here's an example of a well-written commit message:

```git
feat: Add additional sensors

- Added TF-Luna LiDAR
- Added atmospheric pressure sensor
```

Examples of ***bad*** commit messages might be something like:

- `added stuff`
- `fixed bugs`
- `big commit to add stuff`
- `uploaded files`
- `made it work`

Just remember... what would your future self think, looking at these messages and trying to decipher them?

### Committing your first changes

Now that we have our git repo set up, let's commit our first changes!

Open a terminal on your Pi, then run the following commands to commit all your changes with the message "chore: Initial commit".

```bash
cd ~/teamCode
git commit -am "chore: Initial commit"
```

Now, we're all set to continue. If you're using GitHub, pushing to it wil be covered in the next section.

### For future reference...

Whenever you want to commit some changes, open a terminal (on your Pi) and run:

```bash
cd ~/teamCode
git commit -am "<YOUR COMMIT MESSAGE HERE>"
```

Of course, you also need to replace `<YOUR COMMIT MESSAGE HERE>` with the commit message you'd like to use. Also, if you chose to use GitHub, run `git push` after committing.

## Pushing to GitHub

If you chose to use GitHub to track your work, then you can log into your GitHub account with the GitHub CLI.

First, ensure that you're in Development Mode on your Pi and connected to the internet. Then, on your Pi, in a terminal, run:

```bash
gh auth login -p https -w
```

You will now be presented with a one-time code. Write this down, then press enter. On your Pi, your browser may or may not open, and you may experience issues with Firefox - if you're warned about having less than 1GB of RAM, just select `Cancel` or `Exit`, then open https://github.com/login/device in your browser on ***another device***, not the Pi. Enter the one-time code you got earlier, then authorize everything. If everything goes well, you should see a message like:

```txt
Congratulations, you're all set!
Your device is now connected.
```

Now, there's two more steps. First, you need to pick a name for your repo on GitHub. Most likely, you'll want to call it `AerospaceJam` - so we'll use that going forward. Finally, just run these commands in the Pi's terminal:

```bash
cd ~/teamCode
gh repo create AerospaceJam --public --source=.
```

:::note

The above command creates a public repository on GitHub, that any other team can see. If you want to keep your code private instead, replace `--public` with `--private`.

:::

See the above section for more information about committing and pushing to GitHub.

## Additional reading

:::warning

You should look at at least the first two links in this list if you haven't used git before, just to get a baseline idea of its principles and why we're using it.

:::

For more information about git and GitHub, there are other good resources:

- https://www.geeksforgeeks.org/what-is-git/
- https://www.youtube.com/watch?v=2ReR1YJrNOM
- https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F
