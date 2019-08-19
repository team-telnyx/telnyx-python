from __future__ import absolute_import, division, print_function

import sys
from collections import namedtuple

from telnyx import util
from telnyx.six.moves import builtins

PRINT_FUNC_STRING = builtins.__name__ + ".print"

LogTestCase = namedtuple("LogTestCase", "env flag should_output")
FmtTestCase = namedtuple("FmtTestCase", "props expected")


class TestUtil(object):
    DUMMY_REQ_ID = "req_qsxPhqHyLxcoaM"

    def log_test_loop(self, test_cases, logging_func, logger_name, mocker):
        for case in test_cases:
            try:
                logger_mock = mocker.patch(logger_name)
                print_mock = mocker.patch(PRINT_FUNC_STRING)
                mocker.patch("telnyx.log", case.flag)
                mocker.patch("telnyx.util.TELNYX_LOG", case.env)

                logging_func("foo \nbar", y=3)  # function under test

                if case.should_output:
                    print_mock.assert_called_once_with(
                        "message='foo \\nbar' y=3", file=sys.stderr
                    )
                else:
                    print_mock.assert_not_called()
                logger_mock.assert_called_once_with("message='foo \\nbar' y=3")
            finally:
                mocker.stopall()

    def test_log_debug(self, mocker):
        # (TELNYX_LOG, telnyx.log): should_output?
        test_cases = [
            LogTestCase(env=None, flag=None, should_output=False),
            LogTestCase(env=None, flag="debug", should_output=True),
            LogTestCase(env=None, flag="info", should_output=False),
            LogTestCase(env="debug", flag=None, should_output=True),
            LogTestCase(env="debug", flag="debug", should_output=True),
            LogTestCase(env="debug", flag="info", should_output=False),
            LogTestCase(env="info", flag=None, should_output=False),
            LogTestCase(env="info", flag="debug", should_output=True),
            LogTestCase(env="info", flag="info", should_output=False),
        ]
        self.log_test_loop(
            test_cases,
            logging_func=util.log_debug,
            logger_name="telnyx.util.logger.debug",
            mocker=mocker,
        )

    def test_log_info(self, mocker):
        # (TELNYX_LOG, telnyx.log): should_output?
        test_cases = [
            LogTestCase(env=None, flag=None, should_output=False),
            LogTestCase(env=None, flag="debug", should_output=True),
            LogTestCase(env=None, flag="info", should_output=True),
            LogTestCase(env="debug", flag=None, should_output=True),
            LogTestCase(env="debug", flag="debug", should_output=True),
            LogTestCase(env="debug", flag="info", should_output=True),
            LogTestCase(env="info", flag=None, should_output=True),
            LogTestCase(env="info", flag="debug", should_output=True),
            LogTestCase(env="info", flag="info", should_output=True),
        ]
        self.log_test_loop(
            test_cases,
            logging_func=util.log_info,
            logger_name="telnyx.util.logger.info",
            mocker=mocker,
        )

    def test_logfmt(self):
        cases = [
            FmtTestCase(
                props={"foo": "bar", "message": "yes"}, expected="foo=bar message=yes"
            ),
            FmtTestCase(props={"foo": "bar baz"}, expected="foo='bar baz'"),
            FmtTestCase(props={"b": 2, "a": 1, "c": 3}, expected="a=1 b=2 c=3"),
            FmtTestCase(
                props={"key with space": True}, expected="'key with space'=True"
            ),
        ]
        for case in cases:
            result = util.logfmt(case.props)
            assert result == case.expected
