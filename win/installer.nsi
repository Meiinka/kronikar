; Kronikár – Windows installer (per-user, no admin rights needed)
Unicode true
SetCompressor /SOLID lzma

!define APPNAME "Kronikár"
!define APPID "Kronikar"
!define VERSION "1.6"
!define UNINSTKEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APPID}"

!include "MUI2.nsh"
!include "WordFunc.nsh"

Name "${APPNAME}"
OutFile "Kronikar-Setup.exe"
InstallDir "$LOCALAPPDATA\Programs\${APPID}"
InstallDirRegKey HKCU "Software\${APPID}" "InstallDir"
RequestExecutionLevel user
BrandingText "${APPNAME} ${VERSION}"

VIProductVersion "1.6.0.0"
VIAddVersionKey /LANG=1051 "ProductName" "${APPNAME}"
VIAddVersionKey /LANG=1051 "FileDescription" "Inštalátor aplikácie ${APPNAME}"
VIAddVersionKey /LANG=1033 "ProductName" "${APPNAME}"
VIAddVersionKey /LANG=1033 "FileDescription" "${APPNAME} installer"
VIAddVersionKey /LANG=1033 "FileVersion" "${VERSION}"
VIAddVersionKey /LANG=1033 "ProductVersion" "${VERSION}"
VIAddVersionKey /LANG=1033 "LegalCopyright" "© 2026 meiinka · MIT License"
VIAddVersionKey /LANG=1051 "FileVersion" "${VERSION}"
VIAddVersionKey /LANG=1051 "ProductVersion" "${VERSION}"
VIAddVersionKey /LANG=1051 "LegalCopyright" "© 2026 meiinka · MIT License"

!define MUI_ICON "kronikar.ico"
!define MUI_UNICON "kronikar.ico"
!define MUI_ABORTWARNING
!define MUI_WELCOMEPAGE_TITLE "$(WelcomeTitle)"
!define MUI_WELCOMEPAGE_TEXT "$(WelcomeText)"
!define MUI_FINISHPAGE_RUN
!define MUI_FINISHPAGE_RUN_TEXT "$(RunText)"
!define MUI_FINISHPAGE_RUN_FUNCTION LaunchApp

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH
!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES
!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "Slovak"
!insertmacro MUI_LANGUAGE "Czech"

LangString WelcomeTitle ${LANG_SLOVAK} "Inštalácia aplikácie Kronikár"
LangString WelcomeTitle ${LANG_CZECH} "Inštalácia aplikácie Kronikár"
LangString WelcomeTitle ${LANG_ENGLISH} "Kronikár Setup"
LangString WelcomeText ${LANG_SLOVAK} "Kronikár je písacie štúdio pre tvoje knihy: rukopis, svet, vzťahy a export.$\r$\n$\r$\nAplikácia sa otvára v samostatnom okne prehliadača Google Chrome (ak ho nemáš, použije sa Microsoft Edge). Na inštaláciu nie sú potrebné práva správcu.$\r$\n$\r$\nTvoje projekty ostávajú v priečinku, ktorý si v aplikácii vyberieš – inštalácia ani odinštalovanie sa ich nedotkne."
LangString WelcomeText ${LANG_CZECH} "Kronikár je písacie štúdio pre tvoje knihy: rukopis, svet, vzťahy a export.$\r$\n$\r$\nAplikácia sa otvára v samostatnom okne prehliadača Google Chrome (ak ho nemáš, použije sa Microsoft Edge). Na inštaláciu nie sú potrebné práva správcu.$\r$\n$\r$\nTvoje projekty ostávajú v priečinku, ktorý si v aplikácii vyberieš – inštalácia ani odinštalovanie sa ich nedotkne."
LangString WelcomeText ${LANG_ENGLISH} "Kronikár is a writing studio for your books: manuscript, world, relationships and export.$\r$\n$\r$\nThe app opens in its own Google Chrome window (or Microsoft Edge if Chrome is not installed). No administrator rights are needed.$\r$\n$\r$\nYour projects stay in the folder you choose in the app – installing or uninstalling never touches them."
LangString RunText ${LANG_SLOVAK} "Spustiť Kronikár"
LangString RunText ${LANG_CZECH} "Spustiť Kronikár"
LangString RunText ${LANG_ENGLISH} "Launch Kronikár"
LangString ShortDesc ${LANG_SLOVAK} "Písacie štúdio Kronikár"
LangString ShortDesc ${LANG_CZECH} "Písacie štúdio Kronikár"
LangString ShortDesc ${LANG_ENGLISH} "Kronikár writing studio"

Var Browser
Var AppUrl

; find Chrome, fall back to Edge (always present on Windows 10/11)
Function FindBrowser
  ReadRegStr $Browser HKCU "Software\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" ""
  StrCmp $Browser "" 0 done
  ReadRegStr $Browser HKLM "Software\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe" ""
  StrCmp $Browser "" 0 done
  IfFileExists "$PROGRAMFILES64\Google\Chrome\Application\chrome.exe" 0 +3
    StrCpy $Browser "$PROGRAMFILES64\Google\Chrome\Application\chrome.exe"
    Goto done
  IfFileExists "$PROGRAMFILES32\Google\Chrome\Application\chrome.exe" 0 +3
    StrCpy $Browser "$PROGRAMFILES32\Google\Chrome\Application\chrome.exe"
    Goto done
  IfFileExists "$LOCALAPPDATA\Google\Chrome\Application\chrome.exe" 0 +3
    StrCpy $Browser "$LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
    Goto done
  ReadRegStr $Browser HKLM "Software\Microsoft\Windows\CurrentVersion\App Paths\msedge.exe" ""
  StrCmp $Browser "" 0 done
  StrCpy $Browser "$PROGRAMFILES32\Microsoft\Edge\Application\msedge.exe"
  done:
FunctionEnd

; file:///C:/Users/.../Kronikar.html with spaces encoded
Function MakeUrl
  ${WordReplace} "$INSTDIR\Kronikar.html" "\" "/" "+" $AppUrl
  ${WordReplace} "$AppUrl" " " "%20" "+" $AppUrl
  StrCpy $AppUrl "file:///$AppUrl"
FunctionEnd

Function LaunchApp
  Exec '"$Browser" --app="$AppUrl"'
FunctionEnd

Section "Kronikár" SecMain
  SetShellVarContext current
  SetOutPath "$INSTDIR"
  File "Kronikar.html"
  File "kronikar.ico"
  File "pdfmake.min.js"
  Call FindBrowser
  Call MakeUrl
  ; launcher shortcuts
  CreateShortCut "$DESKTOP\${APPNAME}.lnk" "$Browser" '--app="$AppUrl"' "$INSTDIR\kronikar.ico" 0 SW_SHOWNORMAL "" "$(ShortDesc)"
  CreateShortCut "$SMPROGRAMS\${APPNAME}.lnk" "$Browser" '--app="$AppUrl"' "$INSTDIR\kronikar.ico" 0 SW_SHOWNORMAL "" "$(ShortDesc)"
  ; uninstaller + entry in Windows "Apps"
  WriteUninstaller "$INSTDIR\Odinstalovat.exe"
  WriteRegStr HKCU "Software\${APPID}" "InstallDir" "$INSTDIR"
  WriteRegStr HKCU "${UNINSTKEY}" "DisplayName" "${APPNAME}"
  WriteRegStr HKCU "${UNINSTKEY}" "DisplayVersion" "${VERSION}"
  WriteRegStr HKCU "${UNINSTKEY}" "Publisher" "meiinka"
  WriteRegStr HKCU "${UNINSTKEY}" "DisplayIcon" "$INSTDIR\kronikar.ico"
  WriteRegStr HKCU "${UNINSTKEY}" "InstallLocation" "$INSTDIR"
  WriteRegStr HKCU "${UNINSTKEY}" "UninstallString" '"$INSTDIR\Odinstalovat.exe"'
  WriteRegDWORD HKCU "${UNINSTKEY}" "NoModify" 1
  WriteRegDWORD HKCU "${UNINSTKEY}" "NoRepair" 1
  WriteRegDWORD HKCU "${UNINSTKEY}" "EstimatedSize" 4600
SectionEnd

Section "Uninstall"
  SetShellVarContext current
  Delete "$DESKTOP\${APPNAME}.lnk"
  Delete "$SMPROGRAMS\${APPNAME}.lnk"
  Delete "$INSTDIR\Kronikar.html"
  Delete "$INSTDIR\kronikar.ico"
  Delete "$INSTDIR\pdfmake.min.js"
  Delete "$INSTDIR\Odinstalovat.exe"
  RMDir "$INSTDIR"
  DeleteRegKey HKCU "${UNINSTKEY}"
  DeleteRegKey HKCU "Software\${APPID}"
SectionEnd
