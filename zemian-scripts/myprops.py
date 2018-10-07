class Site:

    company_name = "ZSoft Corp."

    @staticmethod
    def company_notice():
        print("Company notice is at class level.")

    def __init__(self):
        self.name = 'My Site'
        self.admin_username = 'zemian'

    @property
    def fmap(self):
        return {
            'myfunc' : lambda x : x * 2,
            'print_me' : self.print_me
        }

    def print_me(self):
        print("Site.company_name=%s" % Site.company_name)
        print("self.name=%s" % self.name)
        print("self.admin_username=%s" % self.admin_username)


print(Site)
print(Site.company_name)
Site.company_notice()

site = Site()
print(site)
print(site.name)
print(site.admin_username)

print(site.fmap)
print(site.print_me)
site.print_me()
