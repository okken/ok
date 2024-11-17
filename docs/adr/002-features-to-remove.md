
# Features to remove

This is more of an ongoing list of features removed and to remove.

## Status 
In progress

## Decision
Lots of features are going to be removed. I'll keep a list at the end of this.

## Context
pytest is awesome. But it's also big, with lots of features.

I think there's a need for a thing like pytest with less features for:
* people new to testing
* people that don't want to be frightened by the --help output
* people with simple projects that don't need a lot of fancy

Most of the removals are going to be driven by what I (Brian) use on a daily
basis and what I don't. But I'm open to hear feedback.

## Options Considered
none. I'm just jumping in.

## Consequences
I'm hoping a lot less features will make `ok` easier to learn than `pytest`. 
But I also hope that there will be a path forward for people to relatively painlessly switch from `ok` to `pytest` if needed.


## Feature Removals

* unittest - I don't use it - removed
* doctest - I don't use it - removed
* pastebin - I don't use it - removed
* pdb - removed
  - This was a hard decision. pytest pdb support is cool. 
  - But also, I think new devs will propbably use VSCode or PyCharm or some other editor to debug tests.
  - So I think this is ok to go
* logging - to be removed
    - main reason is that the logging features take up a ton of --help space. 
    - Also, I don't think people new to testing are going to test logging.
    - But mostly, it adds so much complexity to the UI of pytest. 
    - I think it should have been supported as a plugin and not put into core.
* junitxml - I don't like xml - to be removed
