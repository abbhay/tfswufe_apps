#作者    Abbhay
#github账号    https://github.com/abbhay
#博客    https://abbhay.github.io/
#desc    A kinder Pythoner
import json

import requests

class tfpingjiao(object):
    def __init__(self):
        self.headers = {
            'Host': 'tfapp.tfswufe.edu.cn',
            'Connection': 'keep-alive',
            'Content-Length': '2293',
            'Accept': 'application/json, text/plain, */*',
            'Origin': 'https://tfapp.tfswufe.edu.cn',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; vivo Y67A Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/51.0.2704.81 Mobile Safari/537.36 CombWebView(V 2.1.1)',
            'Content-Type': 'application/json;charset=UTF-8',
            'Referer': 'https://tfapp.tfswufe.edu.cn/comb-jxmyd/?v=1.0.1.2',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh,en-US;q=0.8',
        }
        self.course_url = 'https://tfapp.tfswufe.edu.cn/comb-jxmyd/rest/service/findCourseByKeyIdAndSemester'
        self.post_url = 'https://tfapp.tfswufe.edu.cn/comb-jxmyd/rest/service/submitQuestionnaire'
        self.course_data = {
            "keyId": input("请输入你的学号"),
            "semester":input("请输入你的学期（2018-2019-2）"),
        }
        self.json_course_data = json.dumps(self.course_data)
        self.post_data = {
            "studentKeyId":self.course_data['keyId'],
            "teacherKeyId": "",
            "courseCode": "",
            "courseName": "",
            "semester": self.course_data['semester'],
            "weeks": "第1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17周",
            "data": [
                {
                    "classId": "20190508093208dc04cfc7227446c582",
                    "issueId": "20190508093208c13761c79eac4e19a8",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208dc04cfc7227446c582",
                    "issueId": "20190508093208c2081ac1a65a40a78c",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208dc04cfc7227446c582",
                    "issueId": "201905080932086e4c15a8d2454dbfa1",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208dc04cfc7227446c582",
                    "issueId": "2019050809320861759125987b4b79bf",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208a7ee900873654d4786",
                    "issueId": "2019050809320858d280b658f446daad",
                    "grade": "4"
                },
                {
                    "classId": "20190508093208a7ee900873654d4786",
                    "issueId": "2019050809320872f9a05355044d0d8e",
                    "grade": "4"
                },
                {
                    "classId": "20190508093208a7ee900873654d4786",
                    "issueId": "20190508093208bf26a9d831e849a79b",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208e9e63e65fd1e4fb890",
                    "issueId": "201905080932088f9216fe99714ecba2",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208e9e63e65fd1e4fb890",
                    "issueId": "2019050809320809b6be9b041d46f286",
                    "grade": "4"
                },
                {
                    "classId": "20190508093208e9e63e65fd1e4fb890",
                    "issueId": "201905080932087fdb617253594d8cb6",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208e9e63e65fd1e4fb890",
                    "issueId": "20190508093208840b05ebdd8f4580ac",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208e9e63e65fd1e4fb890",
                    "issueId": "201905080932088577ecf6671e4f0380",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208e9e63e65fd1e4fb890",
                    "issueId": "201905080932083a8d186cb52a46dea8",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208f41c05ffdf4545db88",
                    "issueId": "20190508093208bf27efd65c894127b8",
                    "grade": "4"
                },
                {
                    "classId": "20190508093208f41c05ffdf4545db88",
                    "issueId": "201905080932082fc9b8ebb015416ca0",
                    "grade": "5"
                },
                {
                    "classId": "201905080932088a1744ca22624a47b3",
                    "issueId": "20190508093208178a2889eeee408f9a",
                    "grade": "5"
                },
                {
                    "classId": "201905080932088a1744ca22624a47b3",
                    "issueId": "20190508093208e1074b496971403684",
                    "grade": "5"
                },
                {
                    "classId": "201905080932088a1744ca22624a47b3",
                    "issueId": "201905080932080306c2aa34bb4869ae",
                    "grade": "4"
                },
                {
                    "classId": "201905080932088a1744ca22624a47b3",
                    "issueId": "201905080932089d5f82e28b934d62bc",
                    "grade": "5"
                },
                {
                    "classId": "20190508093208ff0b622a5e6d4f269e",
                    "issueId": "20190508093208cb0d31ddebd643ba84",
                    "grade": "5"
                }
            ]
        }

    def get_course_detail(self):
        detail = requests.post(self.course_url,data=self.json_course_data,headers = self.headers).text
        detail_data = json.loads(detail)
        for courseData in detail_data["result"]["data"]:
            courseCode = courseData['courseCode']
            courseName = courseData['courseName']
            teacherKeyId=courseData['courseData'][0]['teacherKeyId']
            self.deal_post_data(teacherKeyId,courseCode, courseName)

    def deal_post_data(self,teacherKeyId,courseCode,courseName):
        self.post_data['teacherKeyId'] = teacherKeyId
        self.post_data['courseCode'] = courseCode
        self.post_data['courseName'] = courseName

        end =requests.post(self.post_url,headers =self.headers,data=json.dumps(self.post_data))

        if end.status_code == 200:
            print(courseName+end.text)
        else:
            print("失败请重试")



if __name__ == '__main__':
   tf =  tfpingjiao()
   tf.get_course_detail()