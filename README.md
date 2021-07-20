# hm-python-ttrl
following tutorial for hypermodern python

From [here](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)

## Adding requirements

This could be a way to remove the versions and pipe to `poetry add`:

```
cat requirements.txt | sed  's/==.*//' | awk '{print "poetry add " $1}' | xargs  echo
```

This actually creates a command per dep. Might be useful if I wanted to check on dev deps.

Otherwise I could do

```
cat requirements.txt | sed  's/==.*//' | xargs poetry add
```

This would add all of them.
