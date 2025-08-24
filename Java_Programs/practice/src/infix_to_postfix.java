import java.util.Scanner;

    public class infix_to_postfix {

        int MAXSIZE;
        char[] stack;
        int top;

        public infix_to_postfix() {
            MAXSIZE = 100;
            stack = new char[MAXSIZE];
            top = -1;
        }

        void push(char ch) {
            if (top >= MAXSIZE - 1) {
                System.out.println("Overflow");
            }  else {
                stack[++top] = ch;
            }
        }

        char pop() {
            if (top < 0) {
                System.out.println("Underflow");
                return '\0';
            } else {
                return (char) stack[top--];
            }
        }

        int isOperator(char ch) {
            return ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == '^' ? 1 : 0;
        }

        int precedence(char ch) {
            if (ch == '+' || ch == '-') {
                return 1;
            }  else if (ch == '*' || ch == '/') {
                return 2;
            }  else if (ch == '^') {
                return 3;
            } else {
                return -1;
            }
        }

        void infixTOPostfix(char[] infix, char[] postfix) {
            int i, j = 0;
            char ch, popped;
            for (i = 0; infix[i] != '\0'; i++) {
                ch = infix[i];

                if (ch == ' ') {
                    continue; // skip whitespace
                }
                else if (Character.isLetterOrDigit(ch)) {
                    postfix[j++] = ch;
                }
                else if (ch == '(') {
                    push(ch);
                }
                else if (ch == ')') {
                    while ((popped = pop()) != '(') {
                        postfix[j++] = popped;
                    }
                }
                else if (isOperator(ch) == 1) {
                    while (top != -1 && precedence(ch) <= precedence(stack[top])) {
                        postfix[j++] = pop();
                    }
                    push(ch);
                }
            }

            while (top != -1) {
                postfix[j++] = pop();
            }

            postfix[j] = '\0';
        }

        public static void main(String[] args) {
            infix_to_postfix obj = new infix_to_postfix();
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the infix expression: ");
            String infixStr = sc.nextLine();
            infixStr = infixStr.replaceAll("\\s+", "");
            char[] infix = infixStr.toCharArray();
            char[] postfix = new char[infix.length];
            System.out.println("The postfix expression is: ");
            obj.infixTOPostfix(infix, postfix);
            System.out.println(new String(postfix));
            sc.close();
        }

    }