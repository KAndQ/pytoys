#!/usr/bin/python3
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SPREADER = sys.argv[1]

str_plist = ur"""
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>items</key>
    <array>
        <dict>
            <key>assets</key>
            <array>
                <dict>
                    <key>kind</key>
                    <string>software-package</string>
                    <key>url</key>
                    <string>http://phzdownload.gllkgame.com/spreader/phz_${SPREADER}.ipa</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>full-size-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://phzdownload.gllkgame.com:8080/Icon-512.png</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>display-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://phzdownload.gllkgame.com:8080/Icon-57.png</string>
                </dict>
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>com.lkgame.glpaohuzi</string>
                <key>bundle-version</key>
                <string>0</string>
                <key>kind</key>
                <string>software</string>
                <key>title</key>
                <string>跑胡子</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>
"""

str_plist = str_plist.replace("${SPREADER}", SPREADER)

filename = "phz_public_" + SPREADER + ".plist"
file = open(filename, "wb")
file.write(str_plist)
file.close()


