export function parser(commitText: string): Message;

export interface Note {
  title: string,
  text: string
}

export interface Reference {
  action: string;
  owner?: string;
  repository?: string;
  issue: string;
  raw?: string;
  prefix: string;
}

export interface ConventionalChangelogCommit {
  type: string;
  scope: string | null;
  subject: string;
  merge: boolean | null;
  header: string;
  body: string | null;
  footer: string | null;
  notes: Note[];
  references: Reference[];
  mentions: string[];
  revert: boolean | null;
}

export function toConventionalChangelogFormat(ast: Message): ConventionalChangelogCommit;

// unist core - copied from @types/unist

export interface Point {
  /** Line in a source file (1-indexed integer) */
  line: number;
  /** Column in a source file (1-indexed integer) */
  column: number;
  /** Character in a source file (0-indexed integer) */
  offset?: number;
}

export interface Position {
  /** Place of the first character of the parsed source region */
  start: Point;
  /** Place of the first character after the parsed source region */
  end: Point;
}

export interface Node {
  /** The semantic type of the node */
  type: string;
  /** Location of a node in a source document. Undefined when generated */
  position?: Position;
}

export interface Literal extends Node {
  value: unknown;
}

export interface Parent extends Node {
  children: unknown[];
}

// unist conventional commits structure

export interface Message extends Parent {
  type: 'message';
  children: (Summary | Body | Newline | Footer)[];
}

export interface Text extends Literal {
  type: 'text';
  value: string;
}

export interface Newline extends Literal {
  type: 'newline';
  value: string;
}

export interface BreakingChange extends Literal {
  type: 'breaking-change';
  value: '!' | 'BREAKING-CHANGE' | 'BREAKING CHANGE';
}

export interface Summary extends Parent {
  type: 'summary';
  children: (Type | Scope | Separator)[];
}

export interface Type extends Literal {
  type: 'type';
  value: string;
}

export interface Scope extends Literal {
  type: 'scope';
  value: string;
}

export interface Separator extends Literal {
  type: 'separator';
  value: ':' | ' #';
}

export interface Body extends Parent {
  type: 'body';
  children: (Text | Newline)[];
}

export interface Footer extends Parent {
  type: 'footer';
  children: (Token | Separator | Value)[];
}

export interface Token extends Parent {
  type: 'token';
  children: (Type | Scope | BreakingChange)[];
}

export interface Value extends Parent {
  type: 'value';
  children: (Text | Continuation)[];
}

export interface Continuation extends Parent {
  type: 'continuation';
  children: (Newline | Text)[];
}
