```python
import os
from git import Repo

# Define the Heroku buildpacks for the application
buildpacks = [
    'heroku/python',
    'heroku/nodejs'
]

# Define the Heroku app name
app_name = 'motorstack-app'

# Define the Heroku remote repository
heroku_repo = f'https://git.heroku.com/{app_name}.git'

# Define the local repository path
local_repo_path = os.getcwd()

# Initialize the local repository
repo = Repo(local_repo_path)

# Login to Heroku
os.system('heroku login')

# Create a new Heroku app
os.system(f'heroku create {app_name}')

# Set the buildpacks for the Heroku app
for buildpack in buildpacks:
    os.system(f'heroku buildpacks:add {buildpack} --app {app_name}')

# Add the Heroku remote repository to the local repository
repo.create_remote('heroku', heroku_repo)

# Push the local repository to the Heroku remote repository
os.system('git push heroku master')

# Open the deployed application in the web browser
os.system('heroku open')
```