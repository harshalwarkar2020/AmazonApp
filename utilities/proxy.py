import os
import time
def hmaone(region):
    if region != "India":
        os.system("adb shell am start -n com.hidemyass.hidemyassprovpn/com.avast.android.vpn.activity.HmaOnboardingActivity")
        time.sleep(3)
        os.system("adb shell input tap 889 1613")
        time.sleep(1)
        os.system("adb shell input tap 234 160")
        if region == "Indonesia":
            os.system("adb shell input text 'Indonesia' ")
        elif region == "Malaysia":
            os.system("adb shell input text 'Malaysia' ")
        time.sleep(1)
        os.system("adb shell input tap 234 468")
        time.sleep(3)
        os.system("adb shell input keyevent 3")
        time.sleep(2)