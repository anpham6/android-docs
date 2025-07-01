==================
Downloadable Fonts
==================

Google Fonts [#]_ are pre-installed and can be used without any additional configuration. Here is what happens when these settings are enabled::

  squared.settings.outputDocumentEditing = true;
  squared.settings.createManifest = true;
  squared.settings.createBuildDependencies = true;

Enable
======

.. code-block::
  :caption: Install and build [#]_

  await android.addFontProvider(
    "com.google.android.gms.fonts",
    "com.google.android.gms",
    ["MIIEqDCCA5CgAwIBAgIJANWFuGx9007...", "MIIEQzCCAyugAwIBAgIJAMLgh0Zk..."],
    "https://www.googleapis.com/webfonts/v1/webfonts?key=1234567890" // JSON object is synchronous
  );

  squared.parseDocument({ element: document.body, createDownloadableFonts: true }).then(() => squared.saveAs("fonts.zip"));

Output
------

.. code-block:: xml
  :caption: AndroidManifest.xml
  :emphasize-lines: 3

  <manifest xmlns:android="http://schemas.android.com/apk/res/android">
     <application android:theme="@style/AppTheme">
        <meta-data android:name="preloaded_fonts" android:resource="@array/preloaded_fonts" />
     </application>
  </manifest>

.. code-block:: none
  :caption: build.gradle

  dependencies {
      implementation 'androidx.appcompat:appcompat:1.7.0'
  }

Disable
=======

::

  squared.attr("android.resource.fonts", "installGoogleFonts", false); // Use browser and local fonts only

.. [#] https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts
.. [#] https://developers.google.com/fonts/docs/developer_api