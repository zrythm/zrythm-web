# zrythm-web

Website source for https://www.zrythm.org

This project was forked from the GNUnet website source code,
which was licensed under the GPLv3 and includes all Copyright notices of the
original authors.

The original project can be found here:
https://git.gnunet.org/www.git/

# Environment
Create a file called `.credentials` with the following
content:
```
export PAYPAL_CLIENT_ID=
export PAYPAL_SECRET=
export ZRYTHM_ACCOUNTS_TOKEN=
export VERIFY_TRIAL_PACKAGE_URLS=
export GET_VERSION=
```

These are used for fetching order data. Setting them to
empty values will skip fetching order data.

# Building
`make` will create the full bundle in directory `rendered`

# Dependencies
- python-babel
- python-feedparser
- python-polib
- python-semver
- sass

----

Copyright (C) 2019-2021 Alexandros Theodotou

Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.
