from gmail import GMail, Message
from random import choice

gmail = GMail('acaynguyen102@gmail.com','Galileo1@')

# msg = Message('Hello',to='techkidsc4e16@gmail.com',text='Hello')
html_content = """
<p style="text-align: center;"><span style="background-color: #ffff99;"><strong>Đơn xin nghỉ học</strong></span></p>
<p style="text-align: center;"><span style="background-color: #ffff99;">H&ocirc;m nay {{chan chan}} xin thầy cho em nghỉ học nh&eacute;</span></p>
<p style="text-align: center;"><span style="color: #ff6600;"><em><span style="background-color: #ffff99;"><span style="color: #0000ff;">Cảm ơn thầy</span>&nbsp;</span><img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-cool.gif" alt="cool" /></em></span></p>
<p></p>
<p></p>
<p></p>
"""
#placeholder
reasons = ['Đau bụng', 'ốm', 'chán']

reason = choice(reasons)

new_reason = html_content.replace('{{chan chan}}', reason)

msg = Message('Đơn xin nghỉ học',
               to='taurus@galileovietnam.com',
               html=new_reason)
gmail.send(msg)
