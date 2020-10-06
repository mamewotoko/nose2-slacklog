# nose2_slacklog

## Setup

```
pip install -r requirements.txt
```

## Configuration

set webhook_url

```
[unittest]
plugins = nose2_slacklog.slacklog

[slacklog]
always-on = True
webhook_url = https://hooks.slack.com/services/xxxx
username = nose2test
```

## Usage
If you have `always-on=True` inside your `nose2.cfg`:

```
nose2
```

----
Takashi Masuyama < mamewotoko@gmail.com >
https://mamewo.ddo.jp/
