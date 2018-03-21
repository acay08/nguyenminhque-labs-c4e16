from gmail import GMail, Message
from random import choice

gmail = GMail('acaynguyen102@gmail.com','Admin2018')

html_content = """
<p></p>
<p style="text-align: center;"><strong>Đơn xin nghỉ học</strong></p>
<p>K&iacute;nh gửi thầy Tuấn Anh</p>
<p>H&ocirc;m nay {{chan ch&aacute;n}}, vậy xin thầy cho em nghỉ 1 buổi nh&eacute;</p>
<p>Cảm ơn thầy, ^^</p>
<p>Acay</p>
<p></p>
"""

reasons = ["trời xanh mây trắng, học thì quá phí", "trời mưa, đường bẩn"]

reason = choice(reasons)

new_reason = html_content.replace('{{chan ch&aacute;n}}', reason)

msg = Message('Đơn xin nghỉ học',
               to = 'techkidsc4e16@gmail.com',
               cc = 'acaynguyen102@gmail.com',
               html = new_reason)

while True:
    import datetime
    now = datetime.datetime.now()
    hour_time = now.hour, now.minute
    if hour_time == (11, 43):
        gmail.send(msg)
        break
