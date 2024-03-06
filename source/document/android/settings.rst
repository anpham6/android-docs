========
Settings
========

These are the latest default settings for the :target:`android` framework.

.. code-block:: json
  :caption: squared.json [#]_

  {
    "apiVersion": "1.4.0",
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
          "org.jetbrains.kotlin:kotlin-stdlib": "1.9.22",
          "kotlinCompilerExtensionVersion": "1.5.9",
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

Interface
=========

.. code-block:: typescript
  :caption: :external+chrome:doc:`View Module <modules/document>`

  interface DocumentModule {
      handler: "@pi-r/android";
      extensions?: string[];
      versions?: StringMap;
      settings?: {
          broadcast_id?: string | string[];
          users?: Record<string, Record<string, unknown>>;
          extensions?: {
              task?: {
                  exec?: {
                      uid?: number | string;
                      gid?: number | string;
                  };
                  command?: string;
              };
          };
          language?: {
              gradle?: "java" | "kotlin" | "java+kotlin";
          };
          directory?: {
              template?: string;
          };
      };
      permission: PermittedDirectories;
  }

.. [#] https://www.unpkg.com/squared-express/dist/squared.json