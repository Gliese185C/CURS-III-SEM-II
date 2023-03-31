#ifndef INCLUDED_DA_LIBRARY_H
#define INCLUDED_DA_LIBRARY_H

#ifdef DA7ZIP_EXPORTS
#define DA7ZIP_API __declspec(dllexport)
#else
#define DA7ZIP_API __declspec(dllimport)
#endif

#if defined(_MSC_VER) && !defined(LINK_TO_DA7ZIP_LIB)
#define LINK_TO_DA7ZIP_LIB
#endif

#if defined(LINK_TO_DA7ZIP_LIB) && (defined(DONT_LINK_TO_DA7ZIP_LIB) || defined(DA7ZIP_EXPORTS))
#undef LINK_TO_DA7ZIP_LIB
#endif

#ifdef LINK_TO_DA7ZIP_LIB
#pragma comment(lib, "da7zip.lib")
#endif

#endif
