# bug reproduction script for bug #3886 of AmazeFileManager
import sys
import time

import uiautomator2 as u2

# avd_serial: emulator-5554

def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)



    d.app_start("com.amaze.filemanager.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "com.amaze.filemanager.debug":
            break
        time.sleep(2)
    wait()

    # 点击"..."展开设置
    out = d(resourceId="com.amaze.filemanager.debug:id/properties").click()
    if not out:
        print("Success: 点击‘...’展开设置")
    wait()

    # 点击copy
    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击copy")
    wait()

    # 再次点击"..."展开设置
    out = d(resourceId="com.amaze.filemanager.debug:id/properties").click()
    if not out:
        print("Success: 点击‘...’展开设置")
    wait()


    # 点击rename
    out = d.xpath('//android.widget.ListView/android.widget.LinearLayout[5]/android.widget.RelativeLayout[1]').click()
    if not out:
        print("Success: 点击rename")
    wait()


    # 重命名，这里点击键盘输入y
    out = d.xpath('//*[@resource-id="com.android.inputmethod.latin:id/main_keyboard_frame"]/android.view.View[1]/com.android.inputmethod.keyboard.Key[6]').click()
    if not out:
        print("Success: 重命名")
    wait()


    # 点击back键收起键盘
    out = d(resourceId="com.android.systemui:id/back").click()
    if not out:
        print("Success: 点击back键收起键盘")
    wait()

    # 点击save
    out = d(resourceId="com.amaze.filemanager.debug:id/md_buttonDefaultPositive").click()
    if not out:
        print("Success: 点击save")
    wait()

    #点击parse
    out = d(resourceId="com.amaze.filemanager.debug:id/snackBarActionButton").click()
    if not out:
        print("Success: 点击save")
    wait()

    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)