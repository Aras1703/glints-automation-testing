import glints.glints as glints_auto
import glints.constants as const

try:
    glints_auto.glints_test()
    glints_auto.dropdown_languages('English')
    #glints_auto.to_login_page()
    glints_auto.to_jobs_page()
    #glints_auto.to_explore_page()
    glints_auto.search_jobs('QA Engineer')
    glints_auto.job_types('internship', 'freelance')
    glints_auto.remote_option()
    glints_auto.work_locations(const.loc.get("Jkt"), const.loc.get("Bdg"))
    glints_auto.block_advertises()
    glints_auto.work_experiences(const.exp.get("<1"), const.exp.get("1-3"))
    glints_auto.exclude_experience()

except Exception as e:
    if "in PATH" in str(e):
        print(
            'You are trying to run the bot from the command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows : \n'
            '   set PATH=%PATH%;C:path-to-your-folder \n'
        )
    else:
        raise