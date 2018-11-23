heroku to eb cli
================

I'm a long time user of heroku's excelent PaaS. But AWS has a number of advantages that sometimes makes it a better option.

- It can be more cost efficient
- It supports more advanced architectures

The table below is a cheatsheet for people that are moving their service from heroku to eb cli 



Prerequisites
-------------
```
# Install eb cli
pip install awsebcli --upgrade --user

# Use virtualenv
virtualenv -p python3 .env
source .env/bin/activate
```

Credentials
------------
```
Defaults are defined in ~/.aws/credentials

TODO: How to setup project specific?
```

Monitor RAM usage
--------------
```
https://aws.amazon.com/code/amazon-cloudwatch-monitoring-scripts-for-linux/
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html
```

Load balancing
--------------
```
AWS Auto Scaling - Not needed yet.
Configure in EB GUI: Elastic Beanstalk > Configuration > Load Balancer > Processes > Edit > Sessions
```

CD/CI system
------------
```
TODO
- CodeBuild
- CodePipeline
- Push to github.

https://medium.com/hollowverse/how-to-use-aws-codebuild-codepipeline-to-automate-deployment-to-elastic-beanstalk-cff01b725c41

Add a buildspec.yml file to trigger CodeBuild to be used
```

buildspec.yml
```
phases: To go through when building the application

artifacts: Files outputted after build
```

Custom Domain and SSL
---------------------
```
TODO, see: https://tomkadwill.com/running-rails-on-aws-elastic-beanstalk
See: eb labs setup-ssl
```

Configuring a database
------------------------
TODO: I don't need this for now as my service is stateless, will add notes if I ever do.

https://tomkadwill.com/running-rails-on-aws-elastic-beanstalk
https://medium.com/@jameshamann/deploying-rails-5-app-using-elastic-beanstalk-and-postgresql-8ca19bc7648a


Configuring a ElastiCache (Redis) cache
-------------------------

Logging
--------
```
# You can enable "S3 log storage" and "Instance log streaming to CloudWatch Logs" in GUI: Elastic Beanstalk > Configuration > Software.
# or by using `eb logs --cloudwatch-logs enable`

# Instance log streaming must be enabled to use the `--stream` flag in `eb logs`

# Stream error logs
eb logs --stream -g /var/log/httpd/error_log

# Use `eb ssh` to view instance logs in /opt/python/log/application.log
# Or just use `eb log` and look under `/opt/python/log/application.log`

# See application.py for an example of how to store logs

# TODO can't figure out how to stream application.log
# I believe it requires setting up an .ebextension as show here: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.cloudwatchlogs.html#AWSHowTo.cloudwatchlogs.loggroups#AWSHowTo.cloudwatchlogs.files
# But it probably is not worth the effort
```

Connect to S3
-------------
```
By creating a bucket with a name starting with `elasticbeanstalk-`, you will automatically have access.
See save/ and load/ endpoints of the application for an example for using s3 with boto3.

```

Flask app
---------
```
# Run:
python application.py
# Test:
python -m pytest
```

Commands
--------

```
eb init
# Initialize a new eb application

eb create
# Create a new environment (staging, production, testing etc), and upload it to aws.
# load balancer type 2 is always the right choice.
# Use `eb list` to list environments.

eb deploy
# Deploy most recent git commit

eb open
# Open server, similar to `heroku open`.

# Show some status
eb status
eb health

# Change default enviroment
eb use

eb logs
eb logs --stream -g /var/log/eb-activity.log

eb terminate

eb ssh



# Heroku commands to mimic:

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
