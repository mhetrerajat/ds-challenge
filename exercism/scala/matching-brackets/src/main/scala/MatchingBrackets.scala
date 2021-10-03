import scala.collection.mutable.Stack

object MatchingBrackets {
  def isPaired(str: String): Boolean = {
    var stack = Stack[Char]()
    val validChars = Set('(', ')', '{', '}', '[', ']')
    for (char <- str) {
      if (validChars(char)) {

        stack.isEmpty match {
          case true => stack.push(char)
          case false => {
            var prev = stack.pop
            var balancedChar = prev match {
              case '(' => ')'
              case '{' => '}'
              case '[' => ']'
              case _   => prev
            }

            if (!char.equals(balancedChar)) {
              stack.push(prev)
              stack.push(char)
            }
          }
        }
      }
    }
    stack.isEmpty
  }
}
