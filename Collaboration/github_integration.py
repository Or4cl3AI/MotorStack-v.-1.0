```python
import git

def initialize_repository(repo_path):
    """
    Initialize a new git repository at the given path.
    """
    repo = git.Repo.init(repo_path)
    return repo

def add_files(repo, files):
    """
    Add files to the repository.
    """
    repo.index.add(files)

def commit_changes(repo, commit_message):
    """
    Commit changes to the repository.
    """
    repo.index.commit(commit_message)

def push_changes(repo, remote_name='origin'):
    """
    Push changes to the remote repository.
    """
    repo.remotes[remote_name].push()

def pull_changes(repo, remote_name='origin'):
    """
    Pull changes from the remote repository.
    """
    repo.remotes[remote_name].pull()

def create_branch(repo, branch_name):
    """
    Create a new branch in the repository.
    """
    repo.git.checkout('-b', branch_name)

def switch_branch(repo, branch_name):
    """
    Switch to a different branch in the repository.
    """
    repo.git.checkout(branch_name)

def merge_branches(repo, from_branch, to_branch):
    """
    Merge changes from one branch to another.
    """
    repo.git.checkout(to_branch)
    repo.git.merge(from_branch)
```
This python script provides basic functionalities for GitHub integration such as initializing a repository, adding files, committing changes, pushing and pulling changes, creating and switching branches, and merging branches.