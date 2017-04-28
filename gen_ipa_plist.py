#!/usr/bin/python3
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

SPREADER = sys.argv[1]
OUTPUT_FILENAME = sys.argv[2]
GAME = sys.argv[3]

str_plist_phz = ur"""
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

str_plist_czzp = ur"""
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
                    <string>http://czzp.lkgame.com:8080/spreader/czzp_${SPREADER}.ipa</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>full-size-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://czzp.lkgame.com:8080/czzp/Icon-512.png</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>display-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://czzp.lkgame.com:8080/czzp/Icon-57.png</string>
                </dict>
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>com.lkgame.czzp</string>
                <key>bundle-version</key>
                <string>4</string>
                <key>kind</key>
                <string>software</string>
                <key>title</key>
                <string>郴州字牌</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>
"""

str_plist_hgw = ur"""
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
                    <string>http://hhhgwdownload.gllkgame.com/spreader/hgw_${SPREADER}.ipa</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>full-size-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://hhhgwdownload.gllkgame.com/Icon-512.png</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>display-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://hhhgwdownload.gllkgame.com/Icon-57.png</string>
                </dict>
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>com.lkgame.lkhgw</string>
                <key>bundle-version</key>
                <string>0</string>
                <key>kind</key>
                <string>software</string>
                <key>title</key>
                <string>红拐弯</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>
"""

str_plist_glzp = ur"""
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
                    <string>http://glzp.lk78game.com:8080/spread/glzp_${SPREADER}.ipa</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>full-size-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://glzp.lk78game.com:8080/ios/Icon-512.png</string>
                </dict>
                <dict>
                    <key>kind</key>
                    <string>display-image</string>
                    <key>needs-shine</key>
                    <false/>
                    <key>url</key>
                    <string>http://glzp.lk78game.com:8080/ios/Icon-57.png</string>
                </dict>
            </array>
            <key>metadata</key>
            <dict>
                <key>bundle-identifier</key>
                <string>com.lkgame.guilinzp</string>
                <key>bundle-version</key>
                <string>1</string>
                <key>kind</key>
                <string>software</string>
                <key>title</key>
                <string>桂林字牌</string>
            </dict>
        </dict>
    </array>
</dict>
</plist>

"""

if GAME == "phz":
    str_plist = str_plist_phz
elif GAME == "czzp":
    str_plist = str_plist_czzp
elif GAME == "hgw":
    str_plist = str_plist_hgw
elif GAME == "glzp":
    str_plist = str_plist_glzp 

str_plist = str_plist.replace("${SPREADER}", SPREADER)

filename = OUTPUT_FILENAME
file = open(filename, "wb")
file.write(str_plist)
file.close()


