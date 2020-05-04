


```makefile
all: update publish

update:
    jupyter nbconvert --to=html --no-input --ExecutePreprocessor.enabled=True TM-status-report.ipynb

publish:
    git add *.html
    git commit -m "update covid-19 reports `date --iso=s`"
    git push origin master
```


# Updating hourly

To complete the process automation, we add a cron job to run everything once an hour.

Open your cron configuration file with using the command:

```
crontab -e
```

Add a time definition like `15 * * * *` for our `make all` command for reporting.
Here we need to also use the `--directory` option to set the working directory for make, since
the crontab is not in the root of our repository by default.

```cron
# update reports every hour at 15 minutes past to github-pages
15 * * * * make --directory /home/user/your/repo/ all
```

Here are some examples of other cron time definitions:

- `* * * * *` - run every minute (nice for debugging)
- `10 12 * * *` - run every day ten minutes past noon
- `0 0,6,12,18 * * *` - run every six hours


For the final automation part, you'll need to create a new set of [ssh keys for github](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and then configure them as [deploy keys](https://developer.github.com/v3/guides/managing-deploy-keys/#deploy-keys) in the setting of you github repository.
Make sure to mark the keys as having _write_ access. The ssh keys must be generated as passwordless, by entering an empty passphrase in the `ssh-keygen` command, otherwise cron will not be able to push run `git push` correctly.

In short, run:

```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

using :

- use your own your email address
- an appropriate file name,  `/home/you/.ssh/id_rsa_cron_deploy_key`
- an empty passphrase


```makefile
all: update publish

update:
	jupyter nbconvert --to=html --no-input --ExecutePreprocessor.enabled=True --ExecutePreprocessor.timeout=-1 TM-status-report.ipynb

publish:
	git add *.html *.csv
	git commit -m "update covid-19 reports `date --iso=s`"
	GIT_SSH_COMMAND='ssh -i ~/.ssh/id_rsa_cron_deploy_key' git push origin master
```
