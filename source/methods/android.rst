=======
android
=======

.. module:: android

.. function:: setViewModel(data[, sessionId = "0"])

  Imports to be used for layout bindings associated by session.

  :param data: Dictionary of imports and variables
  :type data: |AppViewModel|
  :param string sessionId: Names a session to be used for storage

  Usage::

    squared.parseDocument(() => {
      android.setViewModel(
        {
          import: ["java.util.Map"],
          variable: [{ name: "map", type: "Map&lt;String, String>" }]
        },
        squared.latest()
      );
    });

.. function:: setViewModelByProject(data[, projectId = "_"])

  Imports to be used for layout bindings associated by project.

  :param data: Dictionary of imports and variables
  :type data: |AppViewModel|
  :param string projectId: |projectId|

  Usage::

    android.setViewModelByProject(
      {
        import: ["java.util.Map"],
        variable: [{ name: "map", type: "Map&lt;String, String>" }]
      },
      "project-1"
    );
    await squared.parseDocument({ element: document.body, projectId: "project-1" });

.. function:: addDependency(group, name[, version, type])

  Include a dependency by group and name to an existing or newly created ``build.gradle``. Uses the default project "_" for storage. Any existing dependency with the same group and name will be overwritten.

  :param string group: Namespace of library
  :param string name: Componenent name in library
  :param string version: |VersionDependency|
  :param number type: |GradleDependency|
  :returns: Dictionary key or ""
  :rtype: string
  :requirements:
    - **createBuildDependencies** = *true*

  Usage::

    android.addDependency("androidx.core", "core", "1.12.0"); // Default is "implementation"
    squared.copyTo("/path/project", { dependencyScopes: true }); // Will also include first-level sub-dependencies (optional)

  Alternate::

    android.addDependency("androidx.core", "core", DEPENDENCY_TYPE.COMPILE_ONLY, true); // Uses latest Maven published release
    squared.copyTo("/path/project", { dependencyScopes: "snapshot" });

.. function:: addDependencyByProject(projectId, group, name[, version, type])

  Include a dependency to a project by group and name of an existing or newly created ``build.gradle``. Any existing dependency in the project with the same group and name will be overwritten.

  :param string projectId: |projectId|
  :param string group: Namespace of library
  :param string name: Componenent name in library
  :param string version: |VersionDependency|
  :param number type: |GradleDependency|
  :returns: Dictionary key or ""
  :rtype: string
  :requirements:
    - **createBuildDependencies** = *true*

  Usage::

    android.addDependencyByProject("project-1", "androidx.core", "core", "1.12.0"); // Default is "implementation"
    squared.copyTo("/path/project", { projectId: "project-1", dependencyScopes: true }); // Will also include first-level sub-dependencies (optional)

  Alternate::

    android.addDependencyByProject("project-1", "androidx.core", "core", DEPENDENCY_TYPE.COMPILE_ONLY, true); // Uses latest Maven published release
    squared.copyTo("/path/project", { projectId: "project-1", dependencyScopes: "snapshot" });

.. function:: addFontProvider(authority, package, certs, webFonts)

  Add additional `Web fonts <https://developer.android.com/develop/ui/views/text-and-emoji/downloadable-fonts#using-downloadable-fonts-as-resources>`_ that can be searched for when resolving first available font family. `Google Fonts <https://developers.google.com/fonts/docs/developer_api>`_ is already included.

  :param string authority: Class of font provider library
  :param string package: Namespace of font provider
  :param array certs: List of certificates the font provider is signed with
  :param string webFonts: Web font service URL
  :returns: Success when installed
  :rtype: Promise<boolean>
  :requirements:
    - **targetAPI** >= *26*
    - **createDownloadableFonts** = *true*

  Usage::

    await android.addFontProvider(
      "com.google.android.gms.fonts",
      "com.google.android.gms",
      ["MIIEqDCCA5CgAwIBAgIJANWFuGx9007...", "MIIEQzCCAyugAwIBAgIJAMLgh0Zk..."],
      "https://www.googleapis.com/webfonts/v1/webfonts?key=1234567890" // Pre-built JSON object is synchronous
    );

.. function:: addXmlNs(name, uri)

  Aliases of global namespaces for third-party controls used when resolving layout attributes.

  :param string name: Prefix to be used with attribute
  :param string uri: Full URL namespace of schema

  Usage::

    android.addXmlNs("tools", "http://schemas.android.com/tools"); // https://developer.android.com/studio/write/tool-attributes
    android.customize(16 /* Jelly Bean */, "ImageView", {
      tools: {
        ignore: "ContentDescription",
        targetApi: "16"
      }
    });

  Output:

  .. code-block:: xml

    <FrameLayout xmlns:tools="http://schemas.android.com/tools">
      <ImageView tools:ignore="ContentDescription" tools:targetApi="16">
    </FrameLayout>

.. function:: customize(api, widget, options)

  Global attributes to be applied to every qualifying layout control possibly overwriting any auto-generated attributes.

  :param number api: Android SDK build API version
  :param string widget: Namespace of layout control
  :param object options: Attributes to be applied to control
  :returns: Current state of API and widget
  :rtype: object or undefined
  :requirements:
    - **customizationsBaseAPI** >= *0*
    - **customizationsOverwritePrivilege** = *true*

  Usage::

    android.customize(BUILD_VERSION.ALL /* 0 */, "Button", {
      android: {
        minWidth: "35px",
        minHeight: "25px"
      },
      "_": { // Non-namespaced attributes
        style: "@style/Widget.Material3.Button.TextButton"
      }
    });

  Output:

  .. code-block:: xml

    <Button
      android:minWidth="35dp"
      android:minHeight="25dp"
      style="@style/Widget.Material3.Button.TextButton" />

.. function:: loadCustomizations(name)

  Will merge any saved customizations from the same origin. Any previous calls to :func:`android.customize` may be overwritten.

  :param string name: Unique identifier to be used for local storage

  Usage::

    squared.settings.targetAPI = BUILD_VERSION.T;
    squared.settings.customizationsBaseAPI = 0; // Apply all customizations

    android.loadCustomizations("customize-example"); // Any page in same domain

    android.customize(BUILD_VERSION.T, "Button", { android: { minWidth: "25px" } });
    android.customize(BUILD_VERSION.LATEST, "Button", { android: { minWidth: "30px" } });

  Output:

  .. code-block:: xml

    <Button android:minWidth="25dp" android:minHeight="25dp" />

  Alternate::

    squared.settings.targetAPI = BUILD_VERSION.T;
    squared.settings.customizationsBaseAPI = [BUILD_VERSION.T, BUILD_VERSION.LATEST];

  Output:

  .. code-block:: xml

    <Button android:minWidth="30dp" android:minHeight="25dp" />

.. function:: saveCustomizations(name)

  Any valid customizations created using :func:`android.customize` will be saved to local storage.

  :param string name: Unique identifier to be used for local storage

  Usage::

    android.customize(BUILD_VERSION.ALL /* 0 */, "Button", {
      android: {
        minWidth: "35px",
        minHeight: "25px"
      }
    });
    android.customize(BUILD_VERSION.NEXT /* 35 */, "Button", { // Invalid
      android: {
        minWidth: "35px",
        minHeight: "25px"
      }
    });

.. function:: resetCustomizations()

  All customizations currently being used are deleted. Saved customizations in local storage are not affected.

  Usage::

    android.resetCustomizations();

.. function:: setResolutionByDeviceName(value)

  Sets the resolution when converting browser dimensions into Android device dimensions.

  .. hlist::
    :columns: 4

    * Phone
    * Medium Phone
    * Foldable
    * Tablet
    * Medium Tablet
    * Small Desktop
    * Medium Desktop
    * Desktop
    * Large Desktop
    * Pixel
    * Pixel XL
    * Pixel 2
    * Pixel 2 XL
    * Pixel 3
    * Pixel 3a
    * Pixel 3 XL
    * Pixel 3a XL
    * Pixel 4
    * Pixel 4 XL
    * Pixel 4a
    * Pixel 5
    * Pixel 6
    * Pixel 6a
    * Pixel 6 Pro
    * Pixel 7
    * Pixel 7a
    * Pixel 7 Pro
    * Pixel 8
    * Pixel 8 Pro
    * Pixel C
    * Pixel Fold
    * Nexus 5X
    * Nexus 6
    * Nexus 6P
    * Nexus 7 2012
    * Nexus 7 (2012)
    * Nexus 7
    * Nexus 9
    * Nexus 10
    * TV 4K
    * TV 1080p
    * Television (4K)
    * Television (1080p)
    * TV 720p
    * Television (720p)
    * Automotive
    * Automotive (1024p landscape)

  The exact configuration for each device can be found in the latest Android Studio.

  :param string name: Predefined device name or generic layout
  :returns: Success when applied
  :rtype: boolean

  Usage::

    android.setResolutionByDeviceName("Pixel 3a XL");

  Output::

    squared.settings.resolutionDPI = 411;
    squared.settings.resolutionScreenWidth = 846;
    squared.settings.resolutionScreenHeight = 560;

.. function:: getLocalSettings()

  Controller settings which are based on browser defaults can be modified. These are global changes and affect every call to :func:`parseDocument`.

  :returns: Current modifiable state of settings
  :rtype: |ControllerSettingsUI|

  Usage::

    const { layout, directory, filename, style, mimeType, unsupported, deviations, values } = android.getLocalSettings();

    layout.fileExtension = ".xml";
    directory.string = "res/values";
    style.buttonBorderStyle = "inset";

.. function:: removeObserver(element)

  Forwards the target element to |Application| which will stop it from being monitored for changes.

  :param element: *HTMLElement* instance
  :returns: Success when observed
  :rtype: boolean

  Usage::

    await squared.parseDocument({
      element: document.body,
      observe(mutations, observer, settings) {}
    });

    android.removeObserver(document.body);

.. |projectId| replace:: Names a project to be used for storage
.. |GradleDependency| replace:: Dependency namespace method in Gradle
.. |VersionDependency| replace:: (:sub:`optional (type)`) Exact version requested
.. |AppViewModel| replace:: :ref:`AppViewModel <references-android-main>`
.. |Application| replace:: :ref:`Application <references-squared-base>`
.. |ControllerSettingsUI| replace:: :ref:`ControllerSettingsUI <references-android-application>`