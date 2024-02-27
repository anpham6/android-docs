====
VDOM
====

A minimal framework that is primarily for debugging elements in `DevTools <https://developer.chrome.com/docs/devtools>`_ console. The :ref:`lite <browser-download-vdom-lite>` version is half the download size :alt:`(55kb gzipped)` and was built for browser applications.

Example usage
=============

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