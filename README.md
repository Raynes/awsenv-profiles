# AWS access key switcher

awsenv is a little tool for switching your `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` environment variables based on profiles configured
in `~/.aws/config`.

The [awscli](https://aws.amazon.com/cli/) allows you to switch profiles using
`--profile <profile_name>`, so commands are executed on the proper account.
Sadly, not every tool supports this sort of flag, and it's a pain to export
them manually whenever you need them.

There are other non-AWS-specific tools to manage environments, but they do not
work with AWS configuration/profiles, and often force you to litter your
disk with `.direnv` files and such. They're excellent tools, but I just want
to switch AWS profiles!


## Usage

```
pip install awsenv-profiles
```

This will install a small Python executable, `awsenvp`, and a bash script,
`awsenv.sh`.

Now, edit your `~/.profile` or equivalent and add these lines:

```bash
function awsenv_wrapper() {
  eval $(awsenv.sh $1)
}

alias awsenv=awsenv_wrapper
```

Now, to switch profiles, you can run stuff like this:

```
$ awsenv prod
$ awsenv dev
... and so on
```

## How it works

`awsenvp` is a Python program that takes a profile name as an argument and uses
botocore to find the credentials for it, then it prints out export commands
for `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. If any failures occur,
exit codes are returned to indicate the kind of failure that occurred:

* `3` - You forgot to pass a profile name argument.
* `4` - Profile not found.

`awsenv.sh` is a wrapper around `awsenvp` that runs it and handles exit codes
appropriately. Since the output of `awsenv.sh` is always going to be used with
`eval`, if an error occurs it prints out an echo for the failure.

The idea here is that since bash scripts, unless sourced, cannot export environment
variables to the parent shell, `eval` is necessary.

## Why the name?

I named it awsenv originally, but needed to change the package name because
I didn't realize it was taken on pypi.
