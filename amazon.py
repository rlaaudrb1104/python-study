import requests

헤더스 = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

쿠키 = {
'session-id' :'133-2949173-2218546', 'session-id-time' : '2082787201l' ,  'i18n-prefs' : 'USD' , 'sp-cdn' : 'L5Z9:KR' , 'skin' : 'noskin', 'ubid-main' : '135-4227127-3248022', 'session-token' : '3KJbErxMSFNqZnuKXQP4YO/py8Z6nqnVqnr/yYGZilTXqPgrcDJadNi8VaLUSAw72kZxIRJK6L2Fuw8fCTijNBGZyMGTUcBBrsC2p6UzYArMUPtL0hcjI1S/Wlw3eCpooCGlQanLaIC20lCZiW6a2iusytRS53NEJFHPe6Tj17JRlEBGBjKtXPGGuafSVOrxAJ+hk1eU9gCJRv1CRpth7AWOKvvQ5i0xqT8LQxVzJeWGfTYEZyJQrUF7gA9iAjR1BcsvGA7pYtQ7Sbi35zuIGvqY8+Et1DI9SvUMISFRZHGxioWZYgkkMb2C4yirx6AsWYUUHOBiEUKikGaLjeF0x8PZGAzE62Tx' , 'csm-hit' : 'tb:QG1VHNPS3G388454CSMZ+s-QG1VHNPS3G388454CSMZ|1694595806191&t:1694595806191&adb:adblk_no'
}


r = requests.get('https://www.amazon.com/', headers=헤더스, cookies=쿠키)

print(r.content)
print(r.status_code)