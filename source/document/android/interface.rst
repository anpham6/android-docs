=========
Interface
=========

.. highlight::  typescript

.. code-block::
  :emphasize-lines: 54,63,92,95,152,175,195-196,214-215,222,271-272

  class NodeUI extends Node {
      static linearData(list: NodeUI[], cleared?: Map<NodeUI, string> | null, absolute?: boolean): LinearData;
      static baseline(list: NodeUI[], text?: boolean, image?: boolean): NodeUI | null;
      static partitionRows(list: NodeUI[], cleared?: Map<NodeUI, string> | null): NodeUI[][];
      alignmentType: number;
      contentAltered: boolean;
      baselineActive: boolean;
      baselineAltered: boolean;
      rendered: boolean;
      excluded: boolean;
      rootElement: boolean;
      lineBreakLeading: boolean;
      lineBreakTrailing: boolean;
      floatContainer: boolean;
      absoluteContainer: boolean;
      renderChildren: NodeUI[];
      renderExtension: Extension<NodeUI>[] | null;
      renderTemplates: NodeTemplate<NodeUI>[] | null;
      documentChildren?: NodeUI[];
      setControlType(controlName: string, containerType?: number): void;
      setExclusions(): void;
      setLayout(): void;
      setAlignment(): void;
      setBoxSpacing(): void;
      attr(name: string, attr: string, value?: string, overwrite?: boolean): string;
      attrx(attr: string, value?: string, overwrite?: boolean): string;
      alignParent(...position: AnchorPositionAttr[]): boolean;
      alignSibling(position: AnchorPositionAttr, documentId?: string): string;
      anchorChain(...values: PositionAttr[]): NodeUI[];
      localizeString(value: string): string;
      inherit(node: NodeUI, ...modules: string[]): PlainObject | null;
      inheritApply(module: string, data: PlainObject): void;
      transferData(node: NodeUI, overwrite?: boolean, ...keys: (string | symbol)[]): void;
      clone(id: number): void;
      cloneBase(node: NodeUI): void;
      is(containerType: number): boolean;
      of(containerType: number, ...alignmentType: number[]): boolean;
      namespace(name: string): StringMap;
      namespaces(): [string, StringMap][];
      unsafe(name: string | PlainObject, value?: unknown): unknown;
      delete(name: string, ...attrs: string[]): void;
      deleteOne(name: string, attr: string): void;
      apply(options: PlainObject): void;
      lockAttr(name: string, attr: string): void;
      unlockAttr(name: string, attr: string): void;
      lockedAttr(name: string, attr: string): boolean;
      unsetCache(...attrs: (CssStyleAttr | keyof CacheValueUI)[]): void;
      addAlign(value: number): void;
      removeAlign(value: number): void;
      hasAlign(value: number): boolean;
      hasProcedure(value: number): boolean;
      hasResource(value: number): boolean;
      hasSection(value: number): boolean;
      hasOptimization(value: number): boolean;
      exclude(options: ExcludeOptions): void;
      hide(options?: HideOptions<NodeUI>): NodeTemplate<NodeUI> | null;
      replaceTry(options: ReplaceTryOptions<NodeUI>): boolean;
      removeTry(options?: RemoveTryOptions<NodeUI>): NodeTemplate<NodeUI> | null;
      render(parent: NodeUI): void;
      renderEach(predicate: IteratorPredicate<NodeUI, void>): this;
      parseWidth(value: string, parent?: boolean): number;
      parseHeight(value: string, parent?: boolean): number;
      actualRect(position: PositionAttr, dimension?: BoxType): number;
      actualPadding(attr: BoxPaddingAttr): number;
      actualMargin(attr: BoxMarginAttr): number;
      actualBoxWidth(value?: number): number;
      actualTextHeight(options?: TextHeightOptions): number;
      alignedVertically(siblings?: NodeUI[] | AlignedVerticallyOptions<NodeUI> | null, cleared?: Map<NodeUI, string> | null, horizontal?: boolean): number;
      previousSiblings(options?: TraverseSiblingsOptions): NodeUI[];
      nextSiblings(options?: TraverseSiblingsOptions): NodeUI[];
      actualSpacing(region: BOX_STANDARD): number;
      modifyBox(region: BOX_STANDARD, value: number, negative?: boolean): void;
      setBox(region: BOX_STANDARD, options: BoxOptions): void;
      getBox(region: BOX_STANDARD): [number, number];
      resetBox(region: BOX_STANDARD, node?: NodeUI): void;
      transferBox(region: BOX_STANDARD, node: NodeUI): void;
      registerBox(region: BOX_STANDARD, node?: NodeUI): NodeUI | null;
      setCacheValue(attr: keyof CacheValueUI, value: any): void;
      setCacheState(attr: keyof CacheStateUI<NodeUI>, value: any): void;
      setCacheStyle(attr: keyof CssStyleMap, value: string): void;
      unsetStyle(...attrs: CssStyleAttr[]): void;
      extractAttributes(depth?: number, replaceWith?: AnyObject): string;
      css(attr: CssStyleAttr, value?: string | null, cache?: boolean): string;
      cssSet(attr: CssStyleAttr, value: string, cache?: boolean): string;
      translateX(value: number, options?: TranslateOptions): boolean;
      translateY(value: number, options?: TranslateOptions): boolean;
      flex(attr: "inline" | "row" | "column" | "reverse" | "wrap" | "wrapReverse", parent?: boolean | NodeUI, wrapped?: boolean): boolean;
      flex(attr: "alignContent" | "justifyContent" | "basis" | "alignSelf" | "justifySelf", parent?: boolean | NodeUI, wrapped?: boolean): string;
      flex(attr: "grow" | "shrink" | "order", parent?: boolean | NodeUI, wrapped?: boolean): number;
      flex(attr: string, parent?: boolean | NodeUI, wrapped?: boolean): boolean | number | string;
      getBoxSpacing(region?: BOX_STANDARD): [number, number, number, number];
      getPositionOffset(name: "sticky"): Point;
      getAnchoredSiblings(orientation: OrientationAttr): NodeUI[];
      getPseudoElement(name: PseudoElt | PseudoStyleElt, attr?: CssStyleAttr): CssStyleMap | string | null;
      hasFixedDimension(dimension: DimensionAttr): boolean;
      isResizable(attr: DimensionSizableAttr, not?: string | string[]): boolean;
      fitToScreen(value: Dimension): Dimension;
      getComments(type: ReferenceType, attrs?: CssStyleAttr[]): [string, string];
      cssValue(attr: CssStyleAttr): string;
      cssValues(...attrs: CssStyleAttr[]): string[];
      set documentRoot(value);
      get documentRoot(): boolean;
      set depth(value);
      get depth(): number;
      set parent(value);
      get parent(): NodeUI | null;
      set documentParent(value);
      get documentParent(): NodeUI;
      set containerName(value);
      get containerName(): string;
      set autoPosition(value);
      get autoPosition(): boolean;
      set inlineText(value);
      get inlineText(): boolean;
      set textContent(value);
      get textContent(): string;
      get styleText(): boolean;
      set multiline(value);
      get multiline(): boolean;
      set visible(value);
      get visible(): boolean;
      set controlName(value);
      get controlName(): string;
      set actualParent(value);
      get actualParent(): NodeUI | null;
      set siblingsLeading(value);
      get siblingsLeading(): NodeUI[];
      set siblingsTrailing(value);
      get siblingsTrailing(): NodeUI[];
      set renderParent(value);
      get renderParent(): NodeUI | null;
      set outerWrapper(value);
      get outerWrapper(): NodeUI | null;
      set companion(value);
      get companion(): NodeUI | null;
      set renderedAs(value);
      get renderedAs(): NodeTemplate<NodeUI> | null;
      set horizontalRows(value);
      get horizontalRows(): NodeUI[][]> | null;
      set containerType(value: number);
      get containerType(): number;
      set positioned(value);
      get positioned(): boolean;
      set controlId(name: string);
      get controlId(): string;
      get referenceId(): string;
      get documentId(): string;
      set textIndent(value);
      get textIndent(): number;
      get preIndent(): [string, NodeUI] | null;
      get causesLineBreak(): boolean;
      get afterLineBreak(): boolean;
      set renderExclude(value: boolean);
      get renderExclude(): boolean;
      set renderAs(value);
      get renderAs(): NodeUI | null;
      set labelFor(value);
      get labelFor(): NodeUI | null;
      set innerWrapped(value);
      get innerWrapped(): NodeUI | null;
      set use(value);
      get use(): string;
      set localSettings(value);
      get localSettings(): LocalSettingsUI;
      get extensions(): string[];
      get scrollElement(): boolean;
      get controlElement(): boolean;
      get imageContainer(): boolean;
      get baselineHeight(): number;
      get support(): SupportUI;
      get layoutElement(): boolean;
      get layoutHorizontal(): boolean;
      get layoutVertical(): boolean;
      get nodeGroup(): boolean;
      get tagDisplay(): string;
      get inlineVertical(): boolean;
      get inlineDimension(): boolean;
      get blockStatic(): boolean;
      get blockVertical(): boolean;
      get blockDimension(): boolean;
      get inlineFlow(): boolean;
      get verticalAligned(): boolean;
      get variableWidth(): boolean;
      get variableHeight(): boolean;
      get fullWidth(): boolean;
      get fullHeight(): boolean;
      get fullContentWidth(): boolean;
      get fullContentHeight(): boolean;
      get positiveAxis(): boolean;
      get leftTopAxis(): boolean;
      get baselineElement(): boolean;
      get flowElement(): boolean;
      get flowContent(): boolean;
      get flowChildren(): NodeUI[];
      get flexRow(): boolean;
      get flexColumn(): boolean;
      get previousSibling(): NodeUI | null;
      get nextSibling(): NodeUI | null;
      get firstStaticChild(): NodeUI | null;
      get lastStaticChild(): NodeUI | null;
      get onlyChild(): boolean;
      get onlyStaticChild(): boolean;
      get horizontalRowStart(): boolean;
      get horizontalRowEnd(): boolean;
      get innerBefore(): NodeUI | null;
      get innerAfter(): NodeUI | null;
      get rendering(): boolean;
      get boxReset(): number[];
      get boxAdjustment(): number[];
      get overflowX(): boolean;
      get overflowY(): boolean;
      get textEmpty(): boolean;
      get textWidth(): number;
      get textMetrics(): TextMetrics | null;
      get wordSpacing(): number;
      get innerMostWrapped(): NodeUI;
      get outerMostWrapper(): NodeUI;
      get firstLineStyle(): CssStyleMap | null;
      get firstLetterStyle(): CssStyleMap | null;
      get textAlignLast(): string;
      get textJustified(): boolean;
      get alignContent(): "start" | "end" | "center" | "baseline" | "";
      get transformValue(): string;
      get outerRegion(): BoxRectDimension;
  }

  class View extends NodeUI {
      static availablePercent(nodes: View[], dimension: DimensionAttr, boxSize: number, flexContainer?: boolean): number;
      static getControlName(containerType: number, api?: number): string;
      api: number;
      materialDesign: boolean;
      android(attr: string, value?: string, overwrite?: boolean): string;
      app(attr: string, value?: string, overwrite?: boolean): string;
      clone(id?: number, options?: CloneOptions): View;
      applyOptimizations(): boolean;
      applyCustomizations(overwrite?: boolean): void;
      formatted(value: string, overwrite?: boolean): void;
      mergeGravity(attr: LayoutGravityAttr, alignment: LayoutGravityDirectionAttr, overwrite?: boolean): void;
      anchor(position: AnchorPositionAttr, documentId?: string, overwrite?: boolean): boolean;
      anchorChain(...values: PositionAttr[]): View[];
      anchorParent(orientation: OrientationAttr, bias: number, overwrite: true): boolean;
      anchorParent(orientation: OrientationAttr, bias?: number, style?: LayoutChainStyle, overwrite?: boolean): boolean;
      anchorStyle(orientation: OrientationAttr, bias: number, overwrite: true): void;
      anchorStyle(orientation: OrientationAttr, bias: number, style?: LayoutChainStyle, overwrite?: boolean): void;
      anchorDelete(...position: AnchorPositionAttr[]): void;
      anchorClear(update?: View | boolean, renderParent?: View | null): void;
      deprecated(attr: string, value: string, output: PlainObject): boolean | undefined;
      supported(attr: string, value: string, output: PlainObject): boolean;
      combine(sort: boolean, ...values: string[]): string[];
      combine(...values: string[]): string[];
      setLayoutWidth(value: string, overwrite?: boolean): void;
      setLayoutHeight(value: string, overwrite?: boolean): void;
      setLayoutPercent(value: string, horizontal?: boolean): void;
      setSingleLine(maxLines: boolean, ellipsize?: boolean): void;
      setConstraintDimension(percentAvailable?: number): number;
      setFlexDimension(dimension: DimensionAttr, percentAvailable?: number, weight?: number): number;
      getMatchConstraint(parent?: View, container?: boolean, percent?: boolean): string;
      getAnchorPosition(parent: View, horizontal: boolean, modifyAnchor?: boolean): Partial<BoxRect>;
      isUnstyled(checkMargin?: boolean): boolean;
      isAnchored(options: IsAnchoredOptions): boolean;
      getHorizontalBias(rect?: BoxRect): number;
      getVerticalBias(rect?: BoxRect): number;
      getAbsolutePaddingOffset(region: number, value: number): number;
      getMarginPercent(horizontal: boolean): number;
      getPaddingPercent(horizontal: boolean): number;
      hasFlex(direction: LayoutDirectionAttr): boolean | 0;
      set anchored(value);
      get anchored(): boolean;
      set localSettings(value);
      get localSettings(): LocalSettingsUI;
      set useSystemColors(value);
      get useSystemColors(): boolean;
      get documentId(): string;
      get anchorTarget(): View;
      get constraint(): Constraint<View>;
      get layoutFrame(): boolean;
      get layoutLinear(): boolean;
      get layoutGrid(): boolean;
      get layoutRelative(): boolean;
      get layoutConstraint(): boolean;
      get layoutFragment(): boolean;
      get layoutAnchoring(): boolean;
      get layoutWidth(): string;
      get layoutHeight(): string;
      get inlineWidth(): boolean;
      get inlineHeight(): boolean;
      get blockWidth(): boolean;
      get blockHeight(): boolean;
      get flexibleWidth(): boolean;
      get flexibleHeight(): boolean;
      get flexibleHorizontal(): boolean;
      get watch(): WatchInterval | undefined;
      get tasks(): TaskCommand[] | undefined;
      get target(): HTMLElement | null;
      get support(): SupportUI;
  }

.. versionadded:: 5.3.0

  - *NodeUI* method **hasOptimization** for bypassing incorrect adjustments was created.
  - *NodeUI* method **getPositionOffset** for static position difference was created.
  - *NodeUI* method **actualRect** was migrated from :target:`View` and is no longer abstract.
  - *NodeUI* method **hasFixedDimension** was migrated from :target:`View`.
  - *NodeUI* property getter **afterLineBreak** for start of line detection was created.
  - *NodeUI* property getter **wordSpacing** for trailing margin was created.

.. versionadded:: 5.2.1

  - *NodeUI* property getter **textMetrics** for font dimensions was created.

.. versionadded:: 5.2.0

  - *NodeUI* property getter **tagDisplay** for rendered behavior was created.
  - *NodeUI* property getter **alignContent** for vertical layout position was created.
  - *NodeUI* method **extractAttributes** *optional* argument **replaceWith** as :alt:`AnyObject` was implemented.
  - *NodeUI* method **getPseudoElement** argument **name** with :alt:`PseudoStyleElt` was amended.
  - *NodeUI* method **flex** argument **parent** with :alt:`NodeUI` was amended.
  - *View* property getter **useSystemColors** for device color translation was created.

.. deprecated:: 5.2.0

  - *NodeUI* property getter **flexRow** as :alt:`NodeUI.flex("row")` is pending removal.
  - *NodeUI* property getter **flexColumn** as :alt:`NodeUI.flex("column")` is pending removal.