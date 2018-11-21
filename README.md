heroku vs eb cli
================

I'm a long time user of heroku's excelent PaaS. But AWS has a number of advantages that sometimes makes it a better option.

- It can be more cost efficient
- It supports more advanced architectures

The table below is a cheatsheet for people that are moving their service from heroku to eb cli 

Install eb cli

```
brew install awsebcli
```

Commands

```
eb use
eb deploy
eb open
eb status
eb list
eb logs
eb logs --stream -g /var/log/eb-activity.log
eb create
eb ssh
eb --help
eb status
eb terminate
heroku --version | eb --version

heroku open

heroku run 
heroku run:detached

heroku restart
heroku config
heroku logs --tail

curl -o latest.dump `heroku pg:backups:public-url`

git push heroku master

heroku addons
heroku plugins

heroku buildpack
heroku certs
heroku apps
```
