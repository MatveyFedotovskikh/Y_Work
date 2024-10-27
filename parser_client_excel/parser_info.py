import datetime
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import password as password
from .Auth_2FA.main import password_page
import json
# https://rtschool.s20.online/company/1/customer/index?sort=b_date
# https://rtschool.s20.online/company/1/customer/index?sort=-b_date

class Selenium_test():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--headless")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(
            options=options
        )
    
    def start(self):
        password_page(f'https://rtschool.s20.online/company/1/customer/index?sort=b_date',self.driver, r'Bot_for_Work_devoloper/json/cookies.json')
        # self.driver.get(f'https://rtschool.s20.online/company/1/customer/index?sort=b_date')
        # time.sleep(1)
        # email_input = self.driver.find_element(by=By.ID, value="loginform-username")
        # email_input.clear()
        # email_input.send_keys(password.login_alfa)
        # time.sleep(0.2)
        # password_input = self.driver.find_element(by=By.ID, value="loginform-password")
        # password_input.clear()
        # password_input.send_keys(password.passowrd_alfa)
        # time.sleep(0.2)
        # password_input.send_keys(Keys.ENTER)
        # time.sleep(1) 
        # time.sleep(10)
        # code = get_code(datetime.datetime.now(datetime.timezone.utc))
        # time.sleep(1)
        # code_input = self.driver.find_element(by=By.ID, value='login2faform-code')
        # code_input.clear()
        # code_input.send_keys(code)
        # time.sleep(1)
        # code_input.send_keys(Keys.ENTER)
        # time.sleep(5)
        self.parser_clients_base()
        
        
    # [30.03.2021], [26.01.2022]    
    # https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_study_status_id%5D=&CustomerSearch%5Bf_custom_ovz%5D=&CustomerSearch%5Bf_custom_rassrochka%5D=&CustomerSearch%5Bf_custom_aktivirovalivrss%5D=&CustomerSearch%5Bf_custom_amocrmid%5D=&CustomerSearch%5Bf_custom_perv_urok_from%5D=&CustomerSearch%5Bf_custom_perv_urok_to%5D=&CustomerSearch%5Bf_custom_prices%5D=&CustomerSearch%5Bf_custom_zaprosilidr%5D=&CustomerSearch%5Bf_custom_market%5D=&CustomerSearch%5Bf_custom_ottok_klienta%5D=&CustomerSearch%5Bf_custom_planshetpk%5D=&CustomerSearch%5Bf_last_attend_date_from%5D=&CustomerSearch%5Bf_last_attend_date_to%5D=&CustomerSearch%5Bf_custom_kurs%5D=&CustomerSearch%5Bf_name%5D=&CustomerSearch%5Bf_id%5D=&CustomerSearch%5Bf_gender%5D=&CustomerSearch%5Bf_age_from%5D=&CustomerSearch%5Bf_age_to%5D=&CustomerSearch%5Bf_dob_from%5D=&CustomerSearch%5Bf_dob_to%5D=&CustomerSearch%5Bf_phone%5D=&CustomerSearch%5Bf_comment%5D=&CustomerSearch%5Bf_legal_name%5D=&CustomerSearch%5Bf_balance_from%5D=&CustomerSearch%5Bf_balance_to%5D=&CustomerSearch%5Bf_lesson_count_from%5D=&CustomerSearch%5Bf_lesson_count_to%5D=&CustomerSearch%5Bf_balance_contract_from%5D=&CustomerSearch%5Bf_balance_contract_to%5D=&CustomerSearch%5Bf_balance_bonus_from%5D=&CustomerSearch%5Bf_balance_bonus_to%5D=&CustomerSearch%5Bf_removed%5D=&CustomerSearch%5Bf_removed_from%5D=&CustomerSearch%5Bf_removed_to%5D=&CustomerSearch%5Bf_first_payment_date_from%5D=&CustomerSearch%5Bf_first_payment_date_to%5D=&CustomerSearch%5Bf_level_id%5D=&CustomerSearch%5Bf_assigned_id%5D=&CustomerSearch%5Bf_employee_id%5D=&CustomerSearch%5Bf_lead_source_id%5D=&CustomerSearch%5Bf_color%5D=&CustomerSearch%5Bf_note%5D=&CustomerSearch%5Bf_date_from%5D={}&CustomerSearch%5Bf_date_to%5D={}&CustomerSearch%5Bf_next_lesson_date_from%5D=&CustomerSearch%5Bf_next_lesson_date_to%5D=&CustomerSearch%5Bf_tariff_till_from%5D=&CustomerSearch%5Bf_tariff_till_to%5D=&CustomerSearch%5Bf_customer_reject_id%5D=&CustomerSearch%5Bf_custom_tipzanyatiy%5D=&CustomerSearch%5Bf_custom_ssylkanapu%5D=&CustomerSearch%5Bf_custom_ssylkaamocrm%5D=&CustomerSearch%5Bf_custom_ssylkanaoplatuvamo%5D=&CustomerSearch%5Bf_custom_childname%5D=&CustomerSearch%5Bf_custom_age%5D=&CustomerSearch%5Bf_custom_datarebyonka_from%5D=&CustomerSearch%5Bf_custom_datarebyonka_to%5D=&CustomerSearch%5Bf_custom_yazyk%5D=&CustomerSearch%5Bf_custom_strana%5D=&CustomerSearch%5Bf_custom_chasovoypoyas%5D=&CustomerSearch%5Bf_custom_sex_child%5D=&CustomerSearch%5Bf_custom_zona%5D=&CustomerSearch%5Bf_custom_uchitelivremya%5D=&CustomerSearch%5Bf_custom_discordlogin%5D=&CustomerSearch%5Bf_custom_discordid%5D=&CustomerSearch%5Bf_custom_group%5D=&CustomerSearch%5Bf_custom_khotyatpedagogaspu%5D=&CustomerSearch%5Bf_custom_metodyoplaty%5D=&CustomerSearch%5Bf_custom_prioritetnoepomsk%5D=&CustomerSearch%5Bf_custom_osobennostiuchenika%5D=&CustomerSearch%5Bf_custom_deteyizsemi%5D=&CustomerSearch%5Bf_custom_pervayaoplatav%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_from%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_to%5D=&CustomerSearch%5Bf_custom_zonaoplaty%5D=&CustomerSearch%5Bf_custom_byudzhetpolnogopaket%5D=&CustomerSearch%5Bf_custom_valyutapolnogopaketa%5D=&CustomerSearch%5Bf_custom_polnyypaketprodann%5D=&CustomerSearch%5Bf_custom_rassrochkakolvoplate%5D=&CustomerSearch%5Bf_custom_rassylkakanikuly%5D=&CustomerSearch%5Bf_custom_aktsiibonusnyeuroki%5D=&CustomerSearch%5Bf_custom_formatoplachennykh%5D=&CustomerSearch%5Bf_custom_rssid%5D=&CustomerSearch%5Bf_custom_prioritetnyedni%5D=
    # https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_study_status_id%5D=&CustomerSearch%5Bf_custom_ovz%5D=&CustomerSearch%5Bf_custom_rassrochka%5D=&CustomerSearch%5Bf_custom_aktivirovalivrss%5D=&CustomerSearch%5Bf_custom_amocrmid%5D=&CustomerSearch%5Bf_custom_perv_urok_from%5D=30.03.2021&CustomerSearch%5Bf_custom_perv_urok_to%5D=26.01.2022&CustomerSearch%5Bf_custom_prices%5D=&CustomerSearch%5Bf_custom_zaprosilidr%5D=&CustomerSearch%5Bf_custom_market%5D=&CustomerSearch%5Bf_custom_ottok_klienta%5D=&CustomerSearch%5Bf_custom_planshetpk%5D=&CustomerSearch%5Bf_last_attend_date_from%5D=&CustomerSearch%5Bf_last_attend_date_to%5D=&CustomerSearch%5Bf_custom_kurs%5D=&CustomerSearch%5Bf_name%5D=&CustomerSearch%5Bf_id%5D=&CustomerSearch%5Bf_gender%5D=&CustomerSearch%5Bf_age_from%5D=&CustomerSearch%5Bf_age_to%5D=&CustomerSearch%5Bf_dob_from%5D=&CustomerSearch%5Bf_dob_to%5D=&CustomerSearch%5Bf_phone%5D=&CustomerSearch%5Bf_comment%5D=&CustomerSearch%5Bf_legal_name%5D=&CustomerSearch%5Bf_balance_from%5D=&CustomerSearch%5Bf_balance_to%5D=&CustomerSearch%5Bf_lesson_count_from%5D=&CustomerSearch%5Bf_lesson_count_to%5D=&CustomerSearch%5Bf_balance_contract_from%5D=&CustomerSearch%5Bf_balance_contract_to%5D=&CustomerSearch%5Bf_balance_bonus_from%5D=&CustomerSearch%5Bf_balance_bonus_to%5D=&CustomerSearch%5Bf_removed%5D=&CustomerSearch%5Bf_removed_from%5D=&CustomerSearch%5Bf_removed_to%5D=&CustomerSearch%5Bf_first_payment_date_from%5D=&CustomerSearch%5Bf_first_payment_date_to%5D=&CustomerSearch%5Bf_level_id%5D=&CustomerSearch%5Bf_assigned_id%5D=&CustomerSearch%5Bf_employee_id%5D=&CustomerSearch%5Bf_lead_source_id%5D=&CustomerSearch%5Bf_color%5D=&CustomerSearch%5Bf_note%5D=&CustomerSearch%5Bf_date_from%5D=&CustomerSearch%5Bf_date_to%5D=&CustomerSearch%5Bf_next_lesson_date_from%5D=&CustomerSearch%5Bf_next_lesson_date_to%5D=&CustomerSearch%5Bf_tariff_till_from%5D=&CustomerSearch%5Bf_tariff_till_to%5D=&CustomerSearch%5Bf_customer_reject_id%5D=&CustomerSearch%5Bf_custom_tipzanyatiy%5D=&CustomerSearch%5Bf_custom_ssylkanapu%5D=&CustomerSearch%5Bf_custom_ssylkaamocrm%5D=&CustomerSearch%5Bf_custom_ssylkanaoplatuvamo%5D=&CustomerSearch%5Bf_custom_childname%5D=&CustomerSearch%5Bf_custom_age%5D=&CustomerSearch%5Bf_custom_datarebyonka_from%5D=&CustomerSearch%5Bf_custom_datarebyonka_to%5D=&CustomerSearch%5Bf_custom_yazyk%5D=&CustomerSearch%5Bf_custom_strana%5D=&CustomerSearch%5Bf_custom_chasovoypoyas%5D=&CustomerSearch%5Bf_custom_sex_child%5D=&CustomerSearch%5Bf_custom_zona%5D=&CustomerSearch%5Bf_custom_uchitelivremya%5D=&CustomerSearch%5Bf_custom_discordlogin%5D=&CustomerSearch%5Bf_custom_discordid%5D=&CustomerSearch%5Bf_custom_group%5D=&CustomerSearch%5Bf_custom_khotyatpedagogaspu%5D=&CustomerSearch%5Bf_custom_metodyoplaty%5D=&CustomerSearch%5Bf_custom_prioritetnoepomsk%5D=&CustomerSearch%5Bf_custom_osobennostiuchenika%5D=&CustomerSearch%5Bf_custom_deteyizsemi%5D=&CustomerSearch%5Bf_custom_pervayaoplatav%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_from%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_to%5D=&CustomerSearch%5Bf_custom_zonaoplaty%5D=&CustomerSearch%5Bf_custom_byudzhetpolnogopaket%5D=&CustomerSearch%5Bf_custom_valyutapolnogopaketa%5D=&CustomerSearch%5Bf_custom_polnyypaketprodann%5D=&CustomerSearch%5Bf_custom_rassrochkakolvoplate%5D=&CustomerSearch%5Bf_custom_rassylkakanikuly%5D=&CustomerSearch%5Bf_custom_aktsiibonusnyeuroki%5D=&CustomerSearch%5Bf_custom_formatoplachennykh%5D=&CustomerSearch%5Bf_custom_rssid%5D=&CustomerSearch%5Bf_custom_prioritetnyedni%5D=
    # https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_study_status_id%5D=&CustomerSearch%5Bf_custom_ovz%5D=&CustomerSearch%5Bf_custom_rassrochka%5D=&CustomerSearch%5Bf_custom_aktivirovalivrss%5D=&CustomerSearch%5Bf_custom_amocrmid%5D=&CustomerSearch%5Bf_custom_perv_urok_from%5D={}&CustomerSearch%5Bf_custom_perv_urok_to%5D={}&CustomerSearch%5Bf_custom_prices%5D=&CustomerSearch%5Bf_custom_zaprosilidr%5D=&CustomerSearch%5Bf_custom_market%5D=&CustomerSearch%5Bf_custom_ottok_klienta%5D=&CustomerSearch%5Bf_custom_planshetpk%5D=&CustomerSearch%5Bf_last_attend_date_from%5D=&CustomerSearch%5Bf_last_attend_date_to%5D=&CustomerSearch%5Bf_custom_kurs%5D=&CustomerSearch%5Bf_name%5D=&CustomerSearch%5Bf_id%5D=&CustomerSearch%5Bf_gender%5D=&CustomerSearch%5Bf_age_from%5D=&CustomerSearch%5Bf_age_to%5D=&CustomerSearch%5Bf_dob_from%5D=&CustomerSearch%5Bf_dob_to%5D=&CustomerSearch%5Bf_phone%5D=&CustomerSearch%5Bf_comment%5D=&CustomerSearch%5Bf_legal_name%5D=&CustomerSearch%5Bf_balance_from%5D=&CustomerSearch%5Bf_balance_to%5D=&CustomerSearch%5Bf_lesson_count_from%5D=&CustomerSearch%5Bf_lesson_count_to%5D=&CustomerSearch%5Bf_balance_contract_from%5D=&CustomerSearch%5Bf_balance_contract_to%5D=&CustomerSearch%5Bf_balance_bonus_from%5D=&CustomerSearch%5Bf_balance_bonus_to%5D=&CustomerSearch%5Bf_removed%5D=&CustomerSearch%5Bf_removed_from%5D=&CustomerSearch%5Bf_removed_to%5D=&CustomerSearch%5Bf_first_payment_date_from%5D=&CustomerSearch%5Bf_first_payment_date_to%5D=&CustomerSearch%5Bf_level_id%5D=&CustomerSearch%5Bf_assigned_id%5D=&CustomerSearch%5Bf_employee_id%5D=&CustomerSearch%5Bf_lead_source_id%5D=&CustomerSearch%5Bf_color%5D=&CustomerSearch%5Bf_note%5D=&CustomerSearch%5Bf_date_from%5D=&CustomerSearch%5Bf_date_to%5D=&CustomerSearch%5Bf_next_lesson_date_from%5D=&CustomerSearch%5Bf_next_lesson_date_to%5D=&CustomerSearch%5Bf_tariff_till_from%5D=&CustomerSearch%5Bf_tariff_till_to%5D=&CustomerSearch%5Bf_customer_reject_id%5D=&CustomerSearch%5Bf_custom_tipzanyatiy%5D=&CustomerSearch%5Bf_custom_ssylkanapu%5D=&CustomerSearch%5Bf_custom_ssylkaamocrm%5D=&CustomerSearch%5Bf_custom_ssylkanaoplatuvamo%5D=&CustomerSearch%5Bf_custom_childname%5D=&CustomerSearch%5Bf_custom_age%5D=&CustomerSearch%5Bf_custom_datarebyonka_from%5D=&CustomerSearch%5Bf_custom_datarebyonka_to%5D=&CustomerSearch%5Bf_custom_yazyk%5D=&CustomerSearch%5Bf_custom_strana%5D=&CustomerSearch%5Bf_custom_chasovoypoyas%5D=&CustomerSearch%5Bf_custom_sex_child%5D=&CustomerSearch%5Bf_custom_zona%5D=&CustomerSearch%5Bf_custom_uchitelivremya%5D=&CustomerSearch%5Bf_custom_discordlogin%5D=&CustomerSearch%5Bf_custom_discordid%5D=&CustomerSearch%5Bf_custom_group%5D=&CustomerSearch%5Bf_custom_khotyatpedagogaspu%5D=&CustomerSearch%5Bf_custom_metodyoplaty%5D=&CustomerSearch%5Bf_custom_prioritetnoepomsk%5D=&CustomerSearch%5Bf_custom_osobennostiuchenika%5D=&CustomerSearch%5Bf_custom_deteyizsemi%5D=&CustomerSearch%5Bf_custom_pervayaoplatav%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_from%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_to%5D=&CustomerSearch%5Bf_custom_zonaoplaty%5D=&CustomerSearch%5Bf_custom_byudzhetpolnogopaket%5D=&CustomerSearch%5Bf_custom_valyutapolnogopaketa%5D=&CustomerSearch%5Bf_custom_polnyypaketprodann%5D=&CustomerSearch%5Bf_custom_rassrochkakolvoplate%5D=&CustomerSearch%5Bf_custom_rassylkakanikuly%5D=&CustomerSearch%5Bf_custom_aktsiibonusnyeuroki%5D=&CustomerSearch%5Bf_custom_formatoplachennykh%5D=&CustomerSearch%5Bf_custom_rssid%5D=&CustomerSearch%5Bf_custom_prioritetnyedni%5D=

    def parser_clients_base(self):
        count_all_student = self.dowland_list_start()
        print(count_all_student)

        name_columns = self.name_columns()
        if 'Добавлен' not in name_columns:
            self.driver.find_element(By.XPATH,'//*[@class="crm-ajax-link crm-dashed-link"]').click()
            name_columns_in_settings = self.name_columns_in_settings()
            self.driver.find_element(By.XPATH,f'//*[@id="common-modal-sm"]/div/div/form/div[2]/ul/li[{name_columns_in_settings.index("Добавлен")+1}]/label/span').click()
            self.driver.find_element(By.XPATH,f'//*[@id="common-modal-sm"]/div/div/form/div[3]/button').click()
            count_all_student = self.dowland_list_start()
            name_columns = self.name_columns()
        index_adds = name_columns.index("Добавлен")   
        
        count_files_info = count_all_student//1000
        date_first1 = self.date_get(index_adds)  
        date_first = date_first1

        self.driver.get(f'https://rtschool.s20.online/company/1/customer/index?sort=-b_date')
        count_all_student = self.dowland_list_start()
        

        name_columns = self.name_columns()
        if 'Добавлен' not in name_columns:
            self.driver.find_element(By.XPATH,'//*[@class="crm-ajax-link crm-dashed-link"]').click()
            name_columns_in_settings = self.name_columns_in_settings()
            self.driver.find_element(By.XPATH,f'//*[@id="common-modal-sm"]/div/div/form/div[2]/ul/li[{name_columns_in_settings.index("Добавлен")+1}]/label/span').click()
            self.driver.find_element(By.XPATH,f'//*[@id="common-modal-sm"]/div/div/form/div[3]/button').click()
            count_all_student = self.dowland_list_start()
            name_columns = self.name_columns()
        index_adds = name_columns.index("Добавлен")   
        
        count_files_info = count_all_student//1000
        date_last = self.date_get(index_adds) 

        date_first = date_first.split('.')
        for i in range(len(date_first)):
            date_first[i] = int(date_first[i])
        date_last = date_last.split('.')
        for i in range(len(date_last)):
            date_last[i] = int(date_last[i])
        count_days_work_school = int(( datetime.date(date_last[2], date_last[1], date_last[0]) - datetime.date(date_first[2], date_first[1], date_first[0])).days)
        
        naxt_date = datetime.date(date_first[2], date_first[1], date_first[0]) + datetime.timedelta(count_days_work_school)
        
        # next_date = date_first1.split('.')
        # dates_in_run = [next_date]
        dates_in_run = []
        for i in range(count_files_info*count_files_info):
            next_date = datetime.date(date_first[2], date_first[1], date_first[0]) + datetime.timedelta((count_days_work_school//(count_files_info*count_files_info))*i)
            next_date = str(next_date).split('-')
            for ii in range(len(next_date)):
                next_date[ii] = int(next_date[ii])
            next_date = list(reversed(next_date))
            dates_in_run.append(next_date)
        dates_in_run.append(date_last)
        
        for i in range(len(dates_in_run)-1):
            if dates_in_run[i+1]!=date_last:
                date_test = datetime.date(dates_in_run[i+1][2], dates_in_run[i+1][1], dates_in_run[i+1][0]) - datetime.timedelta(1)
                next_date = str(date_test).split('-')
                for ii in range(len(next_date)):
                    next_date[ii] = int(next_date[ii])
                next_date = list(reversed(next_date))
                date_test = next_date
            else:
                date_test = date_last
            date_now = f'{dates_in_run[i][0]}.{dates_in_run[i][1]}.{dates_in_run[i][2]}'
            date_next = f'{date_test[0]}.{date_test[1]}.{date_test[2]}'
            date_list = date_now.split('.')
            for ii in range (len(date_list)):
                if len(date_list[ii])<2:
                    date_list[ii] = '0'+date_list[ii]
            date_now = f'{date_list[0]}.{date_list[1]}.{date_list[2]}'
            date_list = date_next.split('.')
            for ii in range (len(date_list)):
                if len(date_list[ii])<2:
                    date_list[ii] = '0'+date_list[ii]
            date_next = f'{date_list[0]}.{date_list[1]}.{date_list[2]}'
            self.driver.get(f'https://rtschool.s20.online/company/1/customer/index?CustomerSearch%5Bf_study_status_id%5D=&CustomerSearch%5Bf_custom_ovz%5D=&CustomerSearch%5Bf_custom_rassrochka%5D=&CustomerSearch%5Bf_custom_aktivirovalivrss%5D=&CustomerSearch%5Bf_custom_amocrmid%5D=&CustomerSearch%5Bf_custom_perv_urok_from%5D=&CustomerSearch%5Bf_custom_perv_urok_to%5D=&CustomerSearch%5Bf_custom_prices%5D=&CustomerSearch%5Bf_custom_zaprosilidr%5D=&CustomerSearch%5Bf_custom_market%5D=&CustomerSearch%5Bf_custom_ottok_klienta%5D=&CustomerSearch%5Bf_custom_planshetpk%5D=&CustomerSearch%5Bf_last_attend_date_from%5D=&CustomerSearch%5Bf_last_attend_date_to%5D=&CustomerSearch%5Bf_custom_kurs%5D=&CustomerSearch%5Bf_name%5D=&CustomerSearch%5Bf_id%5D=&CustomerSearch%5Bf_gender%5D=&CustomerSearch%5Bf_age_from%5D=&CustomerSearch%5Bf_age_to%5D=&CustomerSearch%5Bf_dob_from%5D=&CustomerSearch%5Bf_dob_to%5D=&CustomerSearch%5Bf_phone%5D=&CustomerSearch%5Bf_comment%5D=&CustomerSearch%5Bf_legal_name%5D=&CustomerSearch%5Bf_balance_from%5D=&CustomerSearch%5Bf_balance_to%5D=&CustomerSearch%5Bf_lesson_count_from%5D=&CustomerSearch%5Bf_lesson_count_to%5D=&CustomerSearch%5Bf_balance_contract_from%5D=&CustomerSearch%5Bf_balance_contract_to%5D=&CustomerSearch%5Bf_balance_bonus_from%5D=&CustomerSearch%5Bf_balance_bonus_to%5D=&CustomerSearch%5Bf_removed%5D=&CustomerSearch%5Bf_removed_from%5D=&CustomerSearch%5Bf_removed_to%5D=&CustomerSearch%5Bf_first_payment_date_from%5D=&CustomerSearch%5Bf_first_payment_date_to%5D=&CustomerSearch%5Bf_level_id%5D=&CustomerSearch%5Bf_assigned_id%5D=&CustomerSearch%5Bf_employee_id%5D=&CustomerSearch%5Bf_lead_source_id%5D=&CustomerSearch%5Bf_color%5D=&CustomerSearch%5Bf_note%5D=&CustomerSearch%5Bf_date_from%5D={date_now}&CustomerSearch%5Bf_date_to%5D={date_next}&CustomerSearch%5Bf_next_lesson_date_from%5D=&CustomerSearch%5Bf_next_lesson_date_to%5D=&CustomerSearch%5Bf_tariff_till_from%5D=&CustomerSearch%5Bf_tariff_till_to%5D=&CustomerSearch%5Bf_customer_reject_id%5D=&CustomerSearch%5Bf_custom_tipzanyatiy%5D=&CustomerSearch%5Bf_custom_ssylkanapu%5D=&CustomerSearch%5Bf_custom_ssylkaamocrm%5D=&CustomerSearch%5Bf_custom_ssylkanaoplatuvamo%5D=&CustomerSearch%5Bf_custom_childname%5D=&CustomerSearch%5Bf_custom_age%5D=&CustomerSearch%5Bf_custom_datarebyonka_from%5D=&CustomerSearch%5Bf_custom_datarebyonka_to%5D=&CustomerSearch%5Bf_custom_yazyk%5D=&CustomerSearch%5Bf_custom_strana%5D=&CustomerSearch%5Bf_custom_chasovoypoyas%5D=&CustomerSearch%5Bf_custom_sex_child%5D=&CustomerSearch%5Bf_custom_zona%5D=&CustomerSearch%5Bf_custom_uchitelivremya%5D=&CustomerSearch%5Bf_custom_discordlogin%5D=&CustomerSearch%5Bf_custom_discordid%5D=&CustomerSearch%5Bf_custom_group%5D=&CustomerSearch%5Bf_custom_khotyatpedagogaspu%5D=&CustomerSearch%5Bf_custom_metodyoplaty%5D=&CustomerSearch%5Bf_custom_prioritetnoepomsk%5D=&CustomerSearch%5Bf_custom_osobennostiuchenika%5D=&CustomerSearch%5Bf_custom_deteyizsemi%5D=&CustomerSearch%5Bf_custom_pervayaoplatav%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_from%5D=&CustomerSearch%5Bf_custom_datapervoyoplaty_to%5D=&CustomerSearch%5Bf_custom_zonaoplaty%5D=&CustomerSearch%5Bf_custom_byudzhetpolnogopaket%5D=&CustomerSearch%5Bf_custom_valyutapolnogopaketa%5D=&CustomerSearch%5Bf_custom_polnyypaketprodann%5D=&CustomerSearch%5Bf_custom_rassrochkakolvoplate%5D=&CustomerSearch%5Bf_custom_rassylkakanikuly%5D=&CustomerSearch%5Bf_custom_aktsiibonusnyeuroki%5D=&CustomerSearch%5Bf_custom_formatoplachennykh%5D=&CustomerSearch%5Bf_custom_rssid%5D=&CustomerSearch%5Bf_custom_prioritetnyedni%5D=')
            
            count_all_student = self.dowland_list_start()
            if count_all_student != 'Ничего не найдено.':
                self.driver.find_element(By.XPATH,f'//*[@id="page-wrapper"]/div/div[2]/div/div/div[4]/button').click()
                self.dowland_list_export()
                self.driver.find_element(By.XPATH,f'//*[@id="page-wrapper"]/div/div[2]/div/div/div[4]/ul/li[7]/a').click()
                self.dowland_list_in_dowland()  
                self.driver.find_element(By.XPATH,f'//*[@id="exportform-format"]').click()
                self.driver.find_element(By.XPATH,f'//*[@id="exportform-format"]/option[2]').click()
                self.driver.find_element(By.XPATH,f'//*[@id="w0"]/div[2]/button[2]/i').click()
            # time.sleep(30)
        time.sleep(30)
        
    def dowland_list_in_dowland(self):
        try:
            return self.driver.find_element(By.XPATH,f'//*[@id="w0"]/div[2]/button[2]/i').text
        except:
            return self.dowland_list_in_dowland()      
    def dowland_list_export(self):
        try:
            return self.driver.find_element(By.XPATH,f'//*[@id="page-wrapper"]/div/div[2]/div/div/div[4]/ul/li[7]/a').text
        except:
            return self.dowland_list_export()
    def dowland_list_filters(self):
        try:
            return self.driver.find_element(By.XPATH,f'//*[@id="common-modal"]/div/div/form/div[2]/div[73]/div[1]/label').text   
        except:
            return self.dowland_list_filters()
    

    def dowland_list_start(self):
        try:
            return int(self.driver.find_element(By.XPATH,'//*[@id="w1"]/div[1]/span/b[2]').text)
        except:
            return self.dowland_list_start2()
        
    def dowland_list_start2(self):
        try:
            return self.driver.find_element(By.XPATH,'//*[@id="w1-container"]/table/tbody/tr/td/div').text
        except:
            return self.dowland_list_start()
    def date_get(self,index_adds):
        try:
           
           return self.driver.find_element(By.XPATH,f'//*[@id="w1-container"]/table/tbody/tr[1]/td[{index_adds+1}]').text 
        except:
            return self.date_get(index_adds)   
    def name_columns(self):
        try:
            head_colums = self.driver.find_element(By.TAG_NAME, 'thead')
            names_colums_client = head_colums.find_elements(By.TAG_NAME, 'th')
            columns = []
            for name_colum in names_colums_client:
                columns.append(name_colum.text)
            return columns
        except:
            return self.name_columns()

    def name_columns_in_settings(self):
        try:
            
            head_colums = self.driver.find_element(By.XPATH, '//*[@class="sortable-list list-unstyled overflow-auto ui-sortable"]')
            names_colums_client = head_colums.find_elements(By.TAG_NAME, 'li')
            columns = []
            for name_colum in names_colums_client:
                columns.append(name_colum.text)
            return columns
        except:
            return self.name_columns_in_settings()
    
    def name_columns_in_filters(self):
        try:
            
            head_colums = self.driver.find_element(By.XPATH, '//*[@class="modal-body modal-body-search p-md"]')
            names_colums_client = head_colums.find_elements(By.CLASS_NAME, 'form-group')
            columns = []
            for name_colum in names_colums_client:
                columns.append(name_colum.text)
            return columns
        except:
            return self.name_columns_in_filters()
       

def start():
    
    Selenium_test().start()
    


