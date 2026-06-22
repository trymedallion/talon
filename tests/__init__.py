from __future__ import absolute_import
from unittest.mock import *

import talon


# Lightweight replacements for the handful of ``nose.tools`` helpers the test
# suite relies on. ``nose`` is unmaintained and does not run on Python 3.11+
# (it imports the removed ``imp`` module), so we provide the assertions directly
# and run the suite with pytest.
def eq_(a, b, msg=None):
    assert a == b, msg or "%r != %r" % (a, b)


def ok_(expr, msg=None):
    assert expr, msg


def assert_true(expr, msg=None):
    assert expr, msg


def assert_false(expr, msg=None):
    assert not expr, msg


def assert_in(member, container, msg=None):
    assert member in container, msg or "%r not found in %r" % (member, container)


EML_MSG_FILENAME = "tests/fixtures/standard_replies/yahoo.eml"
MSG_FILENAME_WITH_BODY_SUFFIX = ("tests/fixtures/signature/emails/P/"
                                 "johndoeexamplecom_body")
EMAILS_DIR = "tests/fixtures/signature/emails"
TMP_DIR = "tests/fixtures/signature/tmp"

STRIPPED = "tests/fixtures/signature/emails/stripped/"
UNICODE_MSG = ("tests/fixtures/signature/emails/P/"
               "unicode_msg")


talon.init()
