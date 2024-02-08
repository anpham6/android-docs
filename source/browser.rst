=======
Browser
=======

- ES2018

Download
========

android
-------

- https://unpkg.com/squared/dist/squared.min.js
- https://unpkg.com/squared/dist/squared.base.min.js
- https://unpkg.com/squared/dist/android.framework.min.js

chrome
------

- https://unpkg.com/squared/dist/squared.min.js
- https://unpkg.com/squared/dist/squared.base.min.js
- https://unpkg.com/squared/dist/chrome.framework.min.js

vdom
----

- https://unpkg.com/squared/dist/squared.min.js
- https://unpkg.com/squared/dist/squared.base-dom.min.js
- https://unpkg.com/squared/dist/vdom.framework.min.js

.. _browser-download-vdom-lite:

vdom-lite
---------

- https://unpkg.com/squared/dist/squared.min.js
- https://unpkg.com/squared/dist/vdom-lite.framework.min.js

Usage
=====

Library files are in the ``/dist`` folder. A minimum of **two** files are required to run the application.

#. **squared**
#. **squared-base** [#]_
#. *squared-svg* [#]_
#. **framework** [#]_
#. *extensions*

Usable combinations: 1-2-4 + 1-2-4-5 + 1-2-3-4-5 + 1-vdom-lite

File bundles for common combinations are available in the ``/dist/bundles`` folder and do not require a call to *setFramework*.

.. [#] android | chrome | vdom
.. [#] android
.. [#] android | chrome | vdom | vdom-lite