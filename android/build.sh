#!/usr/bin/env bash
# Build and sign Kronikar.apk without Android Studio (Debian/Ubuntu packages:
# aapt apksigner zipalign dalvik-exchange android-sdk-platform-23 openjdk).
#
# Signing key is NOT in the repository. Provide it via environment variables:
#   KRONIKAR_KS=/path/to/kronikar.jks  KRONIKAR_KS_PASS=...  [KRONIKAR_KEY_ALIAS=kronikar]
# Run `python3 tools/build.py` first so assets/index.html exists.
set -e
cd "$(dirname "$0")"
: "${KRONIKAR_KS:?set KRONIKAR_KS to your keystore path}"
: "${KRONIKAR_KS_PASS:?set KRONIKAR_KS_PASS}"
ALIAS="${KRONIKAR_KEY_ALIAS:-kronikar}"
AJ=/usr/lib/android-sdk/platforms/android-23/android.jar
rm -rf gen classes out && mkdir -p gen classes out
aapt package -f -m -J gen -M AndroidManifest.xml -S res -I $AJ
javac -nowarn --release 8 -classpath $AJ -d classes gen/sk/kronikar/app/R.java src/sk/kronikar/app/*.java
dalvik-exchange --dex --min-sdk-version=24 --output=out/classes.dex classes
aapt package -f -M AndroidManifest.xml -S res -A assets -I $AJ -F out/app.unsigned.apk
(cd out && aapt add app.unsigned.apk classes.dex >/dev/null)
zipalign -f -p 4 out/app.unsigned.apk out/app.aligned.apk
apksigner sign --ks "$KRONIKAR_KS" --ks-pass env:KRONIKAR_KS_PASS --key-pass env:KRONIKAR_KS_PASS --ks-key-alias "$ALIAS" --out out/Kronikar.apk out/app.aligned.apk
apksigner verify out/Kronikar.apk
ls -la out/Kronikar.apk
