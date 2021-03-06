# git
## useful commands

```
git log --stat -n3                  # show also which files changed
git diff production development     # what happens, if merge dev -> prod?
git diff --name-status production development # which file were modified
git show 7d3b510790c42f694432d1f4936ec3fa8d7ee817
git pull -r                         # pull, but rebase my commits
git log --oneline --decorate --graph
```
## squash commits before merge
```
git checkout development
git pull --rebase
git merge --squash feature
git commit -m 'squash all commit into single one before merge to prod'
git push origin development
git checkout production
git pull origin development
git push origin production
```

## user config
```
[user]
        name = erolneuhauss
        email = ...
[color]
        ui = true
[credential]
        username = erolneuhauss
```

## repository config
### .git/config: use ssh key instead of password
```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
#	url = https://github.com/erolneuhauss/studies.git
	url = git@github.com:erolneuhauss/studies.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```
### generate ssh key and copy on a windows system
```
ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/home/ec2-user/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/ec2-user/.ssh/id_rsa.
Your public key has been saved in /home/ec2-user/.ssh/id_rsa.pub.
The key fingerprint is:
[...]
The key's randomart image is:
[...]
[ec2-user@ip-172-31-17-56 bash]$ eval "$(ssh-agent -s)"
Agent pid 30008
[ec2-user@ip-172-31-17-56 bash]$ ssh-add ~/.ssh/id_rsa
Identity added: /home/ec2-user/.ssh/id_rsa (/home/ec2-user/.ssh/id_rsa)

cat ~/.ssh/id_rsa.pub > /dev/clipboard
```
Paste key into the accounts profile under "SSH and GPG keys"
#### Before
```
git push origin master
Password for 'https://erolneuhauss@github.com':
```
#### After
```
git push origin master
Everything up-to-date
```



