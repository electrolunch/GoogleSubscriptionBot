#%%
import schedule


#%%




job1 = schedule.every().day.at("09:00").do(check_new_results)