const { isNewline } = require('./type-checks')
const { CR, LF } = require('./codes')

class Scanner {
  constructor (text, pos) {
    this.text = text
    this.pos = pos ? { ...pos } : { line: 1, column: 1, offset: 0 }
  }

  eof () {
    return this.pos.offset >= this.text.length
  }

  next (n) {
    const token = n
      ? this.text.substring(this.pos.offset, this.pos.offset + n)
      : this.peek()

    this.pos.offset += token.length
    this.pos.column += token.length

    if (isNewline(token)) {
      this.pos.line++
      this.pos.column = 1
    }

    return token
  }

  peek () {
    let token = this.text.charAt(this.pos.offset)
    // Consume <CR>? <LF>
    if (token === CR && this.text.charAt(this.pos.offset + 1) === LF) {
      token += LF
    }
    return token
  }

  peekLiteral (literal) {
    const str = this.text.substring(this.pos.offset, this.pos.offset + literal.length)
    return literal === str
  }

  position () {
    return { ...this.pos }
  }

  rewind (pos) {
    this.pos = pos
  }

  enter (type, content) {
    const position = { start: this.position() }
    return Array.isArray(content)
      ? { type, children: content, position }
      : { type, value: content, position }
  }

  exit (node) {
    node.position.end = this.position()
    return node
  }

  abort (node, expectedTokens) {
    const position = `${this.pos.line}:${this.pos.column}`
    const validTokens = expectedTokens
      ? expectedTokens.filter(Boolean).join(', ')
      : `<${node.type}>`

    const error = this.eof()
      ? Error(`unexpected token EOF at ${position}, valid tokens [${validTokens}]`)
      : Error(`unexpected token '${this.peek()}' at ${position}, valid tokens [${validTokens}]`)

    this.rewind(node.position.start)
    return error
  }
}

module.exports = Scanner
