# Git
## branch model
gitlab-flow

- master(default、CRUD)
- feature/hotfix
- pre-production(Lab env)
- production

## opetation
### init
```
git checkout master
git branch production
git push -u origin production
```

### commit
```
git checkout master
git pull
git checkout -b feature/hoge

git add .
git commit -m "${commit_msg}"
git push origin feature/hoge

git checkout master
git branch -d feature/hoge

# same procedure for hotfix
```

### edit commit
```
git reset --hard HEAD^
git rebase -i ${commit_id}
```

#### remove
remove cache
```
git rm -r --cached ${file}
```


## Reference
https://github.com/github/gitignore
https://www.google.com/amp/s/www.tam-tam.co.jp/tipsnote/program/post16686.html/amp
