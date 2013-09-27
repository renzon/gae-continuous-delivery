#!/bin/bash

# This script need the following environment variables:
# APP_NAME: The app id to deploy on google app engine
# BOT_EMAIL: a bot email  which is developer or admin on google app engine project
# BOT_PASSWORD: bot password
# GAE_SDK: The google app engine SDK directory
# BRANCH: the git branch to deploy

set -e  # If occur any error, exit
set -x  # Verbose mode

continuous_delivery/build.sh

$GAE_SDK/appcfg.py update build --email=$BOT_EMAIL --passin <<<"$BOT_PASSWORD"

$GAE_SDK/appcfg.py set_default_version build --email=$BOT_EMAIL --passin <<<"$BOT_PASSWORD"
