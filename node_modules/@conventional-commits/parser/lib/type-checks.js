const { CR, LF, ZWNBSP, TAB, VT, FF, SP, NBSP } = require('./codes')

module.exports = {
  /*
  * <whitespace>   ::= <ZWNBSP> | <TAB> | <VT> | <FF> | <SP> | <NBSP> | <USP>
  */
  isWhitespace (token) {
    return token === ZWNBSP || token === TAB || token === VT || token === FF || token === SP || token === NBSP
  },

  /*
  * <newline>      ::= <CR>? <LF>
  */
  isNewline (token) {
    const chr = token.charAt(0)
    if (chr === CR || chr === LF) return true
  },

  /*
  * <parens>       ::= "(" | ")"
  */
  isParens (token) {
    return token === '(' || token === ')'
  }
}
