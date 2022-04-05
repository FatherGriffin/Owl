from datetime import date
from notecard import Notecard, Notecard_Divider
from paper_scrap import paper_scrap


class database:
    sch_today = []
    schedule_lists = []
    desc_lists = []

    # initialize
    def __init__(self):
        self.today = date.today()

    # creates schedule for the day
    def grab_schedule(self, today=date.today()):
        self.schedule_lists = []
        self.sch_today = []
        strs = []
        start = today.strftime('%Y-%m-%d')
        cal = open('calendar.txt', 'r').read().split('\n')
        rev = False
        for line in cal:
            if rev and line[0:4] != '    ':
                break
            if not rev and line == start:
                rev = True
                continue
            if rev:
                if line[0:8] == '        ':
                    strs.append(line[8:])
                else:
                    strs.append(line[4:])

        temp = []
        # creating 2D array of notecard strings
        for i in range(int(strs.__len__())):
            temp.append(strs[i])
            if int(temp.__len__()) == 3:
                self.schedule_lists.append(temp)
                temp = []

        for i in range(int(self.schedule_lists.__len__())):
            for j in range(2):
                self.sch_today.append(self.schedule_lists[i][j])
                if j == 1:
                    self.desc_lists.append(self.schedule_lists[i][j + 1])
        # sort for optional description with certain keyword
        # thread could even ask for it in sms

    # creates readable list for notecard class to format GUI

    def get_parse_bulletin_list(self):
        delete = ''
        for i in self.sch_today:
            if i[0:3] == 'apt' and i != delete:
                delete = i
                self.sch_today[self.sch_today.index(i)] = '<' + i[5:] + '>'
            elif i[0:3] == 'apt' and i == delete:
                self.sch_today.remove(delete)
            else:
                continue
        temp = []
        index = 0
        for i in self.sch_today:
            if i[:1] == '<':
                while index % 3 != 0:
                    temp.append('')
                    index += 1
                temp.append(i)
            else:
                temp.append(i)
            index += 1
        print(temp)
        return temp

    # translates string list into notecard objects for GUI
    def get_bulletin(self):
        n_count = 1
        temp = []
        ref = self.get_parse_bulletin_list()
        # for i in ref:
        dlc = 0
        tbool = True
        temp.append(Notecard_Divider())

        for count, i in enumerate(ref):
            if i == '':
                continue
            if i[:1] == '<':
                if n_count >= 3:
                    temp.append(Notecard_Divider())
                temp.append(paper_scrap(i[1:-1]))
                n_count = 1
            elif n_count > 2:
                temp.append(Notecard(i, self.desc_lists[dlc], index=count+1))
                dlc += 1
                n_count += 1
            else:
                temp.append(Notecard(i, self.desc_lists[dlc], index=count+1))
                dlc += 1
                n_count += 1
        return temp

    # refreshes bulletin board
    def refresh(self):
        pass

    def del_element(self):
        pass
