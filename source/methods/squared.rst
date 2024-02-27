=======
squared
=======

.. function:: setHostname(value)

  Use another :abbr:`CORS (Cross-Origin Resource Sharing)`-enabled server for processing assets.

  :param string value: http(s)://hostname(:port)

  Usage::

    squared.setHostname("https://localhost:8000");

    squared.setHostname(); // Reset to window.location (e.g. localhost:3000)

.. function:: setEndpoint(name, value)

  Set alternate pathname for API v1 functions.

  :param string name: *ASSETS_COPY* | *ASSETS_ARCHIVE* | *LOADER_DATA* | *THREADS_KILL* | *WEBSOCKET_OBSERVE*
  :param string value: Absolute path to server *GET/POST* method

  Usage::

    squared.setEndpoint("ASSETS_COPY", "/api/v2/assets/copy");

.. function:: setLocalAddress(...values)

  Additional hostnames which are interpreted as localhost. Protocol and port are not required.

  :param string values: Same format as URL.hostname

  Usage::

    squared.setLocalAddress("127.0.0.1", "nodejs-001");

  Alternate::

    squared.setLocalAddress(new URL("http://0.0.0.0"));

.. function:: auth(token)

  Set :abbr:`JWT (JSON Web Token)` authorization token for all requests

  :param string token: Three concatenated Base64url-encoded strings separated by dots

  Usage::

    squared.auth("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNxdWFyZWQiLCJwYXNzd29yZCI6Imp3dDEyMyIsImlhdCI6MTY1MjcxNDQwMH0.xqwQ96LsItilsB1dskzJQqXORaZ4mGMu0FeZezo297c");

.. function:: kill([pid, timeout])

  Abort request if not completed in the given amount of time.

  :param number pid: (optional) File request self-assigned number :alt:`(options.pid)`
  :param number timeout: (optional) Seconds until request expires
  :returns: Promise<number>

  Usage::

    squared.saveAs("example.zip", { pid: 100 });
    squared.kill(100).then(result => {
      if (result > 0) {
        /* KILLED */
      }
    });

    squared.kill(); // Terminate previous request
    squared.kill(0); // By username (auth required)

    squared.kill(-1, 10); // Terminate previous request in 10 seconds
    squared.kill(NaN, 0.5); // Terminate next request in 500 milliseconds

  Alternate::

    squared.kill(-1, "10s"); // Terminate previous request in 10 seconds
    squared.kill("500ms"); // Terminate next request in 500 milliseconds

.. function:: broadcast(callback, socketId)

  Redirect stdout messages to DevTools console.

  :param function callback: See |BroadcastMessageCallback|
  :param string socketId: Unique identifier assigned during server initialization
  :returns: boolean

  Usage::

    squared.broadcast(result => { console.log(result.value); }, "111-111-111"); // Uses "socketId"
    squared.broadcast(result => { console.log(result.value); }, "222-222-222");

    squared.copyTo("/path/to/project", { broadcastId: ["111-111-111", "222-222-222"] });

  Alternate::

    squared.copyTo("/path/to/project", {
      broadcast: {
        socketId: "111-111-111",
        callback: result => {
          console.log(result.value);
        }
      }
    });

    // Messages sent from another API (FileBroadcastOptions)
    squared.broadcast(result => { console.log(result.value); }, { // Uses "socket_id"
      socketId: "333-333-333",
      socketKey: "socket_id",
      secure: true,
      hostname: "1.1.1.1",
      port: 8080
    });

.. function:: setFramework(target[, options, cache])

  Install application interpreter. :alt:`(e.g. android.framework.js)`

  :param object target: Global object implementing |AppFramework|
  :param object options: (optional) Initialize settings with non-default values
  :param boolean cache: (optional) Load previous cached instance and settings

  Usage::

    squared.setFramework(android);
    squared.setFramework(android, true); // Used when switching frameworks
    squared.setFramework(android, { targetAPI: 34, idNamingStyle: "html" });

  Alternate::

    // Save
    squared.setFramework(android, { targetAPI: 26, enabledIncludes: true }, "example"); // Local storage

    // Load
    squared.setFramework(android, "example");

.. function:: extend(map[, framework])

  Add functions and initial variables to the |Node| prototype including overwriting preexisting class definitions. Accessor properties are supported using the *get/set* object syntax.

  :param object map: Attribute object consisting of extensions and overrides
  :param number framework: (optional) See |APP_FRAMEWORK|

  Usage::

    squared.extend({
      _id: 1,
      altId: {
        get() {
          return this._id;
        },
        set(value) {
          this._id += value;
        }
      },
      customId: {
        value: 2,
        configurable: false,
        enumerable: false
      },
      addEvent(eventName, callback) {
        this.element.addEventListener(eventName, callback);
      }
    });
    squared.setFramework(vdom);

    const body = await squared.fromElement(document.body);
    body.altId = 2; // 3
    body.altId = 2; // 5
    body.addEvent("click", function (ev) {
      this.classList.toggle("example");
    });

    squared.extend({ _preferInitial: true }, APP_FRAMEWORK.VDOM /* 1 */ | APP_FRAMEWORK.CHROME /* 4 */); // squared.base.lib.constant
    squared.setFramework(chrome);

.. function:: clear()

  Calls |Application|.clear() for any loaded frameworks and deletes all cached sessions.

  Usage::

    squared.clear();

.. function:: add(...targets)

  Include extensions to be processed with any built-in extensions.

  :param targets: Name of disabled extension or control implementing |Extension|
  :param targets: Tuple of extension and configuration object
  :returns: number

  Usage:

  .. code-block:: javascript

    class Drawer extends squared.base.ExtensionUI {
      constructor(name, framework, options) {
        super(name, framework, options);
        this.options = {
          element: {},
          resource: {},
          self: {},
          navigationView: {}
        };
        this.documentBase = true;
        this.require({ name: "android.external", leading: true });
        this.require("android.widget.menu");
        this.require("android.widget.coordinator");
      }
    }

    const drawer = new Drawer("android.widget.drawer", squared.base.lib.constant.APP_FRAMEWORK.ANDROID /* 2 */);
    squared.add(drawer);

    // Built-in
    squared.add("android.resource.includes");

    const options = {
      element: {
        content: { android: { layout_width: "match_parent" } }
      }
    };
    squared.add(["android.substitute", options]);

.. function:: remove(...targets)

  Exclude extensions by name or control.

  :param targets: Name or control of extensions
  :returns: number

  Usage::

    const drawer = new Drawer("android.widget.drawer", 2);
    squared.add(drawer);

    squared.remove(drawer);
    /* OR */
    squared.remove("android.widget.drawer");

.. function:: get(...targets)

  Retrieve extensions by name only.

  :param string targets: Name of extension
  :returns:
    - |Extension| | undefined
    - |Extension|\[\] :alt:`(multiple)`

  Usage::

    const drawer = squared.get("android.widget.drawer");
    const [drawer, menu] = squared.get("android.widget.drawer", "android.widget.menu");

    drawer.options.navigationView.android = { fitsSystemWindows: "true" };
    menu.project.set(document.getElementId("child-item-id"), await fetch("http://localhost:3000/drawer/menu.json"), "project-1" /* optional */); // Add project data

.. function:: attr(target, name[, value])

  Set or get extension options. **typeof** is enforced and will only set existing attributes.

  :param target: Name or control of extension
  :param string name: Name of attribute in |Extension|.options
  :param value: Any value of an existing attribute
  :returns: unknown

  Usage::

    const items = squared.attr("android.substitute", "viewAttributes" /* string[] */);
    items.push("hint", "buttonTint");
    /* OR */
    squared.attr("android.substitute", "viewAttributes", items.concat(["hint", "buttonTint"]));

    squared.attr("android.substitute", "attributeMapping", { "android:src": "app:srcCompat", "icon": "navigationIcon" }); // Set only and does not merge

.. function:: apply(target, options[, setting])

  Find extension and merge a configuration object with existing |Extension|.options.

  :param target: Name or control of extension
  :param object options: Overriding configuration values
  :param string setting: (optional) Name to use when saving to local storage
  :returns: boolean

  Usage::

    squared.apply("android.widget.toolbar", {
      element: {
        "toolbar-id": {
          android: {
            background: "?android:attr/windowBackground"
          },
          appBar: {
            android: {
              theme: "@style/ThemeOverlay.AppCompat.Dark.ActionBar"
            }
          }
        }
      },
      "toolbar-example" // Save
    });

  Alternate::

    squared.apply("android.widget.toolbar", "toolbar-example"); // Load

.. function:: prefetch(type[, all, ...targets])

  Downloads assets to a memory cache which can be used by an |Application| framework. Provides cross-origin support for CSS.

  :param string type: *css* | *javascript* | *image* | *svg*
  :param boolean all: (:sub:`optional (targets)`) Accept request from any origin
  :param targets: (optional) URL string or root element of a contained Document
  :returns: Promise<|PrefetchItem|\[\]>

  Usage::

    squared.prefetch("css").then(() => squared.parseDocument()); // Cross-origin support

    Promise.all(
      squared.prefetch("css", true), // All stylesheets
      squared.prefetch("css", "./undetected.css", document.getElementById("shadow-id").shadowRoot),
      squared.prefetch("svg", "http://example.com/icon.svg", "../images/android.svg")
    )
    .then(() => squared.parseDocument());

.. function:: parseDocument(...elements)

  Starts at the root target element and creates a virtual DOM structure by cascading into all the children. Assets can be preloaded :alt:`(e.g. images)` which is required with the :doc:`android </framework/android>` framework.

  :param elements: (optional) |targetElement|
  :param elements: (optional) See |ElementSettings|
  :returns:
    - Promise<|Node| | void>
    - Promise<|Node|\[\]> :alt:`(multiple)`

  Usage::

    const body = await squared.parseDocument();

    const section = await squared.parseDocument({
      element: "section-1",
      projectId: "sqd",
      resourceQualifier: "land",
      enabledIncludes: true
    });

.. function:: parseDocumentSync(...elements)

  Starts at the root target element and creates a virtual DOM structure by cascading into all the children. No assets are preloaded which is sufficient for the :doc:`vdom </framework/vdom>` framework.

  :param elements: (optional) |targetElement|
  :param elements: (optional) See |ElementSettings|
  :returns:
    - |Node| | undefined
    - |Node|\[\] :alt:`(multiple)`

  Usage::

    const body = squared.parseDocumentSync();

    const content = squared.parseDocumentSync("content-1");

.. function:: findDocumentNode(target[, all, projectId])

  Can be used before saving rendered document to modify auto-generated |Node| attributes.

  :param target: |targetElement| (selectors are supported)
  :param boolean all: (:sub:`optional (projectId)`) Uses filter to return multiple results
  :param string projectId: (optional) Uses an existing project in the current framework
  :returns:
    - |Node| | undefined
    - |Node|\[\] :alt:`(all)`

  Usage::

    const body = squared.findDocumentNode(document.body);
    const content = squared.findDocumentNode("content-1");

    const section1 = squared.findDocumentNode("section"); // Only if no element has id="section"
    const [section2, section3] = squared.findDocumentNode("main > section", true); // Always an array with "all"

  Alternate::

    const layout = squared.findDocumentNode("relativelayout-1", "project-1"); // Control id
    layout.android("layout_width", "match_parent");

.. function:: latest([count = 1])

  Get any stored session ids from :func:`parseDocument` since the last time :func:`clear` was called.

  :param number count: (optional) How many ids at most to be retrieved
  :returns: string | string[] | undefined

  Usage::

    squared.parseDocument("id-1", "id-2", "id-3").then(() => {
      // ["00001", "00002", "00003"]
      const id3 = squared.latest();
      const id1 = squared.latest(-1);
      const [id2, id3] = squared.latest(2);
      const [id2, id1] = squared.latest(-2);
    });

.. function:: close([projectId])

  Ends the current session or selected project preventing any further modifications. It is called internally when saving or copying.

  :param string projectId: (optional) Targets a project that is not the latest
  :returns: Promise<boolean>

  Usage::

    await squared.close(); // Optional

.. function:: reset([projectId])

  Abandons all stored projects and sets a loaded |Application| to its initial state. The current user settings are retained.

  :param string projectId: (optional) Targets a project that is not the latest

  Usage::

    squared.reset(); // Optional

.. function:: save([projectId, timeout])

  Uses the default |Application|.settings to generate an archive of the current session or selected project.

  :param string projectId: (optional) Targets a project that is not the default project
  :param number timeout: (optional) Maximum time in seconds for build to complete
  :returns: |ResponseData|

  Usage::

    squared.save().then(result => console.log(result)); // Default project "_" is used

    await squared.save("project-1", 10); // 10 seconds for "project-1" to build

  Alternate::

    squared.broadcast(result => { console.log(result.value); }, "111-111-111");
    await squared.save("project-1", "111-111-111"); // broadcastId

.. function:: saveAs(filename[, options, setting, overwrite])

  Save current session or selected project as a new archive using *filename* extension.

  :param string filename: Name of file with a valid archive extension
  :param object options: (optional) See |FileActionOptions|
  :param string setting: (optional) Name of setting for local storage
  :param boolean overwrite: (optional) Will not merge previously saved settings with *options*
  :returns: |ResponseData|

  Usage::

    await squared.parseDocument();
    await squared.saveAs("android.zip", { timeout: 15, log: { showSize: true } }); // Uses default unnamed project "_"

    await squared.parseDocument({ element: document.body, projectId: "project-1" });
    await squared.saveAs("project-1.7z", { projectId: "project-1", throwErrors: true }).catch(err => { // Will cancel partial archive download
      console.log(err);
    });

  Alternate::

    // Save
    squared.saveAs("android.zip", { timeout: 15, log: { showSize: true } }, "android-example"); // Uses own "saveAs" namespace

    // Load
    squared.saveAs("android.zip", "android-example"); // Any page in same domain

.. function:: appendTo(uri[, options, setting, overwrite])

  Save current session or selected project into a copy of an existing archive if found or as a new archive using the file extension.

  :param string uri: Location of file with a valid archive extension
  :param object options: (optional) See |FileActionOptions|
  :param string setting: (optional) Name of setting for local storage
  :param boolean overwrite: (optional) Will not merge previously saved settings with *options*
  :returns: |ResponseData|

  Usage::

    squared.parseDocument().then(async () => {
      await squared.appendTo("http://localhost:3000/archives/android.001", { format: "tar" }); // "tar" is explicit (ignored filename)
    });

    await squared.parseDocument({ element: document.body, projectId: "project-1" });
    squared.appendTo("../data/project-1.7z", { projectId: "project-1" }).then(result => { // Uses NodeJS process.cwd() resolution
      console.log(result);
    });

  Alternate::

    // Save
    squared.appendTo("./android.zip", { timeout: 20, log: { showSize: true } }, "android-example"); // Uses own "appendTo" namespace

    // Load
    squared.appendTo("./android.zip", "android-example"); // Any page in same domain

.. function:: copyTo(pathname[, options, setting, overwrite])

  Save current session or selected project to a local directory.

  :param string pathname: Location of a directory accessible to the server process
  :param object options: (optional) See |FileActionOptions|
  :param string setting: (optional) Name of setting for local storage
  :param boolean overwrite: (optional) Will not merge previously saved settings with *options*
  :returns: |ResponseData|

  Usage::

    await squared.parseDocument();
    await squared.copyTo("./path/to/project", { timeout: 10, log: { showSize: true } });

    squared.parseDocument({ element: document.body, projectId: "project-1" }).then(() => {
      squared.copyTo("/path/project", { projectId: "project-1" }).then(result => console.log(result));
    });

  Alternate::

    // Multiple
    squared.copyTo(["/path/project1", "/path/project2"]); // Copies processed files to "project1" and "project2"

    // Save
    squared.copyTo("./path/to/project", { timeout: 10, log: { showSize: true } }, "android-example"); // Uses own "copyTo" namespace

    // Load
    squared.copyTo("./path/to/project", "android-example"); // Any page in same domain

.. function:: saveFiles(filename[, options, setting, overwrite])

  Save selected assets as a new archive using *filename* extension.

  :param string filename: Name of file with a valid archive extension
  :param object options: (optional) See |FileActionOptions|
  :param string setting: (optional) Name of setting for local storage
  :param boolean overwrite: (optional) Will not merge previously saved settings with *options*
  :returns: |ResponseData|

  Usage::

    const options = {
      assets: [
        {
          pathname: "images",
          filename: "android.png",
          uri: "http://localhost:3000/common/images/android.png"
        },
        {
          pathname: "images",
          filename: "android-ldpi.png",
          uri: "http://localhost:3000/common/images/android-ldpi.png"
        },
        {
          pathname: "images",
          filename: "android-hdpi.png",
          uri: "http://localhost:3000/common/images/android-hdpi.png"
        }
      ]
    };
    await squared.saveFiles("android.zip", options);

  Alternate::

    // Save
    squared.saveFiles("android.zip", options, "android-example"); // Uses own "saveFiles" namespace

    // Load
    squared.saveFiles("android.zip", "android-example"); // Any page in same domain

.. function:: appendFiles(uri[, options, setting, overwrite])

  Save selected assets into a copy of an existing archive if found or as a new archive using the file extension.

  :param string uri: Location of file with a valid archive extension
  :param object options: (optional) See |FileActionOptions|
  :param string setting: (optional) Name of setting for local storage
  :param boolean overwrite: (optional) Will not merge previously saved settings with *options*
  :returns: |ResponseData|

  Usage::

    const options = {
      format: "7z",
      assets: [
        {
          pathname: "images",
          filename: "android-xhdpi.png",
          uri: "http://localhost:3000/common/images/android-xhdpi.png"
        },
        {
          pathname: "images",
          filename: "android-xxhdpi.png",
          uri: "http://localhost:3000/common/images/android-xxhdpi.png"
        },
        {
          pathname: "images",
          filename: "android-xxxhdpi.png",
          uri: "http://localhost:3000/common/images/android-xxxhdpi.png"
        }
      ]
    };
    await squared.appendFiles("http://localhost:3000/archives/android.001", options);

  Alternate::

    // Save
    squared.appendFiles("android.zip", options, "android-example"); // Uses own "appendFiles" namespace

    // Load
    squared.appendFiles("android.zip", "android-example"); // Any page in same domain

.. function:: copyFiles(pathname[, options, setting, overwrite])

  Save selected assets to a local directory.

  :param string pathname: Location of a directory accessible to the server process
  :param object options: (optional) See |FileActionOptions|
  :param string setting: (optional) Name of setting for local storage
  :param boolean overwrite: (optional) Will not merge previously saved settings with *options*
  :returns: |ResponseData|

  Usage::

    const options = {
      assets: [
        {
          pathname: "images",
          filename: "android-xhdpi.png",
          uri: "http://localhost:3000/common/images/android-xhdpi.png"
        },
        {
          pathname: "images",
          filename: "android-xxhdpi.png",
          uri: "http://localhost:3000/common/images/android-xxhdpi.png"
        },
        {
          pathname: "images",
          filename: "android-xxxhdpi.png",
          uri: "http://localhost:3000/common/images/android-xxxhdpi.png"
        }
      ]
    };
    await squared.copyFiles("/path/project", options);

  Alternate::

    // Multiple
    squared.copyFiles(["/path/project1", "/path/project2"], options); // Copies assets to "project1" and "project2"

    // Save
    squared.copyFiles("./path/to/project", options, "android-example"); // Uses own "copyFiles" namespace

    // Load
    squared.copyFiles("./path/to/project", "android-example"); // Any page in same domain

.. function:: getElementById(value[, sync, cache = true])

  Same behavior as native ``document.getElementById`` [#]_ except returns a |Node| instance.

  :param string value: Case-sensitive match against *Element*.id property
  :param boolean sync: (optional) Will block and not wrap query in a Promise
  :param boolean cache: (optional) Use any existing |Node| instance of *Element*
  :returns:
    - Promise<|Node| | null>
    - |Node| | null :alt:`(sync)`

  Usage::

    const { element, attributes } = await squared.getElementById("content-id");

    const content = squared.getElementById("content-id", true); // Synchronous
    const child = content?.find(item => item.elementId === "child-id", { cascade: true });

.. function:: querySelector(selector[, sync, cache = true])

  Same behavior as native ``document.querySelector`` [#]_ except returns a |Node| instance.

  :param string selector: Selector or selectors matching one or more elements
  :param boolean sync: (optional) Will block and not wrap query in a Promise
  :param boolean cache: (optional) Use any existing |Node| instance of *Element*
  :returns:
    - Promise<|Node| | null>
    - |Node| | null :alt:`(sync)`

  Usage::

    const { element, attributes } = await squared.querySelector("section img[src=vdom.png]");

    squared.querySelector("body > p", true)?.each(item => { // Synchronous
      if (item.inline) {
        item.css("display", "inline-block");
      }
    });

.. function:: querySelectorAll(selector[, sync, cache = true])

  Same behavior as native ``document.querySelectorAll`` [#]_ except returns an array of |Node| instances.

  :param string selector: Selector or selectors matching one or more elements
  :param boolean sync: (optional) Will block and not wrap query in a Promise
  :param boolean cache: (optional) Use any existing |Node| instance of *Element*
  :returns:
    - Promise<|Node|\[\] | null>
    - |Node|\[\] | null :alt:`(sync)`

  Usage::

    const [img1, img2] = await squared.querySelectorAll("section img");

    const children = await squared.getElementById("content-id")?.querySelectorAll("*");

.. function:: fromElement(element[, sync, cache])

  Same behavior as :func:`getElementById` except it also accepts a native *Element*. The **cache** parameter by default is not enabled.

  :param element: |targetElement|
  :param boolean sync: (optional) Will block and not wrap query in a Promise
  :param boolean cache: (optional) Use any existing |Node| instance of *Element*
  :returns:
    - Promise<|Node|\[\] | null>
    - |Node|\[\] | null :alt:`(sync)`

  Usage::

    const { element, attributes } = await squared.fromElement(document.body);

    const content = squared.fromElement("content-id", true); // Synchronous
    const child = content?.find(item => item.elementId === "child-id", { cascade: true });

.. function:: fromNode(node[, sync, cache])

  Uses an existing |Node| instance and creates a new instance with any modifications. The **cache** parameter by default is not enabled.

  :param object node: See |Node|
  :param boolean sync: (optional) Will block and not wrap query in a Promise
  :param boolean cache: (optional) Use any existing |Node| instance
  :returns:
    - Promise<|Node|\[\] | null>
    - |Node|\[\] | null :alt:`(sync)`

  Usage::

    let body = await squared.fromElement(document.body);
    document.querySelectorAll("body div").forEach(item => document.body.removeChild(item));
    body = await squared.fromNode(body);

    const img = squared.fromNode(body, true).find(item => item.imageElement); // Synchronous

.. function:: observe([enable = true])

  Uses |MutationObserver| to watch for any changes to the :func:`parseDocument` root element. Start after DOM and third-party libraries are initialized.

  :param boolean enable: (optional) Start or stop all root elements who are monitoring

  Usage::

    await squared.parseDocument({
      element: document.body,
      projectId: "project-1",
      observe(mutations, observer, settings) {
        squared.reset("project-1");
        squared.parseDocument(settings).then(() => {
          squared.copyTo("/path/project", { projectId: "project-1", modified: true }).then(result => console.log(result));
        });
      }
    });

    await squared.copyTo("/path/project", { projectId: "project-1", useOriginalHtmlPage: false }).then(() => {
      squared.observe();
    });

    squared.observe(false); // Discontinue monitoring for changes

  Alternate::

    squared.observe({
      subtree: true,
      childList: true,
      attributes: true,
      characterData: false,
      attributeOldValue: false,
      characterDataOldValue: false
    });

.. function:: observeSrc(targets[, callback, options])

  Can be used to watch external elements which contain modifiable source files.

  :param targets: Elements by either selector or *HTMLElement* (**src** or **href** attribute is required)
  :param function callback: (:alt:`optional (options)`) Method to call when a ``modified`` event is received
  :param object options: (optional) See |FileObserveOptions|
  :returns: Promise<|ObserveSocket| | |ObserveSocket|\[\]>

  Usage::

    const settings = { element: document.body, projectId: "project-1" };
    squared.parseDocument(settings).then(() => {
      squared.observeSrc(
        "link[rel=stylesheet]",
        (ev, element) => {
          squared.reset("project-1");
          squared.parseDocument(settings).then(() => squared.copyTo("/path/project"));
        },
        { port: 8080, secure: false, action: "reload", expires: "1h" } // Optional
      );
    });

  Alternate::

    await squared.observeSrc("link[rel=stylesheet]"); // Will call location.reload()

.. |targetElement| replace:: *Element* target by either an ``id`` string or *HTMLElement*
.. |Application| replace:: :ref:`Application <references-squared-base>`
.. |Node| replace:: :ref:`Node <references-squared-base>`
.. |Extension| replace:: :ref:`Extension <references-squared-base>`
.. |ResponseData| replace:: Promise<:ref:`ResponseData <references-squared-base-file>`>
.. |FileActionOptions| replace:: :ref:`FileActionOptions <references-squared-main>`
.. |ElementSettings| replace:: :ref:`ElementSettings <references-squared-base>`
.. |ObserveSocket| replace:: :ref:`ObserveSocket <references-squared-internal>`
.. |AppFramework| replace:: :ref:`AppFramework <references-squared-base>`
.. |BroadcastMessageCallback| replace:: :ref:`BroadcastMessageCallback <references-squared-base-file>`
.. |APP_FRAMEWORK| replace:: :ref:`APP_FRAMEWORK <references-squared-base>`
.. |PrefetchItem| replace:: :ref:`PrefetchItem <references-squared-main>`
.. |MutationObserver| replace:: :ref:`MutationObserver <references-typescript-dom-generated>`
.. |FileObserveOptions| replace:: :ref:`FileObserveOptions <references-squared-main>`

.. [#] https://developer.mozilla.org/docs/Web/API/Document/getElementById
.. [#] https://developer.mozilla.org/docs/Web/API/Document/querySelector
.. [#] https://developer.mozilla.org/docs/Web/API/Document/querySelectorAll