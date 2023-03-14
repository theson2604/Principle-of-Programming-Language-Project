# Generated from e:\slides\222\principle\assignments\assignment2\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2=")
        buf.write("\u021b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23")
        buf.write("\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$")
        buf.write("\3%\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3")
        buf.write("(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3,\3,\3,\3,\3,\3,\3,\3-\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u014f\n\60\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u015c\n")
        buf.write("\61\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\3\62\5\62")
        buf.write("\u0167\n\62\3\63\3\63\7\63\u016b\n\63\f\63\16\63\u016e")
        buf.write("\13\63\3\63\3\63\3\63\3\64\3\64\7\64\u0175\n\64\f\64\16")
        buf.write("\64\u0178\13\64\3\64\5\64\u017b\n\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\7\64\u0183\n\64\f\64\16\64\u0186\13\64\3")
        buf.write("\64\5\64\u0189\n\64\3\64\3\64\3\64\3\64\3\64\7\64\u0190")
        buf.write("\n\64\f\64\16\64\u0193\13\64\3\64\5\64\u0196\n\64\3\64")
        buf.write("\3\64\3\64\5\64\u019b\n\64\3\65\3\65\7\65\u019f\n\65\f")
        buf.write("\65\16\65\u01a2\13\65\3\65\5\65\u01a5\n\65\3\65\3\65\3")
        buf.write("\66\3\66\5\66\u01ab\n\66\3\66\3\66\3\66\7\66\u01b0\n\66")
        buf.write("\f\66\16\66\u01b3\13\66\3\67\3\67\38\38\39\39\59\u01bb")
        buf.write("\n9\3:\3:\3;\3;\3<\3<\7<\u01c3\n<\f<\16<\u01c6\13<\3=")
        buf.write("\3=\5=\u01ca\n=\3=\6=\u01cd\n=\r=\16=\u01ce\3>\3>\3?\3")
        buf.write("?\3@\3@\3@\3@\7@\u01d9\n@\f@\16@\u01dc\13@\3@\3@\3@\3")
        buf.write("@\3@\3A\3A\3A\3A\7A\u01e7\nA\fA\16A\u01ea\13A\3A\3A\3")
        buf.write("B\6B\u01ef\nB\rB\16B\u01f0\3B\3B\3C\3C\7C\u01f7\nC\fC")
        buf.write("\16C\u01fa\13C\3C\5C\u01fd\nC\3C\3C\3D\3D\7D\u0203\nD")
        buf.write("\fD\16D\u0206\13D\3D\3D\3D\3E\3E\5E\u020d\nE\3F\3F\3F")
        buf.write("\5F\u0212\nF\3G\3G\3G\5G\u0217\nG\3H\3H\3H\3\u01da\2I")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O")
        buf.write(")Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m\2o\2q\2")
        buf.write("s\2u\2w\2y\2{\2}\2\1778\u00819\u0083:\u0085;\u0087<\u0089")
        buf.write("\2\u008b\2\u008d\2\u008f=\3\2\21\3\2\63;\4\2\62;aa\3\2")
        buf.write("\62\62\3\2c|\3\2C\\\3\2\62;\4\2GGgg\4\2--//\4\2\f\f\17")
        buf.write("\17\5\2\13\f\17\17\"\"\7\3\n\f\16\17$$))^^\7\2\n\f\16")
        buf.write("\17$$))^^\n\2$$))^^ddhhppttvv\4\2\n\f\16\17\3\2^^\2\u0242")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u008f\3\2\2\2\3\u0091\3\2\2\2\5\u0093\3\2\2\2\7\u0095")
        buf.write("\3\2\2\2\t\u0097\3\2\2\2\13\u0099\3\2\2\2\r\u009b\3\2")
        buf.write("\2\2\17\u009d\3\2\2\2\21\u00a0\3\2\2\2\23\u00a3\3\2\2")
        buf.write("\2\25\u00a6\3\2\2\2\27\u00a9\3\2\2\2\31\u00ac\3\2\2\2")
        buf.write("\33\u00af\3\2\2\2\35\u00b2\3\2\2\2\37\u00b4\3\2\2\2!\u00b6")
        buf.write("\3\2\2\2#\u00b8\3\2\2\2%\u00ba\3\2\2\2\'\u00bc\3\2\2\2")
        buf.write(")\u00be\3\2\2\2+\u00c0\3\2\2\2-\u00c2\3\2\2\2/\u00c4\3")
        buf.write("\2\2\2\61\u00c6\3\2\2\2\63\u00c8\3\2\2\2\65\u00ca\3\2")
        buf.write("\2\2\67\u00cc\3\2\2\29\u00d0\3\2\2\2;\u00d8\3\2\2\2=\u00de")
        buf.write("\3\2\2\2?\u00e5\3\2\2\2A\u00ed\3\2\2\2C\u00f2\3\2\2\2")
        buf.write("E\u00f8\3\2\2\2G\u0100\3\2\2\2I\u0109\3\2\2\2K\u010c\3")
        buf.write("\2\2\2M\u0111\3\2\2\2O\u0115\3\2\2\2Q\u011b\3\2\2\2S\u011e")
        buf.write("\3\2\2\2U\u0124\3\2\2\2W\u012d\3\2\2\2Y\u0134\3\2\2\2")
        buf.write("[\u0138\3\2\2\2]\u013d\3\2\2\2_\u014e\3\2\2\2a\u015b\3")
        buf.write("\2\2\2c\u0166\3\2\2\2e\u0168\3\2\2\2g\u019a\3\2\2\2i\u01a4")
        buf.write("\3\2\2\2k\u01aa\3\2\2\2m\u01b4\3\2\2\2o\u01b6\3\2\2\2")
        buf.write("q\u01ba\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01c0\3")
        buf.write("\2\2\2y\u01c7\3\2\2\2{\u01d0\3\2\2\2}\u01d2\3\2\2\2\177")
        buf.write("\u01d4\3\2\2\2\u0081\u01e2\3\2\2\2\u0083\u01ee\3\2\2\2")
        buf.write("\u0085\u01f4\3\2\2\2\u0087\u0200\3\2\2\2\u0089\u020c\3")
        buf.write("\2\2\2\u008b\u0211\3\2\2\2\u008d\u0216\3\2\2\2\u008f\u0218")
        buf.write("\3\2\2\2\u0091\u0092\7-\2\2\u0092\4\3\2\2\2\u0093\u0094")
        buf.write("\7/\2\2\u0094\6\3\2\2\2\u0095\u0096\7,\2\2\u0096\b\3\2")
        buf.write("\2\2\u0097\u0098\7\61\2\2\u0098\n\3\2\2\2\u0099\u009a")
        buf.write("\7\'\2\2\u009a\f\3\2\2\2\u009b\u009c\7#\2\2\u009c\16\3")
        buf.write("\2\2\2\u009d\u009e\7<\2\2\u009e\u009f\7<\2\2\u009f\20")
        buf.write("\3\2\2\2\u00a0\u00a1\7(\2\2\u00a1\u00a2\7(\2\2\u00a2\22")
        buf.write("\3\2\2\2\u00a3\u00a4\7~\2\2\u00a4\u00a5\7~\2\2\u00a5\24")
        buf.write("\3\2\2\2\u00a6\u00a7\7?\2\2\u00a7\u00a8\7?\2\2\u00a8\26")
        buf.write("\3\2\2\2\u00a9\u00aa\7>\2\2\u00aa\u00ab\7?\2\2\u00ab\30")
        buf.write("\3\2\2\2\u00ac\u00ad\7@\2\2\u00ad\u00ae\7?\2\2\u00ae\32")
        buf.write("\3\2\2\2\u00af\u00b0\7#\2\2\u00b0\u00b1\7?\2\2\u00b1\34")
        buf.write("\3\2\2\2\u00b2\u00b3\7>\2\2\u00b3\36\3\2\2\2\u00b4\u00b5")
        buf.write("\7@\2\2\u00b5 \3\2\2\2\u00b6\u00b7\7*\2\2\u00b7\"\3\2")
        buf.write("\2\2\u00b8\u00b9\7+\2\2\u00b9$\3\2\2\2\u00ba\u00bb\7}")
        buf.write("\2\2\u00bb&\3\2\2\2\u00bc\u00bd\7\177\2\2\u00bd(\3\2\2")
        buf.write("\2\u00be\u00bf\7]\2\2\u00bf*\3\2\2\2\u00c0\u00c1\7_\2")
        buf.write("\2\u00c1,\3\2\2\2\u00c2\u00c3\7=\2\2\u00c3.\3\2\2\2\u00c4")
        buf.write("\u00c5\7.\2\2\u00c5\60\3\2\2\2\u00c6\u00c7\7<\2\2\u00c7")
        buf.write("\62\3\2\2\2\u00c8\u00c9\7\60\2\2\u00c9\64\3\2\2\2\u00ca")
        buf.write("\u00cb\7?\2\2\u00cb\66\3\2\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7p\2\2\u00ce\u00cf\7v\2\2\u00cf8\3\2\2\2\u00d0")
        buf.write("\u00d1\7k\2\2\u00d1\u00d2\7p\2\2\u00d2\u00d3\7v\2\2\u00d3")
        buf.write("\u00d4\7g\2\2\u00d4\u00d5\7i\2\2\u00d5\u00d6\7g\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7:\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9")
        buf.write("\u00da\7n\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7c\2\2\u00dc")
        buf.write("\u00dd\7v\2\2\u00dd<\3\2\2\2\u00de\u00df\7u\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\u00e1\7t\2\2\u00e1\u00e2\7k\2\2\u00e2")
        buf.write("\u00e3\7p\2\2\u00e3\u00e4\7i\2\2\u00e4>\3\2\2\2\u00e5")
        buf.write("\u00e6\7d\2\2\u00e6\u00e7\7q\2\2\u00e7\u00e8\7q\2\2\u00e8")
        buf.write("\u00e9\7n\2\2\u00e9\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb")
        buf.write("\u00ec\7p\2\2\u00ec@\3\2\2\2\u00ed\u00ee\7x\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7f\2\2\u00f1")
        buf.write("B\3\2\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7t\2\2\u00f4")
        buf.write("\u00f5\7t\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7{\2\2\u00f7")
        buf.write("D\3\2\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa")
        buf.write("\u00fb\7j\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7t\2\2\u00fd")
        buf.write("\u00fe\7k\2\2\u00fe\u00ff\7v\2\2\u00ffF\3\2\2\2\u0100")
        buf.write("\u0101\7h\2\2\u0101\u0102\7w\2\2\u0102\u0103\7p\2\2\u0103")
        buf.write("\u0104\7e\2\2\u0104\u0105\7v\2\2\u0105\u0106\7k\2\2\u0106")
        buf.write("\u0107\7q\2\2\u0107\u0108\7p\2\2\u0108H\3\2\2\2\u0109")
        buf.write("\u010a\7k\2\2\u010a\u010b\7h\2\2\u010bJ\3\2\2\2\u010c")
        buf.write("\u010d\7g\2\2\u010d\u010e\7n\2\2\u010e\u010f\7u\2\2\u010f")
        buf.write("\u0110\7g\2\2\u0110L\3\2\2\2\u0111\u0112\7h\2\2\u0112")
        buf.write("\u0113\7q\2\2\u0113\u0114\7t\2\2\u0114N\3\2\2\2\u0115")
        buf.write("\u0116\7y\2\2\u0116\u0117\7j\2\2\u0117\u0118\7k\2\2\u0118")
        buf.write("\u0119\7n\2\2\u0119\u011a\7g\2\2\u011aP\3\2\2\2\u011b")
        buf.write("\u011c\7f\2\2\u011c\u011d\7q\2\2\u011dR\3\2\2\2\u011e")
        buf.write("\u011f\7d\2\2\u011f\u0120\7t\2\2\u0120\u0121\7g\2\2\u0121")
        buf.write("\u0122\7c\2\2\u0122\u0123\7m\2\2\u0123T\3\2\2\2\u0124")
        buf.write("\u0125\7e\2\2\u0125\u0126\7q\2\2\u0126\u0127\7p\2\2\u0127")
        buf.write("\u0128\7v\2\2\u0128\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a")
        buf.write("\u012b\7w\2\2\u012b\u012c\7g\2\2\u012cV\3\2\2\2\u012d")
        buf.write("\u012e\7t\2\2\u012e\u012f\7g\2\2\u012f\u0130\7v\2\2\u0130")
        buf.write("\u0131\7w\2\2\u0131\u0132\7t\2\2\u0132\u0133\7p\2\2\u0133")
        buf.write("X\3\2\2\2\u0134\u0135\7q\2\2\u0135\u0136\7w\2\2\u0136")
        buf.write("\u0137\7v\2\2\u0137Z\3\2\2\2\u0138\u0139\7c\2\2\u0139")
        buf.write("\u013a\7w\2\2\u013a\u013b\7v\2\2\u013b\u013c\7q\2\2\u013c")
        buf.write("\\\3\2\2\2\u013d\u013e\7q\2\2\u013e\u013f\7h\2\2\u013f")
        buf.write("^\3\2\2\2\u0140\u014f\5\3\2\2\u0141\u014f\5\5\3\2\u0142")
        buf.write("\u014f\5\7\4\2\u0143\u014f\5\t\5\2\u0144\u014f\5\13\6")
        buf.write("\2\u0145\u014f\5\r\7\2\u0146\u014f\5\21\t\2\u0147\u014f")
        buf.write("\5\23\n\2\u0148\u014f\5\25\13\2\u0149\u014f\5\27\f\2\u014a")
        buf.write("\u014f\5\31\r\2\u014b\u014f\5\33\16\2\u014c\u014f\5\35")
        buf.write("\17\2\u014d\u014f\5\37\20\2\u014e\u0140\3\2\2\2\u014e")
        buf.write("\u0141\3\2\2\2\u014e\u0142\3\2\2\2\u014e\u0143\3\2\2\2")
        buf.write("\u014e\u0144\3\2\2\2\u014e\u0145\3\2\2\2\u014e\u0146\3")
        buf.write("\2\2\2\u014e\u0147\3\2\2\2\u014e\u0148\3\2\2\2\u014e\u0149")
        buf.write("\3\2\2\2\u014e\u014a\3\2\2\2\u014e\u014b\3\2\2\2\u014e")
        buf.write("\u014c\3\2\2\2\u014e\u014d\3\2\2\2\u014f`\3\2\2\2\u0150")
        buf.write("\u015c\5!\21\2\u0151\u015c\5#\22\2\u0152\u015c\5%\23\2")
        buf.write("\u0153\u015c\5\'\24\2\u0154\u015c\5)\25\2\u0155\u015c")
        buf.write("\5+\26\2\u0156\u015c\5-\27\2\u0157\u015c\5/\30\2\u0158")
        buf.write("\u015c\5\61\31\2\u0159\u015c\5\63\32\2\u015a\u015c\5\65")
        buf.write("\33\2\u015b\u0150\3\2\2\2\u015b\u0151\3\2\2\2\u015b\u0152")
        buf.write("\3\2\2\2\u015b\u0153\3\2\2\2\u015b\u0154\3\2\2\2\u015b")
        buf.write("\u0155\3\2\2\2\u015b\u0156\3\2\2\2\u015b\u0157\3\2\2\2")
        buf.write("\u015b\u0158\3\2\2\2\u015b\u0159\3\2\2\2\u015b\u015a\3")
        buf.write("\2\2\2\u015cb\3\2\2\2\u015d\u015e\7v\2\2\u015e\u015f\7")
        buf.write("t\2\2\u015f\u0160\7w\2\2\u0160\u0167\7g\2\2\u0161\u0162")
        buf.write("\7h\2\2\u0162\u0163\7c\2\2\u0163\u0164\7n\2\2\u0164\u0165")
        buf.write("\7u\2\2\u0165\u0167\7g\2\2\u0166\u015d\3\2\2\2\u0166\u0161")
        buf.write("\3\2\2\2\u0167d\3\2\2\2\u0168\u016c\5}?\2\u0169\u016b")
        buf.write("\5\u0089E\2\u016a\u0169\3\2\2\2\u016b\u016e\3\2\2\2\u016c")
        buf.write("\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016f\3\2\2\2")
        buf.write("\u016e\u016c\3\2\2\2\u016f\u0170\5}?\2\u0170\u0171\b\63")
        buf.write("\2\2\u0171f\3\2\2\2\u0172\u0176\t\2\2\2\u0173\u0175\t")
        buf.write("\3\2\2\u0174\u0173\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0177\3\2\2\2\u0177\u017b\3\2\2\2\u0178")
        buf.write("\u0176\3\2\2\2\u0179\u017b\t\4\2\2\u017a\u0172\3\2\2\2")
        buf.write("\u017a\u0179\3\2\2\2\u017a\u017b\3\2\2\2\u017b\u017c\3")
        buf.write("\2\2\2\u017c\u017d\5w<\2\u017d\u017e\5y=\2\u017e\u017f")
        buf.write("\b\64\3\2\u017f\u019b\3\2\2\2\u0180\u0184\t\2\2\2\u0181")
        buf.write("\u0183\t\3\2\2\u0182\u0181\3\2\2\2\u0183\u0186\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0189\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0187\u0189\t\4\2\2\u0188\u0180")
        buf.write("\3\2\2\2\u0188\u0187\3\2\2\2\u0189\u018a\3\2\2\2\u018a")
        buf.write("\u018b\5w<\2\u018b\u018c\b\64\4\2\u018c\u019b\3\2\2\2")
        buf.write("\u018d\u0191\t\2\2\2\u018e\u0190\t\3\2\2\u018f\u018e\3")
        buf.write("\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2\u0191\u0192")
        buf.write("\3\2\2\2\u0192\u0196\3\2\2\2\u0193\u0191\3\2\2\2\u0194")
        buf.write("\u0196\t\4\2\2\u0195\u018d\3\2\2\2\u0195\u0194\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0198\5y=\2\u0198\u0199\b\64")
        buf.write("\5\2\u0199\u019b\3\2\2\2\u019a\u017a\3\2\2\2\u019a\u0188")
        buf.write("\3\2\2\2\u019a\u0195\3\2\2\2\u019bh\3\2\2\2\u019c\u01a0")
        buf.write("\t\2\2\2\u019d\u019f\t\3\2\2\u019e\u019d\3\2\2\2\u019f")
        buf.write("\u01a2\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2")
        buf.write("\u01a1\u01a5\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a3\u01a5\t")
        buf.write("\4\2\2\u01a4\u019c\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5\u01a6")
        buf.write("\3\2\2\2\u01a6\u01a7\b\65\6\2\u01a7j\3\2\2\2\u01a8\u01ab")
        buf.write("\5q9\2\u01a9\u01ab\5{>\2\u01aa\u01a8\3\2\2\2\u01aa\u01a9")
        buf.write("\3\2\2\2\u01ab\u01b1\3\2\2\2\u01ac\u01b0\5q9\2\u01ad\u01b0")
        buf.write("\5s:\2\u01ae\u01b0\5{>\2\u01af\u01ac\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2l\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b5\t\5\2\2\u01b5n\3\2\2\2\u01b6")
        buf.write("\u01b7\t\6\2\2\u01b7p\3\2\2\2\u01b8\u01bb\5m\67\2\u01b9")
        buf.write("\u01bb\5o8\2\u01ba\u01b8\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb")
        buf.write("r\3\2\2\2\u01bc\u01bd\t\7\2\2\u01bdt\3\2\2\2\u01be\u01bf")
        buf.write("\t\2\2\2\u01bfv\3\2\2\2\u01c0\u01c4\5\63\32\2\u01c1\u01c3")
        buf.write("\5s:\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4\u01c2")
        buf.write("\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5x\3\2\2\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01c9\t\b\2\2\u01c8\u01ca\t\t\2\2\u01c9")
        buf.write("\u01c8\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\3\2\2\2")
        buf.write("\u01cb\u01cd\t\7\2\2\u01cc\u01cb\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cfz")
        buf.write("\3\2\2\2\u01d0\u01d1\7a\2\2\u01d1|\3\2\2\2\u01d2\u01d3")
        buf.write("\7$\2\2\u01d3~\3\2\2\2\u01d4\u01d5\5\t\5\2\u01d5\u01d6")
        buf.write("\5\7\4\2\u01d6\u01da\3\2\2\2\u01d7\u01d9\13\2\2\2\u01d8")
        buf.write("\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc\u01da\3")
        buf.write("\2\2\2\u01dd\u01de\5\7\4\2\u01de\u01df\5\t\5\2\u01df\u01e0")
        buf.write("\3\2\2\2\u01e0\u01e1\b@\7\2\u01e1\u0080\3\2\2\2\u01e2")
        buf.write("\u01e3\7\61\2\2\u01e3\u01e4\7\61\2\2\u01e4\u01e8\3\2\2")
        buf.write("\2\u01e5\u01e7\n\n\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("\u01eb\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec\bA\7\2")
        buf.write("\u01ec\u0082\3\2\2\2\u01ed\u01ef\t\13\2\2\u01ee\u01ed")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0")
        buf.write("\u01f1\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f3\bB\7\2")
        buf.write("\u01f3\u0084\3\2\2\2\u01f4\u01f8\7$\2\2\u01f5\u01f7\5")
        buf.write("\u0089E\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fc\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01fd\t\f\2\2\u01fc\u01fb\3")
        buf.write("\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u01ff\bC\b\2\u01ff\u0086")
        buf.write("\3\2\2\2\u0200\u0204\7$\2\2\u0201\u0203\5\u0089E\2\u0202")
        buf.write("\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204\u0202\3\2\2\2")
        buf.write("\u0204\u0205\3\2\2\2\u0205\u0207\3\2\2\2\u0206\u0204\3")
        buf.write("\2\2\2\u0207\u0208\5\u008dG\2\u0208\u0209\bD\t\2\u0209")
        buf.write("\u0088\3\2\2\2\u020a\u020d\n\r\2\2\u020b\u020d\5\u008b")
        buf.write("F\2\u020c\u020a\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u008a")
        buf.write("\3\2\2\2\u020e\u020f\7^\2\2\u020f\u0212\t\16\2\2\u0210")
        buf.write("\u0212\t\17\2\2\u0211\u020e\3\2\2\2\u0211\u0210\3\2\2")
        buf.write("\2\u0212\u008c\3\2\2\2\u0213\u0214\7^\2\2\u0214\u0217")
        buf.write("\n\16\2\2\u0215\u0217\n\20\2\2\u0216\u0213\3\2\2\2\u0216")
        buf.write("\u0215\3\2\2\2\u0217\u008e\3\2\2\2\u0218\u0219\13\2\2")
        buf.write("\2\u0219\u021a\bH\n\2\u021a\u0090\3\2\2\2 \2\u014e\u015b")
        buf.write("\u0166\u016c\u0176\u017a\u0184\u0188\u0191\u0195\u019a")
        buf.write("\u01a0\u01a4\u01aa\u01af\u01b1\u01ba\u01c4\u01c9\u01ce")
        buf.write("\u01da\u01e8\u01f0\u01f8\u01fc\u0204\u020c\u0211\u0216")
        buf.write("\13\3\63\2\3\64\3\3\64\4\3\64\5\3\65\6\b\2\2\3C\7\3D\b")
        buf.write("\3H\t")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    SUB = 2
    MUL = 3
    DIV = 4
    MOD = 5
    NOT = 6
    DC = 7
    AND = 8
    OR = 9
    EQ = 10
    LTE = 11
    GTE = 12
    NEQ = 13
    LT = 14
    GT = 15
    LP = 16
    RP = 17
    LCB = 18
    RCB = 19
    LSB = 20
    RSB = 21
    SEMI = 22
    COMMA = 23
    COLON = 24
    DOT = 25
    ASSIGN = 26
    INT = 27
    INTEGER = 28
    FLOAT = 29
    STRING = 30
    BOOLEAN = 31
    VOID = 32
    ARRAY = 33
    INHERIT = 34
    FUNCTION = 35
    IF = 36
    ELSE = 37
    FOR = 38
    WHILE = 39
    DO = 40
    BREAK = 41
    CONTINUE = 42
    RETURN = 43
    OUT = 44
    AUTO = 45
    OF = 46
    OPERATORS = 47
    SEPARATORS = 48
    BOOL_LIT = 49
    STRING_LIT = 50
    FLOAT_LIT = 51
    INT_LIT = 52
    ID = 53
    BLOCK_COMMENT = 54
    LINE_COMMENT = 55
    WS = 56
    UNCLOSE_STRING = 57
    ILLEGAL_ESCAPE = 58
    ERROR_CHAR = 59

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'::'", "'&&'", "'||'", 
            "'=='", "'<='", "'>='", "'!='", "'<'", "'>'", "'('", "')'", 
            "'{'", "'}'", "'['", "']'", "';'", "','", "':'", "'.'", "'='", 
            "'int'", "'integer'", "'float'", "'string'", "'boolean'", "'void'", 
            "'array'", "'inherit'", "'function'", "'if'", "'else'", "'for'", 
            "'while'", "'do'", "'break'", "'continue'", "'return'", "'out'", 
            "'auto'", "'of'" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "DC", "AND", "OR", 
            "EQ", "LTE", "GTE", "NEQ", "LT", "GT", "LP", "RP", "LCB", "RCB", 
            "LSB", "RSB", "SEMI", "COMMA", "COLON", "DOT", "ASSIGN", "INT", 
            "INTEGER", "FLOAT", "STRING", "BOOLEAN", "VOID", "ARRAY", "INHERIT", 
            "FUNCTION", "IF", "ELSE", "FOR", "WHILE", "DO", "BREAK", "CONTINUE", 
            "RETURN", "OUT", "AUTO", "OF", "OPERATORS", "SEPARATORS", "BOOL_LIT", 
            "STRING_LIT", "FLOAT_LIT", "INT_LIT", "ID", "BLOCK_COMMENT", 
            "LINE_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    ruleNames = [ "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "DC", "AND", 
                  "OR", "EQ", "LTE", "GTE", "NEQ", "LT", "GT", "LP", "RP", 
                  "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", "COLON", 
                  "DOT", "ASSIGN", "INT", "INTEGER", "FLOAT", "STRING", 
                  "BOOLEAN", "VOID", "ARRAY", "INHERIT", "FUNCTION", "IF", 
                  "ELSE", "FOR", "WHILE", "DO", "BREAK", "CONTINUE", "RETURN", 
                  "OUT", "AUTO", "OF", "OPERATORS", "SEPARATORS", "BOOL_LIT", 
                  "STRING_LIT", "FLOAT_LIT", "INT_LIT", "ID", "LOW_CHARACTER", 
                  "UP_CHARACTER", "CHARACTER", "DIGIT", "POS_DIGIT", "DEC", 
                  "EXP", "UNDERSCORE", "DBQ", "BLOCK_COMMENT", "LINE_COMMENT", 
                  "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_CHAR", 
                  "ES", "EI", "ERROR_CHAR" ]

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
            actions[49] = self.STRING_LIT_action 
            actions[50] = self.FLOAT_LIT_action 
            actions[51] = self.INT_LIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[70] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def FLOAT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 2:
            self.text = self.text.replace('_', '')
     

        if actionIndex == 3:
            self.text = self.text.replace('_', '')
     

    def INT_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            self.text = self.text.replace('_', '')
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] == '"' and y[-2] == '\\': 
            			raise UncloseString(y[1:])
            		elif y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            raise ErrorToken(self.text)
     


