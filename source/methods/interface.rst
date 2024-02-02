Interface
=========

Functions
---------

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Serve *(API)*

  function setHostname(value: string): void;
  function setEndpoint(name: string, value: string): void;
  function setLocalAddress(...values: (string | URL)[]): void;
  function auth(token: string): void;

  function kill(timeout: string): Promise<number>;
  function kill(pid?: number, timeout?: number | string): Promise<number>;

  function broadcast(callback: BroadcastMessageCallback, socketId: string): boolean;
  function broadcast(callback: BroadcastMessageCallback, options: FileBroadcastOptions): boolean;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Framework

  function setFramework(value: Application, options?: Record<string, unknown>, cache?: boolean): void;
  function setFramework(value: Application, loadAs: string, cache?: boolean): void;
  function setFramework(value: Application, options?: Record<string, unknown>, saveAs?: string, cache?: boolean): void;

  function extend(functionMap: Record<string, unknown>, framework?: number): void;
  function clear(): void;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Extensions

  function add(...values: ExtensionRequestObject[]): number;
  function remove(...values: ExtensionRequest[]): number;
  function get(...values: string[]): Extension | Extension[] | undefined;
  function attr(name: ExtensionRequest, attrName: string, value?: unknown): unknown;

  function apply(value: ExtensionRequest, saveAs: string): boolean;
  function apply(value: ExtensionRequest, options: Record<string, unknown>, saveAs?: string): boolean;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Session *(create)*

  function prefetch(type: "css", all: boolean, ...targets: (Document | ShadowRoot)[]): Promise<PrefetchItem[]>;
  function prefetch(type: "css", ...targets: (Document | ShadowRoot)[]): Promise<PrefetchItem[]>;
  function prefetch(type: "javascript" | "image" | "svg", all: boolean, ...targets: string[]): Promise<PrefetchItem[]>;
  function prefetch(type: "javascript" | "image" | "svg", ...targets: string[]): Promise<PrefetchItem[]>;

  function parseDocument(...elements: RootElement[]): Promise<Node | Node[] | void>;
  function parseDocumentSync(...elements: RootElement[]): Node | Node[] | undefined;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Session *(modify)*

  function findDocumentNode(value: HTMLElement | string, projectId?: string): Node | undefined;
  function findDocumentNode(value: HTMLElement | string, all: true, projectId?: string): Node[];

  function latest(value = 1): string;
  function latest(value: 1 | -1): string;
  function latest(value: number): string[];

  function close(projectId?: string): Promise<boolean>;
  function reset(projectId?: string): void;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Session *(API)*

  function save(): FileActionResult;
  function save(timeout: number): FileActionResult;
  function save(projectId: string, timeout: number): FileActionResult;
  function save(projectId: string, broadcastId?: string): FileActionResult;

  function saveAs(value: string, setting: string): FileActionResult;
  function saveAs(value: string, options?: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function appendTo(value: string, setting: string): FileActionResult;
  function appendTo(value: string, options?: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function copyTo(value: string | string[], setting: string): FileActionResult;
  function copyTo(value: string | string[], options?: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function saveFiles(value: string, setting: string): FileActionResult;
  function saveFiles(value: string, options: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function appendFiles(value: string, setting: string): FileActionResult;
  function appendFiles(value: string, options: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

  function copyFiles(value: string | string[], setting: string): FileActionResult;
  function copyFiles(value: string | string[], options: FileActionOptions, setting?: string, overwrite?: boolean): FileActionResult;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: DOM

  function getElementById(value: string, sync: true, cache = true): Node | null;
  function getElementById(value: string, sync?: false, cache = true): Promise<Node | null>;

  function querySelector(value: string, sync: true, cache = true): Node | null;
  function querySelector(value: string, sync?: false, cache = true): Promise<Node | null>;

  function querySelectorAll(value: string, sync: true, cache = true): Node[];
  function querySelectorAll(value: string, sync?: false, cache = true): Promise<Node[] | null>;

  function fromElement(element: HTMLElement | string, sync: true, cache?: boolean): Node | null;
  function fromElement(element: HTMLElement | string, sync?: false, cache?: boolean): Promise<Node | null>;

  function fromNode(node: Node, sync: true, cache?: boolean): Node | null;
  function fromNode(node: Node, sync?: false, cache?: boolean): Promise<Node | null>;

.. rst-class:: section-caption

.. code-block:: typescript
  :caption: Observe

  function observe(enable = true): void;
  function observe(init: MutationObserverInit): void;

  function observeSrc(element: HTMLElement | string, options: FileObserveOptions): Promise<ObserveSocket | ObserveSocket[]>;
  function observeSrc(element: HTMLElement | string, callback: (ev: MessageEvent, target: HTMLElement) => void, options?: FileObserveOptions): Promise<ObserveSocket | ObserveSocket[]>;

References
----------

.. _references-types:
.. rst-class:: block-list

https://unpkg.com/squared/types/squared.d.ts
  | ExtensionRequest
  | ExtensionRequestObject
  | FileActionOptions
  | FileBroadcastOptions
  | FileObserveOptions
  | PrefetchItem

.. _references-types-base:
.. rst-class:: block-list

https://unpkg.com/squared/types/base/squared.d.ts
  | AppFramework
  | Application
  | ElementSettings
  | FileActionResult
  | Node
  | RootElement

.. _references-types-base-file:
.. rst-class:: block-list

https://unpkg.com/squared/types/base/file.d.ts
  | BroadcastMessageCallback
  | ResponseData

.. _references-types-internal:
.. rst-class:: block-list

https://unpkg.com/squared/types/internal/squared.d.ts
  | ObserveSocket

.. rst-class:: block-list

https://developer.mozilla.org/docs/Web/API/MutationObserver/observe#options
  | MutationObserverInit