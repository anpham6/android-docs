========
Settings
========

These are the latest server default settings for the :target:`android` framework.

.. code-block:: json
  :caption: squared.json [#]_

  {
    "apiVersion": "1.5.0",
    "document": {
      "android": {
        "handler": "@pi-r/android",
        "namespace": "",
        "extensions": [
          "@pi-r/android/extensions/app/manifest",
          "@pi-r/android/extensions/gradle/settings",
          "@pi-r/android/extensions/gradle/dependencies",
          "@pi-r/android/extensions/task"
        ],
        "versions": {
          "org.jetbrains.kotlin:kotlin-stdlib": "2.0.0",
          "kotlinCompilerExtensionVersion": "1.5.14",
          "buildToolsVersion": ""
        },
        "settings": {
          "broadcast_id": "",
          "users": {
            "username": {
              "extensions": null
            }
          },
          "extensions": {
            "task": {
              "exec": {
                "uid": "",
                "gid": ""
              },
              "command": ""
            }
          },
          "language": {
            "gradle": "kotlin"
          },
          "directory": {
            "template": ""
          }
        },
        "permission": {}
      }
    }
  }

References
==========

- https://www.unpkg.com/@pi-r/android/types/index.d.ts

.. [#] https://www.unpkg.com/squared-express/dist/squared.json