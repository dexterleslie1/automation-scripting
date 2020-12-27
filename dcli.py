#!/usr/bin/python2
# -*- coding: UTF-8 -*-

import fire
import cli_freeswitch
import cli_openresty
import cli_kamailio
import cli_develop_env
import logging


class Dcli(object):
    def __init__(self):
        self.openresty = cli_openresty.OpenrestyCli()
        self.freeswitch = cli_freeswitch.FreeswitchCli()
        self.kamailio = cli_kamailio.KamailioCli()
        self.develop_env = cli_develop_env.DevelopEnvCli()


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    fire.Fire(Dcli)
