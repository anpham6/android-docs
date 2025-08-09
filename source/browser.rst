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
- https://unpkg.com/squared/dist/android.framework.min.js :alt:`(ES2020)`

chrome
------

- https://unpkg.com/squared/dist/squared.min.js
- https://unpkg.com/squared/dist/squared.base.min.js
- https://unpkg.com/squared/dist/chrome.framework.min.js :alt:`(ES2020)`

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

File bundles for common combinations are available in the ``/dist/bundles`` folder and do not require a call to :target:`setFramework`.

ES Modules
==========

Bundle
------

A single file with no exports outside of the core methods.

- https://unpkg.com/squared/dist/android.mjs
- https://unpkg.com/squared/dist/chrome.mjs
- https://unpkg.com/squared/dist/vdom.mjs

.. code-block:: html
  :caption: ES2021

  <script type="module">
    import { parseDocument } from "https://unpkg.com/squared/dist/android.mjs";
  <script>

Import maps
-----------

Possibly hundreds of files with all exports and core methods.

- https://unpkg.com/squared/android.js
- https://unpkg.com/squared/chrome.js
- https://unpkg.com/squared/vdom.js

.. code-block:: html
  :caption: ES2021

  <script type="module">
    import { parseDocument } from "https://unpkg.com/squared/android.js";
  <script>

.. tip:: Fastest and easiest to use is the traditional :alt:`(UMD)` non-modular namespaced global reference :target:`squared`. ESM is more appropriately used when bundled into one application :alt:`(web)` and not used with import maps :alt:`(development)`.

.. [#] android | chrome | vdom
.. [#] android
.. [#] android | chrome | vdom | vdom-lite