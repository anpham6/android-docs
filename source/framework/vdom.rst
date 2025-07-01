====
VDOM
====

A minimal framework that is primarily for debugging elements in `DevTools <https://developer.chrome.com/docs/devtools>`_ console. The :ref:`lite <browser-download-vdom-lite>` variation is 25% smaller :alt:`(80kb gzipped)` and was built for web applications.

Example usage
=============

.. code-block:: html
  :caption: ESM [#]_

  <script type="importmap">
    {
      "imports": {
        "squared/": "/js/squared/"
      }
    }
  </script>
  <script type="module">
    import { userSettings, fromElement, getElementById, querySelectorAll } from 'squared/vdom.js';

    document.addEventListener("DOMContentLoaded", async () => {
      userSettings({ // Optional
        createElementMap: true,
        pierceShadowRoot: true,
        adaptStyleMap: true,
        showErrorMessages: true
      });

      const elements = await querySelectorAll("*");
      /* OR */
      const element = await fromElement(document.body);
      /* OR */
      const elements = await getElementById("content-id").querySelectorAll("*");
    });
  </script>

.. caution:: Import maps is part of `Baseline 2023 <https://webstatus.dev/features/import-maps>`_ and is :target:`Newly available`.

.. code-block:: html
  :caption: base-dom

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base-dom.min.js"></script>
  <script src="/dist/vdom.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(vdom, {/* UserSettings */});

      const elements = await squared.querySelectorAll("*");
      /* OR */
      const element = await squared.fromElement(document.body);
      /* OR */
      const elements = await squared.getElementById("content-id").querySelectorAll("*");
    });
  </script>

.. code-block:: html
  :caption: lite

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/vdom-lite.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", () => {
      squared.setFramework(vdom);

      const element = squared.querySelector("body", true); // Synchronous
      /* OR */
      const element = squared.fromElement(document.body, true);
    });
  </script>

.. tip:: Synchronous is the recommended way to query when you are not concerned with image dimensions.

.. [#] https://caniuse.com/import-maps