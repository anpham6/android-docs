VDOM
====

A minimal framework (50kb gzipped) that is useful for debugging in DevTools console. The :any:`lite <browser-download-vdom-lite>` version is half the download size and was built for browser applications.

Example usage
-------------

.. code-block:: html
  :caption: base-dom

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base-dom.min.js"></script>
  <script src="/dist/vdom.framework.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(vdom, {/* settings */});

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
      squared.setFramework(vdom, {/* settings */});

      const element = squared.querySelector("body", true); // Synchronous
      /* OR */
      const element = squared.fromElement(document.body, true);
    });
  </script>