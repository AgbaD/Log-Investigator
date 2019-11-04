class Investigation:
    ''' A program that reads the transaction logs of a company and returns any unusual findings
    based on the changes in pattern of company expenses
    An example of a log
    Feb SLR 4 M
    Feb ENT 800 K
    Mar SLR 4000 K
    Mar ENT 800 K
    Apr SLR 4010 K
    Apr ENT 810 K
    Jul SLR 4 M
    Jul ENT 800 K
    Jul OTR 1200 K
    Aug SLR 4000 K
    Aug ENT 800 K
    Aug OTR 1190 K
    Sep SLR 4000 K
    Sep ENT 800 K
    Sep OTR 1190 K
    '''

    def __init__(self, data):
        '''The data is a list of tuples containing the transaction logs'''
        self.data = data
        self.usu_sal = 0
        self.usu_ent = 0
        self.usu_otr = 0
        self.check()
        final = self.investigate()
        for i in final:
            print(i)

    def check(self):
        '''To check each tuple, gather like terms into a list, i.e salaries, others, entertainments,
        find and return the most occurring salary as the baseline for salaries
         and others and entertainment too.'''
        sal = []
        otr = []
        ent = []
        for value in self.data:
            pre = value
            a = pre[1]  # The type of data; salary, other, entertainment
            b = pre[2]  # The amount involved
            c = pre[3]  # The value; Thousand or Millions
            if a == 'SLR':  # Salary
                if c == 'M':    # Millions
                    b *= 1000   # Change it to thousands
                sal.append(b)   # Add to the list of salaries
            elif a == 'ENT':
                ent.append(b)
            elif a == 'OTR':
                otr.append(b)
        sal_set = set(sal)  # unique salary values
        otr_set = set(otr)  # Unique other values
        ent_set = set(ent)  # Unique entertainment values
        now = {}    # Dictionary of counts-value pairs
        for i in sal_set:
            val = sal.count(i)
            now[val] = i    # Get the count
        if len(now) != 0:
            jay = self.large(now)   # Find the largest count
            self.usu_sal = now[jay]     # Make is the baseline for the salary
        now = {}
        for i in otr_set:
            val = otr.count(i)
            now[val] = i
        if len(now) != 0:
            jar = self.large(now)
            self.usu_otr = now[jar]
        now = {}
        for i in ent_set:
            val = ent.count(i)
            now[val] = i
        if len(now) != 0:
            jam = self.large(now)
            self.usu_ent = now[jam]

    def large(self, dic):
        '''To return the largest key in a dict'''
        start = 0
        for key in dic.keys():
            if key > start:
                start = key
        return start

    def investigate(self):
        '''Performs the actual investigation of checking for unusual rates'''
        result = []
        for value in self.data:
            if value[1] == 'SLR' and value[2] != self.usu_sal:
                if value[2] != self.usu_sal/1000:
                    a = f'{value[0]} has an unusual salary rate of {value[2]} instead of {self.usu_sal}'
                    result.append(a)
            if value[1] == 'ENT' and value[2] != self.usu_ent:
                b = f'{value[0]} has an unusual entertainment rate of {value[2]} instead of {self.usu_ent}'
                result.append(b)
            if value[1] == 'OTR' and value[2] != self.usu_otr:
                c = f'{value[0]} has an unusual other rate of {value[2]} instead of {self.usu_otr}'
                result.append(c)

        return result


data = \
    [('Feb', 'SLR', 4, 'M'), ('Feb', 'ENT', 800, 'K'), ('Mar', 'SLR', 4000, 'K'),
     ('Mar', 'ENT', 800, 'K'), ('Apr', 'SLR', 4010, 'K'), ('Apr', 'ENT', 810, 'K'),
     ('Jul', 'SLR', 4, 'M'), ('Jul', 'ENT', 800, 'K'), ('Jul', 'OTR', 1200, 'K'),
     ('Aug', 'SLR', 4000, 'K'), ('Aug', 'ENT', 800, 'K'), ('Aug', 'OTR', 1190, 'K'),
     ('Sep', 'SLR', 4000, 'K'), ('Sep', 'ENT', 800, 'K'), ('Sep', 'OTR', 1190, 'K')]

if __name__ == '__main__':
    Investigation(data)
