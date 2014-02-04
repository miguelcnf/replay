# replay

Replay is an hacky way to automate the installation/updates of your dev environment, dotfiles, desktop apps, etc. on a clean *nix laptop.

It happens to use ansible-playbook magic under the hood - in fact this is pretty much a nasty hack wrapping over ansible-playbook.

Note that this is a hack and it's heavilly untested, I mean, until now it was only executed on my laptop - so use it at your own risk!

## usage

```
$ ./replay
Usage:
  replay all | hack
  replay (-h | --help | --version)
```

`$ ~/replay all` will run replay against the .replay.yml file in your home

`$ ~/replay hack` will run replay against a .replay.yml that you can create inside the hacking directory in the repo for dev purposes.

## requirements

Pretty sure these are the only explicit dependencies that replay has:
```
docopt>=0.6.1
Jinja2>=2.7.1
ansible>=1.4.3
PyYAML>=3.10
```

Note that replay uses docopt to generate helper messages and perform arg parsing - if you're a python coder and dont know about docopt, stop what you're doing and go [check it out](http://docopt.org/) now - it's seriously awesome.

## why in the world would you do that?

Pretty much inspired by a couple of talks and articles on the subject:

[Automating your development environment with Ansible](http://www.nickhammond.com/automating-development-environment-ansible/) by Nick Hammond
[It's Not Just for Servers: Chefing Your Development Environment (The Pivotal Way)](http://www.youtube.com/watch?v=kfQy8UzBUvY&feature=plcp) at ChefConf 2012

And some similar but much more pretty projects like:

[Sprout](https://github.com/pivotal-sprout/sprout)
[Boxen](http://boxen.github.com/)

## how does it work?

Replay reads a yaml file in your home dir `~/.replay.yml` which contains a list of tasks to be played on the box much like:˙
```
# Box baseline
---
tasks:
  homebrew:
    formulas:
    - wget
    - git
  gem:
    packages:
    - bundler
    - chef
  pip:
    packages:
    - docopt
  dotfiles:
    repo: miguelcnf/dotfiles
    list:
    - .vimrc
    - .gitconfig
```

Based on the content of the yaml file it generates 3 random named temporary files:

- Variables_File
- Playbook_File which includes the dynamic Variables_File
- Inventory_File which only contains the localhost entry and is passed to ansible-playbook

After that it does a hacky syscall to ansible-playbook passing the Inventory_File to `-i` and the Playbook_File as the playbook to run.

If everything goes well you should see ansible doing it's thing on your box.

## how can you try it?

I theory (!) it should be something like...

Clone the github project:
```
$ git clone git@github.com:miguelcnf/replay.git
```

Install requirements with pip:
```
$ cd replay/
$ pip install -f requirements
```

Create your replay file as the example above:
```
$ vim ~/.replay.yml
```

Run replay:
```
$ ./replay all
```

Again I've never actually tested the installation and therefore it might (probably will?) brake.

## what kind of things are implemented?

As a proof of concept I only added support to install formulas with homebrew, packages with pip/gem and a hacky way to install your dotfiles from a github repo.

## what more things you want?

In the short term I'll add my dmg's and brew-cask apps to my task list.

I'll probably look at doing a bash installer that takes care of (doh!) installing things - much like homebrew, rvm, etc.

Including and excluding tasks from runs via the cli - much like strainer.

## author

Miguel Fonseca
@miguelcnf




