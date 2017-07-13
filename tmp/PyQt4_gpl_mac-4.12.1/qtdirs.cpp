#include <QCoreApplication>
#include <QFile>
#include <QLibraryInfo>
#include <QTextStream>

// This is for Qt v5.  The value isn't accurate but triggers the desired
// description of the edition.
#if !defined(QT_EDITION)
#define QT_EDITION      0x200
#endif

int main(int argc, char **argv)
{
    QCoreApplication app(argc, argv);
    QFile outf("qtdirs.out");

    if (!outf.open(QIODevice::WriteOnly|QIODevice::Truncate|QIODevice::Text))
        return 1;

    QTextStream out(&outf);

    out << QLibraryInfo::location(QLibraryInfo::PrefixPath) << '\n';
    out << QLibraryInfo::location(QLibraryInfo::HeadersPath) << '\n';
    out << QLibraryInfo::location(QLibraryInfo::LibrariesPath) << '\n';
    out << QLibraryInfo::location(QLibraryInfo::BinariesPath) << '\n';
    out << QLibraryInfo::location(QLibraryInfo::DataPath) << '\n';
#if QT_VERSION >= 0x050000
    out << QLibraryInfo::location(QLibraryInfo::ArchDataPath) << '\n';
#else
    out << QLibraryInfo::location(QLibraryInfo::DataPath) << '\n';
#endif
    out << QLibraryInfo::location(QLibraryInfo::PluginsPath) << '\n';

    out << QT_VERSION << '\n';
    out << QT_EDITION << '\n';

    out << QLibraryInfo::licensee() << '\n';

#if defined(QT_SHARED) || defined(QT_DLL)
    out << "shared\n";
#else
    out << "static\n";
#endif

    // Determine which features should be disabled.

#if defined(QT_NO_ACCESSIBILITY)
    out << "PyQt_Accessibility\n";
#endif

#if defined(QT_NO_SESSIONMANAGER)
    out << "PyQt_SessionManager\n";
#endif

#if defined(QT_NO_STATUSTIP)
    out << "PyQt_StatusTip\n";
#endif

#if defined(QT_NO_TOOLTIP)
    out << "PyQt_ToolTip\n";
#endif

#if defined(QT_NO_WHATSTHIS)
    out << "PyQt_WhatsThis\n";
#endif

#if defined(QT_NO_OPENSSL)
    out << "PyQt_OpenSSL\n";
#endif

#if defined(QT_NO_SIZEGRIP)
    out << "PyQt_SizeGrip\n";
#endif

#if defined(QT_NO_SYSTEMTRAYICON)
    out << "PyQt_SystemTrayIcon\n";
#endif

#if defined(QT_NO_PRINTDIALOG)
    out << "PyQt_PrintDialog\n";
#endif

#if defined(QT_NO_PRINTER)
    out << "PyQt_Printer\n";
#endif

#if defined(QT_NO_PRINTPREVIEWDIALOG)
    out << "PyQt_PrintPreviewDialog\n";
#endif

#if defined(QT_NO_PRINTPREVIEWWIDGET)
    out << "PyQt_PrintPreviewWidget\n";
#endif

#if defined(QT_NO_RAWFONT)
    out << "PyQt_RawFont\n";
#endif

#if !defined(QT3_SUPPORT) || QT_VERSION >= 0x040200
    out << "PyQt_NoPrintRangeBug\n";
#endif

#if defined(QT_OPENGL_ES)
    out << "PyQt_NoOpenGLES\n";
#endif

#if defined(QT_NO_FPU) || defined(QT_ARCH_ARM) || defined(QT_ARCH_WINDOWSCE) || defined(QT_ARCH_SYMBIAN) || defined(QT_ARCH_VXWORKS)
    out << "PyQt_qreal_double\n";
#endif

    return 0;
}
