### Unstaging
[Undo add i.e. "unstaging"](https://stackoverflow.com/questions/348170/how-do-i-undo-git-add-before-commit)

Genehack: 
You can undo `git add` before commit with
```
git reset <file>
```

which will remove it from the current index (the "about to be committed" list) without changing anything else.

You can use

```
git reset
```

without any file name to unstage all due changes. This can come in handy when there are too many files to be listed one by one in a reasonable amount of time.