heroku to eb cli
================

I'm a long time user of heroku's excelent PaaS. But AWS has a number of advantages that sometimes makes it a better option.

- It can be more cost efficient
- It supports more advanced architectures

The table below is a cheatsheet for people that are moving their service from heroku to eb cli 

- Install eb cli
```
pip install awsebcli --upgrade --user
```

- Setup with git and github
- Environments: development, testing, and production. 

- Setup with CodeBuild & CodePipeline
```
https://medium.com/hollowverse/how-to-use-aws-codebuild-codepipeline-to-automate-deployment-to-elastic-beanstalk-cff01b725c41

Add a buildspec.yml file to trigger CodeBuild to be used
```

- Custom Domain
- SSL

- Configuring the database

See

https://tomkadwill.com/running-rails-on-aws-elastic-beanstalk
https://medium.com/@jameshamann/deploying-rails-5-app-using-elastic-beanstalk-and-postgresql-8ca19bc7648a

```
brew install awsebcli
```

Flask app
---------
```
Run:
python application.py




Files
-----
```
.elasticbeanstalk
  config.yml


```





Commands
--------

```
virtual env


eb init
# Initialize a new eb application

eb create
# Create a new environment, and upload it to aws
# load balancer type 2 is always the right choice




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
