from flet import *
import sqlite3


conn = sqlite3.connect('finearts.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS students (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   code TEXT,
                   phone TEXT,
                   comment TEXT,
                   performance INTEGER,
                   english INTEGER,
                   kurdish INTEGER,
                   history INTEGER,
                   computer INTEGER,
                   photography INTEGER   
 )""")
conn.commit()

def main (page:Page):
    page.title = 'Fine Arts' 
    page.scroll= 'auto'
    page.window.top =1
    page.window.left=960
    page.window.width=390
    page.window.height=740
    page.pgcolor= 'white'
    page.theme_mode= ThemeMode.LIGHT



    table_name ='students'
    query = f'SELECT COUNT(*) FROM {table_name}'
    cursor.execute(query)
    result=cursor.fetchone()
    row_count = result[0]



    def add(e):
        cursor.execute("INSERT INTO students (name, code, phone, comment, performance, english, kurdish, history, computer, photography) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                      (tname.value, tcode.value, tphone.value, tcomment.value, Performance.value, English.value, Kurdish.value, History.value, Computer.value, Photography.value))
    
        
        conn.commit()
        page.add(Text(f"قوتابی {tname.value} بەسەرکەوتوویی تۆمارکرا", color='green'))
    def clyear(e):
        tname.value = ""
        tcode.value = ""
        tphone.value = ""
        tcomment.value = ""
        Performance.value = ""
        English.value = ""
        Kurdish.value = ""
        History.value = ""
        Computer.value = ""
        Photography.value = ""
        page.add(Text("هەموو خانەکان پاککرا", color='orange'))
    
    def show(e):
       
        c = conn.cursor()
        c.execute("SELECT * FROM students")
        users = c.fetchall()
        print(users)

        if not users =="":
            keys = ['id', 'name', 'code', 'phone', 'comment', 'performance', 'english', 'kurdish', 'history', 'computer', 'photography']
            result=[dict(zip(keys,values)) for values in users]
            for x in result:
             
    

             page.add(
                Card(
                    color='black',
                    content=Container(
                        content=Column([
                           ListTile(
                               leading=Icon(Icons.PERSON, color='white'),
                               title=Text(f"ناوی قوتابی: {x['name']}", color='white', size=12, rtl=True),
                               subtitle=Column([
                                      Text(f"کۆدی قوتابی: {x['code']}", color='white', size=12, rtl=True),
                                      Text(f"تەلەفۆن: {x['phone']}", color='white', size=12, rtl=True),
                                      Text(f"تێبینی: {x['comment']}", color='white', size=12, rtl=True),
                                      Text(f" ئینگلیزی: {x['english']}", color='white', size=12, rtl=True),
                                      Text(f" کوردناسی: {x['kurdish']}", color='white', size=12, rtl=True),
                                        Text(f" نواندنی شانۆ: {x['performance']}", color='white', size=12, rtl=True),
                                      Text(f"مێژووی شانۆ: {x['history']}", color='white', size=12, rtl=True),
                                      Text(f"کۆمپیوتەر: {x['computer']}", color='white', size=12, rtl=True),
                                      Text(f"فۆتوگرافی: {x['photography']}", color='white', size=12, rtl=True)
                                 ], alignment=MainAxisAlignment.CENTER, rtl=True),
                           )
                               
                            ],
                            spacing=10,
                            alignment=MainAxisAlignment.START
                        ),
                        padding=padding.all(10),
                        width=300,
                        height=300
                    )

                )
            )
             page.update()

    def remove(e):
        if tcode.value:
            cursor.execute("DELETE FROM students WHERE code = ?", (tcode.value,))
            conn.commit()
            page.add(Text(f"قوتابی بەکۆدی {tcode.value} سڕایەوە", color='red'))
        else:
            page.add(Text("تکایە کۆدی قوتابی بنووسە", color='red'))

       

       
       
    #########تێکستەکان#########
    tname = TextField(label="ناوی قوتابی",icon=Icons.PERSON,rtl=True, height=30)
    tcode = TextField(label="کۆدی قوتابی",icon=Icons.CODE,rtl=True, height=30)
    tphone = TextField(label="تەلەفۆن ",icon=Icons.PHONE,rtl=True,height=30)
    tcomment = TextField(label="تێبینی", icon=Icons.COMMENT,rtl=True,height=30)


    ###########علاماتەکان########
    marktext = Text ("وانەکان",text_align='center' , weight='bold')
    English = TextField(label="زمانی ئینگلیزی", rtl=True, width=125,height=30)
    Kurdish  = TextField(label=" كوردناسي",  rtl=True, width=125,height=30)
    History  = TextField(label="مێژووی شانؤ",  rtl=True, width=125,height=30)
    Computer=TextField(label=" کؤمپیوتەر", rtl=True, width=125,height=30)
    Performance= TextField(label=" نواندني شانۆ",  rtl=True, width=125,height=30)
    Photography= TextField(label="فۆتوگرافی",  rtl=True, width=125,height=30)

    ##########################

    addbutton = ElevatedButton("تۆمار ",icon=Icons.ADD,icon_color='green',width=100,height=40, bgcolor='green',color='white', on_click=add)

    removebutton = ElevatedButton("سڕینەوە",icon=Icons.DELETE,icon_color='red',width=100,height=40, bgcolor='red',color='white', on_click=remove)

    clearbutton = ElevatedButton("پاککردن",icon=Icons.CLEAR,icon_color='orange',width=100,height=40, bgcolor='orange',color='white', on_click=clyear)

    showbuttn = ElevatedButton("پیشاندان ",icon=Icons.SHOW_CHART,icon_color='blue',width=100,height=40, bgcolor='blue',color='white', on_click=show)
    page.add(
        Row([
            Image(src="theater.gif",width=150)
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Text("Fine Arts-Cinema&Theater", size=20, font_family="NRT", color="black", text_align=TextAlign.CENTER)
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Text(" بەشی سینەماوشانۆ", size=16, font_family="NRT", color="black", text_align=TextAlign.CENTER),
            Text(" :قۆناغی یەکەم  ", size=16, font_family="NRT", color="green", text_align=TextAlign.CENTER),
            Text(row_count, size=14, font_family="NRT", color="red", text_align=TextAlign.CENTER)
        ], alignment=MainAxisAlignment.CENTER,rtl=True),

        tname,
        tcode,
        tphone,
        tcomment,

        Row([
            showbuttn,clearbutton
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            English,Kurdish,  
        ], alignment=MainAxisAlignment.CENTER),

        Row([
            Performance,Computer,
        ], alignment=MainAxisAlignment.CENTER),
        Row([
            History,Photography,
        ], alignment=MainAxisAlignment.CENTER),

        Row(
            [
                addbutton,removebutton
            ], alignment=MainAxisAlignment.CENTER,rtl=True
        )
    )

    page.update()
app(main)
