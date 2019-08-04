import sched, time, os
from Schedule import schedule

def main():
    projectPath = os.path.dirname(os.path.realpath(__file__))
    print(time.time())
    s = sched.scheduler(time.time, time.sleep)   
    #s.enter(10, 1, schedule.ExtractData,(projectPath))
   # s.enter(5, 2, schedule.ImportTxtToDatabase(projectPath))
    s.enter(5, 2, schedule.PlotGraph, kwargs={'projectPath': projectPath})
    #s.enter(5, 1, schedule.PostSocialMidia())
    s.run()
    print(time.time())
  
if __name__ == "__main__":    
    username = "lupadocidadao"
    password = "esaniagro12"

   # while True:
    main()