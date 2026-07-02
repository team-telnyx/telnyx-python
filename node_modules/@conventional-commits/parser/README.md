## Conventional Commits Parser

![ci](https://github.com/conventional-commits/parser/workflows/ci/badge.svg)
![nycrc config on GitHub](https://img.shields.io/nycrc/conventional-commits/parser)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg)](https://conventionalcommits.org)

Reference implementation of Conventional Commits specification.

Outputs a tree structure based on the
[unist specification](https://github.com/syntax-tree/unist).

## Install

```
npm i @conventional-commits/parser
```

## Usage

```js
const {parser} = require('@conventional-commits/parser')
const ast = parser('feat(parser): add support for scopes')
```

## API

### `parser(text: string)`

Runs conventional commits parser on the string provided.

* Returns: Object adhering to [unist spec](https://github.com/syntax-tree/unist).

### `toConventionalChangelogFormat(ast: object)`

Given an `object`, representing the parsed commit messages in `unist` format,
returns an object useable by the [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog) ecosystem of libraries.

## The Grammar

The parser is based on the following grammar. An effort is made to keep this
in sync with the written specification on conventionalcommits.org.

```ebnf
/* See: https://tools.ietf.org/html/rfc3629#section-4 */
<UTF8-char>       ::= "Placeholder for UTF-8 grammar"
<UTF8-octets>     ::= <UTF8char>+

<CR>              ::= "0x000D"
<LF>              ::= "0x000A"
<newline>         ::= [<CR>], <LF>
<parens>          ::= "(" | ")"
<ZWNBSP>          ::= "U+FEFF"
<TAB>             ::= "U+0009"
<VT>              ::= "U+000B"
<FF>              ::= "U+000C"
<SP>              ::= "U+0020"
<NBSP>            ::= "U+00A0"
/* See: https://www.ecma-international.org/ecma-262/11.0/index.html#sec-white-space */
<USP>             ::= "Any other Unicode 'Space_Separator' code point"
/* Any non-newline whitespace: */
<whitespace>      ::= <ZWNBSP> | <TAB> | <VT> | <FF> | <SP> | <NBSP> | <USP>

<message>         ::= <summary>, <newline>+, <body>, (<newline>+, <footer>)*
                   |  <summary>, (<newline>+, <footer>)*
                   |  <summary>, <newline>*

/* "!" should be added to the AST as a <breaking-change> node with the value "!" */
<summary>         ::= <type>, "(", <scope>, ")", ["!"], ":", <whitespace>*, <text>
                   |  <type>, ["!"], ":", <whitespace>*, <text>
<type>            ::= <any UTF8-octets except newline or parens or ":" or "!:" or whitespace>+
<scope>           ::= <any UTF8-octets except newline or parens>+
<text>            ::= <any UTF8-octets except newline>*


<body>            ::= [<any body-text except pre-footer>], <newline>, <body>*
                   |  [<any body-text except pre-footer>]
/* For convenience the <breaking-change>, <separator>, <whitespace>, and
 * <text> tokens of <body-text> should be appended as children to <body> */
<body-text>       ::= [<breaking-change>, ":", <whitespace>*], text
/* Note: <pre-footer> is used during parsing, but not returned in the AST. */
<pre-footer>      ::= <newline>+, <footer>

<footer>          ::= <token>, <separator>, <whitespace>*, <value>
/* "!" should be added to the AST as a <breaking-change> node with the value "!" */
<token>           ::= <breaking-change>
                   |  <type>, "(" <scope> ")", ["!"]
                   |  <type>, ["!"]
<separator>       ::= ":" | " #"
<value>           ::= <text>, <continuation>+
                   |  <text>
<continuation>    ::= <newline>, <whitespace>+, <text>

<breaking-change> ::= "BREAKING CHANGE" | "BREAKING-CHANGE"
```
