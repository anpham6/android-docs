=======
Android
=======

The primary function ``parseDocument`` can be called on multiple elements and multiple times per session. The application will continuously and progressively build the layout files into a single entity with combined shared resources.

.. warning:: Calling **save** or **copy** methods before the images or fonts have completely loaded can cause them to be excluded from the generated layout. In these cases you should use the asynchronous :code:`await parseDocument()` or :code:`parseDocument().then()` and not ``parseDocumentSync``.

Example usage
=============

.. code-block:: html

  <script src="/dist/squared.min.js"></script>
  <script src="/dist/squared.base.min.js"></script>
  <script src="/dist/squared.svg.min.js"></script>
  <script src="/dist/android.framework.min.js"></script>
  <script>
    squared.settings.targetAPI = 34; // Optional

    document.addEventListener("DOMContentLoaded", async () => {
      squared.setFramework(android, {/* settings */});

      await squared.parseDocument(); // Node (document.body)
      /* OR */
      await squared.parseDocument(document.querySelector("main"), "fragment-id", /* ...element */); // Node[]
      /* OR */
      await squared.parseDocument(
        { // Custom settings do not affect other layouts
          element: document.body,
          projectId: "project-1", // Default is "_"

          resourceQualifier: "land", // "res/*" folder suffix
          /* OR */
          resourceQualifier: {
            suffix: "land", // Used for "true" or "undefined" groups
            layout: true, // Will copy to "res/layout-land" when "suffix" is defined
            font: false, // Will not copy anything to "res/font" or "res/font-land"
            image: "hdpi", // Will copy to "res/drawable-hdpi"
            video: "w720dp", // Will copy to "res/raw-w720dp"
            audio: "w720dp", // Same as "video" and treated separately
            animation: "v34", // Will copy to "res/anim-v34"
            menu: "", // Will copy to default location "res/menu"
            string: undefined, // Will copy to default location "res/values" when "suffix" is undefined
            integer: undefined,
            fraction: undefined,
            array: undefined,
            color: undefined,
            dimension: undefined,
            style: undefined,
            theme: undefined
          },
          excludeQuery: [
            { selector: "main > article" }, // Hide elements
            {
              // Bypass processing routines
              resource: NODE_RESOURCE.BOX_STYLE, // squared.base.lib.constant
              procedure: NODE_PROCEDURE.OPTIMIZATION,
              section: APP_SECTION.DOM_TRAVERSE
            }
          ],

          /* Extensions */
          include: ["android.substitute"], // Automatically removed after finalize
          exclude: ["squared.list", "squared.grid"], // Disabled only during parseDocument

          /* Optional features */
          enabledMultiline: false,
          enabledSubstitute: true,

          /* Callback events */
          afterCascade(sessionId, node) {/* Restore previous state */},
          beforeCascade(sessionId) {/* Edit element attributes */},
          beforeRender(layout) {/* Edit initial values */},
          afterFinalize(node) {/* Edit controller values */}
        },
        { // Only "element" is required
          element: "fragment-1",
          projectId: "project-1", // Implicit once projectId is not "_"
          resourceQualifier: "port",
          pathname: "app/src/main/res/layout-hdpi", // Will not be overridden by resourceQualifier "port"
          filename: "fragment.xml",
          baseLayoutAsFragment: true,
          baseLayoutAsFragment: ["com.example.fragment", "fragment-tag", "document_id"],
          baseLayoutAsFragment: {
              name: "androidx.navigation.fragment.NavHostFragment",
              documentId: "main_content",
              app: {
                  navGraph: "@navigation/product_list_graph",
                  defaultNavHost: "true"
              }
          }
        }
      );
      await squared.parseDocument({
        element: "fragment-2",
        projectId: "project-2", // Will not conflict with projectId "project-1"
        resourceQualifier: "port",
        enabledFragment: true,
        fragmentableElements: [
          { selector: "main", name: "com.example.fragment", filename: "fragment.xml", documentId: "main_content" }, // document.querySelector
          "main > article" // document.querySelectorAll (declarative double nested fragments are invalid)
        ],
        options: {
          "android.resource.fragment": {
            dynamicNestedFragments: true // FragmentContainerView or FrameLayout as the container (name and tag are ignored)
          }
        }
      });

      await squared.close("project-1"); // Next call to "parseDocument" will reset project (optional)

      // File actions - implicitly calls "close"

      await squared.save(); // Uses defaults from settings
      /* OR */
      await squared.saveAs("project.zip", { projectId: "project-1" });
      await squared.saveAs("default.7z", { throwErrors: true }).catch(err => console.log(err)); // Will cancel partial archive download
      /* OR */
      await squared.copyTo("/path/project-1", { ignoreExtensions: true, profileable: true });
      /* OR */
      await squared.appendTo("http://localhost:3000/archives/project.001", { format: "7z" });

      squared.reset(); // Start new "parseDocument" session (optional)
    });
  </script>

.. code-block::
  :caption: Cross-origin support

  squared.prefetch("css").then(() => squared.parseDocument()); // Chromium
  /* OR */
  Promise.all(
    squared.prefetch("css", true), // All stylesheets
    squared.prefetch("css", "./undetected.css", element.shadowRoot),
    squared.prefetch("svg", "http://embedded.example.com/icon.svg", "../images/android.svg")
  )
  .then(() => squared.parseDocument());

.. code-block::
  :caption: Kill request

  squared.kill("30s").then(pid => { // Abort next request in 30 seconds
    if (pid > 0) {
      /* KILLED */
    }
  });
  /* OR */
  await squared.saveAs("project.zip", { timeout: 10 }); // Cancels request if not complete in 10 seconds

.. code-block::
  :caption: Modify attributes

  squared.parseDocument().then(() => {
    const body = squared.findDocumentNode(document.body);
    body.android("layout_width", "match_parent");
    body.lockAttr("android", "layout_width");
  });

.. code-block::
  :caption: Observe element attributes

  await squared.parseDocument({
    element: document.body,
    observe(mutations, observer, settings) {
      squared.reset(); // Required after a File action
      squared.parseDocument(settings).then(() => {
        squared.copyTo("/path/project", { modified: true }).then(response => console.log(response));
      });
    }
  });
  squared.observe();

.. code-block::
  :caption: Observe element source files

  await squared.observeSrc(
    "link[rel=stylesheet]",
    (ev, element) => {
      squared.reset();
      squared.parseDocument().then(() => squared.copyTo("/path/project"));
    },
    { // squared.json
      port: 8080,
      secure: false,
      action: "reload",
      expires: "1h"
    }
  );