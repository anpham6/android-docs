=======
Unicode
=======

More advanced language features can optionally be enabled per document or disabled by individual element.

Settings
========

::

  squared.settings.supportUnicode = false; // Prefers UTF-8 encoding
  squared.settings.supportUnicode = "utf-16"; // Preserve UTF-16 encoding
  squared.settings.supportUnicode = "emoji"; // Detect views with Emoji characters
  squared.settings.supportUnicode = ["utf-16", "emoji"]; // "utf-16" | "emoji"
  squared.settings.supportUnicode = true; // All available features

Encoding
========

These are the only resource files affected by character encoding. Output encoding is determined by the first call to :func:`parseDocument`.

- res/values/strings.xml
- res/values/string_arrays.xml

.. caution:: Android Studio :alt:`(Gradle)` only supports ``UTF-8``.

Emoji
=====

- https://developer.android.com/develop/ui/views/text-and-emoji/emoji2

.. code-block:: typescript
  :caption: android.resource.strings

  const options: ResourceStringsOptions = {
      enableEmojiViews: true,
      detectEmojiPattern: /(?:\p{Extended_Pictographic}|\p{Emoji_Presentation}|\p{Emoji_Modifier_Base}\p{Emoji_Modifier}|\p{Regional_Indicator}\p{Regional_Indicator}|[#*0-9]\uFE0F?\u20E3)/gu,
      ignoreEmojiPattern: /[©®]/g
  };

  squared.attr("android.resource.strings", "enableEmojiViews", false); // Use standard views only
  squared.attr("android.resource.strings", "detectEmojiPattern", /(?:\p{Extended_Pictographic}|\p{Emoji_Presentation})/gu); // Mainstream Emoji only
  squared.attr("android.resource.strings", "ignoreEmojiPattern", null); // Ignore nothing

.. code-block:: html

  <form id="main">
    <label>🇯🇵:</label>
    <input type="text" placeholder="🌸" value="🌸" />
    <button title="🌸">💀</button>
    <span data-exclude-optimization="UNICODE">😊</span>
  </form>

.. code-block:: xml
  :caption: Output
  :emphasize-lines: 6,10,15

  <LinearLayout
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal" />
    <androidx.emoji2.widget.EmojiTextView
      android:layout_height="wrap_content"
      android:layout_width="wrap_content"
      android:text="@string/text_1" />
    <androidx.emoji2.widget.EmojiEditText
      android:layout_height="wrap_content"
      android:layout_width="wrap_content"
      android:hint="@string/text_2"
      android:text="@string/text_2" />
    <androidx.emoji2.widget.EmojiButton
      android:layout_height="wrap_content"
      android:layout_width="wrap_content"
      android:text="@string/text_3"
      android:tooltipText="@string/text_2" />
    <TextView
      android:layout_height="wrap_content"
      android:layout_width="wrap_content"
      android:text="@string/text_4" />
  </LinearLayout>