import logging
from nose2.events import Plugin
from slack_log_handler import SlackLogHandler


class SlackLog(Plugin):
    configSection = 'slacklog'
    commandLineSwitch = (None, 'slacklog', 'notify failed test case')

    def __init__(self, *args, **kwargs):
        super(SlackLog, self).__init__(*args, **kwargs)
        self._config = {
            'webhook_url': self.config.as_str('webhook_url', default=None),
            'username':  self.config.as_str('username', default='bot')
        }
        slack_handler = SlackLogHandler(self._config['webhook_url'],
                                        username=self._config['username'],
                                        emojis={
                                            logging.INFO: ":white_circle:",
                                            logging.DEBUG: ":black_circle:",
                                            logging.ERROR: ":red_circle:"
                                        })
        logFormat = "%(asctime)s %(levelname)s %(message)s"
        formatter = logging.Formatter(fmt=logFormat)
        slack_handler.setFormatter(formatter)
        self.logger = logging.getLogger("slacklog")
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(slack_handler)
        self.logger.setLevel(logging.DEBUG)

    def testOutcome(self, event):
        """
        Reports the outcome of each test
        """
        test_case_import_path = event.test.id()
        if event.outcome in ['failed', 'error']:
            if event.exc_info:
                message = event.exc_info[0]
            try:
                self.logger.error("{} {} {}".format(test_case_import_path, event.outcome, message))
            except Exception:
                pass

    def afterSummaryReport(self, event):
        """
        After everything is done, send log
        """

        self.logger.info("test finished")
