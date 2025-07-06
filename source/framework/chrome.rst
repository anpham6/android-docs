======
Chrome
======

Uses the :doc:`vdom` framework as the element base but can also export any used resources for further processing. It is adequate for most single page applications and gives you the ability to preview your application before building a working copy of it.

Example usage
=============

.. code-block:: html

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base.min.js"></script>
  <script src="/dist/chrome.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(chrome, {/* UserResourceSettings */});

      await squared.save(); // Uses defaults from settings
      /* OR */
      await squared.saveAs("android.zip", {/* RequestData */});
      /* OR */
      await squared.copyTo("/path/project", {/* RequestData */});
      /* OR */
      await squared.appendTo("/path/to/android.7z", {/* RequestData */});
    });
  </script>

.. code-block:: html
  :caption: Import maps [#]_

  <script type="importmap">
    {
      "imports": {
        "squared/": "/js/squared/"
      }
    }
  </script>
  <script type="module">
    import { appendTo, copyTo, save, saveAs, userSettings } from "squared/chrome.js";
    import { parseColor } from "squared/lib/css.js";

    const blue = parseColor("#0000FF");

    document.addEventListener("DOMContentLoaded", async () => {
      userSettings({ preloadImages: true, preloadFonts: true }); // Optional

      await save(); // Uses defaults from settings
      /* OR */
      await saveAs("android.zip", {/* RequestData */});
      /* OR */
      await copyTo("/path/project", {/* RequestData */});
      /* OR */
      await appendTo("/path/to/android.7z", {/* RequestData */});
    });
  </script>

.. caution:: Import maps is part of `Baseline 2023 <https://webstatus.dev/features/import-maps>`_ and is :target:`Newly available`.

.. code-block:: html
  :caption: ESM

  <script type="module">
    import { chrome, appendTo, copyTo, save, saveAs, userSettings } from "/dist/chrome.mjs";

    document.addEventListener("DOMContentLoaded", async () => {
      userSettings({ preloadImages: true, preloadFonts: true }); // Optional

      await save(); // Uses defaults from settings
      /* OR */
      await saveAs("android.zip", {/* RequestData */});
      /* OR */
      await copyTo("/path/project", {/* RequestData */});
      /* OR */
      await appendTo("/path/to/android.7z", {/* RequestData */});

      const app = chrome.cached(); // Current framework installed
      chrome.lib.constant.UUID.JS = '16'; // Length of auto-generated filenames
    });
  </script>

.. note:: Libraries :alt:`(squared.lib)` are not exported when using an ES bundle.

.. code-block::
  :caption: Observe element

  await squared.copyTo("/path/project", { useOriginalHtmlPage: false, observe: true }).then(() => {
    squared.observe(); // Watch all events
    /* OR */
    squared.observe({
      subtree: true,
      childList: true,
      attributes: true,
      characterData: true,
      attributeOldValue: true,
      characterDataOldValue: true
    });
  });

.. [#] https://caniuse.com/import-maps