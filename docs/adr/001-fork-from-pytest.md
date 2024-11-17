
# Create an "ok" fork of pytest

## Decision
Create ok as a fork of pytest. And have it be a broken connection fork.

## Context
pytest is awesome. But it's also a lot.
It'd be cool if we had another test framework kinda like pytest but with less features. 
For example, `pytest --help` is a little overwhelming.
Also, there's some backwards compatibility to consider with pytest. 
With ok, we don't have anyone relying on legacy functionality. Yet.
So, I want to take advantage of that.

## Options Considered
The kind of fork is tough though.

1. Friendly fork. We could have left `ok` as a friendly fork, with the fork link obvious in GitHub. Actually forking within GitHub.
    * pro: Can get updates from pytest 
    * con: Keeping that up is tough
    * con: Free accounts with GitHub can only have one fork of a project. So I can't work on both pytest fixes and ok with the same GitHub account without paying. Lame.
2. Broken fork connection to pytest. I don't actually know the real name of this. But essentially:
    * Clone a shallow copy of pytest (history not needed)
    * Upload as a new project
    * Actually, it's been a couple of weeks. And I don't really remember the steps, but something like that.
    * pro: easy
    * pro: repo is super fast to clone (no built up history)
    * con: hard to get any updates from pytest

So, I tried a friendly fork initially. I forked from 8.3.2 of pytest. I made some changes, I released an initial version. All was good.  
Then, pytest released 8.3.3. And I tried to sync the versions. And stuff I had deleted started showing up again, and other changes weren't compatible with my changes. and ... yuk

Now we're trying option 2.

We'll have to, I'll have to, monitor fixes from pytest and try to decide if there are some I'd like to incorporate into 'ok'. Or not. We'll see how importand and/or painful it is to keep up with pytest.

But for now, I think I clean break is ok for ok.

After all, this is an experiment.

## Consequences
We shall see.