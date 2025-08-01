====
VDOM
====

A minimal framework that is primarily for debugging elements in `DevTools <https://developer.chrome.com/docs/devtools>`_ console. The :ref:`lite <browser-download-vdom-lite>` variation is 25% smaller :alt:`(80kb gzipped)` and was built for web applications.

Example usage
=============

.. code-block:: html
  :caption: base-dom

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base-dom.min.js"></script>
  <script src="/dist/vdom.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(vdom, { pierceShadowRoot: true, adaptStyleMap: true });

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

.. code-block:: html
  :caption: Import maps [#]_

  <script type="importmap">
    {
      "imports": {
        "squared/": "https://unpkg.com/squared@5.6.0/"
        /* OR */
        "squared/": "/node_modules/squared/" // NodeJS
        /* OR */
        "squared/": "/dist/esm/" // Docker
      }
    }
  </script>
  <script type="module">
    import { fromElement, getElementById, querySelectorAll, userSettings } from "squared/vdom.js";
    import { parseColor } from "squared/lib/css.js";

    const blue = parseColor("#0000FF");

    document.addEventListener("DOMContentLoaded", async () => {
      userSettings({ pierceShadowRoot: true, adaptStyleMap: true }); // Optional

      const elements = await querySelectorAll("*");
      /* OR */
      const element = await fromElement(document.body);
      /* OR */
      const elements = await getElementById("content-id").querySelectorAll("*");
    });
  </script>

.. caution:: Import maps is part of `Baseline 2023 <https://webstatus.dev/features/import-maps>`_ and is :target:`Newly available`.

.. code-block:: html
  :caption: ESM

  <script type="module">
    import { vdom, fromElement, getElementById, querySelectorAll, userSettings } from "/dist/vdom.mjs";

    document.addEventListener("DOMContentLoaded", async () => {
      userSettings({ pierceShadowRoot: true, adaptStyleMap: true }); // Optional

      const elements = await querySelectorAll("*");
      /* OR */
      const element = await fromElement(document.body);
      /* OR */
      const elements = await getElementById("content-id").querySelectorAll("*");

      const { application } = vdom.cached(); // Application instance
    });
  </script>

.. note:: Libraries :alt:`(squared.lib)` are not exported when using an ES bundle.

.. [#] https://caniuse.com/import-maps