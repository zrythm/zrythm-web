# zrythm-web

Website source for https://www.zrythm.org

This project was forked from the GNUnet website source code,
which was licensed under the GPLv3 and includes all Copyright notices of the
original authors.

The original project can be found here:
https://git.gnunet.org/www.git/

# Environment
Set `SENDOWL_KEY`, `SENDOWL_SECRET`, `PAYPAL_CLIENT_ID`
and `PAYPAL_SECRET` to get order data.

These should be in `.credentials`:
```
export SENDOWL_KEY=...
export SENDOWL_SECRET=...
export PAYPAL_CLIENT_ID=...
export PAYPAL_SECRET=...
```

# Building
`make` will create the full bundle in `rendered`

# Dependencies
`python-babel` `python-feedparser` `python-polib`

----

Copyright (C) 2019-2020 Alexandros Theodotou

Copying and distribution of this file, with or without modification,
are permitted in any medium without royalty provided the copyright
notice and this notice are preserved.  This file is offered as-is,
without any warranty.
