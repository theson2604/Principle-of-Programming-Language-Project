# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01e2\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\3\2\3\2\3\2\3\2\7\2\u008e\n\2\f\2\16\2\u0091\13")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\u009c\n\3\f")
        buf.write("\3\16\3\u009f\13\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00b0\n\4\3\4\3\4\3\5\3\5")
        buf.write("\5\5\u00b6\n\5\3\5\7\5\u00b9\n\5\f\5\16\5\u00bc\13\5\3")
        buf.write("\5\5\5\u00bf\n\5\3\6\3\6\7\6\u00c3\n\6\f\6\16\6\u00c6")
        buf.write("\13\6\5\6\u00c8\n\6\3\7\3\7\5\7\u00cc\n\7\3\7\6\7\u00cf")
        buf.write("\n\7\r\7\16\7\u00d0\3\b\3\b\5\b\u00d5\n\b\3\b\7\b\u00d8")
        buf.write("\n\b\f\b\16\b\u00db\13\b\3\b\5\b\u00de\n\b\3\b\3\b\3\t")
        buf.write("\3\t\5\t\u00e4\n\t\3\n\3\n\7\n\u00e8\n\n\f\n\16\n\u00eb")
        buf.write("\13\n\3\n\3\n\3\13\3\13\7\13\u00f1\n\13\f\13\16\13\u00f4")
        buf.write("\13\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3")
        buf.write("%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3.\3/\3/\3/\3\60\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3<\7<\u01b8\n<\f<")
        buf.write("\16<\u01bb\13<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3B")
        buf.write("\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\3B\5B\u01d7\nB\3")
        buf.write("C\6C\u01da\nC\rC\16C\u01db\3C\3C\3D\3D\3D\3\u008f\2E\3")
        buf.write("\3\5\4\7\5\t\2\13\2\r\2\17\6\21\2\23\7\25\b\27\t\31\n")
        buf.write("\33\13\35\f\37\r!\16#\17%\20\'\21)\22+\23-\24/\25\61\26")
        buf.write("\63\27\65\30\67\319\32;\33=\34?\35A\36C\37E G!I\"K#M$")
        buf.write("O%Q&S\'U(W)Y*[+],_-a.c/e\60g\61i\62k\63m\64o\65q\66s\67")
        buf.write("u8w9y\2{\2}\2\177\2\u0081\2\u0083\2\u0085:\u0087;\3\2")
        buf.write("\16\4\2\f\f\17\17\3\2\62\62\4\2GGgg\4\2--//\7\2\f\f\17")
        buf.write("\17$$))^^\b\2))ddhhppttvv\3\2C\\\3\2c|\5\2C\\aac|\3\2")
        buf.write("\63;\3\2\62;\5\2\13\f\17\17\"\"\2\u01f3\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\17\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\3\u0089\3\2\2\2\5\u0097\3\2\2\2\7\u00af\3\2\2")
        buf.write("\2\t\u00be\3\2\2\2\13\u00c0\3\2\2\2\r\u00c9\3\2\2\2\17")
        buf.write("\u00dd\3\2\2\2\21\u00e3\3\2\2\2\23\u00e5\3\2\2\2\25\u00ee")
        buf.write("\3\2\2\2\27\u00fa\3\2\2\2\31\u00fe\3\2\2\2\33\u0103\3")
        buf.write("\2\2\2\35\u0109\3\2\2\2\37\u0111\3\2\2\2!\u0114\3\2\2")
        buf.write("\2#\u0119\3\2\2\2%\u011f\3\2\2\2\'\u0125\3\2\2\2)\u0129")
        buf.write("\3\2\2\2+\u0132\3\2\2\2-\u0135\3\2\2\2/\u013d\3\2\2\2")
        buf.write("\61\u0144\3\2\2\2\63\u014b\3\2\2\2\65\u0150\3\2\2\2\67")
        buf.write("\u0156\3\2\2\29\u015b\3\2\2\2;\u015f\3\2\2\2=\u0168\3")
        buf.write("\2\2\2?\u016b\3\2\2\2A\u0173\3\2\2\2C\u0179\3\2\2\2E\u017b")
        buf.write("\3\2\2\2G\u017d\3\2\2\2I\u017f\3\2\2\2K\u0181\3\2\2\2")
        buf.write("M\u0183\3\2\2\2O\u0185\3\2\2\2Q\u0188\3\2\2\2S\u018b\3")
        buf.write("\2\2\2U\u018e\3\2\2\2W\u0191\3\2\2\2Y\u0193\3\2\2\2[\u0195")
        buf.write("\3\2\2\2]\u0198\3\2\2\2_\u019b\3\2\2\2a\u019e\3\2\2\2")
        buf.write("c\u01a0\3\2\2\2e\u01a2\3\2\2\2g\u01a4\3\2\2\2i\u01a6\3")
        buf.write("\2\2\2k\u01a8\3\2\2\2m\u01aa\3\2\2\2o\u01ac\3\2\2\2q\u01ae")
        buf.write("\3\2\2\2s\u01b0\3\2\2\2u\u01b2\3\2\2\2w\u01b4\3\2\2\2")
        buf.write("y\u01bc\3\2\2\2{\u01be\3\2\2\2}\u01c0\3\2\2\2\177\u01c2")
        buf.write("\3\2\2\2\u0081\u01c4\3\2\2\2\u0083\u01d6\3\2\2\2\u0085")
        buf.write("\u01d9\3\2\2\2\u0087\u01df\3\2\2\2\u0089\u008a\7\61\2")
        buf.write("\2\u008a\u008b\7,\2\2\u008b\u008f\3\2\2\2\u008c\u008e")
        buf.write("\13\2\2\2\u008d\u008c\3\2\2\2\u008e\u0091\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0092\3\2\2\2")
        buf.write("\u0091\u008f\3\2\2\2\u0092\u0093\7,\2\2\u0093\u0094\7")
        buf.write("\61\2\2\u0094\u0095\3\2\2\2\u0095\u0096\b\2\2\2\u0096")
        buf.write("\4\3\2\2\2\u0097\u0098\7\61\2\2\u0098\u0099\7\61\2\2\u0099")
        buf.write("\u009d\3\2\2\2\u009a\u009c\n\2\2\2\u009b\u009a\3\2\2\2")
        buf.write("\u009c\u009f\3\2\2\2\u009d\u009b\3\2\2\2\u009d\u009e\3")
        buf.write("\2\2\2\u009e\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u00a0\u00a1")
        buf.write("\b\3\2\2\u00a1\6\3\2\2\2\u00a2\u00a3\5\t\5\2\u00a3\u00a4")
        buf.write("\5\13\6\2\u00a4\u00a5\5\r\7\2\u00a5\u00b0\3\2\2\2\u00a6")
        buf.write("\u00a7\5\t\5\2\u00a7\u00a8\5\13\6\2\u00a8\u00b0\3\2\2")
        buf.write("\2\u00a9\u00aa\5\13\6\2\u00aa\u00ab\5\r\7\2\u00ab\u00b0")
        buf.write("\3\2\2\2\u00ac\u00ad\5\t\5\2\u00ad\u00ae\5\r\7\2\u00ae")
        buf.write("\u00b0\3\2\2\2\u00af\u00a2\3\2\2\2\u00af\u00a6\3\2\2\2")
        buf.write("\u00af\u00a9\3\2\2\2\u00af\u00ac\3\2\2\2\u00b0\u00b1\3")
        buf.write("\2\2\2\u00b1\u00b2\b\4\3\2\u00b2\b\3\2\2\2\u00b3\u00ba")
        buf.write("\5\177@\2\u00b4\u00b6\7a\2\2\u00b5\u00b4\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00b9\5\u0081")
        buf.write("A\2\u00b8\u00b5\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8")
        buf.write("\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bf\3\2\2\2\u00bc")
        buf.write("\u00ba\3\2\2\2\u00bd\u00bf\t\3\2\2\u00be\u00b3\3\2\2\2")
        buf.write("\u00be\u00bd\3\2\2\2\u00bf\n\3\2\2\2\u00c0\u00c7\5m\67")
        buf.write("\2\u00c1\u00c3\5\u0081A\2\u00c2\u00c1\3\2\2\2\u00c3\u00c6")
        buf.write("\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5")
        buf.write("\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c7\u00c4\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\f\3\2\2\2\u00c9\u00cb\t\4\2")
        buf.write("\2\u00ca\u00cc\t\5\2\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc")
        buf.write("\3\2\2\2\u00cc\u00ce\3\2\2\2\u00cd\u00cf\5\u0081A\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00ce\3\2\2\2")
        buf.write("\u00d0\u00d1\3\2\2\2\u00d1\16\3\2\2\2\u00d2\u00d9\5\177")
        buf.write("@\2\u00d3\u00d5\7a\2\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5")
        buf.write("\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\5\u0081A\2\u00d7")
        buf.write("\u00d4\3\2\2\2\u00d8\u00db\3\2\2\2\u00d9\u00d7\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00de\3\2\2\2\u00db\u00d9\3")
        buf.write("\2\2\2\u00dc\u00de\t\3\2\2\u00dd\u00d2\3\2\2\2\u00dd\u00dc")
        buf.write("\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\b\b\4\2\u00e0")
        buf.write("\20\3\2\2\2\u00e1\u00e4\n\6\2\2\u00e2\u00e4\5\u0083B\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e3\u00e2\3\2\2\2\u00e4\22\3\2")
        buf.write("\2\2\u00e5\u00e9\7$\2\2\u00e6\u00e8\5\21\t\2\u00e7\u00e6")
        buf.write("\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9")
        buf.write("\u00ea\3\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2")
        buf.write("\u00ec\u00ed\b\n\5\2\u00ed\24\3\2\2\2\u00ee\u00f2\7$\2")
        buf.write("\2\u00ef\u00f1\5\21\t\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4")
        buf.write("\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f5\3\2\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\7^\2\2")
        buf.write("\u00f6\u00f7\n\7\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f9\b")
        buf.write("\13\6\2\u00f9\26\3\2\2\2\u00fa\u00fb\5\23\n\2\u00fb\u00fc")
        buf.write("\7$\2\2\u00fc\u00fd\b\f\7\2\u00fd\30\3\2\2\2\u00fe\u00ff")
        buf.write("\7c\2\2\u00ff\u0100\7w\2\2\u0100\u0101\7v\2\2\u0101\u0102")
        buf.write("\7q\2\2\u0102\32\3\2\2\2\u0103\u0104\7d\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7g\2\2\u0106\u0107\7c\2\2\u0107\u0108")
        buf.write("\7m\2\2\u0108\34\3\2\2\2\u0109\u010a\7d\2\2\u010a\u010b")
        buf.write("\7q\2\2\u010b\u010c\7q\2\2\u010c\u010d\7n\2\2\u010d\u010e")
        buf.write("\7g\2\2\u010e\u010f\7c\2\2\u010f\u0110\7p\2\2\u0110\36")
        buf.write("\3\2\2\2\u0111\u0112\7f\2\2\u0112\u0113\7q\2\2\u0113 ")
        buf.write("\3\2\2\2\u0114\u0115\7g\2\2\u0115\u0116\7n\2\2\u0116\u0117")
        buf.write("\7u\2\2\u0117\u0118\7g\2\2\u0118\"\3\2\2\2\u0119\u011a")
        buf.write("\7h\2\2\u011a\u011b\7c\2\2\u011b\u011c\7n\2\2\u011c\u011d")
        buf.write("\7u\2\2\u011d\u011e\7g\2\2\u011e$\3\2\2\2\u011f\u0120")
        buf.write("\7h\2\2\u0120\u0121\7n\2\2\u0121\u0122\7q\2\2\u0122\u0123")
        buf.write("\7c\2\2\u0123\u0124\7v\2\2\u0124&\3\2\2\2\u0125\u0126")
        buf.write("\7h\2\2\u0126\u0127\7q\2\2\u0127\u0128\7t\2\2\u0128(\3")
        buf.write("\2\2\2\u0129\u012a\7h\2\2\u012a\u012b\7w\2\2\u012b\u012c")
        buf.write("\7p\2\2\u012c\u012d\7e\2\2\u012d\u012e\7v\2\2\u012e\u012f")
        buf.write("\7k\2\2\u012f\u0130\7q\2\2\u0130\u0131\7p\2\2\u0131*\3")
        buf.write("\2\2\2\u0132\u0133\7k\2\2\u0133\u0134\7h\2\2\u0134,\3")
        buf.write("\2\2\2\u0135\u0136\7k\2\2\u0136\u0137\7p\2\2\u0137\u0138")
        buf.write("\7v\2\2\u0138\u0139\7g\2\2\u0139\u013a\7i\2\2\u013a\u013b")
        buf.write("\7g\2\2\u013b\u013c\7t\2\2\u013c.\3\2\2\2\u013d\u013e")
        buf.write("\7t\2\2\u013e\u013f\7g\2\2\u013f\u0140\7v\2\2\u0140\u0141")
        buf.write("\7w\2\2\u0141\u0142\7t\2\2\u0142\u0143\7p\2\2\u0143\60")
        buf.write("\3\2\2\2\u0144\u0145\7u\2\2\u0145\u0146\7v\2\2\u0146\u0147")
        buf.write("\7t\2\2\u0147\u0148\7k\2\2\u0148\u0149\7p\2\2\u0149\u014a")
        buf.write("\7i\2\2\u014a\62\3\2\2\2\u014b\u014c\7v\2\2\u014c\u014d")
        buf.write("\7t\2\2\u014d\u014e\7w\2\2\u014e\u014f\7g\2\2\u014f\64")
        buf.write("\3\2\2\2\u0150\u0151\7y\2\2\u0151\u0152\7j\2\2\u0152\u0153")
        buf.write("\7k\2\2\u0153\u0154\7n\2\2\u0154\u0155\7g\2\2\u0155\66")
        buf.write("\3\2\2\2\u0156\u0157\7x\2\2\u0157\u0158\7q\2\2\u0158\u0159")
        buf.write("\7k\2\2\u0159\u015a\7f\2\2\u015a8\3\2\2\2\u015b\u015c")
        buf.write("\7q\2\2\u015c\u015d\7w\2\2\u015d\u015e\7v\2\2\u015e:\3")
        buf.write("\2\2\2\u015f\u0160\7e\2\2\u0160\u0161\7q\2\2\u0161\u0162")
        buf.write("\7p\2\2\u0162\u0163\7v\2\2\u0163\u0164\7k\2\2\u0164\u0165")
        buf.write("\7p\2\2\u0165\u0166\7w\2\2\u0166\u0167\7g\2\2\u0167<\3")
        buf.write("\2\2\2\u0168\u0169\7q\2\2\u0169\u016a\7h\2\2\u016a>\3")
        buf.write("\2\2\2\u016b\u016c\7k\2\2\u016c\u016d\7p\2\2\u016d\u016e")
        buf.write("\7j\2\2\u016e\u016f\7g\2\2\u016f\u0170\7t\2\2\u0170\u0171")
        buf.write("\7k\2\2\u0171\u0172\7v\2\2\u0172@\3\2\2\2\u0173\u0174")
        buf.write("\7c\2\2\u0174\u0175\7t\2\2\u0175\u0176\7t\2\2\u0176\u0177")
        buf.write("\7c\2\2\u0177\u0178\7{\2\2\u0178B\3\2\2\2\u0179\u017a")
        buf.write("\7-\2\2\u017aD\3\2\2\2\u017b\u017c\7,\2\2\u017cF\3\2\2")
        buf.write("\2\u017d\u017e\7\61\2\2\u017eH\3\2\2\2\u017f\u0180\7\'")
        buf.write("\2\2\u0180J\3\2\2\2\u0181\u0182\7/\2\2\u0182L\3\2\2\2")
        buf.write("\u0183\u0184\7#\2\2\u0184N\3\2\2\2\u0185\u0186\7(\2\2")
        buf.write("\u0186\u0187\7(\2\2\u0187P\3\2\2\2\u0188\u0189\7~\2\2")
        buf.write("\u0189\u018a\7~\2\2\u018aR\3\2\2\2\u018b\u018c\7?\2\2")
        buf.write("\u018c\u018d\7?\2\2\u018dT\3\2\2\2\u018e\u018f\7#\2\2")
        buf.write("\u018f\u0190\7?\2\2\u0190V\3\2\2\2\u0191\u0192\7>\2\2")
        buf.write("\u0192X\3\2\2\2\u0193\u0194\7@\2\2\u0194Z\3\2\2\2\u0195")
        buf.write("\u0196\7>\2\2\u0196\u0197\7?\2\2\u0197\\\3\2\2\2\u0198")
        buf.write("\u0199\7@\2\2\u0199\u019a\7?\2\2\u019a^\3\2\2\2\u019b")
        buf.write("\u019c\7<\2\2\u019c\u019d\7<\2\2\u019d`\3\2\2\2\u019e")
        buf.write("\u019f\7*\2\2\u019fb\3\2\2\2\u01a0\u01a1\7+\2\2\u01a1")
        buf.write("d\3\2\2\2\u01a2\u01a3\7]\2\2\u01a3f\3\2\2\2\u01a4\u01a5")
        buf.write("\7_\2\2\u01a5h\3\2\2\2\u01a6\u01a7\7}\2\2\u01a7j\3\2\2")
        buf.write("\2\u01a8\u01a9\7\177\2\2\u01a9l\3\2\2\2\u01aa\u01ab\7")
        buf.write("\60\2\2\u01abn\3\2\2\2\u01ac\u01ad\7.\2\2\u01adp\3\2\2")
        buf.write("\2\u01ae\u01af\7<\2\2\u01afr\3\2\2\2\u01b0\u01b1\7=\2")
        buf.write("\2\u01b1t\3\2\2\2\u01b2\u01b3\7?\2\2\u01b3v\3\2\2\2\u01b4")
        buf.write("\u01b9\5}?\2\u01b5\u01b8\5}?\2\u01b6\u01b8\5\u0081A\2")
        buf.write("\u01b7\u01b5\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8\u01bb\3")
        buf.write("\2\2\2\u01b9\u01b7\3\2\2\2\u01b9\u01ba\3\2\2\2\u01bax")
        buf.write("\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bc\u01bd\t\b\2\2\u01bd")
        buf.write("z\3\2\2\2\u01be\u01bf\t\t\2\2\u01bf|\3\2\2\2\u01c0\u01c1")
        buf.write("\t\n\2\2\u01c1~\3\2\2\2\u01c2\u01c3\t\13\2\2\u01c3\u0080")
        buf.write("\3\2\2\2\u01c4\u01c5\t\f\2\2\u01c5\u0082\3\2\2\2\u01c6")
        buf.write("\u01c7\7^\2\2\u01c7\u01d7\7)\2\2\u01c8\u01c9\7^\2\2\u01c9")
        buf.write("\u01d7\7$\2\2\u01ca\u01cb\7^\2\2\u01cb\u01d7\7^\2\2\u01cc")
        buf.write("\u01cd\7^\2\2\u01cd\u01d7\7d\2\2\u01ce\u01cf\7^\2\2\u01cf")
        buf.write("\u01d7\7h\2\2\u01d0\u01d1\7^\2\2\u01d1\u01d7\7p\2\2\u01d2")
        buf.write("\u01d3\7^\2\2\u01d3\u01d7\7t\2\2\u01d4\u01d5\7^\2\2\u01d5")
        buf.write("\u01d7\7v\2\2\u01d6\u01c6\3\2\2\2\u01d6\u01c8\3\2\2\2")
        buf.write("\u01d6\u01ca\3\2\2\2\u01d6\u01cc\3\2\2\2\u01d6\u01ce\3")
        buf.write("\2\2\2\u01d6\u01d0\3\2\2\2\u01d6\u01d2\3\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d7\u0084\3\2\2\2\u01d8\u01da\t\r\2\2\u01d9")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01d9\3\2\2\2")
        buf.write("\u01db\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01de\b")
        buf.write("C\2\2\u01de\u0086\3\2\2\2\u01df\u01e0\13\2\2\2\u01e0\u01e1")
        buf.write("\bD\b\2\u01e1\u0088\3\2\2\2\27\2\u008f\u009d\u00af\u00b5")
        buf.write("\u00ba\u00be\u00c4\u00c7\u00cb\u00d0\u00d4\u00d9\u00dd")
        buf.write("\u00e3\u00e9\u00f2\u01b7\u01b9\u01d6\u01db\t\b\2\2\3\4")
        buf.write("\2\3\b\3\3\n\4\3\13\5\3\f\6\3D\7")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BLOCK_COMMENT = 1
    LINE_COMMENT = 2
    FLOATLIT = 3
    INTLIT = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6
    STRINGLIT = 7
    AUTO = 8
    BREAK = 9
    BOOL = 10
    DO = 11
    ELSE = 12
    FALSE = 13
    FLOAT = 14
    FOR = 15
    FUNCTION = 16
    IF = 17
    INTEGER = 18
    RETURN = 19
    STRING = 20
    TRUE = 21
    WHILE = 22
    VOID = 23
    OUT = 24
    CONTINUE = 25
    OF = 26
    INHERIT = 27
    ARRAY = 28
    PLUS = 29
    MULT = 30
    DIV = 31
    MOD = 32
    MINUS = 33
    NOT = 34
    AND = 35
    OR = 36
    EQ = 37
    NEQ = 38
    LESS = 39
    GREATER = 40
    LE = 41
    GE = 42
    CONCAT = 43
    LPARENT = 44
    RPARENT = 45
    LBRACKET = 46
    RBRACKET = 47
    LCURLY = 48
    RCURLY = 49
    DOT = 50
    COMMA = 51
    COLON = 52
    SECOLON = 53
    EQASSIGN = 54
    ID = 55
    WS = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'auto'", "'break'", "'boolean'", "'do'", "'else'", "'false'", 
            "'float'", "'for'", "'function'", "'if'", "'integer'", "'return'", 
            "'string'", "'true'", "'while'", "'void'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'+'", "'*'", "'/'", "'%'", 
            "'-'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'<'", "'>'", 
            "'<='", "'>='", "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "','", "':'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "LINE_COMMENT", "FLOATLIT", "INTLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "STRINGLIT", "AUTO", "BREAK", "BOOL", "DO", 
            "ELSE", "FALSE", "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", 
            "RETURN", "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "PLUS", "MULT", "DIV", "MOD", "MINUS", 
            "NOT", "AND", "OR", "EQ", "NEQ", "LESS", "GREATER", "LE", "GE", 
            "CONCAT", "LPARENT", "RPARENT", "LBRACKET", "RBRACKET", "LCURLY", 
            "RCURLY", "DOT", "COMMA", "COLON", "SECOLON", "EQASSIGN", "ID", 
            "WS", "ERROR_CHAR" ]

    ruleNames = [ "BLOCK_COMMENT", "LINE_COMMENT", "FLOATLIT", "INT", "DECIMAL", 
                  "EXP", "INTLIT", "ALLOW_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRINGLIT", "AUTO", "BREAK", "BOOL", "DO", "ELSE", "FALSE", 
                  "FLOAT", "FOR", "FUNCTION", "IF", "INTEGER", "RETURN", 
                  "STRING", "TRUE", "WHILE", "VOID", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "PLUS", "MULT", "DIV", "MOD", 
                  "MINUS", "NOT", "AND", "OR", "EQ", "NEQ", "LESS", "GREATER", 
                  "LE", "GE", "CONCAT", "LPARENT", "RPARENT", "LBRACKET", 
                  "RBRACKET", "LCURLY", "RCURLY", "DOT", "COMMA", "COLON", 
                  "SECOLON", "EQASSIGN", "ID", "UPPER_LETTER", "LOWER_LETTER", 
                  "FULL_LETTER", "DIGIT", "FULL_DIGIT", "ESCAPE_SEQUENCE", 
                  "WS", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.FLOATLIT_action 
            actions[6] = self.INTLIT_action 
            actions[8] = self.UNCLOSE_STRING_action 
            actions[9] = self.ILLEGAL_ESCAPE_action 
            actions[10] = self.STRINGLIT_action 
            actions[66] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise UncloseString(self.text[1:])
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
            raise IllegalEscape(self.text[1:])
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text[1:-1]
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            raise ErrorToken(self.text)
     


